# encoding: UTF-8

structDict = {}

#//////////////////////////////////////////////////////////////////////
#@company shanghai liber information Technology Co.,Ltd
#@file SecurityFtdcL2MDUserApiStruct.h
#@brief 定义业务数据结构
#//////////////////////////////////////////////////////////////////////












#响应信息
CSecurityFtdcRspInfoField = {"ErrorID": "int", "ErrorMsg": "string"}
#错误代码
#错误信息
structDict['CSecurityFtdcRspInfoField'] = CSecurityFtdcRspInfoField


#用户登录信息
CSecurityFtdcUserLoginField = {"TradingDay": "string", "BrokerID": "string", "UserID": "string", "Password": "string",
							   "DataLevel": "string"}
#交易日
#经纪公司代码
#用户代码
#密码
#行情数据等级
structDict['CSecurityFtdcUserLoginField'] = CSecurityFtdcUserLoginField


#用户登出信息
CSecurityFtdcUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSecurityFtdcUserLogoutField'] = CSecurityFtdcUserLogoutField


#指定的合约
CSecurityFtdcSpecificInstrumentField = {"InstrumentID": "string", "ExchangeID": "string"}
#合约代码
#交易所代码
structDict['CSecurityFtdcSpecificInstrumentField'] = CSecurityFtdcSpecificInstrumentField


#Level2行情
CSecurityFtdcL2MarketDataField = {"TradingDay": "string", "TimeStamp": "string", "ExchangeID": "string",
								  "InstrumentID": "string", "PreClosePrice": "float", "OpenPrice": "float",
								  "ClosePrice": "float", "IOPV": "float", "YieldToMaturity": "float",
								  "HighPrice": "float", "LowPrice": "float", "LastPrice": "float", "TradeCount": "int",
								  "TotalTradeVolume": "float", "TotalTradeValue": "float", "TotalBidVolume": "float",
								  "WeightedAvgBidPrice": "float", "AltWeightedAvgBidPrice": "float",
								  "TotalOfferVolume": "float", "WeightedAvgOfferPrice": "float",
								  "AltWeightedAvgOfferPrice": "float", "BidPriceLevel": "int", "OfferPriceLevel": "int",
								  "BidPrice1": "float", "BidVolume1": "int", "BidCount1": "int", "BidPrice2": "float",
								  "BidVolume2": "int", "BidCount2": "int", "BidPrice3": "float", "BidVolume3": "int",
								  "BidCount3": "int", "BidPrice4": "float", "BidVolume4": "int", "BidCount4": "int",
								  "BidPrice5": "float", "BidVolume5": "int", "BidCount5": "int", "BidPrice6": "float",
								  "BidVolume6": "int", "BidCount6": "int", "BidPrice7": "float", "BidVolume7": "int",
								  "BidCount7": "int", "BidPrice8": "float", "BidVolume8": "int", "BidCount8": "int",
								  "BidPrice9": "float", "BidVolume9": "int", "BidCount9": "int", "BidPriceA": "float",
								  "BidVolumeA": "int", "BidCountA": "int", "OfferPrice1": "float",
								  "OfferVolume1": "int", "OfferCount1": "int", "OfferPrice2": "float",
								  "OfferVolume2": "int", "OfferCount2": "int", "OfferPrice3": "float",
								  "OfferVolume3": "int", "OfferCount3": "int", "OfferPrice4": "float",
								  "OfferVolume4": "int", "OfferCount4": "int", "OfferPrice5": "float",
								  "OfferVolume5": "int", "OfferCount5": "int", "OfferPrice6": "float",
								  "OfferVolume6": "int", "OfferCount6": "int", "OfferPrice7": "float",
								  "OfferVolume7": "int", "OfferCount7": "int", "OfferPrice8": "float",
								  "OfferVolume8": "int", "OfferCount8": "int", "OfferPrice9": "float",
								  "OfferVolume9": "int", "OfferCount9": "int", "OfferPriceA": "float",
								  "OfferVolumeA": "int", "OfferCountA": "int"}
