# encoding: UTF-8

structDict = {}

#//////////////////////////////////////////////////////////////////////
#@company shanghai liber information Technology Co.,Ltd
#@file SecurityFtdcUserApiStruct.h
#@brief 定义业务数据结构
#//////////////////////////////////////////////////////////////////////












#响应信息
CSecurityFtdcRspInfoField = {"ErrorID": "int", "ErrorMsg": "string"}
#错误代码
#错误信息
structDict['CSecurityFtdcRspInfoField'] = CSecurityFtdcRspInfoField


#交易所
CSecurityFtdcExchangeField = {"ExchangeID": "string", "ExchangeName": "string", "ExchangeProperty": "string"}
#交易所代码
#交易所名称
#交易所属性
structDict['CSecurityFtdcExchangeField'] = CSecurityFtdcExchangeField


#产品
CSecurityFtdcProductField = {"ProductID": "string", "ProductName": "string", "ExchangeID": "string",
							 "ProductClass": "string", "VolumeMultiple": "int", "PriceTick": "float",
							 "MaxMarketOrderVolume": "int", "MinMarketOrderVolume": "int", "MaxLimitOrderVolume": "int",
							 "MinLimitOrderVolume": "int", "PositionType": "string", "PositionDateType": "string",
							 "EFTMinTradeVolume": "int"}
#产品代码
#产品名称
#交易所代码
#产品类型
#合约数量乘数
#最小变动价位
#市价单最大下单量
#市价单最小下单量
#限价单最大下单量
#限价单最小下单量
#持仓类型
#持仓日期类型
#ETF最小交易单位
structDict['CSecurityFtdcProductField'] = CSecurityFtdcProductField


#合约
CSecurityFtdcInstrumentField = {"InstrumentID": "string", "ExchangeID": "string", "InstrumentName": "string",
								"ExchangeInstID": "string", "ProductID": "string", "ProductClass": "string",
								"DeliveryYear": "int", "DeliveryMonth": "int", "MaxMarketOrderVolume": "int",
								"MinMarketOrderVolume": "int", "MaxLimitOrderVolume": "int",
								"MinLimitOrderVolume": "int", "VolumeMultiple": "int", "PriceTick": "float",
								"CreateDate": "string", "OpenDate": "string", "ExpireDate": "string",
								"StartDelivDate": "string", "EndDelivDate": "string", "InstLifePhase": "string",
								"IsTrading": "int", "PositionType": "string", "OrderCanBeWithdraw": "int",
								"MinBuyVolume": "int", "MinSellVolume": "int", "RightModelID": "string",
								"PosTradeType": "string", "MarketID": "string", "ExecPrice": "float",
								"UnitMargin": "float", "InstrumentType": "string", "OptionsMarginParam1": "float",
								"OptionsMarginParam2": "float"}
#合约代码
#交易所代码
#合约名称
#合约在交易所的代码
#产品代码
#产品类型
#交割年份
#交割月
#市价单最大下单量
#市价单最小下单量
#限价单最大下单量
#限价单最小下单量
#合约数量乘数
#最小变动价位
#创建日
#上市日
#到期日
#开始交割日
#结束交割日
#合约生命周期状态
#当前是否交易
#持仓类型
#报单能否撤单
#最小买下单单位
#最小卖下单单位
#股票权限模版代码
#持仓交易类型
#市场代码
#期权执行价格
#期权单手保证金
#合约类型
#期权保证金参数1
#期权保证金参数2
structDict['CSecurityFtdcInstrumentField'] = CSecurityFtdcInstrumentField


#经纪公司
CSecurityFtdcBrokerField = {"BrokerID": "string", "BrokerAbbr": "string", "BrokerName": "string", "IsActive": "int"}
#经纪公司代码
#经纪公司简称
#经纪公司名称
#是否活跃
structDict['CSecurityFtdcBrokerField'] = CSecurityFtdcBrokerField


#会员编码和经纪公司编码对照表
CSecurityFtdcPartBrokerField = {"BrokerID": "string", "ExchangeID": "string", "ParticipantID": "string",
								"IsActive": "int"}
#经纪公司代码
#交易所代码
#会员代码
#是否活跃
structDict['CSecurityFtdcPartBrokerField'] = CSecurityFtdcPartBrokerField


#投资者
CSecurityFtdcInvestorField = {"InvestorID": "string", "BrokerID": "string", "InvestorGroupID": "string",
							  "InvestorName": "string", "IdentifiedCardType": "string", "IdentifiedCardNo": "string",
							  "IsActive": "int", "SHBranchID": "string", "SZBranchID": "string",
							  "SettleSystemType": "string", "InvestorLevel": "string"}
#投资者代码
#经纪公司代码
#投资者分组代码
#投资者名称
#证件类型
#证件号码
#是否活跃
#上海营业部编号
#深圳营业部编号
#所属结算系统类型
#投资者期权交易等级
structDict['CSecurityFtdcInvestorField'] = CSecurityFtdcInvestorField


#交易编码
CSecurityFtdcTradingCodeField = {"InvestorID": "string", "BrokerID": "string", "ExchangeID": "string",
								 "ClientID": "string", "IsActive": "int", "AccountID": "string", "PBU": "string",
								 "ClientType": "string"}
#投资者代码
#经纪公司代码
#交易所代码
#客户代码
#是否活跃
#AccountID
#交易单元号
#ClientType
structDict['CSecurityFtdcTradingCodeField'] = CSecurityFtdcTradingCodeField


#管理用户
CSecurityFtdcSuperUserField = {"UserID": "string", "UserName": "string", "Password": "string", "IsActive": "int"}
#用户代码
#用户名称
#密码
#是否活跃
structDict['CSecurityFtdcSuperUserField'] = CSecurityFtdcSuperUserField


#管理用户功能权限
CSecurityFtdcSuperUserFunctionField = {"UserID": "string", "FunctionCode": "string"}
#用户代码
#功能代码
structDict['CSecurityFtdcSuperUserFunctionField'] = CSecurityFtdcSuperUserFunctionField


#经纪公司用户
CSecurityFtdcBrokerUserField = {"BrokerID": "string", "UserID": "string", "UserName": "string", "UserType": "string",
								"IsActive": "int", "IsUsingOTP": "int"}
#经纪公司代码
#用户代码
#用户名称
#用户类型
#是否活跃
#是否使用令牌
structDict['CSecurityFtdcBrokerUserField'] = CSecurityFtdcBrokerUserField


#经纪公司用户功能权限
CSecurityFtdcBrokerUserFunctionField = {"BrokerID": "string", "UserID": "string", "BrokerFunctionCode": "string"}
#经纪公司代码
#用户代码
#经纪公司功能代码
structDict['CSecurityFtdcBrokerUserFunctionField'] = CSecurityFtdcBrokerUserFunctionField


#资金账户
CSecurityFtdcTradingAccountField = {"BrokerID": "string", "AccountID": "string", "PreMortgage": "float",
									"PreCredit": "float", "PreDeposit": "float", "PreBalance": "float",
									"PreMargin": "float", "InterestBase": "float", "Interest": "float",
									"Deposit": "float", "Withdraw": "float", "FrozenMargin": "float",
									"FrozenCash": "float", "FrozenCommission": "float", "CurrMargin": "float",
									"CashIn": "float", "Commission": "float", "Balance": "float", "Available": "float",
									"WithdrawQuota": "float", "Reserve": "float", "TradingDay": "string",
									"Credit": "float", "Mortgage": "float", "ExchangeMargin": "float",
									"DeliveryMargin": "float", "ExchangeDeliveryMargin": "float",
									"FrozenTransferFee": "float", "FrozenStampTax": "float", "TransferFee": "float",
									"StampTax": "float", "ConversionAmount": "float", "CreditAmount": "float",
									"StockValue": "float", "BondRepurchaseAmount": "float",
									"ReverseRepurchaseAmount": "float", "CurrencyCode": "string",
									"AccountType": "string", "MarginTradeAmount": "float", "ShortSellAmount": "float",
									"MarginTradeProfit": "float", "ShortSellProfit": "float", "SSStockValue": "float",
									"CreditRatio": "float", "FrozenExecCash": "float", "SSEOptionsBuyAmount": "float",
									"SSEOptionsBuyFrozenAmount": "float", "SettleMargin": "float"}
