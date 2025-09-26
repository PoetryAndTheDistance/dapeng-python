from flask import Blueprint, request
from bao_stack.获取证券元信息.获取交易日信息 import query_trade_dates
from bao_stack.获取证券元信息.获取某日所有证券信息 import query_all_stock
from bao_stack.获取证券元信息.证券基本资料 import query_stock_basic
from bao_stack.板块数据.行业分类 import query_stock_industry
from bao_stack.板块数据.上证50成分股 import query_sz50_stocks
from bao_stack.板块数据.沪深300成分股 import query_hs300_stocks
from bao_stack.板块数据.中证500成分股 import query_zz500_stocks
from bao_stack.K线数据.获取历史A股K线数据 import query_history_k_data_plus_day, query_history_k_data_plus_minute, query_history_k_data_plus_week_moon

# 创建蓝图
bao_stack = Blueprint('证券宝', __name__, url_prefix='/bao_stack')

"""
查询出给定范围的交易日信息

@param start_date：开始日期，为空时默认为2015-01-01。
@param end_date: 结束日期，为空时默认为当前日期。

@return: 
参数名称	参数描述
calendar_date	日期
is_trading_day	是否交易日(0:非交易日;1:交易日)
示例
calendar_date	is_trading_day
2017-01-01	0
2017-01-02	0
2017-01-03	1
"""
@bao_stack.route('/query_trade_dates_api', methods=['POST'])
def query_trade_dates_api():
    param = request.get_json()
    start_date = param.get('start_date')
    end_date = param.get('end_date')
    result = query_trade_dates(start_date, end_date)
    return result


"""
查询给定日期的所有证券信息，

@param day: 需要查询的交易日期，为空时默认当前日期。

@return: 
参数名称	参数描述
code	证券代码
tradeStatus	交易状态(1：正常交易 0：停牌）
code_name	证券名称
示例
code	tradeStatus	code_name
sh.000001	1	上证综合指数
sh.000002	1	上证A股指数
sh.000003	1	上证B股指数
"""
@bao_stack.route('/query_all_stock_api', methods=['POST'])
def query_all_stock_api():
    param = request.get_json()
    day = param.get('day')
    result = query_all_stock(day)
    return result


"""
A股证券基本资料

@param code: A股股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。可以为空；
@param code_name: 股票名称，支持模糊查询，可以为空。
当参数为空时，输出全部股票的基本信息。

@return: 
参数名称	参数描述
code	证券代码
code_name	证券名称
ipoDate	上市日期
outDate	退市日期
type	证券类型，其中1：股票，2：指数，3：其它，4：可转债，5：ETF
status	上市状态，其中1：上市，0：退市
示例
code	code_name	ipoDate	outDate	type	status
sh.600000	浦发银行	1999-11-10		1	1
"""
@bao_stack.route('/query_stock_basic_api', methods=['POST'])
def query_stock_basic_api():
    param = request.get_json()
    code = param.get('code')
    code_name = param.get('code_name')
    result = query_stock_basic(code, code_name)
    return result


"""
行业分类

@param code：A股股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。可以为空；
@param date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

@return: 
参数名称	参数描述
updateDate	更新日期
code	证券代码
code_name	证券名称
industry	所属行业
industryClassification	所属行业类别
示例
updateDate	code	code_name	industry	industryClassification
2018-11-26	sh.600000	浦发银行	J66货币金融服务	证监会行业分类
2018-11-26	sh.600001	邯郸钢铁		证监会行业分类
"""
@bao_stack.route('/query_stock_industry_api', methods=['POST'])
def query_stock_industry_api():
    param = request.get_json()
    code = param.get('code')
    date = param.get('date')
    result = query_stock_industry(code, date)
    return result

"""
上证50成分股

@param date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

@return: 
参数名称	参数描述
updateDate	更新日期
code	证券代码
code_name	证券名称
示例
updateDate	code	code_name
2018-11-26	sh.600000	浦发银行
2018-11-26	sh.600016	民生银行
"""
@bao_stack.route('/query_sz50_stocks_api', methods=['POST'])
def query_sz50_stocks_api():
    param = request.get_json()
    date = param.get('date')
    result = query_sz50_stocks(date)
    return result

