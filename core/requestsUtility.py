import json

import requests


class RequestsUtility:
    def __init__(self):
        self.session = requests.session()

    def request(self, method, url, data=None, **kwargs):
        res = json.dumps(None)
        if str(method).lower() == "get":
            res = self.session.get(url, params=data, **kwargs)
        elif str(method).lower() == "post":
            data = json.dumps(data)
            res = self.session.post(url, data=data, **kwargs)
        return res


if __name__ == '__main__':
    a = requests.request("get", "https://www.baidu.com")
    print(a.headers)
    res = RequestsUtility().request("get", "https://www.baidu.com", None).headers
    print(res)
    res.clear()
    b = requests.request("get", "https://www.baidu.com")
    print(b.headers)