#经纪公司代码
#投资者帐号
#上次质押金额
#上次信用额度
#上次存款额
#上次结算准备金
#上次占用的保证金
#利息基数
#利息收入
#入金金额
#出金金额
#冻结的保证金
#冻结的资金
#冻结的手续费
#当前保证金总额
#资金差额
#手续费
#结算准备金
#现金
#可取资金
#基本准备金
#交易日
#保证金可用余额
#质押金额
#交易所保证金
#投资者交割保证金
#交易所交割保证金
#冻结的过户费
#冻结的印花税
#过户费
#印花税
#折算金额
#授信额度
#证券总价值
#国债回购占用资金
#国债逆回购占用资金
#币种
#账户类型
#融资买入金额
#融券卖出金额
#融资持仓盈亏
#融券持仓盈亏
#融券总市值
#维持担保比例
#行权冻结资金
#期权买入资金(SSE)
#期权买入冻结资金(SSE)
#结算保证金总额
structDict['CSecurityFtdcTradingAccountField'] = CSecurityFtdcTradingAccountField


#禁止登录用户
CSecurityFtdcLoginForbiddenUserField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSecurityFtdcLoginForbiddenUserField'] = CSecurityFtdcLoginForbiddenUserField


#深度行情
CSecurityFtdcDepthMarketDataField = {"TradingDay": "string", "InstrumentID": "string", "ExchangeID": "string",
									 "ExchangeInstID": "string", "LastPrice": "float", "PreSettlementPrice": "float",
									 "PreClosePrice": "float", "PreOpenInterest": "float", "OpenPrice": "float",
									 "HighestPrice": "float", "LowestPrice": "float", "Volume": "float",
									 "Turnover": "float", "OpenInterest": "float", "ClosePrice": "float",
									 "SettlementPrice": "float", "UpperLimitPrice": "float", "LowerLimitPrice": "float",
									 "PreDelta": "float", "CurrDelta": "float", "PreIOPV": "float", "IOPV": "float",
									 "AuctionPrice": "float", "UpdateTime": "string", "UpdateMillisec": "int",
									 "BidPrice1": "float", "BidVolume1": "float", "AskPrice1": "float",
									 "AskVolume1": "float", "BidPrice2": "float", "BidVolume2": "float",
									 "AskPrice2": "float", "AskVolume2": "float", "BidPrice3": "float",
									 "BidVolume3": "float", "AskPrice3": "float", "AskVolume3": "float",
									 "BidPrice4": "float", "BidVolume4": "float", "AskPrice4": "float",
									 "AskVolume4": "float", "BidPrice5": "float", "BidVolume5": "float",
									 "AskPrice5": "float", "AskVolume5": "float", "AveragePrice": "float",
									 "ActionDay": "string", "TradingPhase": "string", "OpenRestriction": "string"}
#交易日
#合约代码
#交易所代码
#合约在交易所的代码
#最新价
#上次结算价
#昨收盘
#昨持仓量
#今开盘
#最高价
#最低价
#数量
#成交金额
#持仓量
#今收盘
#本次结算价
#涨停板价
#跌停板价
#昨虚实度
#今虚实度
#昨日基金净值
#基金净值
#动态参考价格
#最后修改时间
#最后修改毫秒
#申买价一
#申买量一
#申卖价一
#申卖量一
#申买价二
#申买量二
#申卖价二
#申卖量二
#申买价三
#申买量三
#申卖价三
#申卖量三
#申买价四
#申买量四
#申卖价四
#申卖量四
#申买价五
#申买量五
#申卖价五
#申卖量五
#当日均价
#业务日期
#交易阶段
#开仓限制
structDict['CSecurityFtdcDepthMarketDataField'] = CSecurityFtdcDepthMarketDataField


#投资者合约交易权限
CSecurityFtdcInstrumentTradingRightField = {"InstrumentID": "string", "InvestorRange": "string", "BrokerID": "string",
											"InvestorID": "string", "Direction": "string", "TradingRight": "string",
											"ExchangeID": "string", "InstrumentRange": "string"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#买卖
#交易权限
#交易所代码
#股票权限分类
structDict['CSecurityFtdcInstrumentTradingRightField'] = CSecurityFtdcInstrumentTradingRightField


#投资者持仓明细
CSecurityFtdcInvestorPositionDetailField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
											"HedgeFlag": "string", "Direction": "string", "OpenDate": "string",
											"TradeID": "string", "Volume": "float", "OpenPrice": "float",
											"TradingDay": "string", "TradeType": "string", "ExchangeID": "string",
											"Margin": "float", "ExchMargin": "float", "LastSettlementPrice": "float",
											"SettlementPrice": "float", "CloseVolume": "float", "CloseAmount": "float",
											"TransferFee": "float", "StampTax": "float", "Commission": "float",
											"AccountID": "string", "PledgeInPosition": "float",
											"PledgeInFrozenPosition": "float", "RepurchasePosition": "float",
											"Amount": "float", "UnderlyingInstrumentID": "string"}
#合约代码
#经纪公司代码
#投资者代码
#投机套保标志
#买卖
#开仓日期
#成交编号
#数量
#开仓价
#交易日
#成交类型
#交易所代码
#投资者保证金
#交易所保证金
#昨结算价
#结算价
#平仓量
#平仓金额
#过户费
#印花税
#手续费
#AccountID
#质押入库数量
#质押入库冻结数量
#正回购使用的标准券数量
#融资融券金额
#标的合约代码
structDict['CSecurityFtdcInvestorPositionDetailField'] = CSecurityFtdcInvestorPositionDetailField


#债券利息
CSecurityFtdcBondInterestField = {"TradingDay": "string", "ExchangeID": "string", "InstrumentID": "string",
								  "Interest": "float"}
#交易日
#交易所代码
#合约代码
#利息
structDict['CSecurityFtdcBondInterestField'] = CSecurityFtdcBondInterestField


#市值配售信息
CSecurityFtdcMarketRationInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
									  "RationVolume": "float"}
#经纪公司代码
#投资者代码
#交易所代码
#可配售数量
structDict['CSecurityFtdcMarketRationInfoField'] = CSecurityFtdcMarketRationInfoField


#合约手续费率
CSecurityFtdcInstrumentCommissionRateField = {"ExchangeID": "string", "InstrumentID": "string",
											  "InvestorRange": "string", "BrokerID": "string", "InvestorID": "string",
											  "Direction": "string", "StampTaxRateByMoney": "float",
											  "StampTaxRateByVolume": "float", "TransferFeeRateByMoney": "float",
											  "TransferFeeRateByVolume": "float", "TradeFeeByMoney": "float",
											  "TradeFeeByVolume": "float", "MarginByMoney": "float",
											  "MinTradeFee": "float", "MinTransferFee": "float"}
#交易所代码
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#买卖方向
#印花税率
#印花税率(按手数)
#过户费率
#过户费率(按手数)
#交易费
#交易费(按手数)
#交易附加费率
#最小交易费
#最小过户费
structDict['CSecurityFtdcInstrumentCommissionRateField'] = CSecurityFtdcInstrumentCommissionRateField


#余券信息
CSecurityFtdcExcessStockInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
									 "InstrumentID": "string", "ExcessVolume": "float", "ExcessFrozenVolume": "float"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
#余券数量
#余券冻结数量
structDict['CSecurityFtdcExcessStockInfoField'] = CSecurityFtdcExcessStockInfoField


#ETF合约
CSecurityFtdcETFInstrumentField = {"ExchangeID": "string", "ETFInstrumentID": "string",
								   "ETFPurRedInstrumentID": "string", "CreationRedemptionUnit": "int",
								   "Maxcashratio": "float", "Creationredemption": "string",
								   "EstimateCashComponent": "float", "ETFNetValue": "float", "FundClass": "string"}
#交易所代码
#ETF证券代码
#ETF对应申赎代码
#最小申购赎回单位对应的ETF份数
#最大现金替代比例
#基金当天申购赎回状态
#预估金额
#基金申赎单位净值
#基金类别
structDict['CSecurityFtdcETFInstrumentField'] = CSecurityFtdcETFInstrumentField


#ETF股票篮
CSecurityFtdcETFBasketField = {"ExchangeID": "string", "ETFInstrumentID": "string", "StockInstrumentID": "string",
							   "StockInstrumentName": "string", "Volume": "int", "CurrenceReplaceStatus": "string",
							   "Premium": "float", "Amount": "float"}
