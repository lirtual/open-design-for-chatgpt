#!/usr/bin/env python3
"""Check published skills-only sources at the user-facing file boundaries."""
from pathlib import Path
from html.parser import HTMLParser
import json, re, sys, yaml

root=Path(__file__).resolve().parents[1]
skills={'design-brief','design-system','ui-prototype','design-refine','design-review'}
problems=[]
m=json.loads((root/'plugin.json').read_text())
assert m['$schema']=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
assert m['name']=='open-design-for-chatgpt'
iface=m['extensions']['com.openai']['interface']
assert iface['category']=='Creativity' and len(iface['shortDescription'])<=30
assert {p.parent.name for p in (root/'skills').glob('*/SKILL.md')}==skills

for name in sorted(skills):
    directory=root/'skills'/name
    s=(directory/'SKILL.md').read_text()
    assert s.startswith('---\n') and s.count('---')>=2, name
    front=yaml.safe_load(s.split('---',2)[1])
    assert front['name']==name and front['description'], name
    assert (directory/'SKILL.md').stat().st_size<=1048576, name
    agent=yaml.safe_load((directory/'agents/openai.yaml').read_text())
    assert agent['policy']['allow_implicit_invocation'] is False, name
    for doc in directory.rglob('*.md'):
        content=doc.read_text()
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
            if '://' in target or target.startswith('#'):continue
            file=(doc.parent/target.split('#')[0]).resolve()
            if not file.is_relative_to(root) or not file.is_file(): problems.append(f'bad link {doc.relative_to(root)} -> {target}')

class Doc(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=set();self.refs=[];self.viewport=False;self.main=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='main':self.main=True
        if tag=='meta' and a.get('name')=='viewport':self.viewport=True
        for n in ('src','href','action'):
            if re.match(r'(?i)^(https?:)?//|javascript:',a.get(n,'')):problems.append(f'external URL: {a[n]}')
        if tag=='a' and a.get('href','').startswith('#'):self.refs.append(a['href'][1:])
templates=root/'skills/ui-prototype/assets'
assert {p.stem for p in templates.glob('*.html')}=={'web-prototype','saas-landing','dashboard','mobile-app','wireframe-greybox'}
for file in templates.glob('*.html'):
    text=file.read_text()
    d=Doc();d.feed(text)
    if not(d.viewport and d.main):problems.append(f'bad HTML: {file.name}')
    if not set(d.refs).issubset(d.ids):problems.append(f'bad anchors: {file.name}')
    if re.search(r'<artifact|data-od-id|od brand preview',text,re.I):problems.append(f'OpenDesign-only output: {file.name}')
assert {p.stem for p in (root/'skills/design-system/references/systems').glob('*.md')}=={'default','minimal','bento','editorial','enterprise','brutalism'}
for unwanted in ('mcp.json','.app.json','apps','node_modules'):
    if (root/unwanted).exists():problems.append(f'Unexpected service: {unwanted}')
if problems:
    print('\n'.join('FAIL '+p for p in problems));sys.exit(1)
print('PASS: 5 skills, 5 prototypes, 6 systems, references, invocation policy, HTML security')
