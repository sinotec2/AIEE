#kuang@node01 /nas2/kuang/MyPrograms/query_anything
#$ cat time_ser.py

from pandas import *
import os

def str2int(s):
    if type(s)==int:return s
    return int(s.replace('+','').replace(',',''))

fnames=os.popen('ls any*.csv').read().split('\n')

fname='group.csv'
df=read_csv(fname)
grp_dpt={i:j for i,j in zip(df.組別名稱,df.DeptName) if j != '環境工程部'}
grp_dpt.update({'環評組':"環評部","風機組":"環評部","空品組":"永續部","碳管組":"永續部","土水組":"循環部","管線組":"水務部","廠站組":"水務部","場廠組(興建)":"能資部"
,"場廠組(營管)":"能資部","廢棄物組":"循環部"})

dfs=[]
for fname in fnames[:-1]:
    df=read_csv(fname)
    d=fname.split('.')[0][3:]
    df['date']=d[:4]+'-'+d[4:6]+'-'+d[6:8]
    dfs.append(df)
df0=concat(dfs)

for s in ["合計","小幫手"]:
    idx=df0.loc[df0.分組==s].index
    df0=df0.drop(idx)
for c in ["Unnamed: 0","port"]:
    del df0[c]
df0['部門']=[grp_dpt[i] for i in df0.分組]
col=df0.columns
for c in col[1:4]:
    df0[c]=[str2int(s) for s in df0[c]]

df0.set_index('date').to_csv('time_srs.csv')