#交易所代码
#ETF证券代码
#股票证券代码
#股票证券名称
#股票数量
#替代标志
#溢价比例
#总金额
structDict['CSecurityFtdcETFBasketField'] = CSecurityFtdcETFBasketField


#OF合约
CSecurityFtdcOFInstrumentField = {"ExchangeID": "string", "InstrumentID": "string", "Creationredemption": "string",
								  "NetPrice": "float", "FundClass": "string"}
#交易所代码
#OF基金代码
#基金当天申购赎回状态
#基金净值
#基金类别
structDict['CSecurityFtdcOFInstrumentField'] = CSecurityFtdcOFInstrumentField


#SF合约
CSecurityFtdcSFInstrumentField = {"ExchangeID": "string", "InstrumentID": "string", "SFInstrumentID": "string",
								  "SplitMergeStatus": "string", "MinSplitVolume": "int", "MinMergeVolume": "int",
								  "VolumeRatio": "int", "NetPrice": "float"}
#交易所代码
#基金代码
#SF基金代码
#基金当天拆分合并状态
#最小拆分数量
#最小合并数量
#拆分/合并比例
#基金净值
structDict['CSecurityFtdcSFInstrumentField'] = CSecurityFtdcSFInstrumentField


#合约单手保证金
CSecurityFtdcInstrumentUnitMarginField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
										  "InstrumentID": "string", "UnitMargin": "float"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
#合约单手保证金
structDict['CSecurityFtdcInstrumentUnitMarginField'] = CSecurityFtdcInstrumentUnitMarginField


#期权资金限制参数
CSecurityFtdcOptionsFundLimitParamField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
										   "MaxBuyAmount": "float"}
#经纪公司代码
#投资者代码
#交易所代码
#最大可买金额
structDict['CSecurityFtdcOptionsFundLimitParamField'] = CSecurityFtdcOptionsFundLimitParamField


#投资者期权持仓
CSecurityFtdcInvestorOptionsPositionField = {"BrokerID": "string", "InvestorRange": "string", "InvestorID": "string",
											 "ExchangeID": "string", "InstrumentID": "string",
											 "MaxLongPositionLimit": "float", "MaxBuyVolLimit": "float",
											 "MaxPositionLimit": "float", "LongPosition": "float",
											 "ShortPosition": "float", "BuyVolume": "float", "BuyFrozenVolume": "float",
											 "LongFrozenPosition": "float", "ShortFrozenPosition": "float"}
#经纪公司代码
#投资者范围
#投资者代码
#交易所代码
#InstrumentID
#最大多头仓位限制
#最大买开量限制
#最大总仓位限制
#多头持仓
#空头持仓
#买开量
#买开冻结量
#多头冻结持仓
#空头冻结持仓
structDict['CSecurityFtdcInvestorOptionsPositionField'] = CSecurityFtdcInvestorOptionsPositionField


#预交割信息
CSecurityFtdcPreDelivInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
								  "InstrumentID": "string", "DelivType": "string", "UnderlyingInstrumentID": "string",
								  "DelivVolume": "float", "DelivAmount": "float", "ExecVolume": "float",
								  "Direction": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
#交割类型
#标的合约代码
#交割数量
#交割金额
#期权执行数量
#买卖方向
structDict['CSecurityFtdcPreDelivInfoField'] = CSecurityFtdcPreDelivInfoField


#可融券分配信息
CSecurityFtdcCreditStockAssignInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
										   "InstrumentID": "string", "LimitVolume": "float", "YDVolume": "float",
										   "LeftVolume": "float", "FrozenVolume": "float"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
#融券限量
#上日融券数量
#剩余可融券数量
#冻结融券数量
structDict['CSecurityFtdcCreditStockAssignInfoField'] = CSecurityFtdcCreditStockAssignInfoField


#可融资分配信息
CSecurityFtdcCreditCashAssignInfoField = {"BrokerID": "string", "InvestorID": "string", "LimitAmount": "float",
										  "YDAmount": "float"}
#经纪公司代码
#投资者代码
#融资限额
#上日融资金额
structDict['CSecurityFtdcCreditCashAssignInfoField'] = CSecurityFtdcCreditCashAssignInfoField


#证券折算率
CSecurityFtdcConversionRateField = {"ExchangeID": "string", "InstrumentID": "string", "ConversionRate": "float",
									"IsTradingForMargin": "int", "IsTradingForShort": "int"}
#交易所代码
#合约代码
#折算比率
#当前是否支持融资交易
#当前是否支持融券交易
structDict['CSecurityFtdcConversionRateField'] = CSecurityFtdcConversionRateField


#历史信用负债信息
CSecurityFtdcHisCreditDebtInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
									   "InstrumentID": "string", "OpenDate": "string", "Direction": "string",
									   "OpenPrice": "float", "Volume": "float", "Amount": "float"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
#开仓日期
#负债类型
#开仓价
#数量
#融资融券金额
structDict['CSecurityFtdcHisCreditDebtInfoField'] = CSecurityFtdcHisCreditDebtInfoField


#行情静态信息
CSecurityFtdcMarketDataStaticInfoField = {"ExchangeID": "string", "InstrumentID": "string", "UpperLimitPrice": "float",
										  "LowerLimitPrice": "float", "PreSettlementPrice": "float",
										  "PreClosePrice": "float", "PreIOPV": "float", "IsNotTrade": "int"}
#交易所代码
#合约代码
#涨停板价
#跌停板价
#昨结算
#昨收盘
#昨日基金净值
#是否非交易业务
structDict['CSecurityFtdcMarketDataStaticInfoField'] = CSecurityFtdcMarketDataStaticInfoField


#到期回购信息
CSecurityFtdcExpireRepurchInfoField = {"BrokerID": "string", "InvestorID": "string", "AccountID": "string",
									   "ExpireType": "string", "ExchangeID": "string", "InstrumentID": "string",
									   "Volume": "float", "Amount": "float", "Interest": "float"}
#经纪公司代码
#投资者代码
#资金账户代码
#到期类型
#交易所代码
#合约代码
#数量
#金额
#利息
structDict['CSecurityFtdcExpireRepurchInfoField'] = CSecurityFtdcExpireRepurchInfoField


#债券质押为标准券比例
CSecurityFtdcBondPledgeRateField = {"ExchangeID": "string", "InstrumentID": "string", "Ratio": "float"}
#交易所代码
#合约代码
#折算比率
structDict['CSecurityFtdcBondPledgeRateField'] = CSecurityFtdcBondPledgeRateField


#债券质押代码对照关系
CSecurityFtdcPledgeBondField = {"ExchangeID": "string", "InstrumentID": "string", "PledgeID": "string"}
#交易所代码
#合约代码
#质押代码
structDict['CSecurityFtdcPledgeBondField'] = CSecurityFtdcPledgeBondField


#交易所交易员报盘机
CSecurityFtdcTraderOfferField = {"ExchangeID": "string", "BranchPBU": "string", "ParticipantID": "string",
								 "Password": "string", "OfferType": "string", "InstallID": "int",
								 "OrderLocalID": "string", "TraderConnectStatus": "string",
								 "ConnectRequestDate": "string", "ConnectRequestTime": "string",
								 "LastReportDate": "string", "LastReportTime": "string", "ConnectDate": "string",
								 "ConnectTime": "string", "StartDate": "string", "StartTime": "string",
								 "TradingDay": "string", "BrokerID": "string"}
#交易所代码
#交易所交易员代码
#会员代码
#密码
#报盘类型
#安装编号
#本地报单编号
#交易所交易员连接状态
#发出连接请求的日期
#发出连接请求的时间
#上次报告日期
#上次报告时间
#完成连接日期
#完成连接时间
#启动日期
#启动时间
#交易日
#经纪公司代码
structDict['CSecurityFtdcTraderOfferField'] = CSecurityFtdcTraderOfferField


#交易所行情报盘机
CSecurityFtdcMDTraderOfferField = {"ExchangeID": "string", "BranchPBU": "string", "ParticipantID": "string",
								   "Password": "string", "OfferType": "string", "InstallID": "int",
								   "OrderLocalID": "string", "TraderConnectStatus": "string",
								   "ConnectRequestDate": "string", "ConnectRequestTime": "string",
								   "LastReportDate": "string", "LastReportTime": "string", "ConnectDate": "string",
								   "ConnectTime": "string", "StartDate": "string", "StartTime": "string",
								   "TradingDay": "string", "BrokerID": "string"}
