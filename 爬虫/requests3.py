import requests

url = 'https://movie.douban.com/j/chart/top_list'

# 重新封装参数
param = {
    'type': 24,
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 40,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 '
                  'Safari/537.36 Edg/124.0.0.0'
}
resp = requests.get(url, params=param, headers=headers)

print(resp.request.url)
print()
print(resp.json())
resp.close()