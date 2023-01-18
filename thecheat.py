import requests
import sys
from time import sleep
import os

def printf(text):
    for char in text: print("" + char, end="");sys.stdout.flush();sleep(0.045)


def isPhonenumberView(Phonenumber):
    THE = ""
    local_ = ""
    Cyber = ""

    er = "발견 되지 않았습니다."

    r = requests.get(f"https://edge-live.joongna.com/api/scam/globalSearch?keyword={Phonenumber}&fieldType=phone_number&entryType=1")
    
    thecheat = r.json()["data"]["theCheat"]["count"]
    local = r.json()["data"]["local"]["count"]
    cyberCop = r.json()["data"]["local"]["count"]
    
    

    if int(thecheat) == 1:
         THE = '더치트 신고 건수 "있음"'
    if int(local) == 1:
         local_ = "신고 건수 있음"
    if int(cyberCop) == 1:
         Cyber = "사이버범죄 신고시스템\n신고 건수 있음" 
    if int(thecheat) == 0:
         THE = "신고 건수 없음"
    if int(local) == 0:
         local_ = "  신고 건수 없음\n(신고 내역이 없더라도, 안전한 거래라는 것을 보장할 수 없습니다.)"
    if int(cyberCop) == 0:
         Cyber = "  사이버범죄 신고시스템\n신고 건수 없음\n(최근 3개월 동안 3회 미만 사이버범죄 신고시스템 접수 건은 결과에 반영되지 않을 수 있습니다.)"
    else:
         er = "알 수 없는 오류가 발생 하였습니다."



    if int(thecheat) == 1 or int(local) == 1 or int(cyberCop) == 1:
        return print(f"""
        {r.json()["data"]["maskingKeyword"]} 님은 사기 전적이 있습니다.

        더치트 : {THE}

        중고나라 : {local_}

        사이버 범죄 신고 시스템 : {Cyber}


        그외 오류 : {er}
        """)
    elif int(thecheat) == 0 and int(local) == 0 and int(cyberCop) == 0:
        return print(
            f"""
            {r.json()["data"]["maskingKeyword"]} 님은 사기 전적이 없습니다.
            """
        )


def isAccountView(account):
    THE = ""
    local_ = ""
    Cyber = ""

    er = "발견 되지 않았습니다."


    r = requests.get(f"https://edge-live.joongna.com/api/scam/globalSearch?keyword={account}&fieldType=account_number&entryType=1")
    
    thecheat = r.json()["data"]["theCheat"]["count"]
    local = r.json()["data"]["local"]["count"]
    cyberCop = r.json()["data"]["local"]["count"]
    
    

    if int(thecheat) == 1:
         THE = '더치트 신고 건수 "있음"'
    if int(local) == 1:
         local_ = "신고 건수 있음"
    if int(cyberCop) == 1:
         Cyber = "사이버범죄 신고시스템\n신고 건수 있음" 
    if int(thecheat) == 0:
         THE = "신고 건수 없음"
    if int(local) == 0:
         local_ = "  신고 건수 없음\n(신고 내역이 없더라도, 안전한 거래라는 것을 보장할 수 없습니다.)"
    if int(cyberCop) == 0:
         Cyber = "  사이버범죄 신고시스템\n신고 건수 없음\n(최근 3개월 동안 3회 미만 사이버범죄 신고시스템 접수 건은 결과에 반영되지 않을 수 있습니다.)"
    else:
         er = "알 수 없는 오류가 발생 하였습니다."



    if int(thecheat) == 1 or int(local) == 1 or int(cyberCop) == 1:
        return print(f"""
        {r.json()["data"]["maskingKeyword"]} 님은 사기 전적이 있습니다.

        더치트 : {THE}

        중고나라 : {local_}

        사이버 범죄 신고 시스템 : {Cyber}


        그외 오류 : {er}
        """)
    elif int(thecheat) == 0 and int(local) == 0 and int(cyberCop) == 0:
        return print(
            f"""
            {r.json()["data"]["maskingKeyword"]} 님은 사기 전적이 없습니다.
            """
        )


def main():
    os.system("cls")
    printf('WhiteHole The Cheat View Program\n\nIf u want some help command\nPlease Enter "HELP" or "help"')
    input_ = input("\n\n> ")

    number = 0
    account = 0

    if "Phonenumber" in input_: 
        try:
            ph = input_.split(" ")[1] 
            number = ph

            if "-" in number:
                return input("전화번호 사이 '-' 은 지우고 번호만 입력 해 주세요.")
        except Exception as e:
            return input("Phonenumber <number> 형식으로 적어주세요!")
    if "Account" in input_: 
        try:
            ac = input_.split(" ")[1]
            account = ac
        except Exception as e:
            return input("Account <Account> 형식으로 적어주세요!")


    if input_ == "HELP" or input_ == "help":
        print("""
        TheCheat View with Phonenumber&account
        
        Thecheat? -> Finance Prevention Program (fraud,sexual_assault,voice_phishing...)

        Phonenumber <number> - Search for fraud records with phonenumber

        Account <account> - search for fraud records with account

        cls - dos clear

        menu - go to menu page
        """)
        sleep(4)
        main()

    elif input_ == f"Phonenumber {number}":
        isPhonenumberView(number)
    
    elif input_ == f"Account {account}":
        isAccountView(account)

    elif input_ == "cls":
        sleep(1)
        main()
    elif input_ == "menu":
        sleep(2)
        main()
    else:
        print("Invaild command!")
        return main()
    
if __name__ == "__main__":
    main()




    