#交易所代码
#交易所交易员代码
#会员代码
#密码
#报盘类型
#安装编号
#本地报单编号
#交易所交易员连接状态
#发出连接请求的日期
#发出连接请求的时间
#上次报告日期
#上次报告时间
#完成连接日期
#完成连接时间
#启动日期
#启动时间
#交易日
#经纪公司代码
structDict['CSecurityFtdcMDTraderOfferField'] = CSecurityFtdcMDTraderOfferField


#前置状态
CSecurityFtdcFrontStatusField = {"FrontID": "int", "LastReportDate": "string", "LastReportTime": "string",
								 "IsActive": "int"}
#前置编号
#上次报告日期
#上次报告时间
#是否活跃
structDict['CSecurityFtdcFrontStatusField'] = CSecurityFtdcFrontStatusField


#用户会话
CSecurityFtdcUserSessionField = {"FrontID": "int", "SessionID": "int", "BrokerID": "string", "UserID": "string",
								 "LoginDate": "string", "LoginTime": "string", "IPAddress": "string",
								 "UserProductInfo": "string", "InterfaceProductInfo": "string",
								 "ProtocolInfo": "string", "MacAddress": "string"}
#前置编号
#会话编号
#经纪公司代码
#用户代码
#登录日期
#登录时间
#IP地址
#用户端产品信息
#接口端产品信息
#协议信息
#Mac地址
structDict['CSecurityFtdcUserSessionField'] = CSecurityFtdcUserSessionField


#报单
CSecurityFtdcOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
						   "UserID": "string", "ExchangeID": "string", "OrderPriceType": "string",
						   "Direction": "string", "CombOffsetFlag": "string", "CombHedgeFlag": "string",
						   "LimitPrice": "string", "VolumeTotalOriginal": "int", "TimeCondition": "string",
						   "GTDDate": "string", "VolumeCondition": "string", "MinVolume": "int",
						   "ContingentCondition": "string", "StopPrice": "float", "ForceCloseReason": "string",
						   "IsAutoSuspend": "int", "BusinessUnit": "string", "RequestID": "int",
						   "OrderLocalID": "string", "ParticipantID": "string", "ClientID": "string",
						   "ExchangeInstID": "string", "BranchPBU": "string", "InstallID": "int",
						   "OrderSubmitStatus": "string", "AccountID": "string", "NotifySequence": "int",
						   "TradingDay": "string", "OrderSysID": "string", "OrderSource": "string",
						   "OrderStatus": "string", "OrderType": "string", "VolumeTraded": "int", "VolumeTotal": "int",
						   "InsertDate": "string", "InsertTime": "string", "ActiveTime": "string",
						   "SuspendTime": "string", "UpdateTime": "string", "CancelTime": "string",
						   "ActiveTraderID": "string", "ClearingPartID": "string", "SequenceNo": "int",
						   "FrontID": "int", "SessionID": "int", "UserProductInfo": "string", "StatusMsg": "string",
						   "UserForceClose": "int", "ActiveUserID": "string", "BrokerOrderSeq": "int",
						   "RelativeOrderSysID": "string", "BranchID": "string", "TradeAmount": "float", "IsETF": "int",
						   "InstrumentType": "string"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
#交易所代码
#报单价格条件
#买卖方向
#组合开平标志
#组合投机套保标志
#价格
#数量
#有效期类型
#GTD日期
#成交量类型
#最小成交量
#触发条件
#止损价
#强平原因
#自动挂起标志
#业务单元
#请求编号
#本地报单编号
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#报单提交状态
#账户代码
#报单提示序号
#交易日
#报单编号
#报单来源
#报单状态
#报单类型
#今成交数量
#剩余数量
#报单日期
#委托时间
#激活时间
#挂起时间
#最后修改时间
#撤销时间
#最后修改交易所交易员代码
#结算会员编号
#序号
#前置编号
#会话编号
#用户端产品信息
#状态信息
#用户强评标志
#操作用户代码
#经纪公司报单编号
#相关报单
#营业部编号
#成交金额
#是否ETF
#合约类型
structDict['CSecurityFtdcOrderField'] = CSecurityFtdcOrderField


#报单操作
CSecurityFtdcOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
								 "OrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
								 "ExchangeID": "string", "ActionFlag": "string", "LimitPrice": "float",
								 "VolumeChange": "int", "ActionDate": "string", "ActionTime": "string",
								 "BranchPBU": "string", "InstallID": "int", "OrderLocalID": "string",
								 "ActionLocalID": "string", "ParticipantID": "string", "ClientID": "string",
								 "BusinessUnit": "string", "OrderActionStatus": "string", "UserID": "string",
								 "BranchID": "string", "StatusMsg": "string", "InstrumentID": "string",
								 "InstrumentType": "string"}
#经纪公司代码
#投资者代码
#报单操作引用
#报单引用
#请求编号
#前置编号
#会话编号
#交易所代码
#操作标志
#价格
#数量变化
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#本地报单编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
#营业部编号
#状态信息
#合约代码
#合约类型
structDict['CSecurityFtdcOrderActionField'] = CSecurityFtdcOrderActionField


#错误报单
CSecurityFtdcErrOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							  "OrderRef": "string", "UserID": "string", "ExchangeID": "string",
							  "OrderPriceType": "string", "Direction": "string", "CombOffsetFlag": "string",
							  "CombHedgeFlag": "string", "LimitPrice": "string", "VolumeTotalOriginal": "int",
							  "TimeCondition": "string", "GTDDate": "string", "VolumeCondition": "string",
							  "MinVolume": "int", "ContingentCondition": "string", "StopPrice": "float",
							  "ForceCloseReason": "string", "IsAutoSuspend": "int", "BusinessUnit": "string",
							  "RequestID": "int", "UserForceClose": "int", "ErrorID": "int", "ErrorMsg": "string"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
#交易所代码
#报单价格条件
#买卖方向
#组合开平标志
#组合投机套保标志
#价格
#数量
#有效期类型
#GTD日期
#成交量类型
#最小成交量
#触发条件
#止损价
#强平原因
#自动挂起标志
#业务单元
#请求编号
#用户强评标志
#错误代码
#错误信息
structDict['CSecurityFtdcErrOrderField'] = CSecurityFtdcErrOrderField


#错误报单操作
CSecurityFtdcErrOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
									"OrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
									"ExchangeID": "string", "ActionFlag": "string", "LimitPrice": "float",
									"VolumeChange": "int", "ActionDate": "string", "ActionTime": "string",
									"BranchPBU": "string", "InstallID": "int", "OrderLocalID": "string",
									"ActionLocalID": "string", "ParticipantID": "string", "ClientID": "string",
									"BusinessUnit": "string", "OrderActionStatus": "string", "UserID": "string",
									"BranchID": "string", "StatusMsg": "string", "InstrumentID": "string",
									"ErrorID": "int", "ErrorMsg": "string", "InstrumentType": "string"}
#经纪公司代码
#投资者代码
#报单操作引用
#报单引用
#请求编号
#前置编号
#会话编号
#交易所代码
#操作标志
#价格
#数量变化
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#本地报单编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
#营业部编号
#状态信息
#合约代码
#错误代码
#错误信息
#合约类型
structDict['CSecurityFtdcErrOrderActionField'] = CSecurityFtdcErrOrderActionField


#成交
CSecurityFtdcTradeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
						   "UserID": "string", "ExchangeID": "string", "TradeID": "string", "Direction": "string",
						   "OrderSysID": "string", "ParticipantID": "string", "ClientID": "string",
						   "TradingRole": "string", "ExchangeInstID": "string", "OffsetFlag": "string",
						   "HedgeFlag": "string", "Price": "string", "Volume": "int", "TradeDate": "string",
						   "TradeTime": "string", "TradeType": "string", "PriceSource": "string", "BranchPBU": "string",
						   "OrderLocalID": "string", "ClearingPartID": "string", "BusinessUnit": "string",
						   "SequenceNo": "int", "TradeSource": "string", "TradingDay": "string",
						   "BrokerOrderSeq": "int", "TradeAmount": "float", "TradeIndex": "int"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
