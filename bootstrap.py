import sys,json
from pathlib import Path
from ledger import Ledger
root=Path(sys.argv[1]);root.mkdir(exist_ok=True);ledger=Ledger();path=root/'spool.jsonl'
if path.exists():
    with path.open() as stream:
        for line in stream:ledger.apply(json.loads(line))
(root/'bootstrap.json').write_text(json.dumps({'balances':[[*key,value] for key,value in ledger.balances.items()],'offset':path.stat().st_size if path.exists() else 0}))
