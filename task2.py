import requests
import re


response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
response_txt = response.text
pattern = re.compile(r'(.+)\s-\s-\s\[(.+)]\s"(\w+[A-Z])\s(/\w+/\w+)\s.+"\s(\d+)\s(\d+)\s')
result = []
r = pattern.findall(response_txt)
print(r)