#交易所代码
#成交编号
#买卖方向
#报单编号
#会员代码
#客户代码
#交易角色
#合约在交易所的代码
#开平标志
#投机套保标志
#价格
#数量
#成交时期
#成交时间
#成交类型
#成交价来源
#交易所交易员代码
#本地报单编号
#结算会员编号
#业务单元
#序号
#成交来源
#交易日
#经纪公司报单编号
#成交金额
#成交序号
structDict['CSecurityFtdcTradeField'] = CSecurityFtdcTradeField


#投资者持仓
CSecurityFtdcInvestorPositionField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
									  "PosiDirection": "string", "HedgeFlag": "string", "PositionDate": "string",
									  "YdPosition": "float", "Position": "float", "LongFrozen": "float",
									  "ShortFrozen": "float", "LongFrozenAmount": "float", "ShortFrozenAmount": "float",
									  "OpenVolume": "float", "CloseVolume": "float", "OpenAmount": "float",
									  "CloseAmount": "float", "PositionCost": "float", "FrozenCash": "float",
									  "CashIn": "float", "Commission": "float", "PreSettlementPrice": "float",
									  "SettlementPrice": "float", "TradingDay": "string", "OpenCost": "float",
									  "ExchangeMargin": "float", "TodayPosition": "float", "TransferFee": "float",
									  "StampTax": "float", "TodayPurRedVolume": "float", "ConversionRate": "float",
									  "ConversionAmount": "float", "StockValue": "float", "ExchangeID": "string",
									  "AccountID": "string", "PledgeInPosition": "float", "RepurchasePosition": "float",
									  "PurRedShortFrozen": "float", "MarginTradeVolume": "float",
									  "MarginTradeAmount": "float", "MarginTradeFrozenVolume": "float",
									  "MarginTradeFrozenAmount": "float", "MarginTradeConversionProfit": "float",
									  "ShortSellVolume": "float", "ShortSellAmount": "float",
									  "ShortSellFrozenVolume": "float", "ShortSellFrozenAmount": "float",
									  "ShortSellConversionProfit": "float", "SSStockValue": "float",
									  "TodayMTPosition": "float", "TodaySSPosition": "float", "YdOpenCost": "float",
									  "LockPosition": "float", "CoverPosition": "float", "LockFrozenPosition": "float",
									  "UnlockFrozenPosition": "float", "CoverFrozenPosition": "float",
									  "ExecFrozenPosition": "float", "YDCoverPosition": "float"}
#合约代码
#经纪公司代码
#投资者代码
#持仓多空方向
#投机套保标志
#持仓日期
#上日持仓
#总持仓
#多头冻结
#空头冻结
#开仓冻结金额
#开仓冻结金额
#开仓量
#平仓量
#开仓金额
#平仓金额
#持仓成本
#冻结的资金
#资金差额
#手续费
#上次结算价
#本次结算价
#交易日
#开仓成本
#交易所保证金
#今日持仓
#过户费
#印花税
#今日申购赎回数量
#折算率
#折算金额
#证券价值
#交易所代码
#AccountID
#质押入库数量
#正回购使用的标准券数量
#ETF申赎空头冻结
#融资买入数量
#融资买入金额
#融资买入冻结数量
#融资买入冻结金额
#融资买入盈亏
#融券卖出数量
#融券卖出金额
#融券卖出冻结数量
#融券卖出冻结金额
#融券卖出盈亏
#融券总市值
#今日融资持仓
#今日融券持仓
#历史持仓开仓成本
#锁定仓位
#备兑仓位
#锁定冻结仓位
#解锁冻结仓位
#备兑冻结仓位
#行权冻结仓位
#上日备兑仓位
structDict['CSecurityFtdcInvestorPositionField'] = CSecurityFtdcInvestorPositionField


#出入金同步
CSecurityFtdcSyncDepositField = {"DepositSeqNo": "string", "BrokerID": "string", "InvestorID": "string",
								 "Deposit": "float", "IsForce": "int", "AccountID": "string"}
#出入金流水号
#经纪公司代码
#投资者代码
#入金金额
#是否强制进行
#账户代码
structDict['CSecurityFtdcSyncDepositField'] = CSecurityFtdcSyncDepositField


#查询交易所
CSecurityFtdcQryExchangeField = {"ExchangeID": "string"}
#交易所代码
structDict['CSecurityFtdcQryExchangeField'] = CSecurityFtdcQryExchangeField


#查询产品
CSecurityFtdcQryProductField = {"ProductID": "string"}
#产品代码
structDict['CSecurityFtdcQryProductField'] = CSecurityFtdcQryProductField


#查询合约
CSecurityFtdcQryInstrumentField = {"InstrumentID": "string", "ExchangeID": "string", "ExchangeInstID": "string",
								   "ProductID": "string"}
#合约代码
#交易所代码
#合约在交易所的代码
#产品代码
structDict['CSecurityFtdcQryInstrumentField'] = CSecurityFtdcQryInstrumentField


#查询经纪公司
CSecurityFtdcQryBrokerField = {"BrokerID": "string"}
#经纪公司代码
structDict['CSecurityFtdcQryBrokerField'] = CSecurityFtdcQryBrokerField


#查询经纪公司会员代码
CSecurityFtdcQryPartBrokerField = {"ExchangeID": "string", "BrokerID": "string", "ParticipantID": "string"}
#交易所代码
#经纪公司代码
#会员代码
structDict['CSecurityFtdcQryPartBrokerField'] = CSecurityFtdcQryPartBrokerField


#查询投资者
CSecurityFtdcQryInvestorField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSecurityFtdcQryInvestorField'] = CSecurityFtdcQryInvestorField


#查询交易编码
CSecurityFtdcQryTradingCodeField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
									"ClientID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#客户代码
structDict['CSecurityFtdcQryTradingCodeField'] = CSecurityFtdcQryTradingCodeField


#查询管理用户
CSecurityFtdcQrySuperUserField = {"UserID": "string"}
#用户代码
structDict['CSecurityFtdcQrySuperUserField'] = CSecurityFtdcQrySuperUserField


#查询管理用户功能权限
CSecurityFtdcQrySuperUserFunctionField = {"UserID": "string"}
#用户代码
structDict['CSecurityFtdcQrySuperUserFunctionField'] = CSecurityFtdcQrySuperUserFunctionField


#查询经纪公司用户
CSecurityFtdcQryBrokerUserField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSecurityFtdcQryBrokerUserField'] = CSecurityFtdcQryBrokerUserField


#查询经纪公司用户权限
CSecurityFtdcQryBrokerUserFunctionField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSecurityFtdcQryBrokerUserFunctionField'] = CSecurityFtdcQryBrokerUserFunctionField


#查询资金账户
CSecurityFtdcQryTradingAccountField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSecurityFtdcQryTradingAccountField'] = CSecurityFtdcQryTradingAccountField


#查询禁止登录用户
CSecurityFtdcQryLoginForbiddenUserField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSecurityFtdcQryLoginForbiddenUserField'] = CSecurityFtdcQryLoginForbiddenUserField


#查询行情
CSecurityFtdcQryDepthMarketDataField = {"InstrumentID": "string"}
#合约代码
structDict['CSecurityFtdcQryDepthMarketDataField'] = CSecurityFtdcQryDepthMarketDataField


#查询合约交易权限
CSecurityFtdcQryInstrumentTradingRightField = {"ExchangeID": "string", "BrokerID": "string", "InvestorID": "string",
											   "InstrumentID": "string"}
#交易所代码
#经纪公司代码
#投资者代码
#合约代码
structDict['CSecurityFtdcQryInstrumentTradingRightField'] = CSecurityFtdcQryInstrumentTradingRightField


#查询投资者持仓明细
CSecurityFtdcQryInvestorPositionDetailField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#合约代码
structDict['CSecurityFtdcQryInvestorPositionDetailField'] = CSecurityFtdcQryInvestorPositionDetailField


#查询债券利息
CSecurityFtdcQryBondInterestField = {"ExchangeID": "string", "InstrumentID": "string"}
#交易所代码
#合约代码
structDict['CSecurityFtdcQryBondInterestField'] = CSecurityFtdcQryBondInterestField


