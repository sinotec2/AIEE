import os, json
directory = '.'
mom=[]
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
            if "parentname" in data:
                s=data["parentname"]
                if s:mom.append(s)

"""
In [7]: set(mom)
Out[7]:
{
    '環境基本法',
    '環境影響評估法',
    '水污染防治法',
    '空氣污染防制法',
    '廢棄物清理法',
    '土壤及地下水污染整治法',
    '毒性及關注化學物質管理法',
    '溫室氣體減量及管理法',
    '噪音管制法',
    '室內空氣品質管理法',
    '低放射性廢棄物最終處置設施場址設置條例',
    '工廠管理輔導法',
    '放射性物料管理法',
    '民用航空法',
    '海洋污染防治法',
    '游離輻射防護法',
    '災害防救法',
    '石油管理法',
    '科學園區設置管理條例',
    '船舶防止污染國際公約',
    '規費法',
    '野生動物保育法',
    '食品安全衛生管理法',
 }
"""
