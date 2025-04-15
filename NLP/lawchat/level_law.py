from bs4 import BeautifulSoup
import re
import pandas as pd

def parse_law_by_chapter(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    content = soup.select_one("div.law-reg-content")

    current_chapter = None #章
    current_article = None #條
    current_item = None #項：指得是段落
    current_clause = None #款：一、二、
    current_points = None #目：(一)(二)

    results = []

    for tag in content.find_all(recursive=False):
        # 更新章
        if tag.name == "div" and "h3" in tag.get("class", []):
            current_chapter = tag.get_text(strip=True)
            continue

        # 條文段落
        if tag.name == "div" and "row" in tag.get("class", []):
            article_tag = tag.select_one(".col-no a")
            if article_tag:
                current_article = article_tag.get_text(strip=True)
                current_clause = None
                current_points = None

            law_article = tag.select_one(".law-article")
            if not law_article:
                continue

            for line in law_article.select("div"):
                line_text = line.get_text(strip=True)
                if not line_text:
                    continue

                # 款：「一、」開頭
                clause_match = re.match(r"^([一二三四五六七八九十百]+)、", line_text)
                if clause_match:
                    current_clause = clause_match.group(0)
                    current_points = None
                    results.append({
                        "章": current_chapter,
                        "條": current_article,
                        "項": None,
                        "款": current_clause,
                        "目": None,
                        "原文": line_text
                    })
                    continue

                # 款：「（一）」開頭
                points_match = re.match(r"^（[一二三四五六七八九十百]+）", line_text)
                if points_match:
                    current_points = points_match.group(0)
                    results.append({
                        "章": current_chapter,
                        "條": current_article,
                        "項": None,
                        "款": current_clause,
                        "目": current_points,
                        "原文": line_text
                    })
                    continue

                # 一般條文（無項或款）
                results.append({
                    "章": current_chapter,
                    "條": current_article,
                    "項": None,
                    "款": current_clause,
                    "目": current_points,
                    "原文": line_text
                })
    df=pd.DataFrame({
        'chapter':[i['章'] for i in results],
        'article':[i['條'] for i in results],
        'clause':[i['款'] for i in results],
        'points':[i['目'] for i in results],
        'codes':[i['原文'] for i in results],
        })
    df['item']=None
    chaps=set(df.chapter)
    for c in chaps:
        rules=set(df.loc[df.chapter==c,'article'])
        for r in rules:
            boo=(df.chapter==c) & ( df.article==r)
            cr=df.loc[boo].index
            if len(cr)<=1:continue
            itm=1
            df.loc[cr[0],'item']=itm
            for i in cr[1:]:
                if not(df.loc[i,'clause'] or df.loc[i,'points']): itm+=1
                df.loc[i,'item']=itm
    return df

fname="空氣污染防制法.html"
with open(fname,'r') as f:
    df=parse_law_by_chapter(f)
df.to_csv(fname.replace('html','csv'),index=False)    