#交易日
#时间戳
#交易所代码
#合约代码
#昨收盘价
#今开盘价
#收盘价
#净值估值
#到期收益率
#最高价
#最低价
#最新价
#成交笔数
#成交总量
#成交总金额
#委托买入总量
#加权平均委买价
#债券加权平均委买价
#委托卖出总量
#加权平均委卖价
#债券加权平均委卖价格
#买价深度
#卖价深度
#申买价一
#申买量一
#实际买总委托笔数一
#申买价二
#申买量二
#实际买总委托笔数二
#申买价三
#申买量三
#实际买总委托笔数三
#申买价四
#申买量四
#实际买总委托笔数四
#申买价五
#申买量五
#实际买总委托笔数五
#申买价六
#申买量六
#实际买总委托笔数六
#申买价七
#申买量七
#实际买总委托笔数七
#申买价八
#申买量八
#实际买总委托笔数八
#申买价九
#申买量九
#实际买总委托笔数九
#申买价十
#申买量十
#实际买总委托笔数十
#申卖价一
#申卖量一
#实际卖总委托笔数一
#申卖价二
#申卖量二
#实际卖总委托笔数二
#申卖价三
#申卖量三
#实际卖总委托笔数三
#申卖价四
#申卖量四
#实际卖总委托笔数四
#申卖价五
#申卖量五
#实际卖总委托笔数五
#申卖价六
#申卖量六
#实际卖总委托笔数六
#申卖价七
#申卖量七
#实际卖总委托笔数七
#申卖价八
#申卖量八
#实际卖总委托笔数八
#申卖价九
#申卖量九
#实际卖总委托笔数九
#申卖价十
#申卖量十
#实际卖总委托笔数十
structDict['CSecurityFtdcL2MarketDataField'] = CSecurityFtdcL2MarketDataField


#Level2行情更新时间属性
CSecurityFtdcL2UpdateTimeField = {"TradingDay": "string", "TimeStamp": "string", "ExchangeID": "string",
								  "InstrumentID": "string"}
#交易日
#时间戳
#交易所代码
#合约代码
structDict['CSecurityFtdcL2UpdateTimeField'] = CSecurityFtdcL2UpdateTimeField


#Level2行情静态属性
CSecurityFtdcL2StaticField = {"PreClosePrice": "float", "OpenPrice": "float", "ClosePrice": "float", "IOPV": "float",
							  "YieldToMaturity": "float"}
#昨收盘价
#今开盘价
#收盘价
#净值估值
#到期收益率
structDict['CSecurityFtdcL2StaticField'] = CSecurityFtdcL2StaticField


#Level2行情价格区间属性
CSecurityFtdcL2PriceIntervalField = {"HighPrice": "float", "LowPrice": "float"}
#最高价
#最低价
structDict['CSecurityFtdcL2PriceIntervalField'] = CSecurityFtdcL2PriceIntervalField


#Level2行情基本信息
CSecurityFtdcL2BaseField = {"LastPrice": "float"}
#最新价
structDict['CSecurityFtdcL2BaseField'] = CSecurityFtdcL2BaseField


#Level2成交信息
CSecurityFtdcL2TradedField = {"TradeCount": "int", "TotalTradeVolume": "float", "TotalTradeValue": "float"}
#成交笔数
#成交总量
#成交总金额
structDict['CSecurityFtdcL2TradedField'] = CSecurityFtdcL2TradedField


#Level2行情数据属性
CSecurityFtdcL2DataLevelField = {"Price": "float", "Volume": "int", "Count": "int"}
#价格
#数量
#实际总委托笔数
structDict['CSecurityFtdcL2DataLevelField'] = CSecurityFtdcL2DataLevelField


#Level2委买信息
CSecurityFtdcL2BidOrderField = {"TotalBidVolume": "float", "WeightedAvgBidPrice": "float",
								"AltWeightedAvgBidPrice": "float"}
#委托买入总量
#加权平均委买价
#债券加权平均委买价
structDict['CSecurityFtdcL2BidOrderField'] = CSecurityFtdcL2BidOrderField


#Level2委卖信息
CSecurityFtdcL2OfferOrderField = {"TotalOfferVolume": "float", "WeightedAvgOfferPrice": "float",
								  "AltWeightedAvgOfferPrice": "float"}
#委托卖出总量
#加权平均委卖价
#债券加权平均委卖价格
structDict['CSecurityFtdcL2OfferOrderField'] = CSecurityFtdcL2OfferOrderField


#Level2价格深度属性
CSecurityFtdcL2PriceLevelField = {"BidPriceLevel": "int", "OfferPriceLevel": "int"}
#买价深度
#卖价深度
structDict['CSecurityFtdcL2PriceLevelField'] = CSecurityFtdcL2PriceLevelField


