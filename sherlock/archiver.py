import shutil
import os

from colorama import Style, Fore, init

class Archiver():
    def __init__(self, username):
        self.username = username 
        init(autoreset=True)

    def archive_zip(self):
        shutil.make_archive(self.username, 'zip', self.username)
        print((Style.BRIGHT + Fore.YELLOW + "Zipping " + Fore.GREEN + self.username + ".zip" + Fore.YELLOW + " in current directory"))

    def archive_zip_only(self):
        shutil.make_archive(self.username, 'zip', self.username)
        print((Style.BRIGHT + Fore.YELLOW + "Zipping Only " + Fore.GREEN + self.username + ".zip" + Fore.YELLOW + " in current directory [Output folders have been delete]"))
        shutil.rmtree(self.username)