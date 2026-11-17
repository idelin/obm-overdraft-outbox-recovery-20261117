import json,sys,time
from pathlib import Path
from ledger import Ledger
root=Path(sys.argv[1]);root.mkdir(exist_ok=True);ledger=Ledger();offset=0
while True:
    path=root/'spool.jsonl'
    if path.exists():
        with path.open() as f:
            f.seek(offset)
            while True:
                line=f.readline()
                if not line:break
                event=json.loads(line);notice=ledger.apply(event);offset=f.tell()
                if notice:print(json.dumps(notice),flush=True)
    time.sleep(.02)
