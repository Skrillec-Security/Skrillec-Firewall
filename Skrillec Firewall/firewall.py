import sys,os,requests,time
from colorama import Fore, Back, Style

try:
    Token = sys.argv[1]
except IndexError:
    print (f" [Error] Hey! it looks like you tried to open SF manually, please use StartFirewall.py to open Skrillec Firewall!\n [Debug] Syntax : {sys.argv[0]} Token")
    quit()

class Getz:
    def Credentials():
        r = requests.get("https://pastebin.com/raw/GAhfH330").text #<<-- we will use skrillec.pw for our credentials in the future, i do not want to disturb wocky lolz
        r = r.split()
        return r

Loading = ['|', '/', '-', '|', '-', '\\', '|']

class Start:
    def LoginProcess():
        global Loading
        while (True):
            try:
                username = (str(input(f"{Style.RESET_ALL} [{Fore.BLUE}SF{Style.RESET_ALL}] Username : ")))
                password = (str(input(f"{Style.RESET_ALL} [{Fore.BLUE}SF{Style.RESET_ALL}] Password : ")))

                Username = Getz.Credentials()
                Username = Username[0]

                Password = Getz.Credentials()
                Password = Password[1]

                if username != Username and password != Password:
                    print (" [Error] Your username or password is not correct. ")
                    quit()
                else:
                    print (f" [{Fore.GREEN}Success{Style.RESET_ALL}] Welcome back {username}")
                    time.sleep(0.5)
                    for x in range(1,7):
                        os.system("cls")
                        print (f" [{Fore.YELLOW}Loading{Style.RESET_ALL}] Please wait while we install all the requirments for your server. [",Loading[x],']' )
                        time.sleep(1)
                    # Install the actual requirments here so it doesn't do it 6 times.
                    break #<<-- just for now.
            except KeyboardInterrupt:
                print (" [Exit] Exiting.")
                break


class CheckAuth:
    def Authorize():
        global Token
        try:
            AuthToken = open("Modules\\0qw8ieos\\819iojIWSJdkskj.temp", "r").readline()
        except FileNotFoundError:
            return False
        if AuthToken == Token:
            return True
        else:
            return False


if CheckAuth.Authorize() == True:
    os.remove("Modules\\0qw8ieos\\819iojIWSJdkskj.temp")
    print (f" [{Fore.GREEN}Success{Style.RESET_ALL}] Welcome to Skrillec Firewall")
    Start.LoginProcess()
else:
    print (" [Error] Please use StartFirewall.py to use Skrillec Firewall.")
