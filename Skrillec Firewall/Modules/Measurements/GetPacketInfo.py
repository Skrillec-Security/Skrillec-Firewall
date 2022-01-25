import time,subprocess



# ValueError <-- You have to use linux to rrreeennna
class GetCurrent:

    old_rx = 0
    old_tx = 0
    new_rx = 0
    new_tx = 0
    final_rx = 0
    final_tx = 0
    pps = 0

    def set_old(rx, tx):
        GetCurrent.old_rx = rx
        GetCurrent.old_tx = tx

    def set_new(rx, tx):
        GetCurrent.new_rx = rx
        GetCurrent.new_tx = tx
    
    def get_pps():
        GetCurrent.final_rx = GetCurrent.old_rx - GetCurrent.new_rx
        GetCurrent.final_tx = GetCurrent.old_tx - GetCurrent.new_tx
        GetCurrent.pps = GetCurrent.final_tx - GetCurrent.final_rx

    def Interface():
        WiFi_Interface = subprocess.getoutput("ifconfig").split().strip().replace(":", "")[0]
        return WiFi_Interface

    def tx_packets():
        Interface = GetCurrent.Interface()
        return (subprocess.getoutput(f"cat /sys/class/net/{str(Interface)}/statistics/tx_packets"))

    def rx_packets():
        Interface = GetCurrent.Interface()
        return (subprocess.getoutput(f"cat /sys/class/net/{str(Interface)}/statistics/rx_packets"))

    def pps():
        GetCurrent.set_old(GetCurrent.rx_packets(), GetCurrent.tx_packets())
        time.sleep(1)
        GetCurrent.set_new(GetCurrent.rx_packets(), GetCurrent.tx_packets())
        current_pps = GetCurrent.get_pps()
        return current_pps