#Level2行情申买一属性
CSecurityFtdcL2Bid1Field = {"BidPrice1": "float", "BidVolume1": "int", "BidCount1": "int"}
#申买价一
#申买量一
#实际买总委托笔数一
structDict['CSecurityFtdcL2Bid1Field'] = CSecurityFtdcL2Bid1Field


#Level2行情申卖一属性
CSecurityFtdcL2Offer1Field = {"OfferPrice1": "float", "OfferVolume1": "int", "OfferCount1": "int"}
#申卖价一
#申卖量一
#实际卖总委托笔数一
structDict['CSecurityFtdcL2Offer1Field'] = CSecurityFtdcL2Offer1Field


#Level2行情申买二属性
CSecurityFtdcL2Bid2Field = {"BidPrice2": "float", "BidVolume2": "int", "BidCount2": "int"}
#申买价二
#申买量二
#实际买总委托笔数二
structDict['CSecurityFtdcL2Bid2Field'] = CSecurityFtdcL2Bid2Field


#Level2行情申卖二属性
CSecurityFtdcL2Offer2Field = {"OfferPrice2": "float", "OfferVolume2": "int", "OfferCount2": "int"}
#申卖价二
#申卖量二
#实际卖总委托笔数二
structDict['CSecurityFtdcL2Offer2Field'] = CSecurityFtdcL2Offer2Field


#Level2行情申买三属性
CSecurityFtdcL2Bid3Field = {"BidPrice3": "float", "BidVolume3": "int", "BidCount3": "int"}
#申买价三
#申买量三
#实际买总委托笔数三
structDict['CSecurityFtdcL2Bid3Field'] = CSecurityFtdcL2Bid3Field


#Level2行情申卖三属性
CSecurityFtdcL2Offer3Field = {"OfferPrice3": "float", "OfferVolume3": "int", "OfferCount3": "int"}
#申卖价三
#申卖量三
#实际卖总委托笔数三
structDict['CSecurityFtdcL2Offer3Field'] = CSecurityFtdcL2Offer3Field


#Level2行情申买四属性
CSecurityFtdcL2Bid4Field = {"BidPrice4": "float", "BidVolume4": "int", "BidCount4": "int"}
#申买价四
#申买量四
#实际买总委托笔数四
structDict['CSecurityFtdcL2Bid4Field'] = CSecurityFtdcL2Bid4Field


#Level2行情申卖四属性
CSecurityFtdcL2Offer4Field = {"OfferPrice4": "float", "OfferVolume4": "int", "OfferCount4": "int"}
#申卖价四
#申卖量四
#实际卖总委托笔数四
structDict['CSecurityFtdcL2Offer4Field'] = CSecurityFtdcL2Offer4Field


#Level2行情申买五属性
CSecurityFtdcL2Bid5Field = {"BidPrice5": "float", "BidVolume5": "int", "BidCount5": "int"}
#申买价五
#申买量五
#实际买总委托笔数五
structDict['CSecurityFtdcL2Bid5Field'] = CSecurityFtdcL2Bid5Field


#Level2行情申卖五属性
CSecurityFtdcL2Offer5Field = {"OfferPrice5": "float", "OfferVolume5": "int", "OfferCount5": "int"}
#申卖价五
#申卖量五
#实际卖总委托笔数五
structDict['CSecurityFtdcL2Offer5Field'] = CSecurityFtdcL2Offer5Field


#Level2行情申买六属性
CSecurityFtdcL2Bid6Field = {"BidPrice6": "float", "BidVolume6": "int", "BidCount6": "int"}
#申买价六
#申买量六
#实际买总委托笔数六
structDict['CSecurityFtdcL2Bid6Field'] = CSecurityFtdcL2Bid6Field


#Level2行情申卖六属性
CSecurityFtdcL2Offer6Field = {"OfferPrice6": "float", "OfferVolume6": "int", "OfferCount6": "int"}
#申卖价六
#申卖量六
#实际卖总委托笔数六
structDict['CSecurityFtdcL2Offer6Field'] = CSecurityFtdcL2Offer6Field


#Level2行情申买七属性
CSecurityFtdcL2Bid7Field = {"BidPrice7": "float", "BidVolume7": "int", "BidCount7": "int"}
#申买价七
#申买量七
#实际买总委托笔数七
structDict['CSecurityFtdcL2Bid7Field'] = CSecurityFtdcL2Bid7Field


