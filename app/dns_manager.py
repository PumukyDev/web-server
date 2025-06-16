from dotenv import load_dotenv
import requests
import json
import os

load_dotenv(dotenv_path='.env')

DOMAIN_NAME = os.getenv('DOMAIN_NAME')
ID = os.getenv('ID')
SecretKey = os.getenv('SecretKey')
zoneId = os.getenv('zoneId')

def create_txt_record(short_url, original_url):
    url = f"https://api.hosting.ionos.com/dns/v1/zones/{zoneId}/records"
    headers = {
        'accept': 'application/json',
        'X-API-Key': f"{ID}.{SecretKey}",
        'Content-Type': 'application/json'
    }
    data = [{
        "name": f"{short_url}.url-shortener.{DOMAIN_NAME}",
        "type": "TXT",
        "content": original_url,
        "ttl": 3600,
        "prio": 0,
        "disabled": False
    }]
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.status_code == 200 or response.status_code == 201
    except requests.exceptions.RequestException as e:
        print("Error creating DNS record:", e)
        return False

def get_original_url(short_url):
    dns_query_url = f"https://dns.google/resolve?name={short_url}.url-shortener.{DOMAIN_NAME}&type=TXT"
    try:
        response = requests.get(dns_query_url)
        data = response.json()
        if response.status_code == 200 and 'Answer' in data:
            for record in data['Answer']:
                if record['type'] == 16:
                    return record['data'].strip('"')
    except Exception as e:
        print("Error querying DNS:", e)
    return None