"""
沪深300成分股

@param date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

@return: 
参数名称	参数描述
updateDate	更新日期
code	证券代码
code_name	证券名称
示例
updateDate	code	code_name
2018-11-26	sh.600000	浦发银行
2018-11-26	sh.600008	首创股份
"""
@bao_stack.route('/query_hs300_stocks_api', methods=['POST'])
def query_hs300_stocks_api():
    param = request.get_json()
    date = param.get('date')
    result = query_hs300_stocks(date)
    return result

"""
中证500成分股

@param date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。

@return: 
参数名称	参数描述
updateDate	更新日期
code	证券代码
code_name	证券名称
示例
updateDate	code	code_name
2018-11-26	sh.600004	白云机场
2018-11-26	sh.600006	东风汽车
"""
@bao_stack.route('/query_zz500_stocks_api', methods=['POST'])
def query_zz500_stocks_api():
    param = request.get_json()
    date = param.get('date')
    result = query_zz500_stocks(date)
    return result

"""
获取历史A股K线数据-日线

@param
code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
fields：指示简称，支持多指标输入，以半角逗号分隔，填写内容作为返回类型的列。详细指标列表见历史行情指标参数章节，日线与分钟线参数不同。此参数不可为空；
start_date：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
end_date：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线每月最后一个交易日才可以获取。
adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权。 BaoStock提供的是涨跌幅复权算法复权因子，具体介绍见：《复权因子简介》或者《BaoStock复权因子简介》。

@return: 
参数名称	参数描述	说明
date	交易所行情日期	格式：YYYY-MM-DD
code	证券代码	格式：sh.600000。sh：上海，sz：深圳
open	今开盘价格	精度：小数点后4位；单位：人民币元
high	最高价	精度：小数点后4位；单位：人民币元
low	最低价	精度：小数点后4位；单位：人民币元
close	今收盘价	精度：小数点后4位；单位：人民币元
preclose	昨日收盘价	精度：小数点后4位；单位：人民币元
volume	成交数量	单位：股
amount	成交金额	精度：小数点后4位；单位：人民币元
adjustflag	复权状态	不复权、前复权、后复权
turn	换手率	精度：小数点后6位；单位：%
tradestatus	交易状态	1：正常交易 0：停牌
pctChg	涨跌幅（百分比）	精度：小数点后6位
peTTM	滚动市盈率	精度：小数点后6位
psTTM	滚动市销率	精度：小数点后6位
pcfNcfTTM	滚动市现率	精度：小数点后6位
pbMRQ	市净率	精度：小数点后6位
isST	是否ST	1是，0否
示例
[{
  "date" : "2025-09-25",
  "code" : "sh.600000",
  "open" : "12.2300000000",
  "high" : "12.5500000000",
  "low" : "12.1300000000",
  "close" : "12.4300000000",
  "preclose" : "12.2200000000",
  "volume" : "128885102",
  "amount" : "1599981440.2600",
  "adjustflag" : "2",
  "turn" : "0.422600",
  "tradestatus" : "1",
  "pctChg" : "1.718500",
  "peTTM" : "7.896472",
  "psTTM" : "2.190456",
  "pcfNcfTTM" : "-4.696908",
  "pbMRQ" : "0.556804",
  "isST" : "0"
}]
"""
@bao_stack.route('/query_history_k_data_plus_day_api', methods=['POST'])
def query_history_k_data_plus_day_api():
    param = request.get_json()
    code = param.get('code')
    start_date = param.get('start_date')
    end_date = param.get('end_date')
    frequency = param.get('frequency')
    adjustflag = param.get('adjustflag')
    result = query_history_k_data_plus_day(code, start_date, end_date, frequency, adjustflag)
    return result

