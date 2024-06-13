import csv

import requests
import re
# 目标网址




def create_table(data_dict,code):
    csv_file = f"stock_data/{code}.csv"
    fieldnames = [
        'date', 'open', 'close', 'high', 'low', 'volume', 'turnover', 'amp', 'change_ratio', 'change', 'turnover_ratio'
    ]
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for key in data_dict:
            writer.writerow(data_dict[key])
def get_info(code):
    url = ('https://53.push2his.eastmoney.com/api/qt/stock/kline/get?'
           f'cb=jQuery351034085342859108203_1718261426335&secid=1.{code}&'
           'ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4'
           '%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf'
           '58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=1000000&_=1718261426356')
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
# 检查请求是否成功
    if response.status_code == 200:
        text = response.text
        #正则表达式匹配 先匹配日期，再匹配一个逗号和一个实数，最后匹配多个实数并区分结尾逗号
        pattern = r'(\d{4}-\d{2}-\d{2},[-]?\d+(\.\d+)?(?:,[-]?\d+(\.\d+)?)*)(?:"|$)'
        matches = re.findall(pattern, text)
        results = [match[0] for match in matches]
        #创建字典,key为 日期 开盘 收盘 最高 最低 成交量 成交额 振幅 涨跌幅 涨跌额 换手率
        cnt = 0
        data_dict = {}
        for result in results:
            r = result.split(",")
            data_dict[cnt] = {
                "date": r[0],
                "open": r[1],
                "close": r[2],
                "high": r[3],
                "low": r[4],
                "volume": r[5],
                "turnover": r[6],
                "amp": r[7],
                "change_ratio": r[8],
                "change": r[9],
                "turnover_ratio": r[10]
            }
            cnt+=1
    else:
        print(f"请求失败，状态码: {response.status_code}")
    return data_dict

create_table(get_info(600000),600000)