#Level2行情申卖七属性
CSecurityFtdcL2Offer7Field = {"OfferPrice7": "float", "OfferVolume7": "int", "OfferCount7": "int"}
#申卖价七
#申卖量七
#实际卖总委托笔数七
structDict['CSecurityFtdcL2Offer7Field'] = CSecurityFtdcL2Offer7Field


#Level2行情申买八属性
CSecurityFtdcL2Bid8Field = {"BidPrice8": "float", "BidVolume8": "int", "BidCount8": "int"}
#申买价八
#申买量八
#实际买总委托笔数八
structDict['CSecurityFtdcL2Bid8Field'] = CSecurityFtdcL2Bid8Field


#Level2行情申卖八属性
CSecurityFtdcL2Offer8Field = {"OfferPrice8": "float", "OfferVolume8": "int", "OfferCount8": "int"}
#申卖价八
#申卖量八
#实际卖总委托笔数八
structDict['CSecurityFtdcL2Offer8Field'] = CSecurityFtdcL2Offer8Field


#Level2行情申买九属性
CSecurityFtdcL2Bid9Field = {"BidPrice9": "float", "BidVolume9": "int", "BidCount9": "int"}
#申买价九
#申买量九
#实际买总委托笔数九
structDict['CSecurityFtdcL2Bid9Field'] = CSecurityFtdcL2Bid9Field


#Level2行情申卖九属性
CSecurityFtdcL2Offer9Field = {"OfferPrice9": "float", "OfferVolume9": "int", "OfferCount9": "int"}
#申卖价九
#申卖量九
#实际卖总委托笔数九
structDict['CSecurityFtdcL2Offer9Field'] = CSecurityFtdcL2Offer9Field


#Level2行情申买十属性
CSecurityFtdcL2BidAField = {"BidPriceA": "float", "BidVolumeA": "int", "BidCountA": "int"}
#申买价十
#申买量十
#实际买总委托笔数十
structDict['CSecurityFtdcL2BidAField'] = CSecurityFtdcL2BidAField


#Level2行情申卖十属性
CSecurityFtdcL2OfferAField = {"OfferPriceA": "float", "OfferVolumeA": "int", "OfferCountA": "int"}
#申卖价十
#申卖量十
#实际卖总委托笔数十
structDict['CSecurityFtdcL2OfferAField'] = CSecurityFtdcL2OfferAField


#Level2行情申买属性
CSecurityFtdcL2BidField = {"BidPrice1": "float", "BidVolume1": "int", "BidCount1": "int", "BidPrice2": "float",
						   "BidVolume2": "int", "BidCount2": "int", "BidPrice3": "float", "BidVolume3": "int",
						   "BidCount3": "int", "BidPrice4": "float", "BidVolume4": "int", "BidCount4": "int",
						   "BidPrice5": "float", "BidVolume5": "int", "BidCount5": "int", "BidPrice6": "float",
						   "BidVolume6": "int", "BidCount6": "int", "BidPrice7": "float", "BidVolume7": "int",
						   "BidCount7": "int", "BidPrice8": "float", "BidVolume8": "int", "BidCount8": "int",
						   "BidPrice9": "float", "BidVolume9": "int", "BidCount9": "int", "BidPriceA": "float",
						   "BidVolumeA": "int", "BidCountA": "int"}
#申买价一
#申买量一
#实际买总委托笔数一
#申买价二
#申买量二
#实际买总委托笔数二
#申买价三
#申买量三
#实际买总委托笔数三
#申买价四
#申买量四
#实际买总委托笔数四
#申买价五
#申买量五
#实际买总委托笔数五
#申买价六
#申买量六
#实际买总委托笔数六
#申买价七
#申买量七
#实际买总委托笔数七
#申买价八
#申买量八
#实际买总委托笔数八
#申买价九
#申买量九
#实际买总委托笔数九
#申买价十
#申买量十
#实际买总委托笔数十
structDict['CSecurityFtdcL2BidField'] = CSecurityFtdcL2BidField


