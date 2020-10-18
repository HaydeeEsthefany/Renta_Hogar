import requests
import json

from web import config 
 

def generate_request_post(url, params={}):   
    response = requests.post(url, data =params )
    if response.status_code == 200:
        return response.json()

def generate_request_get(url): 
    if config.token !='':
        headers={'Authorization': 'Token {}'.format( config.token  )}
        response = requests.get(url, headers=headers )
    else:
        response = requests.get(url)
    if response.status_code == 200:
        return response.json()   

def web():
	return "http://127.0.0.1:8005/api/"

 


def post_send_email_verify(dir_ip,fullname, since, weeks , adult ,  children , email):
    url = web() + 'user/password/recover/' 
    args = {'dir_ip': dir_ip,'fullname':fullname, 'since':since, 'weeks':weeks , 'adult':weeks ,  'children':children, 'email': email }
    response = True#generate_request_post(url, args)   
    print(url)

    print(args)
    return response