#实现一个Plugin类
from Adapters.Plugin import Plugin
Star_weaving_agent_download = Plugin() 
def load():
    """写你的代码"""
    print("load")
#注册加载代码
Star_weaving_agent_download.register_loadFunc(load)
def enable():
    """写你的代码"""
    import subprocess
    complete = subprocess.call('start cmd /k .\Plugins\Star_weaving_agent_download\call_download.exe', shell=True)
#注册应用代码
Star_weaving_agent_download.register_enableFunc(enable)
def disable():
    """写你的代码"""
    print("disable")
#注册应用代码
Star_weaving_agent_download.register_disableFunc(disable)