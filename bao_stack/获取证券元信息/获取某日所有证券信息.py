import baostock as bs
import pandas as pd
import json

#方法说明：获取指定交易日期所有股票列表。通过API接口获取证券代码及股票交易状态信息，与日K线数据同时更新。可以通过参数‘某交易日’获取数据（包括：A股、指数），数据范围同接口query_history_k_data_plus()。
#http://baostock.com/baostock/index.php/%E5%85%B6%E5%AE%83API
def query_all_stock(day: str):
    print('==========query_all_stock')
    #### 登陆系统 ####
    lg = bs.login()

    #### 获取某日所有证券信息 ####
    rs = bs.query_all_stock(day=day)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 转换为JSON对象 ####
    json_result = result.to_json(orient='records', force_ascii=False)

    #### 打印JSON结果 ####
    #[{"code":"sh.000001","tradeStatus":"1","code_name":"上证综合指数"}]
    print("result:", json_result)

    #### 登出系统 ####
    bs.logout()
    return json.loads(json_result)

if __name__ == '__main__':
    query_all_stock('2025-09-25')