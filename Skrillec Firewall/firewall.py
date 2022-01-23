import sys,os,requests,time,json,platform,requests,subprocess,random
from Modules.Measurements.GetPacketInfo import *
from colorama import Fore, Back, Style
from Modules.bw               import *
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

class getOperating:
    def system():
        return platform.system().strip().replace("'", "")

Loading = ['|', '/', '-', '|', '-', '\\', '|']
GetCommand = Get.Command(getOperating.system())
BlackListedIPS = ['45.41.240.111']


class Drop:
    def IPss(ID):
        global BlackListedIPS
        BlackListedIPCOunt = 0
        with open(f"/root/SkrillecFirewall/Dumps/{ID}.txt", "r") as IPS:
            IPS = IPS.read().splitlines()
            print("")
            for sex in IPS:
                if any(lolz in sex for lolz in BlackListedIPS):
                    print (f" [{Fore.GREEN}SF{Style.RESET_ALL}] Skipped over Blacklisted IP. {BlackListedIPCOunt} Times.")
                    BlackListedIPCOunt += 1
                    pass
                else:
                    os.system(f"ipset -A SkrillecFirewall {sex}")
                    print (f" [{Fore.RED}-{Style.RESET_ALL}] Successfully dropped IP [{sex}] -> Sleeping for 0.5 seconds.")
                    time.sleep(0.5)
class Capture:
    def IPs(CapturingID):
        # 22 is the SSH port, we will make it into the config.
        for x in range (20):
            os.system("netstat -tn 2>/dev/null | grep :22 | awk '{print $5}' | cut -d: -f1 | sort | uniq | sort -nr >> /root/SkrillecFirewall/Dumps/"+CapturingID+".txt")
            time.sleep(0.5) # < -- Give it some time.

class StartSkrillec:
    def Main(username):
        global GetCommand
        Counter = 0
        os.system(GetCommand)
        #try:
        print(f" [{Fore.GREEN}SF{Style.RESET_ALL}] Hello {username} and welcome to Skrillec Firewall.\n [{Fore.YELLOW}>{Style.RESET_ALL}] Your current PPS is [",GetCurrent.pps(),f"]\n [{Fore.BLUE}Prompt{Style.RESET_ALL}] Skrillec is starting in 5 seconds. ")
        time.sleep(5)
        while (True):
            os.system(GetCommand)
            Packets_Per_Second = 1001#GetCurrent.pps()
            time.sleep(0.5) # < -- Give it some time so the pps can be accurate.
            if Packets_Per_Second > 1000: #< --- Threshold.
                CapturingID = str(random.randint(1,100))
                DumpingID   = str(random.randint(1,100))
                os.system(f"screen -dmS -X tcpdump -w /root/{DumpingID}.pcap -c 3000")
                print (f" [{Fore.RED}Alert{Style.RESET_ALL}] Skrillec Firewall -> Detected a new DDoS Attack | {Packets_Per_Second} Peak  [TCPDUMP, IP-LOG]\n [{Fore.GREEN}Details{Style.RESET_ALL} The dump will be saved to /root/SkrillecFirewall/Dumps/{DumpingID}.")
                print (f" [{Fore.RED}Alert{Style.RESET_ALL}] Skrillec Firewall -> Capturing IP's.\n [{Fore.GREEN}Details{Style.RESET_ALL}] The dump will be saved to root/SkrillecFirewall/CapturedIPS/{CapturingID}")
                Capture.IPs(CapturingID)
                print (f" [{Fore.GREEN}Success{Style.RESET_ALL}] Skrillec Firewall Successfully saved Captured IPS.")
                print (f" [{Fore.GREEN}Alert{Style.RESET_ALL}] Using Courvix API to analyze attack #{CapturingID}@{DumpingID}")
                GetJSONRequest = subprocess.getoutput(f'curl -X POST -H "Content-Type: multipart/form-data" -F capture=@{DumpingID}.pcap https://api.courvix.com/attack/analyze')
                time.sleep(1)
                Drop.IPss(CapturingID)
                time.sleep(50)
                
            else:
                print (f" [{Fore.GREEN}Idle{Style.RESET_ALL}] Skrillec Firewall -> Listening. | {GetCurrent.pps()} Packets Per Second")
                time.sleep(5)

        #except:
        #    print(f" [{Fore.RED}Error{Style.RESET_ALL}] Sorry, but there was an error when fetching Packets Per second, please make sure you run Skrillec Firewall with Root privileges.")

class Start:
    def LoginProcess():
        global Loading,GetCommand
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
                        os.system(GetCommand)
                        print (f" [{Fore.YELLOW}Loading{Style.RESET_ALL}] Please wait while we install all the requirments for your server. [",Loading[x],']' )
                        time.sleep(1)
                    # Install the actual requirments here so it doesn't do it 6 times.
                    StartSkrillec.Main(username)
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
