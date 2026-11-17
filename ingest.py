import json,sys,os
from pathlib import Path
root=Path(sys.argv[1]);root.mkdir(exist_ok=True);path=root/'spool.jsonl';seq=0
if path.exists():
    with path.open() as f:
        for line in f:seq=json.loads(line)['seq']
for line in sys.stdin:
    event=json.loads(line);seq+=1;event['seq']=seq
    with path.open('a') as f:f.write(json.dumps(event)+'\n');f.flush();os.fsync(f.fileno())
    print(json.dumps({'seq':seq}),flush=True)
