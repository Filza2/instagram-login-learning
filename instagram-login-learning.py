import requests
username=input('username: ')
password=input('password: ')

headers={
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '321',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'mid=YMEcQAALAAEv7JAHx0HGAT9oOg5e; ig_did=BBD1FACB-65E8-433F-BB27-1554B5DC41E6; ig_nrcb=1; shbid=13126; shbts=1624283106.1767957; rur=PRN; csrftoken=kKQkGJjUqYTQVCewP9FEp6SZypK8iiSt',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'x-asbd-id': '437806',
    'x-csrftoken': 'kKQkGJjUqYTQVCewP9FEp6SZypK8iiSt',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgSX-',
    'x-instagram-ajax': 'a90c0f3c9877',
    'x-requested-with': 'XMLHttpRequest'
    }

data={
    'username': username,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{password}',
    'queryParams': '{}',
    'optIntoOneTap': 'false',
    'stopDeletionNonce': '',
    'trustedDeviceRecords': '{}'
    }


req=requests.post(url='https://www.instagram.com/accounts/login/ajax/',headers=headers,data=data)

print(req.text)

if '"user":false' in req.text:
    print('user not found')
    
elif '"authenticated":true' in req.text:
    print('[+] Done Login')
    sessd=req.cookies['sessionid']
    print(sessd)    
    
elif ('checkpoint_required') in req.text:
    print('Secure') 
    
elif ('"user":true,"authenticated":false') in req.text:
    print('wrong password')  
    
elif '"user":true' in req.text:
    print('wrong password')
    
elif 'Sorry, your password was incorrect. Please double-check your password.' in req.text:
    print('wrong password // username not found')
    
elif req.status_code=="429":
    print('ban')
    
elif 'ip_block' in req.text:
    print('ban')
    
elif 'Please wait a few minutes before you try again.' in req.text:
    print('ban')
    
elif 'We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.' in req.text:
    print('ban')
    
else:
    print('Error read the request for more info')
    
    
#By @TweakPY - @vv1ck