import json

import requests

cookies = {
    'qgqp_b_id': '2725d397ab738c8a971e013318797659',
    'st_si': '55044536185321',
    'st_asi': 'delete',
    'cowCookie': 'true',
    'intellpositionL': '1522.39px',
    'intellpositionT': '855px',
    'st_pvi': '96463330710733',
    'st_sp': '2020-03-17^%^2023^%^3A21^%^3A50',
    'st_inirUrl': 'https^%^3A^%^2F^%^2Fwww.google.com^%^2F',
    'st_sn': '6',
    'st_psi': '20200317232427610-113300300813-8670491663',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = (
    ('pn', '1^'),
    ('pz', '50^'),
    ('po', '0^'),
    ('np', '1^'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5^'),
    ('fltt', '2^'),
    ('invt', '2^'),
    ('fid0', 'f4001^'),
    ('fid', 'f62^'),
    ('fs', 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2,m:0 t:7 f:^!2,m:1 t:3 f:^!2^'),
    ('stat', '1^'),
    ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^'),
    ('rt', '52816729^'),
    #('cb', 'jQuery18302667828638578371_1584501852071^'),
    ('_', '1584501882706'),
)

response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies, verify=False)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://push2.eastmoney.com/api/qt/clist/get?pn=1^&pz=50^&po=0^&np=1^&ut=b2884a393a59ad64002292a3e90d46a5^&fltt=2^&invt=2^&fid0=f4001^&fid=f62^&fs=m:0+t:6+f:^!2,m:0+t:13+f:^!2,m:0+t:80+f:^!2,m:1+t:2+f:^!2,m:1+t:23+f:^!2,m:0+t:7+f:^!2,m:1+t:3+f:^!2^&stat=1^&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^&rt=52816729^&cb=jQuery18302667828638578371_1584501852071^&_=1584501882706', headers=headers, cookies=cookies, verify=False)

resp_dic = json.loads(response.text)
print(resp_dic)
datas = resp_dic.get('data').get('diff')
print(datas)

companies = []
prices = []

for data in datas:
    print(data)
    Company = data.get('f14')
    share_1 = data.get('f184')
    price = data.get('f2')

    if share_1 <= -15:
        companies.append(Company)
        prices.append(price)

print(companies)
print(prices)

from pyecharts.charts import Bar
import pyecharts.options as opts

bar = Bar()
bar.add_xaxis(companies)
bar.add_yaxis('股价图',prices)

bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=-40),
    ),
    yaxis_opts=opts.AxisOpts(name='价格：（元/股）'),
    )

bar.render('股价图.html')


