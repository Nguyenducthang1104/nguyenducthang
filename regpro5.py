import customtkinter as ctk
import random
import threading
import requests
import sys
from time import sleep
from datetime import datetime

# --- CLASS GỐC CỦA BẠN (GIỮ NGUYÊN 100%) ---
class reg_pro5():
    def __init__(self, cookies, name) -> None:
        self.cookies = cookies
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text
        try:
            self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
        except:
            self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]
            
    def Reg(self, name): # Thêm name vào đây để bám sát logic tạo tên ngẫu nhiên
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"'+name+'","page_referrer":"launch_point","actor_id":"'+self.id_acc+'","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }
        
        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)     
        try:
            return response.json()
        except:
            return response.text

# --- GIAO DIỆN ĐA LUỒNG ---
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("DT-TOOL REG PRO5 - NGUYỄN ĐỨC THẮNG")
        self.geometry("900x700")
        self.running = False

        # Cấu hình nhập Cookie
        ctk.CTkLabel(self, text="NHẬP DANH SÁCH COOKIE (MỖI DÒNG 1 ACC):", font=("Arial", 12, "bold")).pack(pady=(10, 5))
        self.txt_cookies = ctk.CTkTextbox(self, width=850, height=150, border_width=2, border_color="#1f538d")
        self.txt_cookies.pack(pady=5)

        # Cấu hình Luồng & Delay
        self.frame_cfg = ctk.CTkFrame(self)
        self.frame_cfg.pack(fill="x", padx=25, pady=10)

        ctk.CTkLabel(self.frame_cfg, text="Số luồng:").pack(side="left", padx=5)
        self.ent_threads = ctk.CTkEntry(self.frame_cfg, width=60)
        self.ent_threads.insert(0, "2")
        self.ent_threads.pack(side="left", padx=5)

        ctk.CTkLabel(self.frame_cfg, text="Delay (s):").pack(side="left", padx=5)
        self.ent_delay = ctk.CTkEntry(self.frame_cfg, width=70)
        self.ent_delay.insert(0, "650")
        self.ent_delay.pack(side="left", padx=5)

        self.btn_run = ctk.CTkButton(self.frame_cfg, text="BẮT ĐẦU", fg_color="green", command=self.toggle)
        self.btn_run.pack(side="right", padx=10)

        # Màn hình Log rõ ràng
        self.txt_log = ctk.CTkTextbox(self, width=850, height=380, font=("Consolas", 12))
        self.txt_log.pack(pady=10, padx=20)

    def log(self, thread_id, msg):
        time_now = datetime.now().strftime("%H:%M:%S")
        self.txt_log.insert("end", f"[{time_now}] [Luồng {thread_id}] {msg}\n")
        self.txt_log.see("end")

    def toggle(self):
        if not self.running:
            self.running = True
            self.btn_run.configure(text="DỪNG LẠI", fg_color="red")
            threading.Thread(target=self.main_manager, daemon=True).start()
        else:
            self.running = False
            self.btn_run.configure(text="BẮT ĐẦU", fg_color="green")

    def worker(self, cookie, thread_id):
        while self.running:
            try:
                # Logic lấy tên ngẫu nhiên giống bản console
                ho = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Võ"]
                lot = ["Văn", "Thị", "Đức", "Minh", "Quốc"]
                ten = ["Anh", "Hùng", "Dũng", "Lan", "Huệ", "Thắng"]
                name = f"{random.choice(ho)} {random.choice(lot)} {random.choice(ten)}"

                self.log(thread_id, f"Đang Reg cho: {name}")
                
                # Gọi API bám sát 100% logic của bạn
                bot = reg_pro5(cookie, name)
                res = bot.Reg(name)
                
                self.log(thread_id, f"Kết quả: {str(res)[:150]}") # Log kết quả API

                # Delay theo thiết lập
                wait = int(self.ent_delay.get())
                self.log(thread_id, f"Đang chờ {wait}s...")
                for i in range(wait, 0, -1):
                    if not self.running: return
                    sleep(1)

            except Exception as e:
                self.log(thread_id, f"Lỗi: {str(e)}")
                break

    def main_manager(self):
        # Lấy list cookie từ TextBox (Xử lý lỗi InvalidHeader)
        data = self.txt_cookies.get("1.0", "end-1c").strip().split('\n')
        cookies = [c.strip() for c in data if c.strip()]
        
        if not cookies:
            self.log(0, "LỖI: Chưa nhập Cookie!")
            self.toggle()
            return

        try:
            max_threads = int(self.ent_threads.get())
        except:
            max_threads = 1

        # Chạy đa luồng
        for i in range(min(max_threads, len(cookies))):
            t = threading.Thread(target=self.worker, args=(cookies[i], i+1), daemon=True)
            t.start()
            sleep(1)

if __name__ == "__main__":
    app = App()
    app.mainloop()