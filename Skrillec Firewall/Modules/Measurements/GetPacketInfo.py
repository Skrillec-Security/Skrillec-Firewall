import time,subprocess



# ValueError <-- You have to use linux to rrreeennna
class GetCurrent:
    def Interface():
        WiFi_Interface = subprocess.getoutput("ifconfig").split()[0]
        WiFi_Interface = WiFi_Interface.strip().replace(":", "")
        return WiFi_Interface
    
    def tx_packets():
        Interface = GetCurrent.Interface()
        return (subprocess.getoutput(f"cat /sys/class/net/{str(Interface)}/statistics/tx_packets"))
    
    def rx_packets():
        Interface = GetCurrent.Interface()
        return (subprocess.getoutput(f"cat /sys/class/net/{str(Interface)}/statistics/rx_packets"))

    def pps():
        x = (int(GetCurrent.rx_packets()))
        y = (int(GetCurrent.tx_packets()))
        PPS = x / y
        PPS = round(PPS)
        return PPS
