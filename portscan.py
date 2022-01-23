import sys
import socket
import time
import threading
print("-"*70)
print("#"*50)
print("simple port scanner build in python by pratv3")
print("#"*50)
print("-"*70)
start_time=time.time()
usage="python3 portscan.py TARGET START_PORT END_PORT"
if len(sys.argv)!=4:
    print(usage)
    sys.exit()
try:
    #reslove name by the dns
    ipaddr=socket.gethostbyname(sys.argv[1])
    print(f"ip address {ipaddr}")
except socket.gaierror:
    # if dns resolving gone fail
    print("DNS does not resolve the name")
    sys.exit()
start_port=int(sys.argv[2])
end_port=int(sys.argv[3])
#dor scanning ports open
def scan_port(port):
    #creation of socket
    s=socket.socket()
    # time out for efficiency and speed
    s.settimeout(2)
    #connection and defining for port open or close
    conn=s.connect_ex((ipaddr,port))
    #condition for the port is open or not
    if conn==0:
        print(f"Port {port} is OPEN")
        #closed the connection nessacary
    s.close()
#used multi threading for speed
for port in range(start_port,end_port+1):
    #multiple threads for the each port
    thread=threading.Thread(target=scan_port,args=(port,))
    thread.start()
end_time=time.time()
print("time elapsed:-",end_time-start_time)