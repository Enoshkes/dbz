import requests

def get_dbz(url):
    response = requests.request('GET',url)
    return response.json()

