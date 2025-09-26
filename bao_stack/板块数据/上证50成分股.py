import baostock as bs
import pandas as pd

#方法说明：通过API接口获取上证50成分股信息，更新频率：每周一更新。返回类型：pandas的DataFrame类型。
#http://baostock.com/baostock/index.php/%E4%B8%8A%E8%AF%8150%E6%88%90%E5%88%86%E8%82%A1
def query_sz50_stocks(date: str):
    print('==========query_sz50_stocks')
    # 登陆系统
    lg = bs.login()

    # 获取上证50成分股
    rs = bs.query_sz50_stocks(date=date)

    # 打印结果集
    sz50_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        sz50_stocks.append(rs.get_row_data())
    result = pd.DataFrame(sz50_stocks, columns=rs.fields)

    #### 转换为JSON对象 ####
    json_result = result.to_json(orient='records', force_ascii=False)

    #### 打印JSON结果 ####
    #[{"updateDate":"2025-09-22","code":"sh.600028","code_name":"中国石化"}]
    print("result:", json_result)

    # 登出系统
    bs.logout()
    return json_result

if __name__ == '__main__':
    query_sz50_stocks(None)