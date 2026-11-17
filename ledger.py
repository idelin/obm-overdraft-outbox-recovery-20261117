class Ledger:
    def __init__(self):self.balances={}
    def apply(self,event):
        key=(event['account'],event['currency']);before=self.balances.get(key,0)
        after=before+event.get('amount',0);self.balances[key]=after
        if before>=0 and after<0:
            return {'event_id':event['id']+':ENTER','account':key[0],'currency':key[1],'seq':event['seq'],'kind':'ENTER','available':after}
        return None
