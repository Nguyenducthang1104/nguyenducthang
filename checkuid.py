import customtkinter as ctk
import requests
from threading import Thread

# Cấu hình giao diện
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FB CHECKER - NGUYEN DUC THANG")
        self.geometry("900x600")

        # --- Khung trên: Nhập dữ liệu ---
        self.label_input = ctk.CTkLabel(self, text="DANH SÁCH UID / DATA:", font=("Arial", 13, "bold"))
        self.label_input.pack(pady=(10, 0))
        
        self.txt_input = ctk.CTkTextbox(self, width=850, height=200)
        self.txt_input.pack(pady=10)

        # --- Khung giữa: Nút bấm ---
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(fill="x", padx=25)

        self.btn_check = ctk.CTkButton(self.btn_frame, text="Check Live", fg_color="#28a745", hover_color="#218838", command=self.start_thread)
        self.btn_check.pack(side="right", padx=5)

        # --- Khung dưới: Kết quả LIVE và DIE ---
        self.res_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.res_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Cột LIVE
        self.live_box_frame = ctk.CTkFrame(self.res_frame)
        self.live_box_frame.pack(side="left", fill="both", expand=True, padx=5)
        self.label_live = ctk.CTkLabel(self.live_box_frame, text="DIE: 0", text_color="#dc3545", font=("Arial", 12, "bold"))
        self.label_live.pack()
        self.txt_live = ctk.CTkTextbox(self.live_box_frame, fg_color="#1a1a1a", text_color="#dc3545")
        self.txt_live.pack(fill="both", expand=True, pady=5)

        # Cột DIE
        self.die_box_frame = ctk.CTkFrame(self.res_frame)
        self.die_box_frame.pack(side="right", fill="both", expand=True, padx=5)
        self.label_die = ctk.CTkLabel(self.die_box_frame, text="LIVE: 0", text_color="#28a745", font=("Arial", 12, "bold"))
        self.label_die.pack()
        self.txt_die = ctk.CTkTextbox(self.die_box_frame, fg_color="#1a1a1a", text_color="#28a745")
        self.txt_die.pack(fill="both", expand=True, pady=5)

    def check_logic(self, uid):
        # Hàm check đơn giản qua Graph API ảnh
        try:
            url = f"https://graph.facebook.com/{uid.split('|')[0]}/picture?type=normal"
            res = requests.get(url, timeout=5)
            return "LIVE" if "static.xx.fbcdn" in res.url and "default" not in res.url else "DIE"
        except: return "ERROR"

    def process_check(self):
        data = self.txt_input.get("1.0", "end-1c").strip().split('\n')
        live_count = 0
        die_count = 0
        
        self.txt_live.delete("1.0", "end")
        self.txt_die.delete("1.0", "end")

        for line in data:
            if not line.strip(): continue
            status = self.check_logic(line.strip())
            
            if status == "LIVE":
                live_count += 1
                self.txt_live.insert("end", line + "\n")
                self.label_live.configure(text=f"DIE: {live_count}")
            else:
                die_count += 1
                self.txt_die.insert("end", line + "\n")
                self.label_die.configure(text=f"LIVE: {die_count}")
            self.update_idletasks()

    def start_thread(self):
        # Chạy trong luồng riêng để không bị treo giao diện
        Thread(target=self.process_check).start()

if __name__ == "__main__":
    app = App()
    app.mainloop()