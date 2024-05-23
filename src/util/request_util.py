import requests


def method_post(url,data):
    response = requests.post(url,data={"cod": data})
    return response.text

