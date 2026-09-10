"""月都学说专项静态检查；不替代新开局界面与实战验证。"""
from pathlib import Path
import re,json,sys,hashlib,argparse
ap=argparse.ArgumentParser()
ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
ap.add_argument('--japan',type=Path)
ap.add_argument('--vanilla',type=Path,default=Path(r'D:\SteamLibrary\steamapps\common\Hearts of Iron IV'))
args=ap.parse_args()
root=G=args.root
J=args.japan or root.parent/'Japan_rework'
V=args.vanilla
def parse(t):
    tokens=re.findall(r'"(?:\\.|[^"\\])*"|#[^\n]*|[{}=]|[^\s{}=#]+',t)
    tokens=[x for x in tokens if not x.startswith('#')]; pos=0
    def body(nested=False):
        nonlocal pos
        out=[]
        while pos<len(tokens):
            k=tokens[pos];pos+=1
            if k=='}':
                assert nested
                return out
            if k=='{':out.append((None,body(True)));continue
            assert k!='='
            if pos<len(tokens) and tokens[pos]=='=':
                pos+=1;v=tokens[pos];pos+=1
                if v=='{':v=body(True)
                out.append((k,v))
            else:out.append(k)
        assert not nested
        return out
    return body()
def dump(nodes,n=0):
    lines=[];pad='    '*n
    for node in nodes:
        if isinstance(node,str):lines.append(pad+node);continue
        k,v=node;head=(k+' = ') if k else ''
        if isinstance(v,list):lines.extend([pad+head+'{',dump(v,n+1),pad+'}'])
        else:lines.append(pad+head+v)
    return '\n'.join(lines)
def get(nodes,k):return next(v for x,v in nodes if x==k)
def put(nodes,k,v):
    for i,(x,old) in enumerate(nodes):
        if x==k:nodes[i]=(k,v);return
    nodes.append((k,v))
def read(p):return parse(p.read_text(encoding='utf-8-sig'))
def resolved(rel):return root/rel if (root/rel).exists() else G/rel
def load(rel):return read(resolved(rel))
gd=load('common/doctrines/grand_doctrines/Renko_LUN_grand_doctrines.txt')
sd=load('common/doctrines/subdoctrines/Renko_LUN_service_subdoctrines.txt')
sf=load('common/doctrines/subdoctrines/Renko_LUN_special_forces_subdoctrine.txt')
td=load('common/doctrines/tracks/Renko_LUN_doctrine_tracks.txt')
assert (len(gd),len(sd),len(sf),len(td))==(3,12,1,12)
entries=json.loads(resolved('Reference/Renko_LUN_doctrine_sources.json').read_text(encoding='utf-8'))
def normal(nodes):
    out=[]
    for k,v in nodes:
        if k in ['name','description','available','visible','ai_will_do']:continue
        if k=='track':v=v.removeprefix('Renko_LUN_')
        if k=='tracks':v=[x.removeprefix('Renko_LUN_') for x in v]
        if k=='rewards':v=[(x.removeprefix('Renko_'),normal(y)) for x,y in v]
        elif isinstance(v,list) and k not in ['tracks']:v=normal(v) if all(isinstance(x,tuple) for x in v) else v
        out.append((k,v))
    return out
for e in entries:
    p=J/e['source'];assert hashlib.sha256(p.read_bytes()).hexdigest()==e['source_sha256']
    original=get(read(p),e['source_key']);actual=get({'grand_doctrines':gd,'subdoctrines':sd,'tracks':td}[e['kind']],e['key'])
    assert normal(original)==normal(actual),(e['key'],'effects differ')
for key,node in gd:
    ts=get(node,'tracks');assert len(ts)==4 and len(set(ts))==4
    assert len(get(node,'milestones'))==4
    for tr in ts:assert sum(get(s,'track')==tr for _,s in sd)==1
    assert get(node,'available')==[('original_tag','LUN')]
for key,node in sd:
    assert len(get(node,'rewards'))==5
    assert get(node,'visible')==[('original_tag','LUN')]
    grand=next(k for k,g in gd if get(node,'track') in get(g,'tracks'))
    assert get(node,'available')==[('original_tag','LUN'),('has_doctrine',grand)]
all_new=dict(gd+sd+sf+td)
effects=get(load('common/scripted_effects/Renko_LUN_doctrine_scripted_effects.txt'),'Renko_LUN_select_designated_doctrines')
chosen={};mastery={};grand_by_folder={}
for k,v in effects:
    if k=='set_grand_doctrine':grand_by_folder['special_forces' if v=='special_forces_quality' else get(all_new[v],'folder')]=v
    elif k=='set_sub_doctrine':
        x=dict(v);slot=(x['folder'],int(x['track']));assert slot not in chosen,('track collision',slot)
        chosen[slot]=x['sub_doctrine']
        expected='special_forces_first' if slot[0]=='special_forces' else get(all_new[grand_by_folder[slot[0]]],'tracks')[slot[1]]
        assert get(all_new[x['sub_doctrine']],'track')==expected
    elif k=='add_mastery':
        x=dict(v);assert x['sub_doctrine'] in chosen.values()
        mastery[x['sub_doctrine']]=float(x['amount'])
assert len(chosen)==len(mastery)==13
for key in chosen.values():
    cost=sum(float(dict(v).get('mastery',100)) for _,v in get(all_new[key],'rewards'))
    assert mastery[key]>=cost,(key,cost)
