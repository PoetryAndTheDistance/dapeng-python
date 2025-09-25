from flask import Blueprint, request
from bao_stack.其它API.获取交易日信息 import query_trade_dates
from bao_stack.其它API.获取某日所有证券信息 import query_all_stock

# 创建蓝图
bao_stack = Blueprint('证券宝', __name__, url_prefix='/bao_stack')

"""
查询出给定范围的交易日信息

@param start_date: 起始日期，默认2015-01-01
@param end_date: 终止日期，默认当前日期
@return: calendar_date 日期；is_trading_day 是否交易日，0:非交易日;1:交易日
"""
@bao_stack.route('/query_trade_dates_api', methods=['POST'])
def query_trade_dates_api():
    param = request.get_json()
    start_date = param.get('start_date')
    end_date = param.get('end_date')
    result = query_trade_dates(start_date, end_date)
    return result


"""查询给定日期的所有证券信息，

@param day: 默认当前日期
@return: code 代码；code_name 名称，tradeStatus 交易状态，0:停牌;1:交易
"""
@bao_stack.route('/query_all_stock_api', methods=['POST'])
def query_all_stock_api():
    param = request.get_json()
    day = param.get('day')
    result = query_all_stock(day)
    return result