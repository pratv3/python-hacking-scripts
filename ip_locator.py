import os
import requests
import socket as s
import geocoder
os.system("figlet Geolocator")
print("###############\nBuild by pratv3\n#############")

o=input("[+]which platform you are using\n1.android\n2.Linux:\n")
if o=="1":
    os.system("apt install w3m -y")
elif o=="2":
    os.system("sudo apt-get install w3m -y")
os.system("pip install geocoder")
k=input("[+]enter the website name without http or https or html tag:--)")
url=(f"http://{k}/")
l=s.gethostbyname(k)
print(f"[*] ip address of the site is {l}")
try:
    p=(requests.get(url))
    print("[*] the website is active")
    print("[+]getting location of the target")
    g=geocoder.ip(l)
    print(g.latlng)
except :
    print("[!] the website is unreachable")
l=input("[!] do you want a recurcive scan on the ip address(y/n)")
if l=="y":
    print("[+] detecting open ports and vulnerablity assesment strategies")
    if o=="2":
        n=os.system(f"sudo nmap -sS  -T4 -vvvv -O -A {l}")
    elif o=="1":
        print("[!]OS Detection and stealth scan disable requires root privilages")
    print("[+] gathering browserleaks info")
    os.system(f"w3m https://browserleaks.com/ip/{l}")
elif l=="n":
    print("[!]exiting the program:(done by user)")