#查询市值配售信息
CSecurityFtdcQryMarketRationInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者帐号
#交易所代码
structDict['CSecurityFtdcQryMarketRationInfoField'] = CSecurityFtdcQryMarketRationInfoField


#查询合约手续费率
CSecurityFtdcQryInstrumentCommissionRateField = {"ExchangeID": "string", "BrokerID": "string", "InvestorID": "string",
												 "InstrumentID": "string", "Direction": "string",
												 "OffsetFlag": "string"}
#交易所代码
#经纪公司代码
#投资者代码
#合约代码
#买卖方向
#开平标志
structDict['CSecurityFtdcQryInstrumentCommissionRateField'] = CSecurityFtdcQryInstrumentCommissionRateField


#查询余券信息
CSecurityFtdcQryExcessStockInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
										"InstrumentID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
structDict['CSecurityFtdcQryExcessStockInfoField'] = CSecurityFtdcQryExcessStockInfoField


#查询投资者帐户关系
CSecurityFtdcQryInvestorAccountField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSecurityFtdcQryInvestorAccountField'] = CSecurityFtdcQryInvestorAccountField


#查询ETF合约
CSecurityFtdcQryETFInstrumentField = {"ExchangeID": "string", "ETFInstrumentID": "string"}
#交易所代码
#ETF证券代码
structDict['CSecurityFtdcQryETFInstrumentField'] = CSecurityFtdcQryETFInstrumentField


#查询ETF股票篮
CSecurityFtdcQryETFBasketField = {"ExchangeID": "string", "ETFInstrumentID": "string"}
#交易所代码
#ETF证券代码
structDict['CSecurityFtdcQryETFBasketField'] = CSecurityFtdcQryETFBasketField


#查询OF合约
CSecurityFtdcQryOFInstrumentField = {"ExchangeID": "string", "OFInstrumentID": "string"}
#交易所代码
#ETF证券代码
structDict['CSecurityFtdcQryOFInstrumentField'] = CSecurityFtdcQryOFInstrumentField


#查询SF合约
CSecurityFtdcQrySFInstrumentField = {"ExchangeID": "string", "SFInstrumentID": "string"}
#交易所代码
#ETF证券代码
structDict['CSecurityFtdcQrySFInstrumentField'] = CSecurityFtdcQrySFInstrumentField


#查询合约单手保证金
CSecurityFtdcQryInstrumentUnitMarginField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
											 "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
structDict['CSecurityFtdcQryInstrumentUnitMarginField'] = CSecurityFtdcQryInstrumentUnitMarginField


#查询期权资金限制参数
CSecurityFtdcQryOptionsFundLimitParamField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CSecurityFtdcQryOptionsFundLimitParamField'] = CSecurityFtdcQryOptionsFundLimitParamField


#查询投资者期权持仓
CSecurityFtdcQryInvestorOptionsPositionField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
												"InstrumentID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#标的合约代码
structDict['CSecurityFtdcQryInvestorOptionsPositionField'] = CSecurityFtdcQryInvestorOptionsPositionField


#查询预交割信息
CSecurityFtdcQryPreDelivInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
									 "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
structDict['CSecurityFtdcQryPreDelivInfoField'] = CSecurityFtdcQryPreDelivInfoField


#查询可融券分配信息
CSecurityFtdcQryCreditStockAssignInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
											  "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
structDict['CSecurityFtdcQryCreditStockAssignInfoField'] = CSecurityFtdcQryCreditStockAssignInfoField


#查询可融资分配信息
CSecurityFtdcQryCreditCashAssignInfoField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSecurityFtdcQryCreditCashAssignInfoField'] = CSecurityFtdcQryCreditCashAssignInfoField


#查询证券折算率
CSecurityFtdcQryConversionRateField = {"ExchangeID": "string", "InstrumentID": "string"}
#交易所代码
#合约代码
structDict['CSecurityFtdcQryConversionRateField'] = CSecurityFtdcQryConversionRateField


#查询历史信用负债信息
CSecurityFtdcQryHisCreditDebtInfoField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
										  "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
structDict['CSecurityFtdcQryHisCreditDebtInfoField'] = CSecurityFtdcQryHisCreditDebtInfoField


#查询行情静态信息
CSecurityFtdcQryMarketDataStaticInfoField = {"ExchangeID": "string", "InstrumentID": "string"}
#交易所代码
#合约代码
structDict['CSecurityFtdcQryMarketDataStaticInfoField'] = CSecurityFtdcQryMarketDataStaticInfoField


#查询到期回购信息
CSecurityFtdcQryExpireRepurchInfoField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSecurityFtdcQryExpireRepurchInfoField'] = CSecurityFtdcQryExpireRepurchInfoField


#查询债券质押为标准券比例
CSecurityFtdcQryBondPledgeRateField = {"ExchangeID": "string", "InstrumentID": "string"}
#交易所代码
#合约代码
structDict['CSecurityFtdcQryBondPledgeRateField'] = CSecurityFtdcQryBondPledgeRateField


#查询债券质押代码对照关系
CSecurityFtdcQryPledgeBondField = {"ExchangeID": "string", "InstrumentID": "string"}
#交易所代码
#合约代码
structDict['CSecurityFtdcQryPledgeBondField'] = CSecurityFtdcQryPledgeBondField


#查询交易员报盘机
CSecurityFtdcQryTraderOfferField = {"ExchangeID": "string", "ParticipantID": "string", "BranchPBU": "string"}
#交易所代码
#会员代码
#交易所交易员代码
structDict['CSecurityFtdcQryTraderOfferField'] = CSecurityFtdcQryTraderOfferField


#查询行情报盘机
CSecurityFtdcQryMDTraderOfferField = {"ExchangeID": "string", "ParticipantID": "string", "BranchPBU": "string"}
#交易所代码
#会员代码
#交易所交易员代码
structDict['CSecurityFtdcQryMDTraderOfferField'] = CSecurityFtdcQryMDTraderOfferField


#查询前置状态
CSecurityFtdcQryFrontStatusField = {"FrontID": "int"}
#前置编号
structDict['CSecurityFtdcQryFrontStatusField'] = CSecurityFtdcQryFrontStatusField


#查询用户会话
CSecurityFtdcQryUserSessionField = {"FrontID": "int", "SessionID": "int", "BrokerID": "string", "UserID": "string"}
#前置编号
#会话编号
#经纪公司代码
#用户代码
structDict['CSecurityFtdcQryUserSessionField'] = CSecurityFtdcQryUserSessionField


#查询报单
CSecurityFtdcQryOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							  "ExchangeID": "string", "OrderSysID": "string", "InsertTimeStart": "string",
							  "InsertTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#报单编号
#开始时间
#结束时间
structDict['CSecurityFtdcQryOrderField'] = CSecurityFtdcQryOrderField


#查询报单操作
CSecurityFtdcQryOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CSecurityFtdcQryOrderActionField'] = CSecurityFtdcQryOrderActionField


#查询错误报单
CSecurityFtdcQryErrOrderField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSecurityFtdcQryErrOrderField'] = CSecurityFtdcQryErrOrderField


#查询错误报单操作
CSecurityFtdcQryErrOrderActionField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSecurityFtdcQryErrOrderActionField'] = CSecurityFtdcQryErrOrderActionField


#查询成交
CSecurityFtdcQryTradeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							  "ExchangeID": "string", "TradeID": "string", "TradeTimeStart": "string",
							  "TradeTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#成交编号
#开始时间
#结束时间
structDict['CSecurityFtdcQryTradeField'] = CSecurityFtdcQryTradeField


#查询投资者持仓
CSecurityFtdcQryInvestorPositionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#合约代码
structDict['CSecurityFtdcQryInvestorPositionField'] = CSecurityFtdcQryInvestorPositionField


#查询出入金流水
CSecurityFtdcQrySyncDepositField = {"BrokerID": "string", "DepositSeqNo": "string"}
#经纪公司代码
#出入金流水号
structDict['CSecurityFtdcQrySyncDepositField'] = CSecurityFtdcQrySyncDepositField


#用户口令变更
CSecurityFtdcUserPasswordUpdateField = {"BrokerID": "string", "UserID": "string", "OldPassword": "string",
										"NewPassword": "string"}
#经纪公司代码
#用户代码
#原来的口令
#新的口令
structDict['CSecurityFtdcUserPasswordUpdateField'] = CSecurityFtdcUserPasswordUpdateField


