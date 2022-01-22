from Modules.bw               import *
from Modules.MakeRandomHash   import *
from Modules.GenerateToken    import *
from Modules.ReadToken        import *
from Modules.CreateURL        import *
from colorama import Fore, Back, Style
try:
    import requests,os,platform,random,time,wget
except:
    os.system("pip install requests,random,wget,colorama")

NeedsToUpdate = True
count         = 1

class getOperating:
    def system():
        return platform.system().strip().replace("'", "")

class UpdateService:
    def UPDATE():
        global NeedsToUpdate,count
        GetCommand = Get.Command(getOperating.system())
        while NeedsToUpdate == (True):
            if count > 10:
                generateRandomHash = randomz.hashing()
                time.sleep(0.5)
                print (f" Updater couldn't update Skrillec Firewall, please try again later. If this keeps happening please contact the owners.\n {generateRandomHash}")
                break
            os.system(GetCommand)
            print (f" Fetching update files [", "*" * count, "]")
            #m = requests.get("http://skrillec.pw/updatereq", timeout=100).text
            m = "True"
            match m:
                case "False":
                    NeedsToUpdate = False
                    count += 1
                    # Start the actual application with the 'CanOpen' token which will not let people in if that token is not valid.
                    GenerateOpenToken = Generate.Token()
                    print (f" [Success] Generated a login token with {count-1} requests.")
                    time.sleep(2)
                    for x in range(1,10):
                        time.sleep(0.3)
                        os.system(GetCommand)
                        print (f" [{Fore.YELLOW}Loading{Style.RESET_ALL}] Skrillec Firewall", "." * x)
                    time.sleep(1)
                    os.system(GetCommand)
                    try:
                        os.system(f'python firewall.py "{Read.token()}"')
                    except:
                        print (f" [{Fore.RED}Error{Style.RESET_ALL}] The file was not found, please contact the owners.")

                case _:
                    NeedsToUpdate = True
                    try:
                        #os.remove("vProtector.py")
                        print (qwiehqweh) # force a error for no literal reason lol
                    except: #FileNotFoundError:
                        print (f" [{Fore.RED}Error{Style.RESET_ALL}] firewall.py was not found... {Fore.GREEN}skipping.{Style.RESET_ALL}")
                    url     = "http://skrillec.pw/updatereq"

                    try:
                        #os.system(f"curl -s {url} -o vProtector.py")
                        GenerateOpenToken = Generate.Token()
                        print (f" [{Fore.GREEN}Success{Style.RESET_ALL}] Generated a login token")
                        time.sleep(1)
                        print (f" [{Fore.GREEN}Success{Style.RESET_ALL}] Updated.\n {Fore.YELLOW}>{Style.RESET_ALL} {url}")
                        print (" --------------------------------------------------")
                        time.sleep(1)
                        os.system(f'python firewall.py "{Read.token()}"')
                        break
                    except:
                        print (f" [{Fore.RED}Error{Style.RESET_ALL}] Couldn't download update.\n --> Exit code 921")
                        break
                    break


UpdateService.UPDATE()
