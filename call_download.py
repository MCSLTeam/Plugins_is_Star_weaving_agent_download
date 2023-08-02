import requests
import subprocess
import json
import base64
import time
print(
'''
 ___  ____   __    ____    _    _  ____    __  _  _  ____  _  _  ___ 
/ __)(_  _) /__\  (  _ \  ( \/\/ )( ___)  /__\( \/ )(_  _)( \( )/ __)
\__ \  )(  /(__)\  )   /   )    (  )__)  /(__)\\  /  _)(_  )  (( (_-.
(___/ (__)(__)(__)(_)\_)  (__/\__)(____)(__)(__)\/  (____)(_)\_)\___/
  /__\  / __)( ___)( \( )(_  _)                                      
 /(__)\( (_-. )__)  )  (   )(                                        
(__)(__)\___/(____)(_)\_)_(__)    _____    __    ____                
(  _ \(  _  )( \/\/ )( \( )(  )  (  _  )  /__\  (  _ \               
 )(_) ))(_)(  )    (  )  (  )(__  )(_)(  /(__)\  )(_) )              
(____/(_____)(__/\__)(_)\_)(____)(_____)(__)(__)(____/                                                      
星织代理下载

作者:星织
博客:https://www.df100.ltd/
请输入url下载您想要的文件
支持域名:civitai.com，github.com
'''
)
def b64encode(s):
    return str(base64.b64encode(s.encode("utf-8")), "utf-8")

def CALLING_RELATIONSHIP(CALLDICT,CALLSTR):
    CALLDICT[CALLSTR]()

def d(url):
    print('服务器下载完成,开始下载至本地')
    url = f'http://swad.df100.ltd/api/download?url={url}'
    r = json.loads(requests.get(url).text)
    file_name = r['file_name']
    file_url = r['url']
    cmd= f'.\Plugins\Star_weaving_agent_download\\aria2c.exe --console-log-level=error -c -x 16 -s 16 {file_url} -o {file_name}'
    complete = subprocess.call(cmd, shell=True)
    print('下载完成')

def r_api(apiname,url):
    return requests.get(f'http://swad.df100.ltd/api/{apiname}?url={url}')

def new_d():
    url = b64encode(input('url:'))
    r = r_api('new-download',url)
    print(r.text)
    if ('Download completed' in r.text):
        print('服务器下载完成,开始下载至本地')
        d(url)
        return True
    elif ('Start downloading' in r.text):
        print('服务器开始下载')
        while True:
            r = r_api('new-download',url)
            print(r.text)
            if ('Download completed' in r.text):
                time.sleep(1)
                d(url)
                return True
            time.sleep(1)
    elif ('Queuing, you are in position' in r.text):
        while True:
            url = r_api('new-download',url)
            r = requests.get(url)
            if ('Queuing, you are in position' in r.text):
                print('排队中,排在第 '+r.text.replace('Queuing, you are in position','')+'位')
            elif('Start downloading' in r.text):
                print('服务器开始下载')
                while True:
                    url = r_api('new-download',url)
                    r = requests.get(url)
                    if ('Download completed' in r.text):
                        time.time(1)
                        d(url)
                        return True
                    time.sleep(1)
            time.sleep(1)
while True:
    new_d()