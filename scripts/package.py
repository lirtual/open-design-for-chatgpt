#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import subprocess
root=Path(__file__).resolve().parents[1]
subprocess.run(['python3',str(root/'scripts/check.py')],check=True)
d=root/'dist';d.mkdir(exist_ok=True)
p=d/'open-design-for-chatgpt-0.1.1.zip'
f=['plugin.json','LICENSE','ATTRIBUTION.md'] + [str(x.relative_to(root)) for x in (root/'skills').rglob('*') if x.is_file() and '__pycache__' not in str(x)]
with ZipFile(p,'w',ZIP_DEFLATED) as z:
    for x in sorted(f):z.write(root/x,arcname='open-design-for-chatgpt/'+x)
print(p)
