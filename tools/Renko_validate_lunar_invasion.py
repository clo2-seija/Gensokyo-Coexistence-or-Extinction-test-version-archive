"""月都侵军静态检查；不替代新开局界面与实战验证。需要 Pillow。"""
from pathlib import Path
import argparse, json, re, hashlib
from PIL import Image

def parse(path):
    text = re.sub(r'#[^\n]*', '', path.read_text(encoding='utf-8-sig'))
    tokens = re.findall(r'"(?:\\.|[^"\\])*"|[{}=]|[^\s{}=]+', text)
    pos = 0
    def body(nested=False):
        nonlocal pos
        result = []
        while pos < len(tokens):
            token = tokens[pos]; pos += 1
            if token == '}':
                assert nested, f'extra closing brace: {path}'
                return result
            assert token not in ('{','='), f'unexpected token: {path}: {token}'
            if pos < len(tokens) and tokens[pos] == '=':
                pos += 1
                assert pos < len(tokens), path
                value = tokens[pos]; pos += 1
                if value == '{': value = body(True)
                else: value = value.strip('"')
                result.append((token.strip('"'), value))
            else: result.append(token.strip('"'))
        assert not nested, f'unclosed brace: {path}'
        return result
    return body()

def mapping(nodes):
    assert all(isinstance(n, tuple) for n in nodes), nodes
    result = dict(nodes)
    assert len(result) == len(nodes), 'duplicate keys'
    return result

