import csv
import datetime

import requests
from bs4 import BeautifulSoup


def get_stock_info(code):
    path = "C:\\Users\\51392\\Desktop\\project\\stock_trading\\stock_data\\"
    path = path + code+'.csv'
    with open(path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        data_dict = {}
        cnt = 0
        for r in reader:
            # 创建字典,key为 日期 开盘 收盘 最高 最低 成交量 成交额 振幅 涨跌幅 涨跌额 换手率
            data_dict[cnt] = {
                "date": datetime.datetime.strptime(r[0], "%Y-%m-%d"),
                "open": float(r[1]),
                "close": float(r[2]),
                "high": float(r[3]),
                "low": float(r[4]),
                "volume": int(r[5]),
                "turnover": float(r[6]),
                "amp": float(r[7]),
                "change_ratio": float(r[8]),
                "change": float(r[9]),
                "turnover_ratio": float(r[10])
            }
            cnt += 1
    return data_dict
def get_code_list(startNumber = -1):
    path = "C:\\Users\\51392\\Desktop\\project\\stock_trading\\stock_data\\code.txt"
    code = []
    with open (path,"r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if startNumber!=-1:
                if startNumber == int(line[0]):
                    code.append(line)
            else:
                code.append(line)
    return code
