# -*-coding:utf-8-*-
from urllib.parse import urlencode

import requests

base_url = "http://weixin.sogou.com/weixin?"

# 超过10页的数据需要登录才能查看，故拼接cookie
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "CXID=4A8D7D5228E7C44A7460EC31FE74D53B; SUID=B44ADD783665860A58D12676000DEF93; ABTEST=0|1510218102|v1; IPLOC=CN1100; SUV=00601785DEF9AA605A041977FE430767; weixinIndexVisited=1; ppinf=5|1510218472|1511428072|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTUlODglQkElRTclOEMlQUN8Y3J0OjEwOjE1MTAyMTg0NzJ8cmVmbmljazoxODolRTUlODglQkElRTclOEMlQUN8dXNlcmlkOjQ0Om85dDJsdUZlMjZ1YXZHQ2ZEVnJXZDNYV0NXdWtAd2VpeGluLnNvaHUuY29tfA; pprdig=mR4KYtsmaiihtCVePyl-niLT503jJgKeAyPQA4Ykiozypf0ugJVdaQDU5tr-sjHhsrRv_TM8jZ389ZRyIFetO--K4he-HGwz-sU_dqdHBY98UbnpNWC-fgin3JYwof6ccTFrM5l3ApK_A4cHu98N_vpv8rLICiBXK7H9Zhrue6I; sgid=29-31867827-AVoEGuiajghnwtFxNSoOibvTM; SNUID=F5F0FD8D47421AACB3C825D2472C8EEB; wuid=AAEkEMVvHAAAAAqRMxu3GgAAAAA=; wapsogou_qq_nickname=%E5%88%BA%E7%8C%AC; w_userid=zL9Mk+JNp+sKl/t5181bx8pu0918kN5voN1NyMZPxu9QyuQG0OVA1qR7zOM=_338467403; wapsogou_qq_headimg=http%3A%2F%2Fwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI7ZuleMUiarkWpNaHXuMs2SicVgQhgjNWPXyd6MOcCYqicsBdBNB9PuIM1KOyiaicOXhZLQpSNmq0HlxA%2F96; usid=aGiJeL7dJRdYTHZ9; sct=6; JSESSIONID=aaargKq-Rsmjg5xCEHv8v; ppmdig=1510643129000000da6b3281d910070b650dad4ad1f7800f",
    "Host": "weixin.sogou.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}

keyword = "风景"


# 0获取网页内容
# 因为当请求为302的时候，网页会自动跳转到反爬虫网页，我们禁止其自动跳转allow_redirects=False
def get_html(url):
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            print("启动代理服务器")
            pass
    except ConnectionError:
        return get_html(url)


# 1 索引页抓取
def get_index(keyword, page):
    params = {
        "query": keyword,
        "type": 2,
        "page": page
    }

    url = base_url + urlencode(params)
    html = get_html(url)
    print(html)

# 中文测试
if __name__ == '__main__':
    get_index(keyword, 20)
