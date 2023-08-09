import wget
import platform
import scapy.all as scapy
import os

def scan(ip):
        scapy.arping(ip)

print(platform.platform())

if "windows" in platform.platform().lower():
    
    npcap = "https://npcap.com/dist/npcap-1.76.exe"

    if not os.path.exists("npcap-1.76.exe"):
        wget.download(npcap, "./")
    else:
        print("[-] File WinPcap NOT dowloaded, it already exists in directory\n")

    print("\n[info] Run to npcap.exe file in order to able capture packets")

    npcap_installed = input("[?] Did you install npcap-1.76.exe? y/n? (Packet capturewill not not if you didn't)")

    if npcap_installed.lower() == "y":
        ip = input("Ip>")
        scan(ip)
        input("Any key to QUIT:")
    elif npcap_installed.lower() == "n":
        print("Run to npcap-1.76.exe file in order to able capture packets")
else:
    ip = input("Ip>")
    scan(ip)