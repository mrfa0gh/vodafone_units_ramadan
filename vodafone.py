import requests

def vodafone_login():
    print(''' Coded By

 ██████  ██   ██  █████  ██      ██     ██  █████  ███████ ██   ██ 
██       ██   ██ ██   ██ ██      ██     ██ ██   ██ ██      ██   ██ 
██   ███ ███████ ███████ ██      ██  █  ██ ███████ ███████ ███████ 
██    ██ ██   ██ ██   ██ ██      ██ ███ ██ ██   ██      ██ ██   ██ 
 ██████  ██   ██ ██   ██ ███████  ███ ███  ██   ██ ███████ ██   ██ 
                                                                   
                                                                   
''')
    username = input("أدخل رقم فودافون: ")
    password = input("أدخل كلمة المرور: ")
    
    url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
    headers = {
        "User-Agent": "okhttp/4.9.1",
        "Accept": "application/json, text/plain, */*",
        "x-agent-operatingsystem": "1630483957",
        "Accept-Encoding": "gzip",
        "x-dynatrace": "MT_3_8_3300078660_17-0_a556db1b-4506-43f3-854a-1d2527767923_0_8377_318",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "clientid": "AnaVodafoneAndroid",
        "x-agent-device": "RMX1911"
    }
    
    data = {
        "username": username,
        "password": password,
        "grant_type": "password",
        "client_secret": "a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",
        "client_id": "my-vodafone-app"
    }
    
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    token = response_json.get("access_token")
    
    if token:
        print("تم الحصول على التوكن بنجاح")
        get_promotion(username, token)
    else:
        print("فشل في الحصول على التوكن")

def get_promotion(username, token):
    url = "https://web.vodafone.com.eg/services/dxl/ramadanpromo/promotion?@type=RamadanHub"
    headers = {
        "User-Agent": "Dart/3.4 (dart:io)",
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "Channel": "WEB",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Msisdn": username,
        "Api-Host": "PromotionHost"
    }
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    print("\n===== بيانات العرض =====")
    for item in response_json:
        if "pattern" in item:
            for pattern in item["pattern"]:
                for action in pattern.get("action", []):
                    for characteristic in action.get("characteristics", []):
                        if characteristic["name"] == "amount":
                            amount = characteristic["value"]
                        elif characteristic["name"] == "GIFT_UNITS":
                            gift_units = characteristic["value"]
                        elif characteristic["name"] == "REMAINING_DEDICATIONS":
                            remaining = characteristic["value"]
                        elif characteristic["name"] == "CARD_SERIAL":
                            card_serial = characteristic["value"]
                    
                    print(f"المبلغ: {amount} جنيه | الوحدات: {gift_units} | المتبقي: {remaining} | رقم البطاقة: {card_serial}")

vodafone_login()
