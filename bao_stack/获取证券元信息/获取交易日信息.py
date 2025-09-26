import baostock as bs
import pandas as pd
import json

#方法说明：通过API接口获取股票交易日信息，可以通过参数设置获取起止年份数据，提供上交所1990-今年数据。 返回类型：pandas的DataFrame类型。
#http://baostock.com/baostock/index.php/%E5%85%B6%E5%AE%83API
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
    #[{"calendar_date":"2025-09-22","is_trading_day":"1"}]
    print("result:", json_result)

    #### 登出系统 ####
    bs.logout()
    return json.loads(json_result)

if __name__ == '__main__':
    query_trade_dates('2025-09-22', '2025-10-22')