import requests #line:1
import time #line:2
import os #line:3
from colorama import init ,Fore ,Style #line:4
init (autoreset =True )#line:6
TOKEN_FILE ='/sdcard/TOKENCHECKER/token/token.txt'#line:8
LOG_FILE ='/sdcard/TOKENCHECKER/credentials/log.txt'#line:9
def create_file_if_not_exists (O0O0OOO00OOO0O0OO ):#line:11
    ""#line:12
    os .makedirs (os .path .dirname (O0O0OOO00OOO0O0OO ),exist_ok =True )#line:13
    if not os .path .isfile (O0O0OOO00OOO0O0OO ):#line:14
        with open (O0O0OOO00OOO0O0OO ,'w')as OO0O0OO0OOOOOO000 :#line:15
            pass #line:16
def check_facebook_token (O0OO0000000O0O0OO ):#line:18
    ""#line:19
    OOO000O00O00OOOOO =f'https://graph.facebook.com/me?fields=id&access_token={O0OO0000000O0O0OO}'#line:20
    O0000O0O0OOO000O0 =requests .get (OOO000O00O00OOOOO )#line:21
    if O0000O0O0OOO000O0 .status_code ==200 :#line:23
        O00000O0O00OOOOOO =O0000O0O0OOO000O0 .json ()#line:24
        OO000000O0O0OO0O0 =O00000O0O00OOOOOO .get ('id','')#line:25
        if OO000000O0O0OO0O0 .startswith (('615','100')):#line:26
            return 'valid','user',OO000000O0O0OO0O0 #line:27
        else :#line:28
            return 'valid','page',OO000000O0O0OO0O0 #line:29
    return 'invalid',None ,None #line:30
def process_tokens ():#line:32
    ""#line:33
    create_file_if_not_exists (TOKEN_FILE )#line:35
    create_file_if_not_exists (LOG_FILE )#line:36
    O00OO0000000OOO0O =[]#line:38
    O0OOO00000OOOO000 =[]#line:39
    OO0O00O000OOOOO0O =set ()#line:40
    OO00O0O0O000000O0 ={}#line:42
    O0O00OOOO0O0000OO =0 #line:44
    O00000000O000OO0O =0 #line:45
    with open (TOKEN_FILE ,'r')as O0000O00000OO0000 :#line:47
        O00000O00OO00O0O0 =O0000O00000OO0000 .read ().splitlines ()#line:48
    with open (LOG_FILE ,'a')as OOO00OOO0OO0O0O0O :#line:50
        for OO0OO0OO0OO0OO0OO in O00000O00OO00O0O0 :#line:51
            if OO0OO0OO0OO0OO0OO in OO00O0O0O000000O0 :#line:53
                OO00O0O0O000000O0 [OO0OO0OO0OO0OO0OO ]+=1 #line:54
            else :#line:55
                OO00O0O0O000000O0 [OO0OO0OO0OO0OO0OO ]=1 #line:56
            OOOOO0OOOO00000O0 ,OO00O000OOOO000O0 ,OOO0O0O00O0O00OOO =check_facebook_token (OO0OO0OO0OO0OO0OO )#line:58
            if OOOOO0OOOO00000O0 =='valid':#line:59
                O00OO0000000OOO0O .append (OO0OO0OO0OO0OO0OO )#line:60
                OOO0O0000O0OO0O00 =f'{OOO0O0O00O0O00OOO} : {OO00O000OOOO000O0} : {OOOOO0OOOO00000O0}'#line:61
                OOO00OOO0OO0O0O0O .write (OOO0O0000O0OO0O00 +'\n')#line:62
                if OO00O000OOOO000O0 =='user':#line:63
                    O0O00OOOO0O0000OO +=1 #line:64
                    print (f'{Fore.GREEN}{OOO0O0000O0OO0O00}{Style.RESET_ALL}')#line:65
                elif OO00O000OOOO000O0 =='page':#line:66
                    O00000000O000OO0O +=1 #line:67
                    print (f'{Fore.GREEN}{OOO0O0000O0OO0O00}{Style.RESET_ALL}')#line:68
            else :#line:69
                O0OOO00000OOOO000 .append (OO0OO0OO0OO0OO0OO )#line:70
                OOO0O0000O0OO0O00 =f'Unknown ID : {OOOOO0OOOO00000O0}'#line:71
                OOO00OOO0OO0O0O0O .write (OOO0O0000O0OO0O00 +'\n')#line:72
                print (f'{Fore.RED}{OOO0O0000O0OO0O00}{Style.RESET_ALL}')#line:73
            time .sleep (0 )#line:75
    OO0O00O000OOOOO0O ={O00OO0OO00OO0O000 for O00OO0OO00OO0O000 ,OO00O00OOO0OOOOO0 in OO00O0O0O000000O0 .items ()if OO00O00OOO0OOOOO0 >1 }#line:78
    O00000O000O0O000O =sum (OO0OOOOO0O000OO00 -1 for OO0OOOOO0O000OO00 in OO00O0O0O000000O0 .values ()if OO0OOOOO0O000OO00 >1 )#line:79
    with open (TOKEN_FILE ,'w')as O0000O00000OO0000 :#line:82
        O0000O00000OO0000 .write ('\n'.join (O00OO0000000OOO0O ))#line:83
    O000OOO0O00O000OO =len (O00OO0000000OOO0O )+len (O0OOO00000OOOO000 )#line:85
    print ("\n"+Fore .CYAN +"Dashboard Summary:"+Style .RESET_ALL )#line:87
    print (f"{Fore.GREEN}Total User Accounts: {Fore.YELLOW}{O0O00OOOO0O0000OO}{Style.RESET_ALL}")#line:88
    print (f"{Fore.GREEN}Total Page Accounts: {Fore.YELLOW}{O00000000O000OO0O}{Style.RESET_ALL}")#line:89
    print (f"{Fore.RED}Total Disabled: {Fore.YELLOW}{len(O0OOO00000OOOO000)}{Style.RESET_ALL}")#line:90
    print (f"{Fore.GREEN}Total Alive: {Fore.YELLOW}{len(O00OO0000000OOO0O)}{Style.RESET_ALL}")#line:91
    print (f"{Fore.CYAN}Total Accounts: {Fore.YELLOW}{O000OOO0O00O000OO}{Style.RESET_ALL}")#line:92
    print (f"{Fore.MAGENTA}Total Duplicate Tokens: {Fore.YELLOW}{O00000O000O0O000O}{Style.RESET_ALL}")#line:93
    if OO0O00O000OOOOO0O :#line:95
        print (f"\n{Fore.MAGENTA}Duplicates Found:{Style.RESET_ALL}")#line:96
        for OO0OO0OO0OO0OO0OO in OO0O00O000OOOOO0O :#line:97
            print (f"- {OO0OO0OO0OO0OO0OO}")#line:98
if __name__ =='__main__':#line:100
    process_tokens ()#line:101