def validate(root, japan, vanilla):
    manifest = json.loads((root/'asset_sources/Renko_LUN_invasion_units/manifest.json').read_text(encoding='utf-8'))
    unit_path = root/'common/units/Renko_LUN_invasion_units.txt'
    units = mapping(mapping(parse(unit_path))['sub_units'])
    assert len(units) == len(manifest) == 5
    sprites = mapping(parse(root/'interface/Renko_LUN_invasion_unit_icons.gfx'))['spriteTypes']
    gfx = [mapping(v) for k,v in sprites if k == 'spriteType']
    assert len(gfx) == 15 and len({x['name'] for x in gfx}) == 15
    eq_text = '\n'.join(p.read_text(encoding='utf-8-sig') for p in (vanilla/'common/units/equipment').rglob('*.txt'))
    core = ['manpower','max_organisation','max_strength','default_morale','weight','supply_consumption','fuel_consumption','own_equipment_fuel_consumption_mult','soft_attack','hard_attack','air_attack','breakthrough','defense','ap_attack','armor_value','suppression','need','combat_width']
    terrain_keys = set(manifest[0]['terrain'])
    for m in manifest:
        u = mapping(units[m['key']]); source = japan/m['source']
        assert hashlib.sha256(source.read_bytes()).hexdigest() == m['source_sha256'], f'Japanese baseline drift: {source}'
        baseline = mapping(mapping(mapping(parse(source))['sub_units'])[m['source_key']])
        # 用户指定例外：中坦歼营装备需求 45 -> 40。
        if m['key'] == 'Renko_LUN_invasion_medium_tankdestroyer':
            baseline['need'] = [('medium_tank_destroyer_chassis', '40')]
        for field in core:
            assert u.get(field) == baseline.get(field), (m['key'], field, 'baseline mismatch')
        assert u['active'] == 'no'
        cats = u['categories']; assert len(cats) == len(set(cats))
        support = m['key'].endswith('_support')
        if support:
            assert u['divisional'] == 'no' and u['group'] == 'support'
            assert 'support' in u['type'] and u.get('special_forces','no') == 'no'
            assert 'category_regimental_support_battalions' in cats
            assert 'combat_width' not in u
            assert not (set(u) & terrain_keys), 'regimental support must have no terrain fields'
            assert not m['terrain']
            assert u['allowed_battalion_groups'] == baseline['allowed_battalion_groups']
        else:
            assert u['special_forces'] == 'yes' and 'category_special_forces' in cats
            assert u['combat_width'] == '2' and 'support' not in u['type']
            assert 'marines' not in u and 'can_exfiltrate_from_coast' not in u
        for equipment, qty in mapping(u['need']).items():
            assert re.search(r'\b'+equipment+r'\s*=\s*\{',eq_text), equipment
            assert int(qty) > 0
        for terrain, values in m['terrain'].items():
            actual = mapping(u[terrain])
            assert {k:float(v) for k,v in actual.items()} == values
            old = mapping(baseline.get(terrain, []))
            for k,v in values.items():
                assert v >= 0 and v >= float(old.get(k,0)), (m['key'],terrain,k)
        for kind, rel in m['paths'].items():
            im = Image.open(root/rel).convert('RGBA'); w,h = im.size
            assert (w,h) == ((152,42) if kind == 'large' else (60,12))
            left,right = im.crop((0,0,w//2,h)),im.crop((w//2,0,w,h))
            assert left.tobytes() == right.tobytes()
            assert left.getbbox() and left.getchannel('A').getextrema() == (0,255)
            suffix = {'large':'medium','map':'medium_white','text':'small'}[kind]
            match = [g for g in gfx if g['name'] == f"GFX_unit_{m['key']}_icon_{suffix}"]
            assert len(match) == 1 and match[0]['texturefile'] == rel and match[0]['noOfFrames'] == '2'
            if kind == 'text': assert match[0]['legacy_lazy_load'] == 'no'
    tech = 'Renko_LUN_invasion_units_tech'
    techdata = mapping(mapping(mapping(parse(root/'common/technologies/Renko_LUN_technologies.txt'))['technologies'])[tech])
    assert set(techdata['enable_subunits']) == set(units)
    assert mapping(techdata['allow']) == {'always':'no'}
    history = (root/'history/countries/LUN - Lunarians.txt').read_bytes()
    assert history.count((tech+' = 1').encode()) == 1
    for lang, folder in [('simp_chinese','simp_chinese'),('english','English')]:
        p = root/f'localisation/{folder}/Renko_LUN_l_{lang}.yml'
        data=p.read_bytes(); assert data.startswith(b'\xef\xbb\xbf') and b'\r' not in data
        keys = re.findall(r'^\s*(\w+):0 "[^"\n]*"$',data.decode('utf-8-sig'),re.M)
        expected = {tech,tech+'_desc'} | set(units) | {k+'_desc' for k in units}
        assert len(expected) == 12 and expected <= set(keys)
        assert len(keys) == len(set(keys)), 'duplicate localisation keys'
        keys = sorted(expected)
        alltext='\n'.join(q.read_text(encoding='utf-8-sig') for q in (root/'localisation'/folder).rglob('*.yml'))
        for key in keys: assert len(re.findall(r'^\s*'+key+r':',alltext,re.M)) == 1,key
    # 全目录检查新标识符唯一性；原有内容不作本轮修复范围。
    allunits='\n'.join(p.read_text(encoding='utf-8-sig') for p in (root/'common/units').glob('*.txt'))
    for key in units: assert len(re.findall(r'^\s*'+key+r'\s*=\s*\{',allunits,re.M)) == 1,key
    allgfx='\n'.join(p.read_text(encoding='utf-8-sig') for p in (root/'interface').glob('*.gfx'))
    for g in gfx: assert len(re.findall(r'name\s*=\s*"'+g['name']+'"',allgfx)) == 1,g['name']
    for rel in ['common/units/Renko_LUN_invasion_units.txt','common/technologies/Renko_LUN_technologies.txt','interface/Renko_LUN_invasion_unit_icons.gfx']:
        data=(root/rel).read_bytes();assert not data.startswith(b'\xef\xbb\xbf') and b'\r' not in data
    assert history.count(b'\n') == history.count(b'\r\n'), 'history line endings changed'
    return {'result':'PASS','units':5,'special_battalions':3,'regimental_support_companies':2,'gfx_registrations':15,'two_frame_pngs':15,'localisation_keys_per_language':12,'baseline_core_stats':'unchanged except user-specified medium TD equipment count = 40','terrain':'infantry complex terrain; armor open terrain only; support has no terrain fields','RuntimeChecks':'NOT RUN'}

if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument('--japan',type=Path)
    ap.add_argument('--vanilla',type=Path,default=Path(r'D:\SteamLibrary\steamapps\common\Hearts of Iron IV'))
    args=ap.parse_args()
    print(json.dumps(validate(args.root,args.japan or args.root.parent/'Japan_rework',args.vanilla),ensure_ascii=False,indent=2))
