import requests
## import pprint


def get_locatin_info():

    return requests.get("http://ip-api.com/json/").json()

if __name__ == "__main__":
       print(get_locatin_info())
