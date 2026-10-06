from datetime import datetime
from app.matching import match
class Store:
 def __init__(self):self.tenders={};self.runs=[]
 def ingest(self,source,rows):
  count=0
  for t in rows:
   t.category,t.score,hits=match(' '.join([t.title,t.description]+[i.description for i in t.items]))
   for i in t.items:i.matched_terms=hits
   if t.score>=25:self.tenders[t.id]=t;count+=1
  self.runs.insert(0,{'source':source,'status':'ok','imported':count,'at':datetime.utcnow(),'error':''});self.runs=self.runs[:8];return count
 def error(self,source,e):self.runs.insert(0,{'source':source,'status':'error','imported':0,'at':datetime.utcnow(),'error':f'{type(e).__name__}: {e}'})
store=Store()
