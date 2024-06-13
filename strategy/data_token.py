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
            r[0] = datetime.datetime.strptime(r[0], "%Y-%m-%d")
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
