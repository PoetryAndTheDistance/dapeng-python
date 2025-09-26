import baostock as bs
import pandas as pd
import json

#方法说明：通过API接口获取证券基本资料，可以通过参数设置获取对应证券代码、证券名称的数据。 返回类型：pandas的DataFrame类型。
#http://baostock.com/baostock/index.php/%E8%AF%81%E5%88%B8%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99
def query_stock_basic(code: str, code_name: str):
    print('==========query_stock_basic')
    #### 登陆系统 ####
    lg = bs.login()

    # 获取证券基本资料
    rs = bs.query_stock_basic(code=code, code_name=code_name)# 支持模糊查询

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 转换为JSON对象 ####
    #[{"code":"sh.000001","code_name":"上证综合指数","ipoDate":"1991-07-15","outDate":"","type":"2","status":"1"}]
    json_result = result.to_json(orient='records', force_ascii=False)

    #### 打印JSON结果 ####
    print("result:", json_result)

    # 登出系统
    bs.logout()
    return json.loads(json_result)

if __name__ == '__main__':
    query_stock_basic(None, None)