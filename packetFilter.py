import pydivert
x = 0
with pydivert.WinDivert("tcp.SrcPort = 443 and tcp.DstPort") as w:
    for packet in w:   
        x = x+1    
        #w.send(packet)