"""
获取历史A股K线数据-分钟线

@param
code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
fields：指示简称，支持多指标输入，以半角逗号分隔，填写内容作为返回类型的列。详细指标列表见历史行情指标参数章节，日线与分钟线参数不同。此参数不可为空；
start_date：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
end_date：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线每月最后一个交易日才可以获取。
adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权。 BaoStock提供的是涨跌幅复权算法复权因子，具体介绍见：《复权因子简介》或者《BaoStock复权因子简介》。

@return: 
参数名称	参数描述	说明
date	交易所行情日期	格式：YYYY-MM-DD
time	交易所行情时间	格式：YYYYMMDDHHMMSSsss
code	证券代码	格式：sh.600000。sh：上海，sz：深圳
open	开盘价格	精度：小数点后4位；单位：人民币元
high	最高价	精度：小数点后4位；单位：人民币元
low	最低价	精度：小数点后4位；单位：人民币元
close	收盘价	精度：小数点后4位；单位：人民币元
volume	成交数量	单位：股； 时间范围内的累计成交数量
amount	成交金额	精度：小数点后4位；单位：人民币元； 时间范围内的累计成交金额
adjustflag	复权状态	不复权、前复权、后复权
示例
[{
  "date" : "2024-12-31",
  "time" : "20241231150000000",
  "code" : "sh.600000",
  "open" : "10.0065457700",
  "high" : "10.0065457700",
  "low" : "9.9871344300",
  "close" : "9.9871344300",
  "volume" : "2855700",
  "amount" : "29389309.0000",
  "adjustflag" : "2"
}]
"""
@bao_stack.route('/query_history_k_data_plus_minute_api', methods=['POST'])
def query_history_k_data_plus_minute_api():
    param = request.get_json()
    code = param.get('code')
    start_date = param.get('start_date')
    end_date = param.get('end_date')
    frequency = param.get('frequency')
    adjustflag = param.get('adjustflag')
    result = query_history_k_data_plus_minute(code, start_date, end_date, frequency, adjustflag)
    return result

"""
获取历史A股K线数据-周月线

@param
code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
fields：指示简称，支持多指标输入，以半角逗号分隔，填写内容作为返回类型的列。详细指标列表见历史行情指标参数章节，日线与分钟线参数不同。此参数不可为空；
start_date：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
end_date：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线每月最后一个交易日才可以获取。
adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权。 BaoStock提供的是涨跌幅复权算法复权因子，具体介绍见：《复权因子简介》或者《BaoStock复权因子简介》。

@return: 
参数名称	参数描述	说明	算法说明
date	交易所行情日期	格式：YYYY-MM-DD	
code	证券代码	格式：sh.600000。sh：上海，sz：深圳	
open	开盘价格	精度：小数点后4位；单位：人民币元	
high	最高价	精度：小数点后4位；单位：人民币元	
low	最低价	精度：小数点后4位；单位：人民币元	
close	收盘价	精度：小数点后4位；单位：人民币元	
volume	成交数量	单位：股	
amount	成交金额	精度：小数点后4位；单位：人民币元	
adjustflag	复权状态	不复权、前复权、后复权	
turn	换手率	精度：小数点后6位；单位：%	
pctChg	涨跌幅（百分比）	精度：小数点后6位	涨跌幅=[(区间最后交易日收盘价-区间首个交易日前收盘价)/区间首个交易日前收盘价]*100%
示例
[{
  "date" : "2025-09-19",
  "code" : "sh.600000",
  "open" : "13.5100000000",
  "high" : "13.6900000000",
  "low" : "12.5600000000",
  "close" : "12.8100000000",
  "volume" : "425333991",
  "amount" : "5559001921.2700",
  "adjustflag" : "2",
  "turn" : "1.394600",
  "pctChg" : "-5.808800"
}]
"""
@bao_stack.route('/query_history_k_data_plus_week_moon_api', methods=['POST'])
def query_history_k_data_plus_week_moon_api():
    param = request.get_json()
    code = param.get('code')
    start_date = param.get('start_date')
    end_date = param.get('end_date')
    frequency = param.get('frequency')
    adjustflag = param.get('adjustflag')
    result = query_history_k_data_plus_week_moon(code, start_date, end_date, frequency, adjustflag)
    return result