#资金账户口令变更域
CSecurityFtdcTradingAccountPasswordUpdateField = {"BrokerID": "string", "AccountID": "string", "OldPassword": "string",
												  "NewPassword": "string"}
#经纪公司代码
#投资者帐号
#原来的口令
#新的口令
structDict['CSecurityFtdcTradingAccountPasswordUpdateField'] = CSecurityFtdcTradingAccountPasswordUpdateField


#手工同步用户动态令牌
CSecurityFtdcManualSyncBrokerUserOTPField = {"BrokerID": "string", "UserID": "string", "OTPType": "string",
											 "FirstOTP": "string", "SecondOTP": "string"}
#经纪公司代码
#用户代码
#动态令牌类型
#第一个动态密码
#第二个动态密码
structDict['CSecurityFtdcManualSyncBrokerUserOTPField'] = CSecurityFtdcManualSyncBrokerUserOTPField


#经纪公司用户口令
CSecurityFtdcBrokerUserPasswordField = {"BrokerID": "string", "UserID": "string", "Password": "string"}
#经纪公司代码
#用户代码
#密码
structDict['CSecurityFtdcBrokerUserPasswordField'] = CSecurityFtdcBrokerUserPasswordField


#资金账户口令域
CSecurityFtdcTradingAccountPasswordField = {"BrokerID": "string", "AccountID": "string", "Password": "string"}
#经纪公司代码
#投资者帐号
#密码
structDict['CSecurityFtdcTradingAccountPasswordField'] = CSecurityFtdcTradingAccountPasswordField


#用户权限
CSecurityFtdcUserRightField = {"BrokerID": "string", "UserID": "string", "UserRightType": "string",
							   "IsForbidden": "int"}
#经纪公司代码
#用户代码
#客户权限类型
#是否禁止
structDict['CSecurityFtdcUserRightField'] = CSecurityFtdcUserRightField


#投资者账户
CSecurityFtdcInvestorAccountField = {"BrokerID": "string", "InvestorID": "string", "AccountID": "string",
									 "IsDefault": "int", "AccountType": "string", "IsActive": "int",
									 "SHBranchPBU": "string", "SZBranchPBU": "string"}
#经纪公司代码
#投资者代码
#投资者帐号
#是否主账户
#账户类型
#是否活跃
#上交所交易单元号
#深交所交易单元号
structDict['CSecurityFtdcInvestorAccountField'] = CSecurityFtdcInvestorAccountField


#用户IP
CSecurityFtdcUserIPField = {"BrokerID": "string", "UserID": "string", "IPAddress": "string", "IPMask": "string",
							"MacAddress": "string"}
#经纪公司代码
#用户代码
#IP地址
#IP地址掩码
#Mac地址
structDict['CSecurityFtdcUserIPField'] = CSecurityFtdcUserIPField


#用户动态令牌参数
CSecurityFtdcBrokerUserOTPParamField = {"BrokerID": "string", "UserID": "string", "OTPVendorsID": "string",
										"SerialNumber": "string", "AuthKey": "string", "LastDrift": "int",
										"LastSuccess": "int", "OTPType": "string"}
#经纪公司代码
#用户代码
#动态令牌提供商
#动态令牌序列号
#令牌密钥
#漂移值
#成功值
#动态令牌类型
structDict['CSecurityFtdcBrokerUserOTPParamField'] = CSecurityFtdcBrokerUserOTPParamField


#用户登录请求
CSecurityFtdcReqUserLoginField = {"TradingDay": "string", "BrokerID": "string", "UserID": "string",
								  "Password": "string", "UserProductInfo": "string", "InterfaceProductInfo": "string",
								  "ProtocolInfo": "string", "MacAddress": "string", "OneTimePassword": "string",
								  "ClientIPAddress": "string", "AuthCode": "string", "RandCode": "string",
								  "HDSerialNumber": "string"}
#交易日
#经纪公司代码
#用户代码
#密码
#用户端产品信息
#接口端产品信息
#协议信息
#Mac地址
#动态密码
#终端IP地址
#客户端认证码
#随机码
#硬盘序列号
structDict['CSecurityFtdcReqUserLoginField'] = CSecurityFtdcReqUserLoginField


#用户登录应答
CSecurityFtdcRspUserLoginField = {"TradingDay": "string", "LoginTime": "string", "BrokerID": "string",
								  "UserID": "string", "SystemName": "string", "FrontID": "int", "SessionID": "int",
								  "MaxOrderRef": "string"}
#交易日
#登录成功时间
#经纪公司代码
#用户代码
#交易系统名称
#前置编号
#会话编号
#最大报单引用
structDict['CSecurityFtdcRspUserLoginField'] = CSecurityFtdcRspUserLoginField


#用户登出请求
CSecurityFtdcUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSecurityFtdcUserLogoutField'] = CSecurityFtdcUserLogoutField


#全部登出信息
CSecurityFtdcLogoutAllField = {"FrontID": "int", "SessionID": "int", "SystemName": "string"}
#前置编号
#会话编号
#系统名称
structDict['CSecurityFtdcLogoutAllField'] = CSecurityFtdcLogoutAllField


#强制交易员退出
CSecurityFtdcForceUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSecurityFtdcForceUserLogoutField'] = CSecurityFtdcForceUserLogoutField


#经纪公司用户激活
CSecurityFtdcActivateBrokerUserField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSecurityFtdcActivateBrokerUserField'] = CSecurityFtdcActivateBrokerUserField


#认证随机码
CSecurityFtdcAuthRandCodeField = {"RandCode": "string"}
#随机码
structDict['CSecurityFtdcAuthRandCodeField'] = CSecurityFtdcAuthRandCodeField


#输入报单
CSecurityFtdcInputOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								"OrderRef": "string", "UserID": "string", "ExchangeID": "string",
								"OrderPriceType": "string", "Direction": "string", "CombOffsetFlag": "string",
								"CombHedgeFlag": "string", "LimitPrice": "string", "VolumeTotalOriginal": "int",
								"TimeCondition": "string", "GTDDate": "string", "VolumeCondition": "string",
								"MinVolume": "int", "ContingentCondition": "string", "StopPrice": "float",
								"ForceCloseReason": "string", "IsAutoSuspend": "int", "BusinessUnit": "string",
								"RequestID": "int", "UserForceClose": "int"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
#交易所代码
#报单价格条件
#买卖方向
#组合开平标志
#组合投机套保标志
#价格
#数量
#有效期类型
#GTD日期
#成交量类型
#最小成交量
#触发条件
#止损价
#强平原因
#自动挂起标志
#业务单元
#请求编号
#用户强评标志
structDict['CSecurityFtdcInputOrderField'] = CSecurityFtdcInputOrderField


#输入报单操作
CSecurityFtdcInputOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
									  "OrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
									  "ExchangeID": "string", "ActionFlag": "string", "LimitPrice": "float",
									  "VolumeChange": "int", "UserID": "string", "InstrumentID": "string",
									  "BranchPBU": "string", "OrderLocalID": "string"}
#经纪公司代码
#投资者代码
#报单操作引用
#报单引用
#请求编号
#前置编号
#会话编号
#交易所代码
#操作标志
#价格
#数量变化
#用户代码
#合约代码
#交易所交易员代码
#本地报单编号
structDict['CSecurityFtdcInputOrderActionField'] = CSecurityFtdcInputOrderActionField


#指定的合约
CSecurityFtdcSpecificInstrumentField = {"InstrumentID": "string", "ExchangeID": "string"}
#合约代码
#交易所代码
structDict['CSecurityFtdcSpecificInstrumentField'] = CSecurityFtdcSpecificInstrumentField


#指定的交易所
CSecurityFtdcSpecificExchangeField = {"ExchangeID": "string"}
#交易所代码
structDict['CSecurityFtdcSpecificExchangeField'] = CSecurityFtdcSpecificExchangeField


#行情基础属性
CSecurityFtdcMarketDataBaseField = {"TradingDay": "string", "PreSettlementPrice": "float", "PreClosePrice": "float",
									"PreOpenInterest": "float", "PreDelta": "float", "PreIOPV": "float"}
#交易日
#上次结算价
#昨收盘
#昨持仓量
#昨虚实度
#昨日基金净值
structDict['CSecurityFtdcMarketDataBaseField'] = CSecurityFtdcMarketDataBaseField


