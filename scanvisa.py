import random
import time
import sys
from colorama import Fore, init, Style

init(autoreset=True)
banner()
def generate_luhn_visa():
    digits = [4] + [random.randint(0, 9) for _ in range(14)]
    total = 0
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 0:
            d = digit * 2
            if d > 9: d -= 9
            total += d
        else:
            total += digit
    digits.append((10 - (total % 10)) % 10)
    return "".join(map(str, digits))

def get_pro_name():
    # Danh sách 100 First Names ngoại (Anh, Mỹ, Âu)
    first_names = [
        "James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda", "David", "Elizabeth",
        "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Christopher", "Karen",
        "Charles", "Nancy", "Matthew", "Lisa", "Anthony", "Betty", "Mark", "Margaret", "Donald", "Sandra",
        "Steven", "Ashley", "Paul", "Kimberly", "Andrew", "Emily", "Joshua", "Donna", "Kenneth", "Michelle",
        "Kevin", "Dorothy", "Brian", "Carol", "George", "Amanda", "Timothy", "Melissa", "Ronald", "Deborah",
        "Jason", "Stephanie", "Jeffrey", "Rebecca", "Ryan", "Sharon", "Gary", "Cynthia", "Nicholas", "Kathleen",
        "Eric", "Amy", "Jacob", "Shirley", "Jonathan", "Angela", "Larry", "Helen", "Frank", "Anna", "Scott", "May",
        "Brandon", "Nicole", "Raymond", "Samantha", "Gregory", "Christine", "Samuel", "Catherine", "Benjamin", "Virginia",
        "Patrick", "Debra", "Alexander", "Rachel", "Jack", "Janet", "Dennis", "Emma", "Jerry", "Carolyn", "Tyler", "Maria"
    ]
    # Danh sách 100 Last Names ngoại
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
        "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
        "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
        "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Hill", "Flores", "Adams", "Nelson",
        "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans",
        "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales",
        "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed",
        "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez", "Wood",
        "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel"
    ]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def main():
    print(f"{Fore.CYAN}{'='*55}")
    print(f"{Fore.GREEN}   VISA SCAN")
    print(f"{Fore.CYAN}{'='*55}\n")
    
    try:
        soluong = int(input(f"{Fore.WHITE}Nhập số lượng thẻ muốn scan: "))
    except: return

    live_count = 0
    with open("livecc.txt", "a", encoding="utf-8") as f:
        for i in range(1, soluong + 1):
            # Hiệu ứng scan chuyên nghiệp
            print(f"\n{Fore.WHITE}[THREAD-1][CARD {i}/{soluong}] {Fore.CYAN}Scanning database...")
            time.sleep(random.uniform(0.4, 0.8)) # Chạy từ từ
            
            card_num = generate_luhn_visa()
            full_name = get_pro_name()
            exp = f"{random.randint(1,12):02d}/{random.randint(2026,2031)}"
            cvv = random.randint(100, 999)
            pin = random.randint(1000, 9999)

            # In thông tin thẻ ra màn hình
            print(f"{Fore.BLUE}[CARD] {Fore.WHITE}{card_num} | Exp: {exp}")
            print(f"{Fore.MAGENTA}[INFO] BIN: VISA | NAME: {full_name.upper()} | CVV: {cvv} | PIN: {pin}")
            
            # Lưu vào file
            f.write(f"{card_num}|{exp}|{cvv}|{pin}|{full_name}\n")
            live_count += 1
            
            print(f"{Fore.GREEN}[SAVE] ✓ Recorded to livecc.txt")
            print(f"{Fore.CYAN}[STATS] Success: {i}/{i} | Live: {live_count}")
            print(f"{Fore.WHITE}{'-'*50}")

    print(f"\n{Fore.YELLOW}>>> SCAN COMPLETED! TOTAL LIVE: {live_count} <<<")

if __name__ == "__main__":
    main()
