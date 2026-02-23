import requests
import json


banners = """
oooooooooo.   ooooo     ooo   .oooooo.        ooooooooooooo ooooo   ooooo       .o.       ooooo      ooo   .oooooo.    
`888'   `Y8b  `888'     `8'  d8P'  `Y8b       8'   888   `8 `888'   `888'      .888.      `888b.     `8'  d8P'  `Y8b   
 888      888  888       8  888                    888       888     888      .8"888.      8 `88b.    8  888           
 888      888  888       8  888                    888       888ooooo888     .8' `888.     8   `88b.  8  888           
 888      888  888       8  888                    888       888     888    .88ooo8888.    8     `88b.8  888     ooooo  
 888     d88'  `88.    .8'  `88b    ooo            888       888     888   .8'     `888.   8       `888  `88.    .88'  
o888bood8P'      `YbodP'     `Y8bood8P'           o888o     o888o   o888o o88o     o8888o o8o        `8   `Y8bood8P'   
                                                                                                                      
"""
print(banners)

thongtin = f"""
------------------------------------------
Coder By: Nguyen Duc Thang
Tele: @vodanh89
------------------------------------------
"""

# Cách in ra màn hình

print('\x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗')
print('\x1b[38;5;208m║ \x1b[38;5;207mTele: @vodanh89                                              \x1b[38;5;207m ║')
print('\x1b[38;5;208m║ \x1b[38;5;99mCode By: Nguyen Duc Thang                                    \x1b[38;5;207m ║')
print('\x1b[38;5;208m║ \x1b[38;5;26mVision 1.0                                                   \x1b[38;5;207m ║')
print('\x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝')
print('\x1b[38;5;46m-----------------------------------------------------------------')
def banner():
    print('[0m', end='')
    clear()
    a = Colorate.Horizontal(Colors.blue_to_green, banners)
    print(a)
    print(thongtin)
    vanlong(17)


LOGIN_URL = "https://tuongtaccheo.com/login.php"
TANGXU_URL = "https://tuongtaccheo.com/caidat/tangxu.php"

username = input("Tài khoản: ")
password = input("Mật khẩu: ")

usernhan = input("Tài khoản người nhận: ")
passnicktang = input("Mật khẩu người nhận: ")
sluong = input("Số xu muốn tặng: ")
loai = input("Loại (xu/malucsub/maluclikepage/maluccmttiktok): ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.6,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://tuongtaccheo.com",
    "Referer": "https://tuongtaccheo.com/index.php"
}

login_data = {
    "username": username,
    "password": password,
    "submit": "ĐĂNG NHẬP"
}

with requests.Session() as s:
    s.headers.update(headers)

    print("[*] Đang đăng nhập...")
    login_resp = s.post(LOGIN_URL, data=login_data, allow_redirects=True)
    if "login.php" in login_resp.url:
        print("❌ Đăng nhập thất bại. Kiểm tra lại tài khoản hoặc mật khẩu.")
    else:
        print("✅ Đăng nhập thành công!")

        tang_data = {
            "usernhan": usernhan,
            "passnicktang": passnicktang,
            "sluong": sluong,
            "loai": loai
        }

        print(f"[*] Đang tặng {sluong} {loai} cho {usernhan}...")
        tang_resp = s.post(TANGXU_URL, data=tang_data)

        res_text = tang_resp.text.strip()

        codes = {
            "0": "Bạn không có quyền tặng xu/mã lực",
            "1": "Mật khẩu không đúng",
            "2": "Tài khoản nhận không hợp lệ",
            "3": "Không đủ xu hoặc mã lực",
            "4": "🎉 Tặng thành công",
            "5": "Số xu/mã lực không hợp lệ",
            "6": "Vui lòng tặng chậm lại"
        }

        print("Kết quả:", codes.get(res_text, f"Phản hồi: {res_text}"))


