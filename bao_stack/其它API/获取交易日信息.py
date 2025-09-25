import baostock as bs
import pandas as pd

def query_trade_dates(start_date: str, end_date: str):
    print('==========query_trade_dates')
    #### 登陆系统 ####
    lg = bs.login()

    #### 获取交易日信息 ####
    rs = bs.query_trade_dates(start_date=start_date, end_date=end_date)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 转换为JSON对象 ####
    json_result = result.to_json(orient='records', force_ascii=False)

    #### 打印JSON结果 ####
    print("result:",json_result)

    #### 登出系统 ####
    bs.logout()
    return json_result

if __name__ == '__main__':
    query_trade_dates('2025-09-22', '2025-10-22')