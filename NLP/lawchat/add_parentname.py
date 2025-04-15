import os, ollama, json

def olm(s):
    prompt = """
    你是一個資深的律師，習慣台灣的環保法律，使用繁體中文，台灣的母法條文特徵會在第1條敘明法律的目的，子法則會敘明依據哪個母法，並稱母法為"本法"。
    我會給你某個法律的第一條條文。
    請檢查文字中是否"精確"含有甚麼法律名稱，如果有，請回覆我名稱。如果沒有精確的名稱，請回覆我"無"。
    不要臆測、不要解釋、不要說明。
    """
    host="http://l40.sinotech-eng.com:55083"
    model="jcai/llama3-taide-lx-8b-chat-alpha1:f16"
    client = ollama.Client(host=host)
    response = client.chat(
        model=model,
        messages=[
          {'role': 'user', 'content': f"{prompt}以下是第一條的條文內容：{s}"}
        ]
    )
    if response:
        return response.message.content.replace('\n','')
    else:
        return None
directory='./'
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
            if "codes" in data:
                s=olm(data["codes"]['第 1 條']).replace('。','')
                if len(s)<2:
                    data.update({"parentname":False})
                else:
                    data.update({"parentname":s.replace('汙','污')})
                    with open(file_path, 'w') as f:
                        json.dump(data,f)
