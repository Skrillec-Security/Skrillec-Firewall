import time,subprocess



# ValueError <-- You have to use linux to rrreeennna
class GetCurrent:
    def Interface():
        WiFi_Interface = subprocess.getoutput("ifconfig")
        WiFi_Interface = WiFi_Interface.strip().replace(":", "")
        return WiFi_Interface
    
    def tx_packets():
        Interface = GetCurrent.Interface()
        return (subprocess.getoutput(int(f"cat /sys/class/net/{Interface}/statistics/rx_packets")))
    
    def rx_packets():
        Interface = GetCurrent.Interface()
        return (subprocess.getoutput(int(f"cat /sys/class/net/{Interface}/statistics/rx_packets")))
    def pps():
        x = GetCurrent.rx_packets()
        y = GetCurrent.tx_packets()
        PPS = rx_packets - tx_packets
        return PPS