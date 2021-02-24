import requests , sys , time , os , socket
from bs4 import BeautifulSoup as bSoup 
from colorama import init , Fore
init()

def Main() :
    os.system('cls')

    banner = """
  █▀ █ █ █▀█ █▀█ ▀█▀ █▀▀ █▄ █   █ █ █▀█ █ 
  ▄█ █▀█ █▄█ █▀▄  █  ██▄ █ ▀█   █▄█ █▀▄ █▄▄"""

    tagline = """                                          [v 1.0]
--------------------------------------------------
  Hide Your Malicious Links   [+] By GH0STH4CK3R
--------------------------------------------------
 """
    def banners() :
        print(Fore.CYAN+banner)
        print(Fore.LIGHTCYAN_EX+tagline)
    banners()    

    itms = ["Checking for internet /","Checking for internet -","Checking for internet \\","Checking for internet |"]

    def spinning_cursor():
        while True:
            for cursor in itms:
                yield cursor

    spinner = spinning_cursor()
    for iii in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
    try:
        ip = socket.gethostbyname("www.google.com")  
    except Exception as e:
        os.system('cls')
        banners()
        print(Fore.LIGHTRED_EX + "No Internet !")  
        time.sleep(5)
        exit()    

    os.system('cls')
    banners()
    
    print(Fore.CYAN + "[01] Facebook")
    print("[02] Google")
    print("[03] Instagram")
    print("[04] Youtube")
    print("[05] Twitter")
    smedia = input("\nSelector > ")
    if smedia == "01" :
        social = "https://www.facebook.com"
    elif smedia == "02" :
        social = "https://www.google.com"
    elif smedia == "03" :
        social = "https://www.instagram.com"
    elif smedia == "04" :
        social = "https://www.youtube.com"
    elif smedia == "05" :
        social = "https://www.twitter.com"
    else :
        print("Default option selected !")
        social = "https:/www.facebook.com" 

    iurl = input("\nEnter Url : ")

    postname = input("\nName for Post link (amazing-tricks) : ")    

    url = "https://www.shorturl.at/shortener.php"
    data = {"u": iurl}

    res = requests.post(url,data=data)
    rcode = res.status_code

    if  rcode == 200 :
        #rdata = res.text
        page_html = res.text
        page_soup = bSoup(page_html,"html.parser")
        urltag = page_soup.find("input",{"id":"shortenurl"})

        surl = urltag['value']
        full_url = social + "-" + postname + "@" + surl

        print(Fore.LIGHTGREEN_EX + "\nCopy This Link >  ",full_url)

    else :
        print(Fore.LIGHTRED_EX + "Error !",rcode)
    
    print(Fore.CYAN+"")
    loop = int(input("Shorten another link ?\n\n[98] Yes\n[99] No\n\nChoice > "))
    if loop == 98 :
        Main()
    else:
        exit()    


Main()        
