import baostock as bs
import pandas as pd
import json

#方法说明：通过API接口获取沪深300成分股信息，更新频率：每周一更新。返回类型：pandas的DataFrame类型。
#http://baostock.com/baostock/index.php/%E6%B2%AA%E6%B7%B1300%E6%88%90%E5%88%86%E8%82%A1
def query_hs300_stocks(date: str):
    print('==========query_hs300_stocks')
    # 登陆系统
    lg = bs.login()

    # 获取沪深300成分股
    rs = bs.query_hs300_stocks(date=date)

    # 打印结果集
    hs300_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        hs300_stocks.append(rs.get_row_data())
    result = pd.DataFrame(hs300_stocks, columns=rs.fields)

    #### 转换为JSON对象 ####
    json_result = result.to_json(orient='records', force_ascii=False)

    #### 打印JSON结果 ####
    #[{"updateDate":"2025-09-22","code":"sh.600000","code_name":"浦发银行"}]
    print("result:", json_result)

    # 登出系统
    bs.logout()
    return json.loads(json_result)

if __name__ == '__main__':
    query_hs300_stocks(None)