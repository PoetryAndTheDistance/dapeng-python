import baostock as bs
import pandas as pd
import json

#方法说明：通过API接口获取行业分类信息，更新频率：每周一更新。返回类型：pandas的DataFrame类型。
#http://baostock.com/baostock/index.php/%E8%A1%8C%E4%B8%9A%E5%88%86%E7%B1%BB
def query_stock_industry(code: str, date: str):
    print('==========query_stock_industry')
    # 登陆系统
    lg = bs.login()

    # 获取行业分类数据
    rs = bs.query_stock_industry(code=code, date=date)

    # 打印结果集
    industry_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        industry_list.append(rs.get_row_data())
    result = pd.DataFrame(industry_list, columns=rs.fields)

    #### 转换为JSON对象 ####
    json_result = result.to_json(orient='records', force_ascii=False)

    #### 打印JSON结果 ####
    #[{"updateDate":"2025-09-22","code":"sh.600000","code_name":"浦发银行","industry":"J66货币金融服务","industryClassification":"证监会行业分类"}]
    print("result:", json_result)

    # 登出系统
    bs.logout()
    return json.loads(json_result)

if __name__ == '__main__':
    query_stock_industry(None, None)