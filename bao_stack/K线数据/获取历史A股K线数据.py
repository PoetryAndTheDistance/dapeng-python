import baostock as bs
import pandas as pd
import json

#通过API接口获取A股历史（1990-12-19至当前时间）（不复权、前复权、后复权）交易数据，可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据，适合搭配均线数据进行选股和分析。返回类型：pandas的DataFrame类型。
#http://baostock.com/baostock/index.php/A%E8%82%A1K%E7%BA%BF%E6%95%B0%E6%8D%AE

#日线
def query_history_k_data_plus_day(code: str, start_date: str, end_date: str, frequency: str, adjustflag: str):
    print('==========query_history_k_data_plus_day')
    # 登陆系统
    lg = bs.login()

    #### 获取沪深A股历史K线数据 ####
    # 日线指标：date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST
    rs = bs.query_history_k_data_plus(code,
                                      "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST",
                                      start_date=start_date, end_date=end_date,
                                      frequency=frequency, adjustflag=adjustflag)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 转换为JSON对象 ####
    json_result = result.to_json(orient='records', force_ascii=False)

    #### 打印JSON结果 ####
    #[{"date":"2025-09-25","code":"sh.600000","open":"12.2300000000","high":"12.5500000000","low":"12.1300000000","close":"12.4300000000","preclose":"12.2200000000","volume":"128885102","amount":"1599981440.2600","adjustflag":"2","turn":"0.422600","tradestatus":"1","pctChg":"1.718500","peTTM":"7.896472","psTTM":"2.190456","pcfNcfTTM":"-4.696908","pbMRQ":"0.556804","isST":"0"}]
    print("result:", json_result)

    # 登出系统
    bs.logout()
    return json.loads(json_result)

#分钟
def query_history_k_data_plus_minute(code: str, start_date: str, end_date: str, frequency: str, adjustflag: str):
    print('==========query_history_k_data_plus_minute')
    # 登陆系统
    lg = bs.login()

    #### 获取沪深A股历史K线数据 ####
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    rs = bs.query_history_k_data_plus(code,
                                      "date,time,code,open,high,low,close,volume,amount,adjustflag",
                                      start_date=start_date, end_date=end_date,
                                      frequency=frequency, adjustflag=adjustflag)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 转换为JSON对象 ####
    json_result = result.to_json(orient='records', force_ascii=False)

    #### 打印JSON结果 ####
    #[{"date":"2024-07-01","time":"20240701093500000","code":"sh.600000","open":"7.6956544200","high":"7.7331028600","low":"7.6862923100","close":"7.7050165300","volume":"1396900","amount":"11516198.0000","adjustflag":"2"}]
    print("result:", json_result)

    # 登出系统
    bs.logout()
    return json.loads(json_result)

#周月线
def query_history_k_data_plus_week_moon(code: str, start_date: str, end_date: str, frequency: str, adjustflag: str):
    print('==========query_history_k_data_plus_week_moon')
    # 登陆系统
    lg = bs.login()

    #### 获取沪深A股历史K线数据 ####
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    rs = bs.query_history_k_data_plus(code,
                                      "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
                                      start_date=start_date, end_date=end_date,
                                      frequency=frequency, adjustflag=adjustflag)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 转换为JSON对象 ####
    json_result = result.to_json(orient='records', force_ascii=False)

    #### 打印JSON结果 ####
    #[{"date":"2025-09-19","code":"sh.600000","open":"13.5100000000","high":"13.6900000000","low":"12.5600000000","close":"12.8100000000","volume":"425333991","amount":"5559001921.2700","adjustflag":"2","turn":"1.394600","pctChg":"-5.808800"}]
    print("result:", json_result)

    # 登出系统
    bs.logout()
    return json.loads(json_result)

if __name__ == '__main__':
    query_history_k_data_plus_day(code='sh.600000', start_date=None, end_date=None, frequency = 'd', adjustflag = '2')
    #query_history_k_data_plus_minute(code='sh.600000', start_date='2024-07-01', end_date='2024-12-31', frequency = '5', adjustflag = '2')
    # query_history_k_data_plus_week_moon(code='sh.600000', start_date=None, end_date=None, frequency = 'w', adjustflag = '2')