#行情静态属性
CSecurityFtdcMarketDataStaticField = {"OpenPrice": "float", "HighestPrice": "float", "LowestPrice": "float",
									  "ClosePrice": "float", "UpperLimitPrice": "float", "LowerLimitPrice": "float",
									  "SettlementPrice": "float", "CurrDelta": "float", "IOPV": "float",
									  "AuctionPrice": "float"}
#今开盘
#最高价
#最低价
#今收盘
#涨停板价
#跌停板价
#本次结算价
#今虚实度
#基金净值
#动态参考价格
structDict['CSecurityFtdcMarketDataStaticField'] = CSecurityFtdcMarketDataStaticField


#行情最新成交属性
CSecurityFtdcMarketDataLastMatchField = {"LastPrice": "float", "Volume": "float", "Turnover": "float",
										 "OpenInterest": "float"}
#最新价
#数量
#成交金额
#持仓量
structDict['CSecurityFtdcMarketDataLastMatchField'] = CSecurityFtdcMarketDataLastMatchField


#行情最优价属性
CSecurityFtdcMarketDataBestPriceField = {"BidPrice1": "float", "BidVolume1": "float", "AskPrice1": "float",
										 "AskVolume1": "float"}
#申买价一
#申买量一
#申卖价一
#申卖量一
structDict['CSecurityFtdcMarketDataBestPriceField'] = CSecurityFtdcMarketDataBestPriceField


#行情申买二、三属性
CSecurityFtdcMarketDataBid23Field = {"BidPrice2": "float", "BidVolume2": "float", "BidPrice3": "float",
									 "BidVolume3": "float"}
#申买价二
#申买量二
#申买价三
#申买量三
structDict['CSecurityFtdcMarketDataBid23Field'] = CSecurityFtdcMarketDataBid23Field


#行情申卖二、三属性
CSecurityFtdcMarketDataAsk23Field = {"AskPrice2": "float", "AskVolume2": "float", "AskPrice3": "float",
									 "AskVolume3": "float"}
#申卖价二
#申卖量二
#申卖价三
#申卖量三
structDict['CSecurityFtdcMarketDataAsk23Field'] = CSecurityFtdcMarketDataAsk23Field


#行情申买四、五属性
CSecurityFtdcMarketDataBid45Field = {"BidPrice4": "float", "BidVolume4": "float", "BidPrice5": "float",
									 "BidVolume5": "float"}
#申买价四
#申买量四
#申买价五
#申买量五
structDict['CSecurityFtdcMarketDataBid45Field'] = CSecurityFtdcMarketDataBid45Field


#行情申卖四、五属性
CSecurityFtdcMarketDataAsk45Field = {"AskPrice4": "float", "AskVolume4": "float", "AskPrice5": "float",
									 "AskVolume5": "float"}
#申卖价四
#申卖量四
#申卖价五
#申卖量五
structDict['CSecurityFtdcMarketDataAsk45Field'] = CSecurityFtdcMarketDataAsk45Field


#行情更新时间属性
CSecurityFtdcMarketDataUpdateTimeField = {"InstrumentID": "string", "UpdateTime": "string", "UpdateMillisec": "int",
										  "ActionDay": "string", "TradingPhase": "string", "OpenRestriction": "string"}
#合约代码
#最后修改时间
#最后修改毫秒
#业务日期
#交易阶段
#开仓限制
structDict['CSecurityFtdcMarketDataUpdateTimeField'] = CSecurityFtdcMarketDataUpdateTimeField


#成交均价
CSecurityFtdcMarketDataAveragePriceField = {"AveragePrice": "float"}
#当日均价
structDict['CSecurityFtdcMarketDataAveragePriceField'] = CSecurityFtdcMarketDataAveragePriceField


#行情交易所代码属性
CSecurityFtdcMarketDataExchangeField = {"ExchangeID": "string"}
#交易所代码
structDict['CSecurityFtdcMarketDataExchangeField'] = CSecurityFtdcMarketDataExchangeField


#信息分发
CSecurityFtdcDisseminationField = {"SequenceSeries": "int", "SequenceNo": "int"}
#序列系列号
#序列号
structDict['CSecurityFtdcDisseminationField'] = CSecurityFtdcDisseminationField


#资金转账输入
CSecurityFtdcInputFundTransferField = {"BrokerID": "string", "InvestorID": "string", "AccountID": "string",
									   "Password": "string", "UserID": "string", "TradeAmount": "float",
									   "Digest": "string", "AccountType": "string"}
#经纪公司代码
#投资者代码
#投资者资金帐号
#资金帐户密码
#用户代码
#交易金额
#摘要
#账户类型
structDict['CSecurityFtdcInputFundTransferField'] = CSecurityFtdcInputFundTransferField


#资金转账
CSecurityFtdcFundTransferField = {"BrokerID": "string", "InvestorID": "string", "AccountID": "string",
								  "Password": "string", "UserID": "string", "TradeAmount": "float", "Digest": "string",
								  "SessionID": "int", "LiberSerial": "int", "PlateSerial": "int",
								  "TransferSerial": "string", "TradingDay": "string", "TradeTime": "string",
								  "FundDirection": "string", "ErrorID": "int", "ErrorMsg": "string"}
#经纪公司代码
#投资者代码
#投资者资金帐号
#资金帐户密码
#用户代码
#交易金额
#摘要
#会话编号
#Liber核心流水号
#转账平台流水号
#第三方流水号
#交易日
#转账时间
#出入金方向
#错误代码
#错误信息
structDict['CSecurityFtdcFundTransferField'] = CSecurityFtdcFundTransferField


#资金转账查询请求
CSecurityFtdcQryFundTransferSerialField = {"BrokerID": "string", "AccountID": "string", "AccountType": "string"}
#经纪公司代码
#投资者资金帐号
#账户类型
structDict['CSecurityFtdcQryFundTransferSerialField'] = CSecurityFtdcQryFundTransferSerialField


#资金内转
CSecurityFtdcFundInterTransferField = {"BrokerID": "string", "InvestorID": "string", "UserID": "string",
									   "AccountID": "string", "Password": "string", "TradeAmount": "float",
									   "TransferType": "string", "SerialID": "int"}
#经纪公司代码
#投资者代码
#用户代码
#资金账户代码
#资金账户密码
#金额
#内转类型
#资金内转编号
structDict['CSecurityFtdcFundInterTransferField'] = CSecurityFtdcFundInterTransferField


#资金内转流水
CSecurityFtdcFundInterTransferSerialField = {"BrokerID": "string", "InvestorID": "string", "UserID": "string",
											 "AccountID": "string", "Password": "string", "TradeAmount": "float",
											 "TransferType": "string", "SerialID": "int", "TransferTime": "string",
											 "ErrorID": "int", "ErrorMsg": "string"}
#经纪公司代码
#投资者代码
#用户代码
#资金账户代码
#资金账户密码
#金额
#内转类型
#资金内转编号
#转账时间
#错误代码
#错误信息
structDict['CSecurityFtdcFundInterTransferSerialField'] = CSecurityFtdcFundInterTransferSerialField


#资金内转流水查询请求
CSecurityFtdcQryFundInterTransferSerialField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSecurityFtdcQryFundInterTransferSerialField'] = CSecurityFtdcQryFundInterTransferSerialField


#获取数据库信息
CSecurityFtdcFetchDBInfoField = {"UserID": "string", "Password": "string", "DBIndex": "string", "IPAddress": "string",
								 "IPPort": "int", "DBName": "string", "DBUserID": "string", "DBPassword": "string"}
#用户代码
#密码
#数据库索引
#数据库IP地址
#数据库IP端口
#数据库名称
#数据库用户名
#数据库密码
structDict['CSecurityFtdcFetchDBInfoField'] = CSecurityFtdcFetchDBInfoField


#MD用户信息
CSecurityFtdcMDUserInfoField = {"BrokerID": "string", "UserID": "string", "UserName": "string", "Password": "string",
								"MDSysID": "int", "MaxStockCount": "int", "MaxOptionsCount": "int"}
#经纪公司代码
#用户代码
#用户名称
#密码
#行情系统编号
#股票最大订阅数量
#期权最大订阅数量
structDict['CSecurityFtdcMDUserInfoField'] = CSecurityFtdcMDUserInfoField





