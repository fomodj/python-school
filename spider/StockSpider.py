import pandas as pd
import requests
import random
import time
import json
import jsonpath
import csv

# 读取股票代码
data = pd.DataFrame(pd.read_excel('2020-05-20.xlsx',encoding='utf-8'))
# print(data['股票代码'])#获取列名为姓名这一列的内容

# 构造headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
'Cookie':'Cookie: device_id=24700f9f1986800ab4fcc880530dd0ed; s=bx17l9zje4; remember=1; xq_a_token=c6bb829c4c888f0ec74e8e7df277988dc13bd996; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjM5MTY4MjM3NjMsImlzcyI6InVjIiwiZXhwIjoxNTkyNTcxODYxLCJjdG0iOjE1ODk5Nzk4NjE2NzEsImNpZCI6ImQ5ZDBuNEFadXAifQ.KydCcsioS634tyZiy-Nc305w5wdVPDxOM9dWnYhsq2Zi6-3iH2D_vG1tRF5qPB63FL-F1-ASa1KwOtG81jdj0yrOgnp1ftvU_AqwNQk9alCWkEAKkrJMXwEP5s-WsGw00gI0i4i716Fa5XfSCFoDxT06zgQY9O3fOl-0mMTaxp5n2SJQE_g_8qwuUMo73QP9eWlm3ZzmkRboUkJjisNlFcN47s_62XinrIwDGsKLIQWVkT5Pp1Kded27bRBndmvi4iHJpybaGs1yt057pvIDO2_jUBsDO-TX4d6thKl0OCgtL2ZBkis4Z2jw7cYExUDRuEEz87uOlt6sA_p7NBpjRQ; xqat=c6bb829c4c888f0ec74e8e7df277988dc13bd996; xq_r_token=95ae60340e95370663bf8309c4275add3e0529e3; xq_is_login=1; u=3916823763; is_overseas=0'}

# 新建CSV并写入表头
f = open('雪球网股票信息.csv', 'w', encoding='utf-8-sig', newline='')
fileheader = ["股票代码", "股票简称", "股票(元)", "市盈率(TTM)", "市净率", "每股收益", "股息(TTM)", "股息率(TTM)"]
dict_writer = csv.DictWriter(f, fileheader)
dict_writer.writeheader()
f.close()

# 定义写入爬取的信息
def write_file():
    f = open('雪球网股票信息.csv', 'a+', encoding='utf-8-sig', newline='')
    w = csv.DictWriter(f, infomation.keys())
    w.writerow(infomation)
    f.close()

# 定义爬取网页
for i in range(len(data)):
    stocklist = str(data['股票代码'][i]).split('.')[0]
    stockexchange = str(data['股票代码'][i]).split('.')[1]
    if stockexchange == 'SH':
        url = 'https://stock.xueqiu.com/v5/stock/quote.json?symbol=SH' + stocklist +'&extend=detail'
    elif stockexchange == 'SZ':
        url = 'https://stock.xueqiu.com/v5/stock/quote.json?symbol=SZ' + stocklist +'&extend=detail'
    else:
        print('网页加载错误！')
        continue
    print("开始爬取 {}(股票代码:{}) 的信息...".format(data['股票简称'][i],data['股票代码'][i]))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    html = json.loads(html)
    # ["股票代码", "股票简称", "股票(元)", "市盈率(TTM)", "市净率","每股收益","股息(TTM)","股息率(TTM)"]
    infomation = {
        '股票代码':data['股票代码'][i],
        '股票简称':data['股票简称'][i],
        '股票(元)':data['现价(元)'][i],
        '市盈率(TTM)': str(jsonpath.jsonpath(html, '$..pe_ttm')[0]),
        '市净率': jsonpath.jsonpath(html, '$..pb')[0],
        '每股收益': jsonpath.jsonpath(html, '$..eps')[0],
        '股息(TTM)': jsonpath.jsonpath(html, '$..dividend')[0],
        '股息率(TTM)': jsonpath.jsonpath(html, '$..dividend_yield')[0],
    }
    write_file()
    time.sleep(random.randint(1, 3)) # 添加延迟时间，防反爬虫
    print('第{}家企业的信息已爬取完成！ 当前进度:{:.2f}%'.format(i+1,(i+1) * 100 / len(data))) # 显示当前进度
    print('*'*50)