#Level2行情申卖属性
CSecurityFtdcL2OfferField = {"OfferPrice1": "float", "OfferVolume1": "int", "OfferCount1": "int",
							 "OfferPrice2": "float", "OfferVolume2": "int", "OfferCount2": "int",
							 "OfferPrice3": "float", "OfferVolume3": "int", "OfferCount3": "int",
							 "OfferPrice4": "float", "OfferVolume4": "int", "OfferCount4": "int",
							 "OfferPrice5": "float", "OfferVolume5": "int", "OfferCount5": "int",
							 "OfferPrice6": "float", "OfferVolume6": "int", "OfferCount6": "int",
							 "OfferPrice7": "float", "OfferVolume7": "int", "OfferCount7": "int",
							 "OfferPrice8": "float", "OfferVolume8": "int", "OfferCount8": "int",
							 "OfferPrice9": "float", "OfferVolume9": "int", "OfferCount9": "int",
							 "OfferPriceA": "float", "OfferVolumeA": "int", "OfferCountA": "int"}
#申卖价一
#申卖量一
#实际卖总委托笔数一
#申卖价二
#申卖量二
#实际卖总委托笔数二
#申卖价三
#申卖量三
#实际卖总委托笔数三
#申卖价四
#申卖量四
#实际卖总委托笔数四
#申卖价五
#申卖量五
#实际卖总委托笔数五
#申卖价六
#申卖量六
#实际卖总委托笔数六
#申卖价七
#申卖量七
#实际卖总委托笔数七
#申卖价八
#申卖量八
#实际卖总委托笔数八
#申卖价九
#申卖量九
#实际卖总委托笔数九
#申卖价十
#申卖量十
#实际卖总委托笔数十
structDict['CSecurityFtdcL2OfferField'] = CSecurityFtdcL2OfferField


#Level2指数行情
CSecurityFtdcL2IndexField = {"TradingDay": "string", "TimeStamp": "string", "ExchangeID": "string",
							 "InstrumentID": "string", "PreCloseIndex": "float", "OpenIndex": "float",
							 "CloseIndex": "float", "HighIndex": "float", "LowIndex": "float", "LastIndex": "float",
							 "TurnOver": "float", "TotalVolume": "float"}
#交易日
#行情时间（秒）
#交易所代码
#指数代码
#前收盘指数
#今开盘指数
#今日收盘指数
#最高指数
#最低指数
#最新指数
#参与计算相应指数的成交金额（元）
#参与计算相应指数的交易数量（手）
structDict['CSecurityFtdcL2IndexField'] = CSecurityFtdcL2IndexField


#Level2行情用户信息
CSecurityFtdcL2UserInfoField = {"BrokerID": "string", "UserID": "string", "UserName": "string", "Password": "string",
								"DataLevel": "string"}
#经纪公司代码
#用户代码
#用户名称
#密码
#行情数据等级
structDict['CSecurityFtdcL2UserInfoField'] = CSecurityFtdcL2UserInfoField


#UDP组播组信息
CSecurityFtdcMulticastGroupInfoField = {"GroupIP": "string", "GroupPort": "int", "SourceIP": "string"}
#组播组IP地址
#组播组IP端口
#源地址
structDict['CSecurityFtdcMulticastGroupInfoField'] = CSecurityFtdcMulticastGroupInfoField


#Level2逐笔委托
CSecurityFtdcL2OrderField = {"OrderGroupID": "int", "OrderIndex": "int", "OrderTime": "string", "ExchangeID": "string",
							 "InstrumentID": "string", "Price": "float", "Volume": "int", "OrderKind": "string",
							 "FunctionCode": "string"}
#委托组
#委托序号
#委托时间（秒）
#交易所代码
#合约代码
#委托价格
#委托数量
#报单类型
#功能码
structDict['CSecurityFtdcL2OrderField'] = CSecurityFtdcL2OrderField


#Level2逐笔成交
CSecurityFtdcL2TradeField = {"TradeGroupID": "int", "TradeIndex": "int", "BuyIndex": "int", "SellIndex": "int",
							 "TradeTime": "string", "ExchangeID": "string", "InstrumentID": "string", "Price": "float",
							 "Volume": "int", "OrderKind": "string", "FunctionCode": "string"}
#成交组
#成交序号
#买方委托序号
#卖方委托序号
#成交时间（秒）
#交易所代码
#合约代码
#成交价格
#成交数量
#报单类型
#功能码
structDict['CSecurityFtdcL2TradeField'] = CSecurityFtdcL2TradeField






