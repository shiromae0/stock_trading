import statistics

from data_token import get_stock_info,get_code_list
code = get_code_list(6)
def check_TD(windows = 2):
    win = 0
    lose = 0
    change_ratio = []
    cnt = 0
    for c in code:
        cnt+=1
        if cnt>500:
            break
        data_dict = get_stock_info(c)
        for i in range(12,len(data_dict)-windows):
            is_buy_setup = True
            for j in range(9):
                if float(data_dict[i - j]['close']) >= float(data_dict[i - j - 4]['close']):
                    is_buy_setup = False
                    break
            if is_buy_setup == True:
                if float(data_dict[i + windows]['close'])>float(data_dict[i]['close']):
                    win += 1
                else:
                    lose += 1
                if float(data_dict[i]['close'])!=0:
                    change_ratio.append(float(data_dict[i + windows]['close'])/float(data_dict[i]['close'])-1)
    print(win/(win+lose),len(change_ratio),sum(change_ratio)/len(change_ratio),statistics.median(change_ratio))
def check_momentum(windows = 7):
    win = 0
    lose = 0
    change_ratio = []
    cnt = 0
    for c in code:
        cnt += 1
        if cnt > 300:
            break
        data_dict = get_stock_info(c)
        for i in range(12, len(data_dict) - windows):
            is_buy_setup = True
            for j in range(5):
                if float(data_dict[i - j]['close']) >= float(data_dict[i - j]['open']):
                    is_buy_setup = False
                    break
            if is_buy_setup == True:
                if float(data_dict[i + windows]['close']) > float(data_dict[i]['close']):
                    win += 1
                else:
                    lose += 1
                if float(data_dict[i]['close']) != 0:
                    change_ratio.append(float(data_dict[i + windows]['close']) / float(data_dict[i]['close']) - 1)
    print(win / (win + lose), len(change_ratio), sum(change_ratio) / len(change_ratio), statistics.median(change_ratio))
check_momentum(2)
check_momentum(4)
check_momentum(7)
check_momentum(10)