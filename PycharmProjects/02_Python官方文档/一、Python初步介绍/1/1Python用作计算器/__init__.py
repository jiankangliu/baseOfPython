import requests
import os
url="http://www.baidu.com"
r=requests.get(url)
print(r.status_code)
print(type(r))