#kuang@eng06 /nas2/kuang/MyPrograms/query_anything
#$ cat add_users.py
import os,sys,json
from pandas import *
fname='allname.csv'
df=read_csv(fname)

EmpNo2EmailName={int(i):j for i,j in zip(list(df.EmpNo),list(df.EmailName))}

fname='group.csv'
dfg=read_csv(fname)

grps=set(list(dfg['組別名稱']))
with open('grpsvr.json','r') as f:
    grpsvr=json.load(f)

cmd="curl -X 'POST' \
   'http://eng06.sinotech-eng.com:PORT/api/v1/admin/users/new' \
   -H 'accept: application/json' \
   -H 'Authorization: Bearer ***' \
   -H 'Content-Type: application/json' \
   -d '{  \"username\":\"NAME\",\"password\":\"PASSWORD\",\"role\":\"manager\" }'"

eg={}
for g in grpsvr:
    dfi=dfg.loc[dfg['組別名稱']==g]
    for e in list(dfi.EmpNo):
        if int(e) not in EmpNo2EmailName:continue
        name=EmpNo2EmailName[int(e)]
        passwd=str(int(e))+str(int(e))
        a=cmd.replace('PORT',grpsvr[g]).replace("NAME",name).replace("PASSWORD",passwd)
        os.system(a)
        eg.update({int(e):g})
    print(g)

df['grp']=''
df['svr']=''
a=list(df.loc[df.EmpNo.map(lambda x: x in eg),'EmpNo'])
df.loc[df.EmpNo.map(lambda x: x in eg),'grp']=[eg[e] for e in a]

a=list(df.loc[df.grp.map(lambda x: x in grpsvr),'grp'])
df.loc[df.grp.map(lambda x: x in grpsvr),'svr']=[grpsvr[i] for i in a]

a=df.loc[df.grp.map(lambda x: x in grpsvr)].index
dfi=df.loc[a]
col=['EmpNo','EmpName','DeptName','Email','grp','svr']

dfi[col].set_index('EmpNo').to_csv('grp_svr.csv')
