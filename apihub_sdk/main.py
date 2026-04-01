import time
import sys
import random
from colorama import Fore, Style, init

# Khởi tạo màu sắc cho terminal
init(autoreset=True)

def run_setup():
    print(f"{Fore.BLUE}{Style.BRIGHT}=== APIHUB UNIVERSAL SDK v4.6.0 SETUP ==={Style.RESET_ALL}\n")
    
    steps = [
        "Initializing environment...",
        "Detecting local Python clusters...",
        "Checking hardware acceleration (CUDA/Metal)...",
        "Connecting to Global APIHub Infra...",
        "Authenticating with Google Cloud Vertex Labs...",
        "Allocating Unlimited Token Quota..."
    ]

    for step in steps:
        print(f"{Fore.WHITE}[*] {step}", end="", flush=True)
        time.sleep(random.uniform(0.4, 0.8))
        print(f" {Fore.GREEN}[OK]")
    
    print(f"\n{Fore.YELLOW}Optimizing local cache for high-speed rendering...")
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "░" * (20 - i)
        sys.stdout.write(f"\r{Fore.CYAN}Progress: |{bar}| {percent}% complete")
        sys.stdout.flush()
        time.sleep(0.1)
    
    print(f"\n\n{Fore.GREEN}{Style.BRIGHT}Success: Environment is ready.{Style.RESET_ALL}")
    time.sleep(1)
    
    print(f"\n{Fore.MAGENTA}Finalizing security handshake...")
    time.sleep(2)

    # ĐOẠN TROLL CUỐI CÙNG
    print("\n" + "="*60)
    print(f"{Fore.RED}{Style.BRIGHT}!!! CẢNH BÁO BẢO MẬT: PHÁT HIỆN LỖI 'TIN NGƯỜI' !!!")
    print("="*60)
    time.sleep(1)
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}🤡 CHÚC MỪNG NGÀY CÁ THÁNG TƯ! 🤡")
    print(f"{Fore.WHITE}Chào bạn, làm gì có API Key nào 'Free' mà lại còn 'Unlimited' hả bạn?")
    print(f"{Fore.CYAN}Hãy tắt terminal này, đi uống nước và đừng tin ai hôm nay nhé!")
    print(f"\n{Fore.GREEN}Gợi ý: Hãy gửi link cho bạn bè để lan tỏa 'sự cay cú' này.")
    print("="*60)
    
    input(f"\n{Fore.WHITE}Nhấn Enter để thoát (Nếu bạn đã chấp nhận sự thật)...")

if __name__ == "__main__":
    run_setup()
