import baostock as bs
import pandas as pd

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
    print("result:", json_result)

    #### 登出系统 ####
    bs.logout()
    return json_result

if __name__ == '__main__':
    query_all_stock('2025-09-25')