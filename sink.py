import sys,json,os
from pathlib import Path
root=Path(sys.argv[1]);root.mkdir(exist_ok=True)
for line in sys.stdin:
    notice=json.loads(line)
    with (root/'receipt.jsonl').open('a') as f:f.write(json.dumps(notice)+'\n');f.flush();os.fsync(f.fileno())
    print(json.dumps({'ok':True}),flush=True)
