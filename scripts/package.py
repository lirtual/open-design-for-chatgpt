#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import subprocess
import json
root=Path(__file__).resolve().parents[1]
subprocess.run(['python3',str(root/'scripts/check.py')],check=True)
d=root/'dist';d.mkdir(exist_ok=True)
manifest=json.loads((root/'plugin.json').read_text())
p=d/(manifest['name']+'-'+manifest['version']+'.zip')
base_files=['plugin.json','LICENSE','ATTRIBUTION.md']
skill_entries=list((root/'skills').rglob('*'))
if (root/'skills').is_symlink() or any(x.is_symlink() for x in skill_entries + [root/x for x in base_files]):
    raise SystemExit('Refusing to package symlinked source files or directories')
f=base_files + [str(x.relative_to(root)) for x in skill_entries if x.is_file() and '__pycache__' not in str(x)]
with ZipFile(p,'w',ZIP_DEFLATED) as z:
    for x in sorted(f):z.write(root/x,arcname=manifest['name']+'/'+x)
with ZipFile(p) as z:
    expected={manifest['name']+'/'+x for x in f}
    assert set(z.namelist())==expected, 'Package file list does not match source inputs'
    assert json.loads(z.read(manifest['name']+'/plugin.json'))==manifest, 'Packaged manifest mismatch'
print(p)
