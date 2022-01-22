import sys,os

try:
    Token = sys.argv[1]
except IndexError:
    print (f" [Error] Hey! it looks like you tried to open SF manually, please use StartFirewall.py to open Skrillec Firewall!\n [Debug] Syntax : {sys.argv[0]} Token")
    quit()

class Getz:
    def Credentials():
        r = requests.get("https://pastebin.com/raw/GAhfH330") #<<-- we will use skrillec.pw for our credentials in the future, i do not want to disturb wocky lolz
        r = r.strip()
        return r

class Start:
    def LoginProcess():
        while (True):
            try:
                username = (str(input(" Username : ")))
                password = (str(input(" Password : ")))
                Username = Getz.Credentials()
                Username = Username[0]
                Password = Getz.Credentials()
                Password = Password[1]

                if username != Username & password != Password:
                    print (" [Error] Your username or password is not correct. ")
                else:
                    print (f" [Success] Welcome back {Username}")
                    break
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
    print (" [Success] Welcome to Skrillec Firewall")
    Start.LoginProcess()
else:
    print (" [Error] Please use StartFirewall.py to use Skrillec Firewall.")