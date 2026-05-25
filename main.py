import requests
import time

# ID iVAS Anda
ACCOUNT_CODE = "4092470212"

def main():
    url = f"https://api.ivassms.com/v1/action?account_id={ACCOUNT_CODE}&action=get_earnings"
    print(f"[*] Memulai monitoring untuk ID: {ACCOUNT_CODE}")
    while True:
        try:
            response = requests.get(url, timeout=10).json()
            print(f"[+] Respon Server: {response}")
        except Exception as e:
            print(f"[-] Terjadi error: {e}")
        time.sleep(10)

if __name__ == "__main__":
    main()