assert set(grand_by_folder)=={'land','naval','air','special_forces'}
special=dict(sf)['Renko_LUN_lunar_host'];assert get(special,'track')=='special_forces_first'
rew=dict(get(special,'rewards'));width=get(get(rew['Renko_assault_cohesion'],'Renko_LUN_invasion_infantry'),'combat_width')
assert width=='-0.2'
terrains={'plains','desert','forest','hills','mountain','jungle','marsh','urban','river','amphibious','fort'}
for _,r in get(special,'rewards'):
    for k,v in r:
        if k.startswith('Renko_LUN_invasion_') and k!='Renko_LUN_invasion_infantry':assert not terrains.intersection(dict(v))
units=dict(get(load('common/units/Renko_LUN_invasion_units.txt'),'sub_units'))
for k in ['Renko_LUN_invasion_medium_armor','Renko_LUN_invasion_medium_tankdestroyer']:
    u=dict(units[k]);assert terrains.intersection(u)=={'plains','desert'}
    for tr in ['plains','desert']:assert dict(u[tr])=={'attack':'0.05','movement':'0.05'}
    baseline=dict(get(read(G/'common/units/Renko_LUN_invasion_units.txt'),'sub_units'))[k]
    assert [(x,v) for x,v in units[k] if x not in terrains]==[(x,v) for x,v in baseline if x not in terrains]
baseunits=dict(get(read(G/'common/units/Renko_LUN_invasion_units.txt'),'sub_units'))
for k in units:
    if k.endswith('_support') or k.endswith('_infantry'):assert units[k]==baseunits[k]
dec=dict(get(load('common/decisions/Renko_LUN_lunar_war_high_command_decisions.txt'),'Renko_LUN_lunar_war_high_command_category'))
d=dict(dec['Renko_LUN_adopt_designated_doctrines']);assert d['fire_only_once']=='yes' and d['cost']=='0'
assert get(d['ai_will_do'],'factor')=='100'
locpath=resolved('localisation/simp_chinese/Renko_LUN_doctrines_l_simp_chinese.yml');locbytes=locpath.read_bytes()
assert locbytes.startswith(b'\xef\xbb\xbf') and b'\r' not in locbytes
locpairs=re.findall(r'^\s*(\w+):0 "([^"\n]*)"$',locbytes.decode('utf-8-sig'),re.M);loc=dict(locpairs)
assert len(locpairs)==len(loc)
for key,n in gd+sd+sf:
    assert get(n,'name') in loc and get(n,'description') in loc
    if ('rewards' in dict(n)):
        for rk,_ in get(n,'rewards'):assert key+'_'+rk in loc and key+'_'+rk+'_desc' in loc
for k,v in loc.items():
    for ref in re.findall(r'\$([^$]+)\$',v):
        assert ref in loc or any(re.search(r'^\s*'+re.escape(ref)+':',p.read_text(encoding='utf-8-sig'),re.M) for p in (V/'localisation/simp_chinese').rglob('*.yml')),ref
    assert v.count('§!')==len(re.findall(r'§[^!]',v)),k
# Verify copied activation fields that refer to actual unit/category/equipment/project/tactic definitions.
definition_text='\n'.join(p.read_text(encoding='utf-8-sig') for base in [V,G] for rel in ['common/units','common/special_projects/projects'] for p in (base/rel).rglob('*.txt'))
tactics='\n'.join((base/'common/combat_tactics.txt').read_text(encoding='utf-8-sig') for base in [V,G] if (base/'common/combat_tactics.txt').exists())
refs=set()
control={'folder','track','tracks','name','description','icon','xp_cost','xp_type','available','visible','ai_will_do','mastery','milestones','rewards','effect','equipment_bonus','modifiers','enable_tactic','max_track_rows','max_track_columns'}
def scan_effect(node):
    for k,v in node:
        if k=='enable_tactic':assert re.search(r'\b'+re.escape(v)+r'\s*=',tactics),v
        if k=='equipment_bonus':
            for eq,_ in v:refs.add(eq)
        elif k=='rewards':
            for _,r in v:scan_effect(r)
        elif k=='milestones':
            for _,r in v:scan_effect(r)
        elif isinstance(v,list) and k not in control:refs.add(k)
for _,node in gd+sd+sf:scan_effect(node)
missing=[k for k in refs if not re.search(r'\b'+re.escape(k)+r'\b',definition_text)]
assert not missing,('missing unit/category/equipment',missing)
gfxtext='\n'.join(p.read_text(encoding='utf-8-sig') for base in [V,G] for p in (base/'interface').rglob('*.gfx'))
for key,node in gd+sd+sf+td:
    for k,v in node:
        if k in ['icon','background','icon_frame','reward_gfx']:
            assert re.search(r'\bname\s*=\s*"?'+re.escape(v.strip('"'))+r'\b',gfxtext),(key,v)
report={'result':'PASS','grand_doctrines':3,'service_subdoctrines':12,'special_subdoctrines':1,'exclusive_tracks':12,'source_effect_comparisons':27,'selected_tracks':13,'mastery_per_subdoctrine':1000,'special_mastery_required':600,'chinese_localisation_keys':len(loc),'references_checked':len(refs),'RuntimeChecks':'NOT RUN'}
print(json.dumps(report,ensure_ascii=False,indent=2))
