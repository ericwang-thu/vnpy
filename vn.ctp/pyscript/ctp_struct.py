# encoding: UTF-8

structDict = {}

#//////////////////////////////////////////////////////////////////////
#@system 新一代交易所系统
#@company 上海期货信息技术有限公司
#@file ThostFtdcUserApiStruct.h
#@brief 定义了客户端接口使用的业务数据结构
#@history 

#//////////////////////////////////////////////////////////////////////










#信息分发
CThostFtdcDisseminationField = {"SequenceSeries": "int", "SequenceNo": "int"}
#序列系列号
#序列号
structDict['CThostFtdcDisseminationField'] = CThostFtdcDisseminationField


#用户登录请求
CThostFtdcReqUserLoginField = {"TradingDay": "string", "BrokerID": "string", "UserID": "string", "Password": "string",
							   "UserProductInfo": "string", "InterfaceProductInfo": "string", "ProtocolInfo": "string",
							   "MacAddress": "string", "OneTimePassword": "string", "ClientIPAddress": "string"}
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
structDict['CThostFtdcReqUserLoginField'] = CThostFtdcReqUserLoginField


#用户登录应答
CThostFtdcRspUserLoginField = {"TradingDay": "string", "LoginTime": "string", "BrokerID": "string", "UserID": "string",
							   "SystemName": "string", "FrontID": "int", "SessionID": "int", "MaxOrderRef": "string",
							   "SHFETime": "string", "DCETime": "string", "CZCETime": "string", "FFEXTime": "string",
							   "INETime": "string"}
#交易日
#登录成功时间
#经纪公司代码
#用户代码
#交易系统名称
#前置编号
#会话编号
#最大报单引用
#上期所时间
#大商所时间
#郑商所时间
#中金所时间
#能源中心时间
structDict['CThostFtdcRspUserLoginField'] = CThostFtdcRspUserLoginField


#用户登出请求
CThostFtdcUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CThostFtdcUserLogoutField'] = CThostFtdcUserLogoutField


#强制交易员退出
CThostFtdcForceUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CThostFtdcForceUserLogoutField'] = CThostFtdcForceUserLogoutField


#客户端认证请求
CThostFtdcReqAuthenticateField = {"BrokerID": "string", "UserID": "string", "UserProductInfo": "string",
								  "AuthCode": "string"}
#经纪公司代码
#用户代码
#用户端产品信息
#认证码
structDict['CThostFtdcReqAuthenticateField'] = CThostFtdcReqAuthenticateField


#客户端认证响应
CThostFtdcRspAuthenticateField = {"BrokerID": "string", "UserID": "string", "UserProductInfo": "string"}
#经纪公司代码
#用户代码
#用户端产品信息
structDict['CThostFtdcRspAuthenticateField'] = CThostFtdcRspAuthenticateField


#客户端认证信息
CThostFtdcAuthenticationInfoField = {"BrokerID": "string", "UserID": "string", "UserProductInfo": "string",
									 "AuthInfo": "string", "IsResult": "int"}
#经纪公司代码
#用户代码
#用户端产品信息
#认证信息
#是否为认证结果
structDict['CThostFtdcAuthenticationInfoField'] = CThostFtdcAuthenticationInfoField


#银期转帐报文头
CThostFtdcTransferHeaderField = {"Version": "string", "TradeCode": "string", "TradeDate": "string",
								 "TradeTime": "string", "TradeSerial": "string", "FutureID": "string",
								 "BankID": "string", "BankBrchID": "string", "OperNo": "string", "DeviceID": "string",
								 "RecordNum": "string", "SessionID": "int", "RequestID": "int"}
#版本号，常量，1.0
#交易代码，必填
#交易日期，必填，格式：yyyymmdd
#交易时间，必填，格式：hhmmss
#发起方流水号，N/A
#期货公司代码，必填
#银行代码，根据查询银行得到，必填
#银行分中心代码，根据查询银行得到，必填
#操作员，N/A
#交易设备类型，N/A
#记录数，N/A
#会话编号，N/A
#请求编号，N/A
structDict['CThostFtdcTransferHeaderField'] = CThostFtdcTransferHeaderField


#银行资金转期货请求，TradeCode=202001
CThostFtdcTransferBankToFutureReqField = {"FutureAccount": "string", "FuturePwdFlag": "char", "FutureAccPwd": "string",
										  "TradeAmt": "float", "CustFee": "float", "CurrencyCode": "string"}
#期货资金账户
#密码标志
#密码
#转账金额
#客户手续费
#币种：RMB-人民币 USD-美圆 HKD-港元
structDict['CThostFtdcTransferBankToFutureReqField'] = CThostFtdcTransferBankToFutureReqField


#银行资金转期货请求响应
CThostFtdcTransferBankToFutureRspField = {"RetCode": "string", "RetInfo": "string", "FutureAccount": "string",
										  "TradeAmt": "float", "CustFee": "float", "CurrencyCode": "string"}
#响应代码
#响应信息
#资金账户
#转帐金额
#应收客户手续费
#币种
structDict['CThostFtdcTransferBankToFutureRspField'] = CThostFtdcTransferBankToFutureRspField


#期货资金转银行请求，TradeCode=202002
CThostFtdcTransferFutureToBankReqField = {"FutureAccount": "string", "FuturePwdFlag": "char", "FutureAccPwd": "string",
										  "TradeAmt": "float", "CustFee": "float", "CurrencyCode": "string"}
#期货资金账户
#密码标志
#密码
#转账金额
#客户手续费
#币种：RMB-人民币 USD-美圆 HKD-港元
structDict['CThostFtdcTransferFutureToBankReqField'] = CThostFtdcTransferFutureToBankReqField


#期货资金转银行请求响应
CThostFtdcTransferFutureToBankRspField = {"RetCode": "string", "RetInfo": "string", "FutureAccount": "string",
										  "TradeAmt": "float", "CustFee": "float", "CurrencyCode": "string"}
#响应代码
#响应信息
#资金账户
#转帐金额
#应收客户手续费
#币种
structDict['CThostFtdcTransferFutureToBankRspField'] = CThostFtdcTransferFutureToBankRspField


#查询银行资金请求，TradeCode=204002
CThostFtdcTransferQryBankReqField = {"FutureAccount": "string", "FuturePwdFlag": "char", "FutureAccPwd": "string",
									 "CurrencyCode": "string"}
#期货资金账户
#密码标志
#密码
#币种：RMB-人民币 USD-美圆 HKD-港元
structDict['CThostFtdcTransferQryBankReqField'] = CThostFtdcTransferQryBankReqField


#查询银行资金请求响应
CThostFtdcTransferQryBankRspField = {"RetCode": "string", "RetInfo": "string", "FutureAccount": "string",
									 "TradeAmt": "float", "UseAmt": "float", "FetchAmt": "float",
									 "CurrencyCode": "string"}
#响应代码
#响应信息
#资金账户
#银行余额
#银行可用余额
#银行可取余额
#币种
structDict['CThostFtdcTransferQryBankRspField'] = CThostFtdcTransferQryBankRspField


#查询银行交易明细请求，TradeCode=204999
CThostFtdcTransferQryDetailReqField = {"FutureAccount": "string"}
#期货资金账户
structDict['CThostFtdcTransferQryDetailReqField'] = CThostFtdcTransferQryDetailReqField


#查询银行交易明细请求响应
CThostFtdcTransferQryDetailRspField = {"TradeDate": "string", "TradeTime": "string", "TradeCode": "string",
									   "FutureSerial": "int", "FutureID": "string", "FutureAccount": "string",
									   "BankSerial": "int", "BankID": "string", "BankBrchID": "string",
									   "BankAccount": "string", "CertCode": "string", "CurrencyCode": "string",
									   "TxAmount": "float", "Flag": "char"}
#交易日期
#交易时间
#交易代码
#期货流水号
#期货公司代码
#资金帐号
#银行流水号
#银行代码
#银行分中心代码
#银行账号
#证件号码
#货币代码
#发生金额
#有效标志
structDict['CThostFtdcTransferQryDetailRspField'] = CThostFtdcTransferQryDetailRspField


#响应信息
CThostFtdcRspInfoField = {"ErrorID": "int", "ErrorMsg": "string"}
#错误代码
#错误信息
structDict['CThostFtdcRspInfoField'] = CThostFtdcRspInfoField


#交易所
CThostFtdcExchangeField = {"ExchangeID": "string", "ExchangeName": "string", "ExchangeProperty": "char"}
#交易所代码
#交易所名称
#交易所属性
structDict['CThostFtdcExchangeField'] = CThostFtdcExchangeField


#产品
CThostFtdcProductField = {"ProductID": "string", "ProductName": "string", "ExchangeID": "string",
						  "ProductClass": "char", "VolumeMultiple": "int", "PriceTick": "float",
						  "MaxMarketOrderVolume": "int", "MinMarketOrderVolume": "int", "MaxLimitOrderVolume": "int",
						  "MinLimitOrderVolume": "int", "PositionType": "char", "PositionDateType": "char",
						  "CloseDealType": "char", "TradeCurrencyID": "string", "MortgageFundUseRange": "char",
						  "ExchangeProductID": "string", "UnderlyingMultiple": "float"}
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
#平仓处理类型
#交易币种类型
#质押资金可用范围
#交易所产品代码
#合约基础商品乘数
structDict['CThostFtdcProductField'] = CThostFtdcProductField


#合约
CThostFtdcInstrumentField = {"InstrumentID": "string", "ExchangeID": "string", "InstrumentName": "string",
							 "ExchangeInstID": "string", "ProductID": "string", "ProductClass": "char",
							 "DeliveryYear": "int", "DeliveryMonth": "int", "MaxMarketOrderVolume": "int",
							 "MinMarketOrderVolume": "int", "MaxLimitOrderVolume": "int", "MinLimitOrderVolume": "int",
							 "VolumeMultiple": "int", "PriceTick": "float", "CreateDate": "string",
							 "OpenDate": "string", "ExpireDate": "string", "StartDelivDate": "string",
							 "EndDelivDate": "string", "InstLifePhase": "char", "IsTrading": "int",
							 "PositionType": "char", "PositionDateType": "char", "LongMarginRatio": "float",
							 "ShortMarginRatio": "float", "MaxMarginSideAlgorithm": "char",
							 "UnderlyingInstrID": "string", "StrikePrice": "float", "OptionsType": "char",
							 "UnderlyingMultiple": "float", "CombinationType": "char", "MinBuyVolume": "int",
							 "MinSellVolume": "int", "InstrumentCode": "string"}
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
#持仓日期类型
#多头保证金率
#空头保证金率
#是否使用大额单边保证金算法
#基础商品代码
#执行价
#期权类型
#合约基础商品乘数
#组合类型
#最小买下单单位
#最小卖下单单位
#合约标识码
structDict['CThostFtdcInstrumentField'] = CThostFtdcInstrumentField


#经纪公司
CThostFtdcBrokerField = {"BrokerID": "string", "BrokerAbbr": "string", "BrokerName": "string", "IsActive": "int"}
#经纪公司代码
#经纪公司简称
#经纪公司名称
#是否活跃
structDict['CThostFtdcBrokerField'] = CThostFtdcBrokerField


#交易所交易员
CThostFtdcTraderField = {"ExchangeID": "string", "TraderID": "string", "ParticipantID": "string", "Password": "string",
						 "InstallCount": "int", "BrokerID": "string"}
#交易所代码
#交易所交易员代码
#会员代码
#密码
#安装数量
#经纪公司代码
structDict['CThostFtdcTraderField'] = CThostFtdcTraderField


#投资者
CThostFtdcInvestorField = {"InvestorID": "string", "BrokerID": "string", "InvestorGroupID": "string",
						   "InvestorName": "string", "IdentifiedCardType": "char", "IdentifiedCardNo": "string",
						   "IsActive": "int", "Telephone": "string", "Address": "string", "OpenDate": "string",
						   "Mobile": "string", "CommModelID": "string", "MarginModelID": "string"}
#投资者代码
#经纪公司代码
#投资者分组代码
#投资者名称
#证件类型
#证件号码
#是否活跃
#联系电话
#通讯地址
#开户日期
#手机
#手续费率模板代码
#保证金率模板代码
structDict['CThostFtdcInvestorField'] = CThostFtdcInvestorField


#交易编码
CThostFtdcTradingCodeField = {"InvestorID": "string", "BrokerID": "string", "ExchangeID": "string",
							  "ClientID": "string", "IsActive": "int", "ClientIDType": "char", "BranchID": "string",
							  "BizType": "char"}
#投资者代码
#经纪公司代码
#交易所代码
#客户代码
#是否活跃
#交易编码类型
#营业部编号
#业务类型
structDict['CThostFtdcTradingCodeField'] = CThostFtdcTradingCodeField


#会员编码和经纪公司编码对照表
CThostFtdcPartBrokerField = {"BrokerID": "string", "ExchangeID": "string", "ParticipantID": "string", "IsActive": "int"}
#经纪公司代码
#交易所代码
#会员代码
#是否活跃
structDict['CThostFtdcPartBrokerField'] = CThostFtdcPartBrokerField


#管理用户
CThostFtdcSuperUserField = {"UserID": "string", "UserName": "string", "Password": "string", "IsActive": "int"}
#用户代码
#用户名称
#密码
#是否活跃
structDict['CThostFtdcSuperUserField'] = CThostFtdcSuperUserField


#管理用户功能权限
CThostFtdcSuperUserFunctionField = {"UserID": "string", "FunctionCode": "char"}
#用户代码
#功能代码
structDict['CThostFtdcSuperUserFunctionField'] = CThostFtdcSuperUserFunctionField


#投资者组
CThostFtdcInvestorGroupField = {"BrokerID": "string", "InvestorGroupID": "string", "InvestorGroupName": "string"}
#经纪公司代码
#投资者分组代码
#投资者分组名称
structDict['CThostFtdcInvestorGroupField'] = CThostFtdcInvestorGroupField


#资金账户
CThostFtdcTradingAccountField = {"BrokerID": "string", "AccountID": "string", "PreMortgage": "float",
								 "PreCredit": "float", "PreDeposit": "float", "PreBalance": "float",
								 "PreMargin": "float", "InterestBase": "float", "Interest": "float", "Deposit": "float",
								 "Withdraw": "float", "FrozenMargin": "float", "FrozenCash": "float",
								 "FrozenCommission": "float", "CurrMargin": "float", "CashIn": "float",
								 "Commission": "float", "CloseProfit": "float", "PositionProfit": "float",
								 "Balance": "float", "Available": "float", "WithdrawQuota": "float", "Reserve": "float",
								 "TradingDay": "string", "SettlementID": "int", "Credit": "float", "Mortgage": "float",
								 "ExchangeMargin": "float", "DeliveryMargin": "float",
								 "ExchangeDeliveryMargin": "float", "ReserveBalance": "float", "CurrencyID": "string",
								 "PreFundMortgageIn": "float", "PreFundMortgageOut": "float", "FundMortgageIn": "float",
								 "FundMortgageOut": "float", "FundMortgageAvailable": "float",
								 "MortgageableFund": "float", "SpecProductMargin": "float",
								 "SpecProductFrozenMargin": "float", "SpecProductCommission": "float",
								 "SpecProductFrozenCommission": "float", "SpecProductPositionProfit": "float",
								 "SpecProductCloseProfit": "float", "SpecProductPositionProfitByAlg": "float",
								 "SpecProductExchangeMargin": "float", "BizType": "char"}
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
#平仓盈亏
#持仓盈亏
#期货结算准备金
#可用资金
#可取资金
#基本准备金
#交易日
#结算编号
#信用额度
#质押金额
#交易所保证金
#投资者交割保证金
#交易所交割保证金
#保底期货结算准备金
#币种代码
#上次货币质入金额
#上次货币质出金额
#货币质入金额
#货币质出金额
#货币质押余额
#可质押货币金额
#特殊产品占用保证金
#特殊产品冻结保证金
#特殊产品手续费
#特殊产品冻结手续费
#特殊产品持仓盈亏
#特殊产品平仓盈亏
#根据持仓盈亏算法计算的特殊产品持仓盈亏
#特殊产品交易所保证金
#业务类型
structDict['CThostFtdcTradingAccountField'] = CThostFtdcTradingAccountField


#投资者持仓
CThostFtdcInvestorPositionField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
								   "PosiDirection": "char", "HedgeFlag": "char", "PositionDate": "char",
								   "YdPosition": "int", "Position": "int", "LongFrozen": "int", "ShortFrozen": "int",
								   "LongFrozenAmount": "float", "ShortFrozenAmount": "float", "OpenVolume": "int",
								   "CloseVolume": "int", "OpenAmount": "float", "CloseAmount": "float",
								   "PositionCost": "float", "PreMargin": "float", "UseMargin": "float",
								   "FrozenMargin": "float", "FrozenCash": "float", "FrozenCommission": "float",
								   "CashIn": "float", "Commission": "float", "CloseProfit": "float",
								   "PositionProfit": "float", "PreSettlementPrice": "float", "SettlementPrice": "float",
								   "TradingDay": "string", "SettlementID": "int", "OpenCost": "float",
								   "ExchangeMargin": "float", "CombPosition": "int", "CombLongFrozen": "int",
								   "CombShortFrozen": "int", "CloseProfitByDate": "float",
								   "CloseProfitByTrade": "float", "TodayPosition": "int", "MarginRateByMoney": "float",
								   "MarginRateByVolume": "float", "StrikeFrozen": "int", "StrikeFrozenAmount": "float",
								   "AbandonFrozen": "int", "ExchangeID": "string", "YdStrikeFrozen": "int"}
#合约代码
#经纪公司代码
#投资者代码
#持仓多空方向
#投机套保标志
#持仓日期
#上日持仓
#今日持仓
#多头冻结
#空头冻结
#开仓冻结金额
#开仓冻结金额
#开仓量
#平仓量
#开仓金额
#平仓金额
#持仓成本
#上次占用的保证金
#占用的保证金
#冻结的保证金
#冻结的资金
#冻结的手续费
#资金差额
#手续费
#平仓盈亏
#持仓盈亏
#上次结算价
#本次结算价
#交易日
#结算编号
#开仓成本
#交易所保证金
#组合成交形成的持仓
#组合多头冻结
#组合空头冻结
#逐日盯市平仓盈亏
#逐笔对冲平仓盈亏
#今日持仓
#保证金率
#保证金率(按手数)
#执行冻结
#执行冻结金额
#放弃执行冻结
#交易所代码
#执行冻结的昨仓
structDict['CThostFtdcInvestorPositionField'] = CThostFtdcInvestorPositionField


#合约保证金率
CThostFtdcInstrumentMarginRateField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
									   "InvestorID": "string", "HedgeFlag": "char", "LongMarginRatioByMoney": "float",
									   "LongMarginRatioByVolume": "float", "ShortMarginRatioByMoney": "float",
									   "ShortMarginRatioByVolume": "float", "IsRelative": "int"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#投机套保标志
#多头保证金率
#多头保证金费
#空头保证金率
#空头保证金费
#是否相对交易所收取
structDict['CThostFtdcInstrumentMarginRateField'] = CThostFtdcInstrumentMarginRateField


#合约手续费率
CThostFtdcInstrumentCommissionRateField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
										   "InvestorID": "string", "OpenRatioByMoney": "float",
										   "OpenRatioByVolume": "float", "CloseRatioByMoney": "float",
										   "CloseRatioByVolume": "float", "CloseTodayRatioByMoney": "float",
										   "CloseTodayRatioByVolume": "float", "ExchangeID": "string",
										   "BizType": "char"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#开仓手续费率
#开仓手续费
#平仓手续费率
#平仓手续费
#平今手续费率
#平今手续费
#交易所代码
#业务类型
structDict['CThostFtdcInstrumentCommissionRateField'] = CThostFtdcInstrumentCommissionRateField


#深度行情
CThostFtdcDepthMarketDataField = {"TradingDay": "string", "InstrumentID": "string", "ExchangeID": "string",
								  "ExchangeInstID": "string", "LastPrice": "float", "PreSettlementPrice": "float",
								  "PreClosePrice": "float", "PreOpenInterest": "float", "OpenPrice": "float",
								  "HighestPrice": "float", "LowestPrice": "float", "Volume": "int", "Turnover": "float",
								  "OpenInterest": "float", "ClosePrice": "float", "SettlementPrice": "float",
								  "UpperLimitPrice": "float", "LowerLimitPrice": "float", "PreDelta": "float",
								  "CurrDelta": "float", "UpdateTime": "string", "UpdateMillisec": "int",
								  "BidPrice1": "float", "BidVolume1": "int", "AskPrice1": "float", "AskVolume1": "int",
								  "BidPrice2": "float", "BidVolume2": "int", "AskPrice2": "float", "AskVolume2": "int",
								  "BidPrice3": "float", "BidVolume3": "int", "AskPrice3": "float", "AskVolume3": "int",
								  "BidPrice4": "float", "BidVolume4": "int", "AskPrice4": "float", "AskVolume4": "int",
								  "BidPrice5": "float", "BidVolume5": "int", "AskPrice5": "float", "AskVolume5": "int",
								  "AveragePrice": "float", "ActionDay": "string"}
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
structDict['CThostFtdcDepthMarketDataField'] = CThostFtdcDepthMarketDataField


#投资者合约交易权限
CThostFtdcInstrumentTradingRightField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
										 "InvestorID": "string", "TradingRight": "char", "ExchangeID": "string",
										 "BizType": "char"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#交易权限
#交易所代码
#业务类型
structDict['CThostFtdcInstrumentTradingRightField'] = CThostFtdcInstrumentTradingRightField


#经纪公司用户
CThostFtdcBrokerUserField = {"BrokerID": "string", "UserID": "string", "UserName": "string", "UserType": "char",
							 "IsActive": "int", "IsUsingOTP": "int"}
#经纪公司代码
#用户代码
#用户名称
#用户类型
#是否活跃
#是否使用令牌
structDict['CThostFtdcBrokerUserField'] = CThostFtdcBrokerUserField


#经纪公司用户口令
CThostFtdcBrokerUserPasswordField = {"BrokerID": "string", "UserID": "string", "Password": "string"}
#经纪公司代码
#用户代码
#密码
structDict['CThostFtdcBrokerUserPasswordField'] = CThostFtdcBrokerUserPasswordField


#经纪公司用户功能权限
CThostFtdcBrokerUserFunctionField = {"BrokerID": "string", "UserID": "string", "BrokerFunctionCode": "char"}
#经纪公司代码
#用户代码
#经纪公司功能代码
structDict['CThostFtdcBrokerUserFunctionField'] = CThostFtdcBrokerUserFunctionField


#交易所交易员报盘机
CThostFtdcTraderOfferField = {"ExchangeID": "string", "TraderID": "string", "ParticipantID": "string",
							  "Password": "string", "InstallID": "int", "OrderLocalID": "string",
							  "TraderConnectStatus": "char", "ConnectRequestDate": "string",
							  "ConnectRequestTime": "string", "LastReportDate": "string", "LastReportTime": "string",
							  "ConnectDate": "string", "ConnectTime": "string", "StartDate": "string",
							  "StartTime": "string", "TradingDay": "string", "BrokerID": "string",
							  "MaxTradeID": "string", "MaxOrderMessageReference": "string", "BizType": "char"}
#交易所代码
#交易所交易员代码
#会员代码
#密码
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
#本席位最大成交编号
#本席位最大报单备拷
#业务类型
structDict['CThostFtdcTraderOfferField'] = CThostFtdcTraderOfferField


#投资者结算结果
CThostFtdcSettlementInfoField = {"TradingDay": "string", "SettlementID": "int", "BrokerID": "string",
								 "InvestorID": "string", "SequenceNo": "int", "Content": "string"}
#交易日
#结算编号
#经纪公司代码
#投资者代码
#序号
#消息正文
structDict['CThostFtdcSettlementInfoField'] = CThostFtdcSettlementInfoField


#合约保证金率调整
CThostFtdcInstrumentMarginRateAdjustField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
											 "InvestorID": "string", "HedgeFlag": "char",
											 "LongMarginRatioByMoney": "float", "LongMarginRatioByVolume": "float",
											 "ShortMarginRatioByMoney": "float", "ShortMarginRatioByVolume": "float",
											 "IsRelative": "int"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#投机套保标志
#多头保证金率
#多头保证金费
#空头保证金率
#空头保证金费
#是否相对交易所收取
structDict['CThostFtdcInstrumentMarginRateAdjustField'] = CThostFtdcInstrumentMarginRateAdjustField


#交易所保证金率
CThostFtdcExchangeMarginRateField = {"BrokerID": "string", "InstrumentID": "string", "HedgeFlag": "char",
									 "LongMarginRatioByMoney": "float", "LongMarginRatioByVolume": "float",
									 "ShortMarginRatioByMoney": "float", "ShortMarginRatioByVolume": "float"}
#经纪公司代码
#合约代码
#投机套保标志
#多头保证金率
#多头保证金费
#空头保证金率
#空头保证金费
structDict['CThostFtdcExchangeMarginRateField'] = CThostFtdcExchangeMarginRateField


#交易所保证金率调整
CThostFtdcExchangeMarginRateAdjustField = {"BrokerID": "string", "InstrumentID": "string", "HedgeFlag": "char",
										   "LongMarginRatioByMoney": "float", "LongMarginRatioByVolume": "float",
										   "ShortMarginRatioByMoney": "float", "ShortMarginRatioByVolume": "float",
										   "ExchLongMarginRatioByMoney": "float",
										   "ExchLongMarginRatioByVolume": "float",
										   "ExchShortMarginRatioByMoney": "float",
										   "ExchShortMarginRatioByVolume": "float", "NoLongMarginRatioByMoney": "float",
										   "NoLongMarginRatioByVolume": "float", "NoShortMarginRatioByMoney": "float",
										   "NoShortMarginRatioByVolume": "float"}
#经纪公司代码
#合约代码
#投机套保标志
#跟随交易所投资者多头保证金率
#跟随交易所投资者多头保证金费
#跟随交易所投资者空头保证金率
#跟随交易所投资者空头保证金费
#交易所多头保证金率
#交易所多头保证金费
#交易所空头保证金率
#交易所空头保证金费
#不跟随交易所投资者多头保证金率
#不跟随交易所投资者多头保证金费
#不跟随交易所投资者空头保证金率
#不跟随交易所投资者空头保证金费
structDict['CThostFtdcExchangeMarginRateAdjustField'] = CThostFtdcExchangeMarginRateAdjustField


#汇率
CThostFtdcExchangeRateField = {"BrokerID": "string", "FromCurrencyID": "string", "FromCurrencyUnit": "float",
							   "ToCurrencyID": "string", "ExchangeRate": "float"}
#经纪公司代码
#源币种
#源币种单位数量
#目标币种
#汇率
structDict['CThostFtdcExchangeRateField'] = CThostFtdcExchangeRateField


#结算引用
CThostFtdcSettlementRefField = {"TradingDay": "string", "SettlementID": "int"}
#交易日
#结算编号
structDict['CThostFtdcSettlementRefField'] = CThostFtdcSettlementRefField


#当前时间
CThostFtdcCurrentTimeField = {"CurrDate": "string", "CurrTime": "string", "CurrMillisec": "int", "ActionDay": "string"}
#当前日期
#当前时间
#当前时间（毫秒）
#业务日期
structDict['CThostFtdcCurrentTimeField'] = CThostFtdcCurrentTimeField


#通讯阶段
CThostFtdcCommPhaseField = {"TradingDay": "string", "CommPhaseNo": "int", "SystemID": "string"}
#交易日
#通讯时段编号
#系统编号
structDict['CThostFtdcCommPhaseField'] = CThostFtdcCommPhaseField


#登录信息
CThostFtdcLoginInfoField = {"FrontID": "int", "SessionID": "int", "BrokerID": "string", "UserID": "string",
							"LoginDate": "string", "LoginTime": "string", "IPAddress": "string",
							"UserProductInfo": "string", "InterfaceProductInfo": "string", "ProtocolInfo": "string",
							"SystemName": "string", "Password": "string", "MaxOrderRef": "string", "SHFETime": "string",
							"DCETime": "string", "CZCETime": "string", "FFEXTime": "string", "MacAddress": "string",
							"OneTimePassword": "string", "INETime": "string"}
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
#系统名称
#密码
#最大报单引用
#上期所时间
#大商所时间
#郑商所时间
#中金所时间
#Mac地址
#动态密码
#能源中心时间
structDict['CThostFtdcLoginInfoField'] = CThostFtdcLoginInfoField


#登录信息
CThostFtdcLogoutAllField = {"FrontID": "int", "SessionID": "int", "SystemName": "string"}
#前置编号
#会话编号
#系统名称
structDict['CThostFtdcLogoutAllField'] = CThostFtdcLogoutAllField


#前置状态
CThostFtdcFrontStatusField = {"FrontID": "int", "LastReportDate": "string", "LastReportTime": "string",
							  "IsActive": "int"}
#前置编号
#上次报告日期
#上次报告时间
#是否活跃
structDict['CThostFtdcFrontStatusField'] = CThostFtdcFrontStatusField


#用户口令变更
CThostFtdcUserPasswordUpdateField = {"BrokerID": "string", "UserID": "string", "OldPassword": "string",
									 "NewPassword": "string"}
#经纪公司代码
#用户代码
#原来的口令
#新的口令
structDict['CThostFtdcUserPasswordUpdateField'] = CThostFtdcUserPasswordUpdateField


#输入报单
CThostFtdcInputOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							 "OrderRef": "string", "UserID": "string", "OrderPriceType": "char", "Direction": "char",
							 "CombOffsetFlag": "string", "CombHedgeFlag": "string", "LimitPrice": "float",
							 "VolumeTotalOriginal": "int", "TimeCondition": "char", "GTDDate": "string",
							 "VolumeCondition": "char", "MinVolume": "int", "ContingentCondition": "char",
							 "StopPrice": "float", "ForceCloseReason": "char", "IsAutoSuspend": "int",
							 "BusinessUnit": "string", "RequestID": "int", "UserForceClose": "int",
							 "IsSwapOrder": "int", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
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
#互换单标志
#交易所代码
structDict['CThostFtdcInputOrderField'] = CThostFtdcInputOrderField


#报单
CThostFtdcOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
						"UserID": "string", "OrderPriceType": "char", "Direction": "char", "CombOffsetFlag": "string",
						"CombHedgeFlag": "string", "LimitPrice": "float", "VolumeTotalOriginal": "int",
						"TimeCondition": "char", "GTDDate": "string", "VolumeCondition": "char", "MinVolume": "int",
						"ContingentCondition": "char", "StopPrice": "float", "ForceCloseReason": "char",
						"IsAutoSuspend": "int", "BusinessUnit": "string", "RequestID": "int", "OrderLocalID": "string",
						"ExchangeID": "string", "ParticipantID": "string", "ClientID": "string",
						"ExchangeInstID": "string", "TraderID": "string", "InstallID": "int",
						"OrderSubmitStatus": "char", "NotifySequence": "int", "TradingDay": "string",
						"SettlementID": "int", "OrderSysID": "string", "OrderSource": "char", "OrderStatus": "char",
						"OrderType": "char", "VolumeTraded": "int", "VolumeTotal": "int", "InsertDate": "string",
						"InsertTime": "string", "ActiveTime": "string", "SuspendTime": "string", "UpdateTime": "string",
						"CancelTime": "string", "ActiveTraderID": "string", "ClearingPartID": "string",
						"SequenceNo": "int", "FrontID": "int", "SessionID": "int", "UserProductInfo": "string",
						"StatusMsg": "string", "UserForceClose": "int", "ActiveUserID": "string",
						"BrokerOrderSeq": "int", "RelativeOrderSysID": "string", "ZCETotalTradedVolume": "int",
						"IsSwapOrder": "int", "BranchID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
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
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#报单提交状态
#报单提示序号
#交易日
#结算编号
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
#郑商所成交数量
#互换单标志
#营业部编号
structDict['CThostFtdcOrderField'] = CThostFtdcOrderField


#交易所报单
CThostFtdcExchangeOrderField = {"OrderPriceType": "char", "Direction": "char", "CombOffsetFlag": "string",
								"CombHedgeFlag": "string", "LimitPrice": "float", "VolumeTotalOriginal": "int",
								"TimeCondition": "char", "GTDDate": "string", "VolumeCondition": "char",
								"MinVolume": "int", "ContingentCondition": "char", "StopPrice": "float",
								"ForceCloseReason": "char", "IsAutoSuspend": "int", "BusinessUnit": "string",
								"RequestID": "int", "OrderLocalID": "string", "ExchangeID": "string",
								"ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string",
								"TraderID": "string", "InstallID": "int", "OrderSubmitStatus": "char",
								"NotifySequence": "int", "TradingDay": "string", "SettlementID": "int",
								"OrderSysID": "string", "OrderSource": "char", "OrderStatus": "char",
								"OrderType": "char", "VolumeTraded": "int", "VolumeTotal": "int",
								"InsertDate": "string", "InsertTime": "string", "ActiveTime": "string",
								"SuspendTime": "string", "UpdateTime": "string", "CancelTime": "string",
								"ActiveTraderID": "string", "ClearingPartID": "string", "SequenceNo": "int",
								"BranchID": "string"}
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
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#报单提交状态
#报单提示序号
#交易日
#结算编号
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
#营业部编号
structDict['CThostFtdcExchangeOrderField'] = CThostFtdcExchangeOrderField


#交易所报单插入失败
CThostFtdcExchangeOrderInsertErrorField = {"ExchangeID": "string", "ParticipantID": "string", "TraderID": "string",
										   "InstallID": "int", "OrderLocalID": "string", "ErrorID": "int",
										   "ErrorMsg": "string"}
#交易所代码
#会员代码
#交易所交易员代码
#安装编号
#本地报单编号
#错误代码
#错误信息
structDict['CThostFtdcExchangeOrderInsertErrorField'] = CThostFtdcExchangeOrderInsertErrorField


#输入报单操作
CThostFtdcInputOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
								   "OrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
								   "ExchangeID": "string", "OrderSysID": "string", "ActionFlag": "char",
								   "LimitPrice": "float", "VolumeChange": "int", "UserID": "string",
								   "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#报单操作引用
#报单引用
#请求编号
#前置编号
#会话编号
#交易所代码
#报单编号
#操作标志
#价格
#数量变化
#用户代码
#合约代码
structDict['CThostFtdcInputOrderActionField'] = CThostFtdcInputOrderActionField


#报单操作
CThostFtdcOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
							  "OrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
							  "ExchangeID": "string", "OrderSysID": "string", "ActionFlag": "char",
							  "LimitPrice": "float", "VolumeChange": "int", "ActionDate": "string",
							  "ActionTime": "string", "TraderID": "string", "InstallID": "int",
							  "OrderLocalID": "string", "ActionLocalID": "string", "ParticipantID": "string",
							  "ClientID": "string", "BusinessUnit": "string", "OrderActionStatus": "char",
							  "UserID": "string", "StatusMsg": "string", "InstrumentID": "string", "BranchID": "string"}
#经纪公司代码
#投资者代码
#报单操作引用
#报单引用
#请求编号
#前置编号
#会话编号
#交易所代码
#报单编号
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
#状态信息
#合约代码
#营业部编号
structDict['CThostFtdcOrderActionField'] = CThostFtdcOrderActionField


#交易所报单操作
CThostFtdcExchangeOrderActionField = {"ExchangeID": "string", "OrderSysID": "string", "ActionFlag": "char",
									  "LimitPrice": "float", "VolumeChange": "int", "ActionDate": "string",
									  "ActionTime": "string", "TraderID": "string", "InstallID": "int",
									  "OrderLocalID": "string", "ActionLocalID": "string", "ParticipantID": "string",
									  "ClientID": "string", "BusinessUnit": "string", "OrderActionStatus": "char",
									  "UserID": "string", "BranchID": "string"}
#交易所代码
#报单编号
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
structDict['CThostFtdcExchangeOrderActionField'] = CThostFtdcExchangeOrderActionField


#交易所报单操作失败
CThostFtdcExchangeOrderActionErrorField = {"ExchangeID": "string", "OrderSysID": "string", "TraderID": "string",
										   "InstallID": "int", "OrderLocalID": "string", "ActionLocalID": "string",
										   "ErrorID": "int", "ErrorMsg": "string", "BrokerID": "string"}
#交易所代码
#报单编号
#交易所交易员代码
#安装编号
#本地报单编号
#操作本地编号
#错误代码
#错误信息
#经纪公司代码
structDict['CThostFtdcExchangeOrderActionErrorField'] = CThostFtdcExchangeOrderActionErrorField


#交易所成交
CThostFtdcExchangeTradeField = {"ExchangeID": "string", "TradeID": "string", "Direction": "char",
								"OrderSysID": "string", "ParticipantID": "string", "ClientID": "string",
								"TradingRole": "char", "ExchangeInstID": "string", "OffsetFlag": "char",
								"HedgeFlag": "char", "Price": "float", "Volume": "int", "TradeDate": "string",
								"TradeTime": "string", "TradeType": "char", "PriceSource": "char", "TraderID": "string",
								"OrderLocalID": "string", "ClearingPartID": "string", "BusinessUnit": "string",
								"SequenceNo": "int", "TradeSource": "char"}
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
structDict['CThostFtdcExchangeTradeField'] = CThostFtdcExchangeTradeField


#成交
CThostFtdcTradeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
						"UserID": "string", "ExchangeID": "string", "TradeID": "string", "Direction": "char",
						"OrderSysID": "string", "ParticipantID": "string", "ClientID": "string", "TradingRole": "char",
						"ExchangeInstID": "string", "OffsetFlag": "char", "HedgeFlag": "char", "Price": "float",
						"Volume": "int", "TradeDate": "string", "TradeTime": "string", "TradeType": "char",
						"PriceSource": "char", "TraderID": "string", "OrderLocalID": "string",
						"ClearingPartID": "string", "BusinessUnit": "string", "SequenceNo": "int",
						"TradingDay": "string", "SettlementID": "int", "BrokerOrderSeq": "int", "TradeSource": "char"}
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
#交易日
#结算编号
#经纪公司报单编号
#成交来源
structDict['CThostFtdcTradeField'] = CThostFtdcTradeField


#用户会话
CThostFtdcUserSessionField = {"FrontID": "int", "SessionID": "int", "BrokerID": "string", "UserID": "string",
							  "LoginDate": "string", "LoginTime": "string", "IPAddress": "string",
							  "UserProductInfo": "string", "InterfaceProductInfo": "string", "ProtocolInfo": "string",
							  "MacAddress": "string"}
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
structDict['CThostFtdcUserSessionField'] = CThostFtdcUserSessionField


#查询最大报单数量
CThostFtdcQueryMaxOrderVolumeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
									  "Direction": "char", "OffsetFlag": "char", "HedgeFlag": "char",
									  "MaxVolume": "int", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#买卖方向
#开平标志
#投机套保标志
#最大允许报单数量
#交易所代码
structDict['CThostFtdcQueryMaxOrderVolumeField'] = CThostFtdcQueryMaxOrderVolumeField


#投资者结算结果确认信息
CThostFtdcSettlementInfoConfirmField = {"BrokerID": "string", "InvestorID": "string", "ConfirmDate": "string",
										"ConfirmTime": "string"}
#经纪公司代码
#投资者代码
#确认日期
#确认时间
structDict['CThostFtdcSettlementInfoConfirmField'] = CThostFtdcSettlementInfoConfirmField


#出入金同步
CThostFtdcSyncDepositField = {"DepositSeqNo": "string", "BrokerID": "string", "InvestorID": "string",
							  "Deposit": "float", "IsForce": "int", "CurrencyID": "string"}
#出入金流水号
#经纪公司代码
#投资者代码
#入金金额
#是否强制进行
#币种代码
structDict['CThostFtdcSyncDepositField'] = CThostFtdcSyncDepositField


#货币质押同步
CThostFtdcSyncFundMortgageField = {"MortgageSeqNo": "string", "BrokerID": "string", "InvestorID": "string",
								   "FromCurrencyID": "string", "MortgageAmount": "float", "ToCurrencyID": "string"}
#货币质押流水号
#经纪公司代码
#投资者代码
#源币种
#质押金额
#目标币种
structDict['CThostFtdcSyncFundMortgageField'] = CThostFtdcSyncFundMortgageField


#经纪公司同步
CThostFtdcBrokerSyncField = {"BrokerID": "string"}
#经纪公司代码
structDict['CThostFtdcBrokerSyncField'] = CThostFtdcBrokerSyncField


#正在同步中的投资者
CThostFtdcSyncingInvestorField = {"InvestorID": "string", "BrokerID": "string", "InvestorGroupID": "string",
								  "InvestorName": "string", "IdentifiedCardType": "char", "IdentifiedCardNo": "string",
								  "IsActive": "int", "Telephone": "string", "Address": "string", "OpenDate": "string",
								  "Mobile": "string", "CommModelID": "string", "MarginModelID": "string"}
#投资者代码
#经纪公司代码
#投资者分组代码
#投资者名称
#证件类型
#证件号码
#是否活跃
#联系电话
#通讯地址
#开户日期
#手机
#手续费率模板代码
#保证金率模板代码
structDict['CThostFtdcSyncingInvestorField'] = CThostFtdcSyncingInvestorField


#正在同步中的交易代码
CThostFtdcSyncingTradingCodeField = {"InvestorID": "string", "BrokerID": "string", "ExchangeID": "string",
									 "ClientID": "string", "IsActive": "int", "ClientIDType": "char",
									 "BranchID": "string"}
#投资者代码
#经纪公司代码
#交易所代码
#客户代码
#是否活跃
#交易编码类型
#营业部编号
structDict['CThostFtdcSyncingTradingCodeField'] = CThostFtdcSyncingTradingCodeField


#正在同步中的投资者分组
CThostFtdcSyncingInvestorGroupField = {"BrokerID": "string", "InvestorGroupID": "string", "InvestorGroupName": "string"}
#经纪公司代码
#投资者分组代码
#投资者分组名称
structDict['CThostFtdcSyncingInvestorGroupField'] = CThostFtdcSyncingInvestorGroupField


#正在同步中的交易账号
CThostFtdcSyncingTradingAccountField = {"BrokerID": "string", "AccountID": "string", "PreMortgage": "float",
										"PreCredit": "float", "PreDeposit": "float", "PreBalance": "float",
										"PreMargin": "float", "InterestBase": "float", "Interest": "float",
										"Deposit": "float", "Withdraw": "float", "FrozenMargin": "float",
										"FrozenCash": "float", "FrozenCommission": "float", "CurrMargin": "float",
										"CashIn": "float", "Commission": "float", "CloseProfit": "float",
										"PositionProfit": "float", "Balance": "float", "Available": "float",
										"WithdrawQuota": "float", "Reserve": "float", "TradingDay": "string",
										"SettlementID": "int", "Credit": "float", "Mortgage": "float",
										"ExchangeMargin": "float", "DeliveryMargin": "float",
										"ExchangeDeliveryMargin": "float", "ReserveBalance": "float",
										"CurrencyID": "string", "PreFundMortgageIn": "float",
										"PreFundMortgageOut": "float", "FundMortgageIn": "float",
										"FundMortgageOut": "float", "FundMortgageAvailable": "float",
										"MortgageableFund": "float", "SpecProductMargin": "float",
										"SpecProductFrozenMargin": "float", "SpecProductCommission": "float",
										"SpecProductFrozenCommission": "float", "SpecProductPositionProfit": "float",
										"SpecProductCloseProfit": "float", "SpecProductPositionProfitByAlg": "float",
										"SpecProductExchangeMargin": "float"}
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
#平仓盈亏
#持仓盈亏
#期货结算准备金
#可用资金
#可取资金
#基本准备金
#交易日
#结算编号
#信用额度
#质押金额
#交易所保证金
#投资者交割保证金
#交易所交割保证金
#保底期货结算准备金
#币种代码
#上次货币质入金额
#上次货币质出金额
#货币质入金额
#货币质出金额
#货币质押余额
#可质押货币金额
#特殊产品占用保证金
#特殊产品冻结保证金
#特殊产品手续费
#特殊产品冻结手续费
#特殊产品持仓盈亏
#特殊产品平仓盈亏
#根据持仓盈亏算法计算的特殊产品持仓盈亏
#特殊产品交易所保证金
structDict['CThostFtdcSyncingTradingAccountField'] = CThostFtdcSyncingTradingAccountField


#正在同步中的投资者持仓
CThostFtdcSyncingInvestorPositionField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
										  "PosiDirection": "char", "HedgeFlag": "char", "PositionDate": "char",
										  "YdPosition": "int", "Position": "int", "LongFrozen": "int",
										  "ShortFrozen": "int", "LongFrozenAmount": "float",
										  "ShortFrozenAmount": "float", "OpenVolume": "int", "CloseVolume": "int",
										  "OpenAmount": "float", "CloseAmount": "float", "PositionCost": "float",
										  "PreMargin": "float", "UseMargin": "float", "FrozenMargin": "float",
										  "FrozenCash": "float", "FrozenCommission": "float", "CashIn": "float",
										  "Commission": "float", "CloseProfit": "float", "PositionProfit": "float",
										  "PreSettlementPrice": "float", "SettlementPrice": "float",
										  "TradingDay": "string", "SettlementID": "int", "OpenCost": "float",
										  "ExchangeMargin": "float", "CombPosition": "int", "CombLongFrozen": "int",
										  "CombShortFrozen": "int", "CloseProfitByDate": "float",
										  "CloseProfitByTrade": "float", "TodayPosition": "int",
										  "MarginRateByMoney": "float", "MarginRateByVolume": "float",
										  "StrikeFrozen": "int", "StrikeFrozenAmount": "float", "AbandonFrozen": "int",
										  "ExchangeID": "string", "YdStrikeFrozen": "int"}
#合约代码
#经纪公司代码
#投资者代码
#持仓多空方向
#投机套保标志
#持仓日期
#上日持仓
#今日持仓
#多头冻结
#空头冻结
#开仓冻结金额
#开仓冻结金额
#开仓量
#平仓量
#开仓金额
#平仓金额
#持仓成本
#上次占用的保证金
#占用的保证金
#冻结的保证金
#冻结的资金
#冻结的手续费
#资金差额
#手续费
#平仓盈亏
#持仓盈亏
#上次结算价
#本次结算价
#交易日
#结算编号
#开仓成本
#交易所保证金
#组合成交形成的持仓
#组合多头冻结
#组合空头冻结
#逐日盯市平仓盈亏
#逐笔对冲平仓盈亏
#今日持仓
#保证金率
#保证金率(按手数)
#执行冻结
#执行冻结金额
#放弃执行冻结
#交易所代码
#执行冻结的昨仓
structDict['CThostFtdcSyncingInvestorPositionField'] = CThostFtdcSyncingInvestorPositionField


#正在同步中的合约保证金率
CThostFtdcSyncingInstrumentMarginRateField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
											  "InvestorID": "string", "HedgeFlag": "char",
											  "LongMarginRatioByMoney": "float", "LongMarginRatioByVolume": "float",
											  "ShortMarginRatioByMoney": "float", "ShortMarginRatioByVolume": "float",
											  "IsRelative": "int"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#投机套保标志
#多头保证金率
#多头保证金费
#空头保证金率
#空头保证金费
#是否相对交易所收取
structDict['CThostFtdcSyncingInstrumentMarginRateField'] = CThostFtdcSyncingInstrumentMarginRateField


#正在同步中的合约手续费率
CThostFtdcSyncingInstrumentCommissionRateField = {"InstrumentID": "string", "InvestorRange": "char",
												  "BrokerID": "string", "InvestorID": "string",
												  "OpenRatioByMoney": "float", "OpenRatioByVolume": "float",
												  "CloseRatioByMoney": "float", "CloseRatioByVolume": "float",
												  "CloseTodayRatioByMoney": "float", "CloseTodayRatioByVolume": "float",
												  "ExchangeID": "string"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#开仓手续费率
#开仓手续费
#平仓手续费率
#平仓手续费
#平今手续费率
#平今手续费
#交易所代码
structDict['CThostFtdcSyncingInstrumentCommissionRateField'] = CThostFtdcSyncingInstrumentCommissionRateField


#正在同步中的合约交易权限
CThostFtdcSyncingInstrumentTradingRightField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
												"InvestorID": "string", "TradingRight": "char", "ExchangeID": "string"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#交易权限
#交易所代码
structDict['CThostFtdcSyncingInstrumentTradingRightField'] = CThostFtdcSyncingInstrumentTradingRightField


#查询报单
CThostFtdcQryOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						   "ExchangeID": "string", "OrderSysID": "string", "InsertTimeStart": "string",
						   "InsertTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#报单编号
#开始时间
#结束时间
structDict['CThostFtdcQryOrderField'] = CThostFtdcQryOrderField


#查询成交
CThostFtdcQryTradeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						   "ExchangeID": "string", "TradeID": "string", "TradeTimeStart": "string",
						   "TradeTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#成交编号
#开始时间
#结束时间
structDict['CThostFtdcQryTradeField'] = CThostFtdcQryTradeField


#查询投资者持仓
CThostFtdcQryInvestorPositionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
									  "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryInvestorPositionField'] = CThostFtdcQryInvestorPositionField


#查询资金账户
CThostFtdcQryTradingAccountField = {"BrokerID": "string", "InvestorID": "string", "CurrencyID": "string",
									"BizType": "char"}
#经纪公司代码
#投资者代码
#币种代码
#业务类型
structDict['CThostFtdcQryTradingAccountField'] = CThostFtdcQryTradingAccountField


#查询投资者
CThostFtdcQryInvestorField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQryInvestorField'] = CThostFtdcQryInvestorField


#查询交易编码
CThostFtdcQryTradingCodeField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
								 "ClientID": "string", "ClientIDType": "char"}
#经纪公司代码
#投资者代码
#交易所代码
#客户代码
#交易编码类型
structDict['CThostFtdcQryTradingCodeField'] = CThostFtdcQryTradingCodeField


#查询投资者组
CThostFtdcQryInvestorGroupField = {"BrokerID": "string"}
#经纪公司代码
structDict['CThostFtdcQryInvestorGroupField'] = CThostFtdcQryInvestorGroupField


#查询合约保证金率
CThostFtdcQryInstrumentMarginRateField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
										  "HedgeFlag": "char"}
#经纪公司代码
#投资者代码
#合约代码
#投机套保标志
structDict['CThostFtdcQryInstrumentMarginRateField'] = CThostFtdcQryInstrumentMarginRateField


#查询手续费率
CThostFtdcQryInstrumentCommissionRateField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
											  "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryInstrumentCommissionRateField'] = CThostFtdcQryInstrumentCommissionRateField


#查询合约交易权限
CThostFtdcQryInstrumentTradingRightField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
											"ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryInstrumentTradingRightField'] = CThostFtdcQryInstrumentTradingRightField


#查询经纪公司
CThostFtdcQryBrokerField = {"BrokerID": "string"}
#经纪公司代码
structDict['CThostFtdcQryBrokerField'] = CThostFtdcQryBrokerField


#查询交易员
CThostFtdcQryTraderField = {"ExchangeID": "string", "ParticipantID": "string", "TraderID": "string"}
#交易所代码
#会员代码
#交易所交易员代码
structDict['CThostFtdcQryTraderField'] = CThostFtdcQryTraderField


#查询管理用户功能权限
CThostFtdcQrySuperUserFunctionField = {"UserID": "string"}
#用户代码
structDict['CThostFtdcQrySuperUserFunctionField'] = CThostFtdcQrySuperUserFunctionField


#查询用户会话
CThostFtdcQryUserSessionField = {"FrontID": "int", "SessionID": "int", "BrokerID": "string", "UserID": "string"}
#前置编号
#会话编号
#经纪公司代码
#用户代码
structDict['CThostFtdcQryUserSessionField'] = CThostFtdcQryUserSessionField


#查询经纪公司会员代码
CThostFtdcQryPartBrokerField = {"ExchangeID": "string", "BrokerID": "string", "ParticipantID": "string"}
#交易所代码
#经纪公司代码
#会员代码
structDict['CThostFtdcQryPartBrokerField'] = CThostFtdcQryPartBrokerField


#查询前置状态
CThostFtdcQryFrontStatusField = {"FrontID": "int"}
#前置编号
structDict['CThostFtdcQryFrontStatusField'] = CThostFtdcQryFrontStatusField


#查询交易所报单
CThostFtdcQryExchangeOrderField = {"ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string",
								   "ExchangeID": "string", "TraderID": "string"}
#会员代码
#客户代码
#合约在交易所的代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeOrderField'] = CThostFtdcQryExchangeOrderField


#查询报单操作
CThostFtdcQryOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CThostFtdcQryOrderActionField'] = CThostFtdcQryOrderActionField


#查询交易所报单操作
CThostFtdcQryExchangeOrderActionField = {"ParticipantID": "string", "ClientID": "string", "ExchangeID": "string",
										 "TraderID": "string"}
#会员代码
#客户代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeOrderActionField'] = CThostFtdcQryExchangeOrderActionField


#查询管理用户
CThostFtdcQrySuperUserField = {"UserID": "string"}
#用户代码
structDict['CThostFtdcQrySuperUserField'] = CThostFtdcQrySuperUserField


#查询交易所
CThostFtdcQryExchangeField = {"ExchangeID": "string"}
#交易所代码
structDict['CThostFtdcQryExchangeField'] = CThostFtdcQryExchangeField


#查询产品
CThostFtdcQryProductField = {"ProductID": "string", "ProductClass": "char", "ExchangeID": "string"}
#产品代码
#产品类型
#交易所代码
structDict['CThostFtdcQryProductField'] = CThostFtdcQryProductField


#查询合约
CThostFtdcQryInstrumentField = {"InstrumentID": "string", "ExchangeID": "string", "ExchangeInstID": "string",
								"ProductID": "string"}
#合约代码
#交易所代码
#合约在交易所的代码
#产品代码
structDict['CThostFtdcQryInstrumentField'] = CThostFtdcQryInstrumentField


#查询行情
CThostFtdcQryDepthMarketDataField = {"InstrumentID": "string", "ExchangeID": "string"}
#合约代码
#交易所代码
structDict['CThostFtdcQryDepthMarketDataField'] = CThostFtdcQryDepthMarketDataField


#查询经纪公司用户
CThostFtdcQryBrokerUserField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CThostFtdcQryBrokerUserField'] = CThostFtdcQryBrokerUserField


#查询经纪公司用户权限
CThostFtdcQryBrokerUserFunctionField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CThostFtdcQryBrokerUserFunctionField'] = CThostFtdcQryBrokerUserFunctionField


#查询交易员报盘机
CThostFtdcQryTraderOfferField = {"ExchangeID": "string", "ParticipantID": "string", "TraderID": "string"}
#交易所代码
#会员代码
#交易所交易员代码
structDict['CThostFtdcQryTraderOfferField'] = CThostFtdcQryTraderOfferField


#查询出入金流水
CThostFtdcQrySyncDepositField = {"BrokerID": "string", "DepositSeqNo": "string"}
#经纪公司代码
#出入金流水号
structDict['CThostFtdcQrySyncDepositField'] = CThostFtdcQrySyncDepositField


#查询投资者结算结果
CThostFtdcQrySettlementInfoField = {"BrokerID": "string", "InvestorID": "string", "TradingDay": "string"}
#经纪公司代码
#投资者代码
#交易日
structDict['CThostFtdcQrySettlementInfoField'] = CThostFtdcQrySettlementInfoField


#查询交易所保证金率
CThostFtdcQryExchangeMarginRateField = {"BrokerID": "string", "InstrumentID": "string", "HedgeFlag": "char"}
#经纪公司代码
#合约代码
#投机套保标志
structDict['CThostFtdcQryExchangeMarginRateField'] = CThostFtdcQryExchangeMarginRateField


#查询交易所调整保证金率
CThostFtdcQryExchangeMarginRateAdjustField = {"BrokerID": "string", "InstrumentID": "string", "HedgeFlag": "char"}
#经纪公司代码
#合约代码
#投机套保标志
structDict['CThostFtdcQryExchangeMarginRateAdjustField'] = CThostFtdcQryExchangeMarginRateAdjustField


#查询汇率
CThostFtdcQryExchangeRateField = {"BrokerID": "string", "FromCurrencyID": "string", "ToCurrencyID": "string"}
#经纪公司代码
#源币种
#目标币种
structDict['CThostFtdcQryExchangeRateField'] = CThostFtdcQryExchangeRateField


#查询货币质押流水
CThostFtdcQrySyncFundMortgageField = {"BrokerID": "string", "MortgageSeqNo": "string"}
#经纪公司代码
#货币质押流水号
structDict['CThostFtdcQrySyncFundMortgageField'] = CThostFtdcQrySyncFundMortgageField


#查询报单
CThostFtdcQryHisOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							  "ExchangeID": "string", "OrderSysID": "string", "InsertTimeStart": "string",
							  "InsertTimeEnd": "string", "TradingDay": "string", "SettlementID": "int"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#报单编号
#开始时间
#结束时间
#交易日
#结算编号
structDict['CThostFtdcQryHisOrderField'] = CThostFtdcQryHisOrderField


#当前期权合约最小保证金
CThostFtdcOptionInstrMiniMarginField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
										"InvestorID": "string", "MinMargin": "float", "ValueMethod": "char",
										"IsRelative": "int", "ExchangeID": "string"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#单位（手）期权合约最小保证金
#取值方式
#是否跟随交易所收取
#交易所代码
structDict['CThostFtdcOptionInstrMiniMarginField'] = CThostFtdcOptionInstrMiniMarginField


#当前期权合约保证金调整系数
CThostFtdcOptionInstrMarginAdjustField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
										  "InvestorID": "string", "SShortMarginRatioByMoney": "float",
										  "SShortMarginRatioByVolume": "float", "HShortMarginRatioByMoney": "float",
										  "HShortMarginRatioByVolume": "float", "AShortMarginRatioByMoney": "float",
										  "AShortMarginRatioByVolume": "float", "IsRelative": "int",
										  "ExchangeID": "string"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#投机空头保证金调整系数
#投机空头保证金调整系数
#保值空头保证金调整系数
#保值空头保证金调整系数
#套利空头保证金调整系数
#套利空头保证金调整系数
#是否跟随交易所收取
#交易所代码
structDict['CThostFtdcOptionInstrMarginAdjustField'] = CThostFtdcOptionInstrMarginAdjustField


#当前期权合约手续费的详细内容
CThostFtdcOptionInstrCommRateField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
									  "InvestorID": "string", "OpenRatioByMoney": "float", "OpenRatioByVolume": "float",
									  "CloseRatioByMoney": "float", "CloseRatioByVolume": "float",
									  "CloseTodayRatioByMoney": "float", "CloseTodayRatioByVolume": "float",
									  "StrikeRatioByMoney": "float", "StrikeRatioByVolume": "float",
									  "ExchangeID": "string"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#开仓手续费率
#开仓手续费
#平仓手续费率
#平仓手续费
#平今手续费率
#平今手续费
#执行手续费率
#执行手续费
#交易所代码
structDict['CThostFtdcOptionInstrCommRateField'] = CThostFtdcOptionInstrCommRateField


#期权交易成本
CThostFtdcOptionInstrTradeCostField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
									   "HedgeFlag": "char", "FixedMargin": "float", "MiniMargin": "float",
									   "Royalty": "float", "ExchFixedMargin": "float", "ExchMiniMargin": "float",
									   "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#投机套保标志
#期权合约保证金不变部分
#期权合约最小保证金
#期权合约权利金
#交易所期权合约保证金不变部分
#交易所期权合约最小保证金
#交易所代码
structDict['CThostFtdcOptionInstrTradeCostField'] = CThostFtdcOptionInstrTradeCostField


#期权交易成本查询
CThostFtdcQryOptionInstrTradeCostField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
										  "HedgeFlag": "char", "InputPrice": "float", "UnderlyingPrice": "float",
										  "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#投机套保标志
#期权合约报价
#标的价格,填0则用昨结算价
#交易所代码
structDict['CThostFtdcQryOptionInstrTradeCostField'] = CThostFtdcQryOptionInstrTradeCostField


#期权手续费率查询
CThostFtdcQryOptionInstrCommRateField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
										 "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryOptionInstrCommRateField'] = CThostFtdcQryOptionInstrCommRateField


#股指现货指数
CThostFtdcIndexPriceField = {"BrokerID": "string", "InstrumentID": "string", "ClosePrice": "float",
							 "ExchangeID": "string"}
#经纪公司代码
#合约代码
#指数现货收盘价
#交易所代码
structDict['CThostFtdcIndexPriceField'] = CThostFtdcIndexPriceField


#输入的执行宣告
CThostFtdcInputExecOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								 "ExecOrderRef": "string", "UserID": "string", "Volume": "int", "RequestID": "int",
								 "BusinessUnit": "string", "OffsetFlag": "char", "HedgeFlag": "char",
								 "ActionType": "char", "PosiDirection": "char", "ReservePositionFlag": "char",
								 "CloseFlag": "char", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#执行宣告引用
#用户代码
#数量
#请求编号
#业务单元
#开平标志
#投机套保标志
#执行类型
#保留头寸申请的持仓方向
#期权行权后是否保留期货头寸的标记
#期权行权后生成的头寸是否自动平仓
#交易所代码
structDict['CThostFtdcInputExecOrderField'] = CThostFtdcInputExecOrderField


#输入执行宣告操作
CThostFtdcInputExecOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ExecOrderActionRef": "int",
									   "ExecOrderRef": "string", "RequestID": "int", "FrontID": "int",
									   "SessionID": "int", "ExchangeID": "string", "ExecOrderSysID": "string",
									   "ActionFlag": "char", "UserID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#执行宣告操作引用
#执行宣告引用
#请求编号
#前置编号
#会话编号
#交易所代码
#执行宣告操作编号
#操作标志
#用户代码
#合约代码
structDict['CThostFtdcInputExecOrderActionField'] = CThostFtdcInputExecOrderActionField


#执行宣告
CThostFtdcExecOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							"ExecOrderRef": "string", "UserID": "string", "Volume": "int", "RequestID": "int",
							"BusinessUnit": "string", "OffsetFlag": "char", "HedgeFlag": "char", "ActionType": "char",
							"PosiDirection": "char", "ReservePositionFlag": "char", "CloseFlag": "char",
							"ExecOrderLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
							"ClientID": "string", "ExchangeInstID": "string", "TraderID": "string", "InstallID": "int",
							"OrderSubmitStatus": "char", "NotifySequence": "int", "TradingDay": "string",
							"SettlementID": "int", "ExecOrderSysID": "string", "InsertDate": "string",
							"InsertTime": "string", "CancelTime": "string", "ExecResult": "char",
							"ClearingPartID": "string", "SequenceNo": "int", "FrontID": "int", "SessionID": "int",
							"UserProductInfo": "string", "StatusMsg": "string", "ActiveUserID": "string",
							"BrokerExecOrderSeq": "int", "BranchID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#执行宣告引用
#用户代码
#数量
#请求编号
#业务单元
#开平标志
#投机套保标志
#执行类型
#保留头寸申请的持仓方向
#期权行权后是否保留期货头寸的标记
#期权行权后生成的头寸是否自动平仓
#本地执行宣告编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#执行宣告提交状态
#报单提示序号
#交易日
#结算编号
#执行宣告编号
#报单日期
#插入时间
#撤销时间
#执行结果
#结算会员编号
#序号
#前置编号
#会话编号
#用户端产品信息
#状态信息
#操作用户代码
#经纪公司报单编号
#营业部编号
structDict['CThostFtdcExecOrderField'] = CThostFtdcExecOrderField


#执行宣告操作
CThostFtdcExecOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ExecOrderActionRef": "int",
								  "ExecOrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
								  "ExchangeID": "string", "ExecOrderSysID": "string", "ActionFlag": "char",
								  "ActionDate": "string", "ActionTime": "string", "TraderID": "string",
								  "InstallID": "int", "ExecOrderLocalID": "string", "ActionLocalID": "string",
								  "ParticipantID": "string", "ClientID": "string", "BusinessUnit": "string",
								  "OrderActionStatus": "char", "UserID": "string", "ActionType": "char",
								  "StatusMsg": "string", "InstrumentID": "string", "BranchID": "string"}
#经纪公司代码
#投资者代码
#执行宣告操作引用
#执行宣告引用
#请求编号
#前置编号
#会话编号
#交易所代码
#执行宣告操作编号
#操作标志
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#本地执行宣告编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
#执行类型
#状态信息
#合约代码
#营业部编号
structDict['CThostFtdcExecOrderActionField'] = CThostFtdcExecOrderActionField


#执行宣告查询
CThostFtdcQryExecOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							   "ExchangeID": "string", "ExecOrderSysID": "string", "InsertTimeStart": "string",
							   "InsertTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#执行宣告编号
#开始时间
#结束时间
structDict['CThostFtdcQryExecOrderField'] = CThostFtdcQryExecOrderField


#交易所执行宣告信息
CThostFtdcExchangeExecOrderField = {"Volume": "int", "RequestID": "int", "BusinessUnit": "string", "OffsetFlag": "char",
									"HedgeFlag": "char", "ActionType": "char", "PosiDirection": "char",
									"ReservePositionFlag": "char", "CloseFlag": "char", "ExecOrderLocalID": "string",
									"ExchangeID": "string", "ParticipantID": "string", "ClientID": "string",
									"ExchangeInstID": "string", "TraderID": "string", "InstallID": "int",
									"OrderSubmitStatus": "char", "NotifySequence": "int", "TradingDay": "string",
									"SettlementID": "int", "ExecOrderSysID": "string", "InsertDate": "string",
									"InsertTime": "string", "CancelTime": "string", "ExecResult": "char",
									"ClearingPartID": "string", "SequenceNo": "int", "BranchID": "string"}
#数量
#请求编号
#业务单元
#开平标志
#投机套保标志
#执行类型
#保留头寸申请的持仓方向
#期权行权后是否保留期货头寸的标记
#期权行权后生成的头寸是否自动平仓
#本地执行宣告编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#执行宣告提交状态
#报单提示序号
#交易日
#结算编号
#执行宣告编号
#报单日期
#插入时间
#撤销时间
#执行结果
#结算会员编号
#序号
#营业部编号
structDict['CThostFtdcExchangeExecOrderField'] = CThostFtdcExchangeExecOrderField


#交易所执行宣告查询
CThostFtdcQryExchangeExecOrderField = {"ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string",
									   "ExchangeID": "string", "TraderID": "string"}
#会员代码
#客户代码
#合约在交易所的代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeExecOrderField'] = CThostFtdcQryExchangeExecOrderField


#执行宣告操作查询
CThostFtdcQryExecOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CThostFtdcQryExecOrderActionField'] = CThostFtdcQryExecOrderActionField


#交易所执行宣告操作
CThostFtdcExchangeExecOrderActionField = {"ExchangeID": "string", "ExecOrderSysID": "string", "ActionFlag": "char",
										  "ActionDate": "string", "ActionTime": "string", "TraderID": "string",
										  "InstallID": "int", "ExecOrderLocalID": "string", "ActionLocalID": "string",
										  "ParticipantID": "string", "ClientID": "string", "BusinessUnit": "string",
										  "OrderActionStatus": "char", "UserID": "string", "ActionType": "char",
										  "BranchID": "string"}
#交易所代码
#执行宣告操作编号
#操作标志
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#本地执行宣告编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
#执行类型
#营业部编号
structDict['CThostFtdcExchangeExecOrderActionField'] = CThostFtdcExchangeExecOrderActionField


#交易所执行宣告操作查询
CThostFtdcQryExchangeExecOrderActionField = {"ParticipantID": "string", "ClientID": "string", "ExchangeID": "string",
											 "TraderID": "string"}
#会员代码
#客户代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeExecOrderActionField'] = CThostFtdcQryExchangeExecOrderActionField


#错误执行宣告
CThostFtdcErrExecOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							   "ExecOrderRef": "string", "UserID": "string", "Volume": "int", "RequestID": "int",
							   "BusinessUnit": "string", "OffsetFlag": "char", "HedgeFlag": "char",
							   "ActionType": "char", "PosiDirection": "char", "ReservePositionFlag": "char",
							   "CloseFlag": "char", "ExchangeID": "string", "ErrorID": "int", "ErrorMsg": "string"}
#经纪公司代码
#投资者代码
#合约代码
#执行宣告引用
#用户代码
#数量
#请求编号
#业务单元
#开平标志
#投机套保标志
#执行类型
#保留头寸申请的持仓方向
#期权行权后是否保留期货头寸的标记
#期权行权后生成的头寸是否自动平仓
#交易所代码
#错误代码
#错误信息
structDict['CThostFtdcErrExecOrderField'] = CThostFtdcErrExecOrderField


#查询错误执行宣告
CThostFtdcQryErrExecOrderField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQryErrExecOrderField'] = CThostFtdcQryErrExecOrderField


#错误执行宣告操作
CThostFtdcErrExecOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ExecOrderActionRef": "int",
									 "ExecOrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
									 "ExchangeID": "string", "ExecOrderSysID": "string", "ActionFlag": "char",
									 "UserID": "string", "InstrumentID": "string", "ErrorID": "int",
									 "ErrorMsg": "string"}
#经纪公司代码
#投资者代码
#执行宣告操作引用
#执行宣告引用
#请求编号
#前置编号
#会话编号
#交易所代码
#执行宣告操作编号
#操作标志
#用户代码
#合约代码
#错误代码
#错误信息
structDict['CThostFtdcErrExecOrderActionField'] = CThostFtdcErrExecOrderActionField


#查询错误执行宣告操作
CThostFtdcQryErrExecOrderActionField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQryErrExecOrderActionField'] = CThostFtdcQryErrExecOrderActionField


#投资者期权合约交易权限
CThostFtdcOptionInstrTradingRightField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
										  "InvestorID": "string", "Direction": "char", "TradingRight": "char",
										  "ExchangeID": "string", "HedgeFlag": "char"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#买卖方向
#交易权限
#交易所代码
#投机套保标志
structDict['CThostFtdcOptionInstrTradingRightField'] = CThostFtdcOptionInstrTradingRightField


#查询期权合约交易权限
CThostFtdcQryOptionInstrTradingRightField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
											 "Direction": "char", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#买卖方向
#交易所代码
structDict['CThostFtdcQryOptionInstrTradingRightField'] = CThostFtdcQryOptionInstrTradingRightField


#输入的询价
CThostFtdcInputForQuoteField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								"ForQuoteRef": "string", "UserID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#询价引用
#用户代码
#交易所代码
structDict['CThostFtdcInputForQuoteField'] = CThostFtdcInputForQuoteField


#询价
CThostFtdcForQuoteField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						   "ForQuoteRef": "string", "UserID": "string", "ForQuoteLocalID": "string",
						   "ExchangeID": "string", "ParticipantID": "string", "ClientID": "string",
						   "ExchangeInstID": "string", "TraderID": "string", "InstallID": "int", "InsertDate": "string",
						   "InsertTime": "string", "ForQuoteStatus": "char", "FrontID": "int", "SessionID": "int",
						   "StatusMsg": "string", "ActiveUserID": "string", "BrokerForQutoSeq": "int"}
#经纪公司代码
#投资者代码
#合约代码
#询价引用
#用户代码
#本地询价编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#报单日期
#插入时间
#询价状态
#前置编号
#会话编号
#状态信息
#操作用户代码
#经纪公司询价编号
structDict['CThostFtdcForQuoteField'] = CThostFtdcForQuoteField


#询价查询
CThostFtdcQryForQuoteField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							  "ExchangeID": "string", "InsertTimeStart": "string", "InsertTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#开始时间
#结束时间
structDict['CThostFtdcQryForQuoteField'] = CThostFtdcQryForQuoteField


#交易所询价信息
CThostFtdcExchangeForQuoteField = {"ForQuoteLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
								   "ClientID": "string", "ExchangeInstID": "string", "TraderID": "string",
								   "InstallID": "int", "InsertDate": "string", "InsertTime": "string",
								   "ForQuoteStatus": "char"}
#本地询价编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#报单日期
#插入时间
#询价状态
structDict['CThostFtdcExchangeForQuoteField'] = CThostFtdcExchangeForQuoteField


#交易所询价查询
CThostFtdcQryExchangeForQuoteField = {"ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string",
									  "ExchangeID": "string", "TraderID": "string"}
#会员代码
#客户代码
#合约在交易所的代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeForQuoteField'] = CThostFtdcQryExchangeForQuoteField


#输入的报价
CThostFtdcInputQuoteField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							 "QuoteRef": "string", "UserID": "string", "AskPrice": "float", "BidPrice": "float",
							 "AskVolume": "int", "BidVolume": "int", "RequestID": "int", "BusinessUnit": "string",
							 "AskOffsetFlag": "char", "BidOffsetFlag": "char", "AskHedgeFlag": "char",
							 "BidHedgeFlag": "char", "AskOrderRef": "string", "BidOrderRef": "string",
							 "ForQuoteSysID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#报价引用
#用户代码
#卖价格
#买价格
#卖数量
#买数量
#请求编号
#业务单元
#卖开平标志
#买开平标志
#卖投机套保标志
#买投机套保标志
#衍生卖报单引用
#衍生买报单引用
#应价编号
#交易所代码
structDict['CThostFtdcInputQuoteField'] = CThostFtdcInputQuoteField


#输入报价操作
CThostFtdcInputQuoteActionField = {"BrokerID": "string", "InvestorID": "string", "QuoteActionRef": "int",
								   "QuoteRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
								   "ExchangeID": "string", "QuoteSysID": "string", "ActionFlag": "char",
								   "UserID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#报价操作引用
#报价引用
#请求编号
#前置编号
#会话编号
#交易所代码
#报价操作编号
#操作标志
#用户代码
#合约代码
structDict['CThostFtdcInputQuoteActionField'] = CThostFtdcInputQuoteActionField


#报价
CThostFtdcQuoteField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "QuoteRef": "string",
						"UserID": "string", "AskPrice": "float", "BidPrice": "float", "AskVolume": "int",
						"BidVolume": "int", "RequestID": "int", "BusinessUnit": "string", "AskOffsetFlag": "char",
						"BidOffsetFlag": "char", "AskHedgeFlag": "char", "BidHedgeFlag": "char",
						"QuoteLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
						"ClientID": "string", "ExchangeInstID": "string", "TraderID": "string", "InstallID": "int",
						"NotifySequence": "int", "OrderSubmitStatus": "char", "TradingDay": "string",
						"SettlementID": "int", "QuoteSysID": "string", "InsertDate": "string", "InsertTime": "string",
						"CancelTime": "string", "QuoteStatus": "char", "ClearingPartID": "string", "SequenceNo": "int",
						"AskOrderSysID": "string", "BidOrderSysID": "string", "FrontID": "int", "SessionID": "int",
						"UserProductInfo": "string", "StatusMsg": "string", "ActiveUserID": "string",
						"BrokerQuoteSeq": "int", "AskOrderRef": "string", "BidOrderRef": "string",
						"ForQuoteSysID": "string", "BranchID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#报价引用
#用户代码
#卖价格
#买价格
#卖数量
#买数量
#请求编号
#业务单元
#卖开平标志
#买开平标志
#卖投机套保标志
#买投机套保标志
#本地报价编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#报价提示序号
#报价提交状态
#交易日
#结算编号
#报价编号
#报单日期
#插入时间
#撤销时间
#报价状态
#结算会员编号
#序号
#卖方报单编号
#买方报单编号
#前置编号
#会话编号
#用户端产品信息
#状态信息
#操作用户代码
#经纪公司报价编号
#衍生卖报单引用
#衍生买报单引用
#应价编号
#营业部编号
structDict['CThostFtdcQuoteField'] = CThostFtdcQuoteField


#报价操作
CThostFtdcQuoteActionField = {"BrokerID": "string", "InvestorID": "string", "QuoteActionRef": "int",
							  "QuoteRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
							  "ExchangeID": "string", "QuoteSysID": "string", "ActionFlag": "char",
							  "ActionDate": "string", "ActionTime": "string", "TraderID": "string", "InstallID": "int",
							  "QuoteLocalID": "string", "ActionLocalID": "string", "ParticipantID": "string",
							  "ClientID": "string", "BusinessUnit": "string", "OrderActionStatus": "char",
							  "UserID": "string", "StatusMsg": "string", "InstrumentID": "string", "BranchID": "string"}
#经纪公司代码
#投资者代码
#报价操作引用
#报价引用
#请求编号
#前置编号
#会话编号
#交易所代码
#报价操作编号
#操作标志
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#本地报价编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
#状态信息
#合约代码
#营业部编号
structDict['CThostFtdcQuoteActionField'] = CThostFtdcQuoteActionField


#报价查询
CThostFtdcQryQuoteField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						   "ExchangeID": "string", "QuoteSysID": "string", "InsertTimeStart": "string",
						   "InsertTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#报价编号
#开始时间
#结束时间
structDict['CThostFtdcQryQuoteField'] = CThostFtdcQryQuoteField


#交易所报价信息
CThostFtdcExchangeQuoteField = {"AskPrice": "float", "BidPrice": "float", "AskVolume": "int", "BidVolume": "int",
								"RequestID": "int", "BusinessUnit": "string", "AskOffsetFlag": "char",
								"BidOffsetFlag": "char", "AskHedgeFlag": "char", "BidHedgeFlag": "char",
								"QuoteLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
								"ClientID": "string", "ExchangeInstID": "string", "TraderID": "string",
								"InstallID": "int", "NotifySequence": "int", "OrderSubmitStatus": "char",
								"TradingDay": "string", "SettlementID": "int", "QuoteSysID": "string",
								"InsertDate": "string", "InsertTime": "string", "CancelTime": "string",
								"QuoteStatus": "char", "ClearingPartID": "string", "SequenceNo": "int",
								"AskOrderSysID": "string", "BidOrderSysID": "string", "ForQuoteSysID": "string",
								"BranchID": "string"}
#卖价格
#买价格
#卖数量
#买数量
#请求编号
#业务单元
#卖开平标志
#买开平标志
#卖投机套保标志
#买投机套保标志
#本地报价编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#报价提示序号
#报价提交状态
#交易日
#结算编号
#报价编号
#报单日期
#插入时间
#撤销时间
#报价状态
#结算会员编号
#序号
#卖方报单编号
#买方报单编号
#应价编号
#营业部编号
structDict['CThostFtdcExchangeQuoteField'] = CThostFtdcExchangeQuoteField


#交易所报价查询
CThostFtdcQryExchangeQuoteField = {"ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string",
								   "ExchangeID": "string", "TraderID": "string"}
#会员代码
#客户代码
#合约在交易所的代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeQuoteField'] = CThostFtdcQryExchangeQuoteField


#报价操作查询
CThostFtdcQryQuoteActionField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CThostFtdcQryQuoteActionField'] = CThostFtdcQryQuoteActionField


#交易所报价操作
CThostFtdcExchangeQuoteActionField = {"ExchangeID": "string", "QuoteSysID": "string", "ActionFlag": "char",
									  "ActionDate": "string", "ActionTime": "string", "TraderID": "string",
									  "InstallID": "int", "QuoteLocalID": "string", "ActionLocalID": "string",
									  "ParticipantID": "string", "ClientID": "string", "BusinessUnit": "string",
									  "OrderActionStatus": "char", "UserID": "string"}
#交易所代码
#报价操作编号
#操作标志
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#本地报价编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
structDict['CThostFtdcExchangeQuoteActionField'] = CThostFtdcExchangeQuoteActionField


#交易所报价操作查询
CThostFtdcQryExchangeQuoteActionField = {"ParticipantID": "string", "ClientID": "string", "ExchangeID": "string",
										 "TraderID": "string"}
#会员代码
#客户代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeQuoteActionField'] = CThostFtdcQryExchangeQuoteActionField


#期权合约delta值
CThostFtdcOptionInstrDeltaField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
								   "InvestorID": "string", "Delta": "float", "ExchangeID": "string"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#Delta值
#交易所代码
structDict['CThostFtdcOptionInstrDeltaField'] = CThostFtdcOptionInstrDeltaField


#发给做市商的询价请求
CThostFtdcForQuoteRspField = {"TradingDay": "string", "InstrumentID": "string", "ForQuoteSysID": "string",
							  "ForQuoteTime": "string", "ActionDay": "string", "ExchangeID": "string"}
#交易日
#合约代码
#询价编号
#询价时间
#业务日期
#交易所代码
structDict['CThostFtdcForQuoteRspField'] = CThostFtdcForQuoteRspField


#当前期权合约执行偏移值的详细内容
CThostFtdcStrikeOffsetField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
							   "InvestorID": "string", "Offset": "float", "ExchangeID": "string"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#执行偏移值
#交易所代码
structDict['CThostFtdcStrikeOffsetField'] = CThostFtdcStrikeOffsetField


#期权执行偏移值查询
CThostFtdcQryStrikeOffsetField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#合约代码
structDict['CThostFtdcQryStrikeOffsetField'] = CThostFtdcQryStrikeOffsetField


#录入锁定
CThostFtdcInputLockField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "LockRef": "string",
							"UserID": "string", "Volume": "int", "RequestID": "int", "BusinessUnit": "string",
							"LockType": "char", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#锁定引用
#用户代码
#数量
#请求编号
#业务单元
#锁定类型
#交易所代码
structDict['CThostFtdcInputLockField'] = CThostFtdcInputLockField


#锁定
CThostFtdcLockField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "LockRef": "string",
					   "UserID": "string", "Volume": "int", "RequestID": "int", "BusinessUnit": "string",
					   "LockType": "char", "LockLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
					   "ClientID": "string", "ExchangeInstID": "string", "TraderID": "string", "InstallID": "int",
					   "OrderSubmitStatus": "char", "NotifySequence": "int", "TradingDay": "string",
					   "SettlementID": "int", "LockSysID": "string", "InsertDate": "string", "InsertTime": "string",
					   "CancelTime": "string", "LockStatus": "char", "ClearingPartID": "string", "SequenceNo": "int",
					   "FrontID": "int", "SessionID": "int", "UserProductInfo": "string", "StatusMsg": "string",
					   "ActiveUserID": "string", "BrokerLockSeq": "int", "BranchID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#锁定引用
#用户代码
#数量
#请求编号
#业务单元
#锁定类型
#本地锁定编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#执行宣告提交状态
#报单提示序号
#交易日
#结算编号
#锁定编号
#报单日期
#插入时间
#撤销时间
#锁定状态
#结算会员编号
#序号
#前置编号
#会话编号
#用户端产品信息
#状态信息
#操作用户代码
#经纪公司报单编号
#营业部编号
structDict['CThostFtdcLockField'] = CThostFtdcLockField


#查询锁定
CThostFtdcQryLockField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						  "ExchangeID": "string", "LockSysID": "string", "InsertTimeStart": "string",
						  "InsertTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#锁定编号
#开始时间
#结束时间
structDict['CThostFtdcQryLockField'] = CThostFtdcQryLockField


#锁定证券仓位
CThostFtdcLockPositionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							   "ExchangeID": "string", "Volume": "int", "FrozenVolume": "int"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#数量
#冻结数量
structDict['CThostFtdcLockPositionField'] = CThostFtdcLockPositionField


#查询锁定证券仓位
CThostFtdcQryLockPositionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								  "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryLockPositionField'] = CThostFtdcQryLockPositionField


#当前ETF期权合约手续费的详细内容
CThostFtdcETFOptionInstrCommRateField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
										 "InvestorID": "string", "OpenRatioByMoney": "float",
										 "OpenRatioByVolume": "float", "CloseRatioByMoney": "float",
										 "CloseRatioByVolume": "float", "CloseTodayRatioByMoney": "float",
										 "CloseTodayRatioByVolume": "float", "StrikeRatioByMoney": "float",
										 "StrikeRatioByVolume": "float", "ExchangeID": "string", "HedgeFlag": "char",
										 "PosiDirection": "char"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#开仓手续费率
#开仓手续费
#平仓手续费率
#平仓手续费
#平今手续费率
#平今手续费
#执行手续费率
#执行手续费
#交易所代码
#投机套保标志
#持仓方向
structDict['CThostFtdcETFOptionInstrCommRateField'] = CThostFtdcETFOptionInstrCommRateField


#ETF期权手续费率查询
CThostFtdcQryETFOptionInstrCommRateField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
											"ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryETFOptionInstrCommRateField'] = CThostFtdcQryETFOptionInstrCommRateField


#输入的持仓冻结
CThostFtdcPosiFreezeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							 "ExchangeID": "string", "OrderLocalID": "string", "TraderID": "string",
							 "ParticipantID": "string", "InstallID": "int", "Volume": "int", "FreezeReasonType": "char",
							 "FreezeType": "char"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#本地报单编号
#交易所交易员代码
#会员代码
#安装编号
#数量
#冻结原因
#冻结类型
structDict['CThostFtdcPosiFreezeField'] = CThostFtdcPosiFreezeField


#查询锁定
CThostFtdcQryExchangeLockField = {"ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string",
								  "ExchangeID": "string", "TraderID": "string"}
#会员代码
#客户代码
#合约在交易所的代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeLockField'] = CThostFtdcQryExchangeLockField


#交易所锁定
CThostFtdcExchangeLockField = {"Volume": "int", "RequestID": "int", "BusinessUnit": "string", "LockType": "char",
							   "LockLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
							   "ClientID": "string", "ExchangeInstID": "string", "TraderID": "string",
							   "InstallID": "int", "OrderSubmitStatus": "char", "NotifySequence": "int",
							   "TradingDay": "string", "SettlementID": "int", "LockSysID": "string",
							   "InsertDate": "string", "InsertTime": "string", "CancelTime": "string",
							   "LockStatus": "char", "ClearingPartID": "string", "SequenceNo": "int",
							   "BranchID": "string"}
#数量
#请求编号
#业务单元
#锁定类型
#本地锁定编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#执行宣告提交状态
#报单提示序号
#交易日
#结算编号
#锁定编号
#报单日期
#插入时间
#撤销时间
#锁定状态
#结算会员编号
#序号
#营业部编号
structDict['CThostFtdcExchangeLockField'] = CThostFtdcExchangeLockField


#交易所操作错误
CThostFtdcExchangeExecOrderActionErrorField = {"ExchangeID": "string", "ExecOrderSysID": "string", "TraderID": "string",
											   "InstallID": "int", "ExecOrderLocalID": "string",
											   "ActionLocalID": "string", "ErrorID": "int", "ErrorMsg": "string",
											   "BrokerID": "string"}
#交易所代码
#执行宣告编号
#交易所交易员代码
#安装编号
#本地执行宣告编号
#操作本地编号
#错误代码
#错误信息
#经纪公司代码
structDict['CThostFtdcExchangeExecOrderActionErrorField'] = CThostFtdcExchangeExecOrderActionErrorField


#输入批量报单操作
CThostFtdcInputBatchOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
										"RequestID": "int", "FrontID": "int", "SessionID": "int",
										"ExchangeID": "string", "UserID": "string"}
#经纪公司代码
#投资者代码
#报单操作引用
#请求编号
#前置编号
#会话编号
#交易所代码
#用户代码
structDict['CThostFtdcInputBatchOrderActionField'] = CThostFtdcInputBatchOrderActionField


#批量报单操作
CThostFtdcBatchOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
								   "RequestID": "int", "FrontID": "int", "SessionID": "int", "ExchangeID": "string",
								   "ActionDate": "string", "ActionTime": "string", "TraderID": "string",
								   "InstallID": "int", "ActionLocalID": "string", "ParticipantID": "string",
								   "ClientID": "string", "BusinessUnit": "string", "OrderActionStatus": "char",
								   "UserID": "string", "StatusMsg": "string"}
#经纪公司代码
#投资者代码
#报单操作引用
#请求编号
#前置编号
#会话编号
#交易所代码
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
#状态信息
structDict['CThostFtdcBatchOrderActionField'] = CThostFtdcBatchOrderActionField


#交易所批量报单操作
CThostFtdcExchangeBatchOrderActionField = {"ExchangeID": "string", "ActionDate": "string", "ActionTime": "string",
										   "TraderID": "string", "InstallID": "int", "ActionLocalID": "string",
										   "ParticipantID": "string", "ClientID": "string", "BusinessUnit": "string",
										   "OrderActionStatus": "char", "UserID": "string"}
#交易所代码
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
structDict['CThostFtdcExchangeBatchOrderActionField'] = CThostFtdcExchangeBatchOrderActionField


#查询批量报单操作
CThostFtdcQryBatchOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CThostFtdcQryBatchOrderActionField'] = CThostFtdcQryBatchOrderActionField


#投资者持仓限制
CThostFtdcLimitPosiField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							"ExchangeID": "string", "TotalVolume": "int", "LongVolume": "int", "OpenVolume": "int",
							"LongAmount": "float", "TotalVolumeFrozen": "int", "LongVolumeFrozen": "int",
							"OpenVolumeFrozen": "int", "LongAmountFrozen": "float"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#总数量限制
#多头数量限制
#当日多头开仓数量限制
#多头持仓金额限制
#总数量冻结
#多头数量冻结
#当日多头开仓数量冻结
#多头持仓金额冻结
structDict['CThostFtdcLimitPosiField'] = CThostFtdcLimitPosiField


#查询投资者持仓限制
CThostFtdcQryLimitPosiField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							   "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryLimitPosiField'] = CThostFtdcQryLimitPosiField


#经纪公司持仓限制
CThostFtdcBrokerLimitPosiField = {"BrokerID": "string", "InstrumentID": "string", "ExchangeID": "string",
								  "TotalVolume": "float", "LongVolume": "float", "TotalVolumeFrozen": "float",
								  "LongVolumeFrozen": "float"}
#经纪公司代码
#合约代码
#交易所代码
#总数量限制
#多头数量限制
#总数量冻结
#多头数量冻结
structDict['CThostFtdcBrokerLimitPosiField'] = CThostFtdcBrokerLimitPosiField


#查询经纪公司持仓限制
CThostFtdcQryBrokerLimitPosiField = {"BrokerID": "string", "InstrumentID": "string", "ExchangeID": "string"}
#经纪公司代码
#合约代码
#交易所代码
structDict['CThostFtdcQryBrokerLimitPosiField'] = CThostFtdcQryBrokerLimitPosiField


#投资者证券持仓限制
CThostFtdcLimitPosiSField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							 "ExchangeID": "string", "TotalVolume": "int", "OpenVolume": "int",
							 "TotalVolumeFrozen": "int", "OpenVolumeFrozen": "int"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#总数量限制
#当日开仓数量限制
#总数量冻结
#当日开仓数量冻结
structDict['CThostFtdcLimitPosiSField'] = CThostFtdcLimitPosiSField


#查询投资者证券持仓限制
CThostFtdcQryLimitPosiSField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								"ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryLimitPosiSField'] = CThostFtdcQryLimitPosiSField


#投资者持仓限制参数
CThostFtdcLimitPosiParamField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
								 "InvestorID": "string", "ExchangeID": "string", "TotalVolume": "int",
								 "LongVolume": "int", "OpenVolume": "int", "LongAmount": "float"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#交易所代码
#总数量限制
#多头数量限制
#当日多头开仓数量限制
#多头持仓金额限制
structDict['CThostFtdcLimitPosiParamField'] = CThostFtdcLimitPosiParamField


#经纪公司持仓限制参数
CThostFtdcBrokerLimitPosiParamField = {"BrokerID": "string", "InstrumentID": "string", "ExchangeID": "string",
									   "TotalVolume": "float", "LongVolume": "float"}
#经纪公司代码
#合约代码
#交易所代码
#总数量限制
#多头数量限制
structDict['CThostFtdcBrokerLimitPosiParamField'] = CThostFtdcBrokerLimitPosiParamField


#投资者证券持仓限制参数
CThostFtdcLimitPosiParamSField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
								  "InvestorID": "string", "ExchangeID": "string", "TotalVolume": "int",
								  "OpenVolume": "int"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#交易所代码
#总数量限制
#当日开仓数量限制
structDict['CThostFtdcLimitPosiParamSField'] = CThostFtdcLimitPosiParamSField


#输入证券处置操作
CThostFtdcInputStockDisposalActionField = {"BrokerID": "string", "InvestorID": "string",
										   "StockDisposalActionRef": "int", "StockDisposalRef": "string",
										   "RequestID": "int", "FrontID": "int", "SessionID": "int",
										   "ExchangeID": "string", "StockDisposalSysID": "string", "ActionFlag": "char",
										   "UserID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#证券处置操作引用
#证券处置引用
#请求编号
#前置编号
#会话编号
#交易所代码
#证券处置操作编号
#操作标志
#用户代码
#合约代码
structDict['CThostFtdcInputStockDisposalActionField'] = CThostFtdcInputStockDisposalActionField


#证券处置操作
CThostFtdcStockDisposalActionField = {"BrokerID": "string", "InvestorID": "string", "StockDisposalActionRef": "int",
									  "StockDisposalRef": "string", "RequestID": "int", "FrontID": "int",
									  "SessionID": "int", "ExchangeID": "string", "StockDisposalSysID": "string",
									  "ActionFlag": "char", "ActionDate": "string", "ActionTime": "string",
									  "TraderID": "string", "InstallID": "int", "StockDisposalLocalID": "string",
									  "ActionLocalID": "string", "ParticipantID": "string", "ClientID": "string",
									  "BusinessUnit": "string", "OrderActionStatus": "char", "UserID": "string",
									  "ActionType": "char", "StatusMsg": "string", "InstrumentID": "string",
									  "BranchID": "string"}
#经纪公司代码
#投资者代码
#证券处置操作引用
#证券处置引用
#请求编号
#前置编号
#会话编号
#交易所代码
#证券处置操作编号
#操作标志
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#本地证券处置编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
#执行类型
#状态信息
#合约代码
#营业部编号
structDict['CThostFtdcStockDisposalActionField'] = CThostFtdcStockDisposalActionField


#证券处置操作查询
CThostFtdcQryStockDisposalActionField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CThostFtdcQryStockDisposalActionField'] = CThostFtdcQryStockDisposalActionField


#交易所证券处置操作
CThostFtdcExchangeStockDisposalActionField = {"ExchangeID": "string", "StockDisposalSysID": "string",
											  "ActionFlag": "char", "ActionDate": "string", "ActionTime": "string",
											  "TraderID": "string", "InstallID": "int",
											  "StockDisposalLocalID": "string", "ActionLocalID": "string",
											  "ParticipantID": "string", "ClientID": "string", "BusinessUnit": "string",
											  "OrderActionStatus": "char", "UserID": "string", "ActionType": "char",
											  "BranchID": "string"}
#交易所代码
#证券处置操作编号
#操作标志
#操作日期
#操作时间
#交易所交易员代码
#安装编号
#本地证券处置编号
#操作本地编号
#会员代码
#客户代码
#业务单元
#报单操作状态
#用户代码
#执行类型
#营业部编号
structDict['CThostFtdcExchangeStockDisposalActionField'] = CThostFtdcExchangeStockDisposalActionField


#错误证券处置操作
CThostFtdcQryExchangeStockDisposalActionField = {"ParticipantID": "string", "ClientID": "string",
												 "ExchangeID": "string", "TraderID": "string"}
#会员代码
#客户代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeStockDisposalActionField'] = CThostFtdcQryExchangeStockDisposalActionField


#查询错误证券处置操作
CThostFtdcQryErrStockDisposalActionField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQryErrStockDisposalActionField'] = CThostFtdcQryErrStockDisposalActionField


#交易所证券处置操作错误
CThostFtdcExchangeStockDisposalActionErrorField = {"ExchangeID": "string", "StockDisposalSysID": "string",
												   "TraderID": "string", "InstallID": "int",
												   "StockDisposalLocalID": "string", "ActionLocalID": "string",
												   "ErrorID": "int", "ErrorMsg": "string", "BrokerID": "string"}
#交易所代码
#证券处置编号
#交易所交易员代码
#安装编号
#本地证券处置编号
#操作本地编号
#错误代码
#错误信息
#经纪公司代码
structDict['CThostFtdcExchangeStockDisposalActionErrorField'] = CThostFtdcExchangeStockDisposalActionErrorField


#错误证券处置操作
CThostFtdcErrStockDisposalActionField = {"BrokerID": "string", "InvestorID": "string", "StockDisposalActionRef": "int",
										 "StockDisposalRef": "string", "RequestID": "int", "FrontID": "int",
										 "SessionID": "int", "ExchangeID": "string", "StockDisposalSysID": "string",
										 "ActionFlag": "char", "UserID": "string", "InstrumentID": "string",
										 "ErrorID": "int", "ErrorMsg": "string"}
#经纪公司代码
#投资者代码
#证券处置操作引用
#证券处置引用
#请求编号
#前置编号
#会话编号
#交易所代码
#证券处置操作编号
#操作标志
#用户代码
#合约代码
#错误代码
#错误信息
structDict['CThostFtdcErrStockDisposalActionField'] = CThostFtdcErrStockDisposalActionField


#投资者分级
CThostFtdcInvestorLevelField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
								"LevelType": "char"}
#经纪公司代码
#投资者代码
#交易所代码
#投资者分级类型
structDict['CThostFtdcInvestorLevelField'] = CThostFtdcInvestorLevelField


#组合合约安全系数
CThostFtdcCombInstrumentGuardField = {"BrokerID": "string", "InstrumentID": "string", "GuarantRatio": "float"}
#经纪公司代码
#合约代码
#
structDict['CThostFtdcCombInstrumentGuardField'] = CThostFtdcCombInstrumentGuardField


#组合合约安全系数查询
CThostFtdcQryCombInstrumentGuardField = {"BrokerID": "string", "InstrumentID": "string"}
#经纪公司代码
#合约代码
structDict['CThostFtdcQryCombInstrumentGuardField'] = CThostFtdcQryCombInstrumentGuardField


#输入的申请组合
CThostFtdcInputCombActionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								  "CombActionRef": "string", "UserID": "string", "Direction": "char", "Volume": "int",
								  "CombDirection": "char", "HedgeFlag": "char", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#组合引用
#用户代码
#买卖方向
#数量
#组合指令方向
#投机套保标志
#交易所代码
structDict['CThostFtdcInputCombActionField'] = CThostFtdcInputCombActionField


#申请组合
CThostFtdcCombActionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							 "CombActionRef": "string", "UserID": "string", "Direction": "char", "Volume": "int",
							 "CombDirection": "char", "HedgeFlag": "char", "ActionLocalID": "string",
							 "ExchangeID": "string", "ParticipantID": "string", "ClientID": "string",
							 "ExchangeInstID": "string", "TraderID": "string", "InstallID": "int",
							 "ActionStatus": "char", "NotifySequence": "int", "TradingDay": "string",
							 "SettlementID": "int", "SequenceNo": "int", "FrontID": "int", "SessionID": "int",
							 "UserProductInfo": "string", "StatusMsg": "string"}
#经纪公司代码
#投资者代码
#合约代码
#组合引用
#用户代码
#买卖方向
#数量
#组合指令方向
#投机套保标志
#本地申请组合编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#组合状态
#报单提示序号
#交易日
#结算编号
#序号
#前置编号
#会话编号
#用户端产品信息
#状态信息
structDict['CThostFtdcCombActionField'] = CThostFtdcCombActionField


#申请组合查询
CThostFtdcQryCombActionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								"ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryCombActionField'] = CThostFtdcQryCombActionField


#交易所申请组合信息
CThostFtdcExchangeCombActionField = {"Direction": "char", "Volume": "int", "CombDirection": "char", "HedgeFlag": "char",
									 "ActionLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
									 "ClientID": "string", "ExchangeInstID": "string", "TraderID": "string",
									 "InstallID": "int", "ActionStatus": "char", "NotifySequence": "int",
									 "TradingDay": "string", "SettlementID": "int", "SequenceNo": "int"}
#买卖方向
#数量
#组合指令方向
#投机套保标志
#本地申请组合编号
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#组合状态
#报单提示序号
#交易日
#结算编号
#序号
structDict['CThostFtdcExchangeCombActionField'] = CThostFtdcExchangeCombActionField


#交易所申请组合查询
CThostFtdcQryExchangeCombActionField = {"ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string",
										"ExchangeID": "string", "TraderID": "string"}
#会员代码
#客户代码
#合约在交易所的代码
#交易所代码
#交易所交易员代码
structDict['CThostFtdcQryExchangeCombActionField'] = CThostFtdcQryExchangeCombActionField


#产品报价汇率
CThostFtdcProductExchRateField = {"ProductID": "string", "QuoteCurrencyID": "string", "ExchangeRate": "float"}
#产品代码
#报价币种类型
#汇率
structDict['CThostFtdcProductExchRateField'] = CThostFtdcProductExchRateField


#产品报价汇率查询
CThostFtdcQryProductExchRateField = {"ProductID": "string"}
#产品代码
structDict['CThostFtdcQryProductExchRateField'] = CThostFtdcQryProductExchRateField


#输入的指定
CThostFtdcInputDesignateField = {"BrokerID": "string", "InvestorID": "string", "DesignateRef": "string",
								 "UserID": "string", "DesignateType": "char", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#指定登记引用
#用户代码
#指定方向
#交易所代码
structDict['CThostFtdcInputDesignateField'] = CThostFtdcInputDesignateField


#指定
CThostFtdcDesignateField = {"BrokerID": "string", "InvestorID": "string", "DesignateRef": "string", "UserID": "string",
							"DesignateType": "char", "DesignateLocalID": "string", "ExchangeID": "string",
							"ParticipantID": "string", "ClientID": "string", "TraderID": "string", "InstallID": "int",
							"DesignateStatus": "char", "NotifySequence": "int", "TradingDay": "string",
							"SettlementID": "int", "InsertDate": "string", "InsertTime": "string", "FrontID": "int",
							"SessionID": "int", "UserProductInfo": "string", "StatusMsg": "string",
							"BranchID": "string"}
#经纪公司代码
#投资者代码
#指定登记引用
#用户代码
#指定方向
#本地指定编号
#交易所代码
#会员代码
#客户代码
#交易所交易员代码
#安装编号
#指定状态
#报单提示序号
#交易日
#结算编号
#报单日期
#插入时间
#前置编号
#会话编号
#用户端产品信息
#状态信息
#营业部编号
structDict['CThostFtdcDesignateField'] = CThostFtdcDesignateField


#申请指定
CThostFtdcQryDesignateField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CThostFtdcQryDesignateField'] = CThostFtdcQryDesignateField


#交易所指定信息
CThostFtdcExchangeDesignateField = {"DesignateType": "char", "DesignateLocalID": "string", "ExchangeID": "string",
									"ParticipantID": "string", "ClientID": "string", "TraderID": "string",
									"InstallID": "int", "DesignateStatus": "char", "NotifySequence": "int",
									"TradingDay": "string", "SettlementID": "int", "InsertDate": "string",
									"InsertTime": "string", "BranchID": "string"}
#指定方向
#本地指定编号
#交易所代码
#会员代码
#客户代码
#交易所交易员代码
#安装编号
#指定状态
#报单提示序号
#交易日
#结算编号
#报单日期
#插入时间
#营业部编号
structDict['CThostFtdcExchangeDesignateField'] = CThostFtdcExchangeDesignateField


#输入的证券处置
CThostFtdcInputStockDisposalField = {"BrokerID": "string", "InvestorID": "string", "StockDisposalRef": "string",
									 "UserID": "string", "InstrumentID": "string", "Volume": "int",
									 "StockDisposalType": "char", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#证券处置登记引用
#用户代码
#合约代码
#数量
#证券处置方向
#交易所代码
structDict['CThostFtdcInputStockDisposalField'] = CThostFtdcInputStockDisposalField


#证券处置
CThostFtdcStockDisposalField = {"BrokerID": "string", "InvestorID": "string", "StockDisposalRef": "string",
								"UserID": "string", "InstrumentID": "string", "Volume": "int",
								"StockDisposalType": "char", "StockDisposalLocalID": "string", "ExchangeID": "string",
								"ExchangeInstID": "string", "ParticipantID": "string", "ClientID": "string",
								"TraderID": "string", "InstallID": "int", "StockDisposalStatus": "char",
								"NotifySequence": "int", "TradingDay": "string", "SettlementID": "int",
								"InsertDate": "string", "InsertTime": "string", "FrontID": "int", "SessionID": "int",
								"UserProductInfo": "string", "StatusMsg": "string", "BranchID": "string",
								"StockDisposalSysID": "string", "BusinessUnit": "string"}
#经纪公司代码
#投资者代码
#证券处置登记引用
#用户代码
#合约代码
#数量
#证券处置方向
#本地证券处置编号
#交易所代码
#合约在交易所的代码
#会员代码
#客户代码
#交易所交易员代码
#安装编号
#证券处置状态
#报单提示序号
#交易日
#结算编号
#报单日期
#插入时间
#前置编号
#会话编号
#用户端产品信息
#状态信息
#营业部编号
#证券处置操作编号
#业务单元
structDict['CThostFtdcStockDisposalField'] = CThostFtdcStockDisposalField


#申请证券处置
CThostFtdcQryStockDisposalField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CThostFtdcQryStockDisposalField'] = CThostFtdcQryStockDisposalField


#交易所证券处置信息
CThostFtdcExchangeStockDisposalField = {"Volume": "int", "StockDisposalType": "char", "StockDisposalLocalID": "string",
										"ExchangeID": "string", "ExchangeInstID": "string", "ParticipantID": "string",
										"ClientID": "string", "TraderID": "string", "InstallID": "int",
										"StockDisposalStatus": "char", "NotifySequence": "int", "TradingDay": "string",
										"SettlementID": "int", "InsertDate": "string", "InsertTime": "string",
										"BranchID": "string", "StockDisposalSysID": "string", "BusinessUnit": "string"}
#数量
#证券处置方向
#本地证券处置编号
#交易所代码
#合约在交易所的代码
#会员代码
#客户代码
#交易所交易员代码
#安装编号
#证券处置状态
#报单提示序号
#交易日
#结算编号
#报单日期
#插入时间
#营业部编号
#证券处置操作编号
#业务单元
structDict['CThostFtdcExchangeStockDisposalField'] = CThostFtdcExchangeStockDisposalField


#查询投资者分级
CThostFtdcQryInvestorLevelField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CThostFtdcQryInvestorLevelField'] = CThostFtdcQryInvestorLevelField


#查询询价价差参数
CThostFtdcQryForQuoteParamField = {"BrokerID": "string", "InstrumentID": "string", "ExchangeID": "string"}
#经纪公司代码
#合约代码
#交易所代码
structDict['CThostFtdcQryForQuoteParamField'] = CThostFtdcQryForQuoteParamField


#询价价差参数
CThostFtdcForQuoteParamField = {"BrokerID": "string", "InstrumentID": "string", "ExchangeID": "string",
								"LastPrice": "float", "PriceInterval": "float"}
#经纪公司代码
#合约代码
#交易所代码
#最新价
#价差
structDict['CThostFtdcForQuoteParamField'] = CThostFtdcForQuoteParamField


#查询行权冻结
CThostFtdcQryExecFreezeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								"ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryExecFreezeField'] = CThostFtdcQryExecFreezeField


#行权冻结
CThostFtdcExecFreezeField = {"InstrumentID": "string", "ExchangeID": "string", "BrokerID": "string",
							 "InvestorID": "string", "PosiDirection": "char", "OptionsType": "char", "Volume": "int",
							 "FrozenAmount": "float"}
#标的合约代码
#交易所代码
#经纪公司代码
#投资者代码
#持仓多空方向
#期权类型
#冻结的数量_单位股
#冻结金额
structDict['CThostFtdcExecFreezeField'] = CThostFtdcExecFreezeField


#市场行情
CThostFtdcMarketDataField = {"TradingDay": "string", "InstrumentID": "string", "ExchangeID": "string",
							 "ExchangeInstID": "string", "LastPrice": "float", "PreSettlementPrice": "float",
							 "PreClosePrice": "float", "PreOpenInterest": "float", "OpenPrice": "float",
							 "HighestPrice": "float", "LowestPrice": "float", "Volume": "int", "Turnover": "float",
							 "OpenInterest": "float", "ClosePrice": "float", "SettlementPrice": "float",
							 "UpperLimitPrice": "float", "LowerLimitPrice": "float", "PreDelta": "float",
							 "CurrDelta": "float", "UpdateTime": "string", "UpdateMillisec": "int",
							 "ActionDay": "string"}
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
#最后修改时间
#最后修改毫秒
#业务日期
structDict['CThostFtdcMarketDataField'] = CThostFtdcMarketDataField


#行情基础属性
CThostFtdcMarketDataBaseField = {"TradingDay": "string", "PreSettlementPrice": "float", "PreClosePrice": "float",
								 "PreOpenInterest": "float", "PreDelta": "float"}
#交易日
#上次结算价
#昨收盘
#昨持仓量
#昨虚实度
structDict['CThostFtdcMarketDataBaseField'] = CThostFtdcMarketDataBaseField


#行情静态属性
CThostFtdcMarketDataStaticField = {"OpenPrice": "float", "HighestPrice": "float", "LowestPrice": "float",
								   "ClosePrice": "float", "UpperLimitPrice": "float", "LowerLimitPrice": "float",
								   "SettlementPrice": "float", "CurrDelta": "float"}
#今开盘
#最高价
#最低价
#今收盘
#涨停板价
#跌停板价
#本次结算价
#今虚实度
structDict['CThostFtdcMarketDataStaticField'] = CThostFtdcMarketDataStaticField


#行情最新成交属性
CThostFtdcMarketDataLastMatchField = {"LastPrice": "float", "Volume": "int", "Turnover": "float",
									  "OpenInterest": "float"}
#最新价
#数量
#成交金额
#持仓量
structDict['CThostFtdcMarketDataLastMatchField'] = CThostFtdcMarketDataLastMatchField


#行情最优价属性
CThostFtdcMarketDataBestPriceField = {"BidPrice1": "float", "BidVolume1": "int", "AskPrice1": "float",
									  "AskVolume1": "int"}
#申买价一
#申买量一
#申卖价一
#申卖量一
structDict['CThostFtdcMarketDataBestPriceField'] = CThostFtdcMarketDataBestPriceField


#行情申买二、三属性
CThostFtdcMarketDataBid23Field = {"BidPrice2": "float", "BidVolume2": "int", "BidPrice3": "float", "BidVolume3": "int"}
#申买价二
#申买量二
#申买价三
#申买量三
structDict['CThostFtdcMarketDataBid23Field'] = CThostFtdcMarketDataBid23Field


#行情申卖二、三属性
CThostFtdcMarketDataAsk23Field = {"AskPrice2": "float", "AskVolume2": "int", "AskPrice3": "float", "AskVolume3": "int"}
#申卖价二
#申卖量二
#申卖价三
#申卖量三
structDict['CThostFtdcMarketDataAsk23Field'] = CThostFtdcMarketDataAsk23Field


#行情申买四、五属性
CThostFtdcMarketDataBid45Field = {"BidPrice4": "float", "BidVolume4": "int", "BidPrice5": "float", "BidVolume5": "int"}
#申买价四
#申买量四
#申买价五
#申买量五
structDict['CThostFtdcMarketDataBid45Field'] = CThostFtdcMarketDataBid45Field


#行情申卖四、五属性
CThostFtdcMarketDataAsk45Field = {"AskPrice4": "float", "AskVolume4": "int", "AskPrice5": "float", "AskVolume5": "int"}
#申卖价四
#申卖量四
#申卖价五
#申卖量五
structDict['CThostFtdcMarketDataAsk45Field'] = CThostFtdcMarketDataAsk45Field


#行情更新时间属性
CThostFtdcMarketDataUpdateTimeField = {"InstrumentID": "string", "UpdateTime": "string", "UpdateMillisec": "int",
									   "ActionDay": "string", "ExchangeID": "string"}
#合约代码
#最后修改时间
#最后修改毫秒
#业务日期
#交易所代码
structDict['CThostFtdcMarketDataUpdateTimeField'] = CThostFtdcMarketDataUpdateTimeField


#行情交易所代码属性
CThostFtdcMarketDataExchangeField = {"ExchangeID": "string"}
#交易所代码
structDict['CThostFtdcMarketDataExchangeField'] = CThostFtdcMarketDataExchangeField


#指定的合约
CThostFtdcSpecificInstrumentField = {"InstrumentID": "string"}
#合约代码
structDict['CThostFtdcSpecificInstrumentField'] = CThostFtdcSpecificInstrumentField


#合约状态
CThostFtdcInstrumentStatusField = {"ExchangeID": "string", "ExchangeInstID": "string", "SettlementGroupID": "string",
								   "InstrumentID": "string", "InstrumentStatus": "char", "TradingSegmentSN": "int",
								   "EnterTime": "string", "EnterReason": "char"}
#交易所代码
#合约在交易所的代码
#结算组代码
#合约代码
#合约交易状态
#交易阶段编号
#进入本状态时间
#进入本状态原因
structDict['CThostFtdcInstrumentStatusField'] = CThostFtdcInstrumentStatusField


#查询合约状态
CThostFtdcQryInstrumentStatusField = {"ExchangeID": "string", "ExchangeInstID": "string"}
#交易所代码
#合约在交易所的代码
structDict['CThostFtdcQryInstrumentStatusField'] = CThostFtdcQryInstrumentStatusField


#投资者账户
CThostFtdcInvestorAccountField = {"BrokerID": "string", "InvestorID": "string", "AccountID": "string",
								  "CurrencyID": "string"}
#经纪公司代码
#投资者代码
#投资者帐号
#币种代码
structDict['CThostFtdcInvestorAccountField'] = CThostFtdcInvestorAccountField


#浮动盈亏算法
CThostFtdcPositionProfitAlgorithmField = {"BrokerID": "string", "AccountID": "string", "Algorithm": "char",
										  "Memo": "string", "CurrencyID": "string"}
#经纪公司代码
#投资者帐号
#盈亏算法
#备注
#币种代码
structDict['CThostFtdcPositionProfitAlgorithmField'] = CThostFtdcPositionProfitAlgorithmField


#会员资金折扣
CThostFtdcDiscountField = {"BrokerID": "string", "InvestorRange": "char", "InvestorID": "string", "Discount": "float"}
#经纪公司代码
#投资者范围
#投资者代码
#资金折扣比例
structDict['CThostFtdcDiscountField'] = CThostFtdcDiscountField


#查询转帐银行
CThostFtdcQryTransferBankField = {"BankID": "string", "BankBrchID": "string"}
#银行代码
#银行分中心代码
structDict['CThostFtdcQryTransferBankField'] = CThostFtdcQryTransferBankField


#转帐银行
CThostFtdcTransferBankField = {"BankID": "string", "BankBrchID": "string", "BankName": "string", "IsActive": "int"}
#银行代码
#银行分中心代码
#银行名称
#是否活跃
structDict['CThostFtdcTransferBankField'] = CThostFtdcTransferBankField


#查询投资者持仓明细
CThostFtdcQryInvestorPositionDetailField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
											"ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryInvestorPositionDetailField'] = CThostFtdcQryInvestorPositionDetailField


#投资者持仓明细
CThostFtdcInvestorPositionDetailField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
										 "HedgeFlag": "char", "Direction": "char", "OpenDate": "string",
										 "TradeID": "string", "Volume": "int", "OpenPrice": "float",
										 "TradingDay": "string", "SettlementID": "int", "TradeType": "char",
										 "CombInstrumentID": "string", "ExchangeID": "string",
										 "CloseProfitByDate": "float", "CloseProfitByTrade": "float",
										 "PositionProfitByDate": "float", "PositionProfitByTrade": "float",
										 "Margin": "float", "ExchMargin": "float", "MarginRateByMoney": "float",
										 "MarginRateByVolume": "float", "LastSettlementPrice": "float",
										 "SettlementPrice": "float", "CloseVolume": "int", "CloseAmount": "float"}
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
#结算编号
#成交类型
#组合合约代码
#交易所代码
#逐日盯市平仓盈亏
#逐笔对冲平仓盈亏
#逐日盯市持仓盈亏
#逐笔对冲持仓盈亏
#投资者保证金
#交易所保证金
#保证金率
#保证金率(按手数)
#昨结算价
#结算价
#平仓量
#平仓金额
structDict['CThostFtdcInvestorPositionDetailField'] = CThostFtdcInvestorPositionDetailField


#资金账户口令域
CThostFtdcTradingAccountPasswordField = {"BrokerID": "string", "AccountID": "string", "Password": "string",
										 "CurrencyID": "string"}
#经纪公司代码
#投资者帐号
#密码
#币种代码
structDict['CThostFtdcTradingAccountPasswordField'] = CThostFtdcTradingAccountPasswordField


#交易所行情报盘机
CThostFtdcMDTraderOfferField = {"ExchangeID": "string", "TraderID": "string", "ParticipantID": "string",
								"Password": "string", "InstallID": "int", "OrderLocalID": "string",
								"TraderConnectStatus": "char", "ConnectRequestDate": "string",
								"ConnectRequestTime": "string", "LastReportDate": "string", "LastReportTime": "string",
								"ConnectDate": "string", "ConnectTime": "string", "StartDate": "string",
								"StartTime": "string", "TradingDay": "string", "BrokerID": "string",
								"MaxTradeID": "string", "MaxOrderMessageReference": "string", "BizType": "char"}
#交易所代码
#交易所交易员代码
#会员代码
#密码
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
#本席位最大成交编号
#本席位最大报单备拷
#业务类型
structDict['CThostFtdcMDTraderOfferField'] = CThostFtdcMDTraderOfferField


#查询行情报盘机
CThostFtdcQryMDTraderOfferField = {"ExchangeID": "string", "ParticipantID": "string", "TraderID": "string"}
#交易所代码
#会员代码
#交易所交易员代码
structDict['CThostFtdcQryMDTraderOfferField'] = CThostFtdcQryMDTraderOfferField


#查询客户通知
CThostFtdcQryNoticeField = {"BrokerID": "string"}
#经纪公司代码
structDict['CThostFtdcQryNoticeField'] = CThostFtdcQryNoticeField


#客户通知
CThostFtdcNoticeField = {"BrokerID": "string", "Content": "string", "SequenceLabel": "string"}
#经纪公司代码
#消息正文
#经纪公司通知内容序列号
structDict['CThostFtdcNoticeField'] = CThostFtdcNoticeField


#用户权限
CThostFtdcUserRightField = {"BrokerID": "string", "UserID": "string", "UserRightType": "char", "IsForbidden": "int"}
#经纪公司代码
#用户代码
#客户权限类型
#是否禁止
structDict['CThostFtdcUserRightField'] = CThostFtdcUserRightField


#查询结算信息确认域
CThostFtdcQrySettlementInfoConfirmField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQrySettlementInfoConfirmField'] = CThostFtdcQrySettlementInfoConfirmField


#装载结算信息
CThostFtdcLoadSettlementInfoField = {"BrokerID": "string"}
#经纪公司代码
structDict['CThostFtdcLoadSettlementInfoField'] = CThostFtdcLoadSettlementInfoField


#经纪公司可提资金算法表
CThostFtdcBrokerWithdrawAlgorithmField = {"BrokerID": "string", "WithdrawAlgorithm": "char", "UsingRatio": "float",
										  "IncludeCloseProfit": "char", "AllWithoutTrade": "char",
										  "AvailIncludeCloseProfit": "char", "IsBrokerUserEvent": "int",
										  "CurrencyID": "string", "FundMortgageRatio": "float",
										  "BalanceAlgorithm": "char"}
#经纪公司代码
#可提资金算法
#资金使用率
#可提是否包含平仓盈利
#本日无仓且无成交客户是否受可提比例限制
#可用是否包含平仓盈利
#是否启用用户事件
#币种代码
#货币质押比率
#权益算法
structDict['CThostFtdcBrokerWithdrawAlgorithmField'] = CThostFtdcBrokerWithdrawAlgorithmField


#资金账户口令变更域
CThostFtdcTradingAccountPasswordUpdateV1Field = {"BrokerID": "string", "InvestorID": "string", "OldPassword": "string",
												 "NewPassword": "string"}
#经纪公司代码
#投资者代码
#原来的口令
#新的口令
structDict['CThostFtdcTradingAccountPasswordUpdateV1Field'] = CThostFtdcTradingAccountPasswordUpdateV1Field


#资金账户口令变更域
CThostFtdcTradingAccountPasswordUpdateField = {"BrokerID": "string", "AccountID": "string", "OldPassword": "string",
											   "NewPassword": "string", "CurrencyID": "string"}
#经纪公司代码
#投资者帐号
#原来的口令
#新的口令
#币种代码
structDict['CThostFtdcTradingAccountPasswordUpdateField'] = CThostFtdcTradingAccountPasswordUpdateField


#查询组合合约分腿
CThostFtdcQryCombinationLegField = {"CombInstrumentID": "string", "LegID": "int", "LegInstrumentID": "string"}
#组合合约代码
#单腿编号
#单腿合约代码
structDict['CThostFtdcQryCombinationLegField'] = CThostFtdcQryCombinationLegField


#查询组合合约分腿
CThostFtdcQrySyncStatusField = {"TradingDay": "string"}
#交易日
structDict['CThostFtdcQrySyncStatusField'] = CThostFtdcQrySyncStatusField


#组合交易合约的单腿
CThostFtdcCombinationLegField = {"CombInstrumentID": "string", "LegID": "int", "LegInstrumentID": "string",
								 "Direction": "char", "LegMultiple": "int", "ImplyLevel": "int"}
#组合合约代码
#单腿编号
#单腿合约代码
#买卖方向
#单腿乘数
#派生层数
structDict['CThostFtdcCombinationLegField'] = CThostFtdcCombinationLegField


#数据同步状态
CThostFtdcSyncStatusField = {"TradingDay": "string", "DataSyncStatus": "char"}
#交易日
#数据同步状态
structDict['CThostFtdcSyncStatusField'] = CThostFtdcSyncStatusField


#查询联系人
CThostFtdcQryLinkManField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQryLinkManField'] = CThostFtdcQryLinkManField


#联系人
CThostFtdcLinkManField = {"BrokerID": "string", "InvestorID": "string", "PersonType": "char",
						  "IdentifiedCardType": "char", "IdentifiedCardNo": "string", "PersonName": "string",
						  "Telephone": "string", "Address": "string", "ZipCode": "string", "Priority": "int",
						  "UOAZipCode": "string", "PersonFullName": "string"}
#经纪公司代码
#投资者代码
#联系人类型
#证件类型
#证件号码
#名称
#联系电话
#通讯地址
#邮政编码
#优先级
#开户邮政编码
#全称
structDict['CThostFtdcLinkManField'] = CThostFtdcLinkManField


#查询经纪公司用户事件
CThostFtdcQryBrokerUserEventField = {"BrokerID": "string", "UserID": "string", "UserEventType": "char"}
#经纪公司代码
#用户代码
#用户事件类型
structDict['CThostFtdcQryBrokerUserEventField'] = CThostFtdcQryBrokerUserEventField


#查询经纪公司用户事件
CThostFtdcBrokerUserEventField = {"BrokerID": "string", "UserID": "string", "UserEventType": "char",
								  "EventSequenceNo": "int", "EventDate": "string", "EventTime": "string",
								  "UserEventInfo": "string", "InvestorID": "string", "InstrumentID": "string",
								  "ExchangeID": "string"}
#经纪公司代码
#用户代码
#用户事件类型
#用户事件序号
#事件发生日期
#事件发生时间
#用户事件信息
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcBrokerUserEventField'] = CThostFtdcBrokerUserEventField


#查询签约银行请求
CThostFtdcQryContractBankField = {"BrokerID": "string", "BankID": "string", "BankBrchID": "string"}
#经纪公司代码
#银行代码
#银行分中心代码
structDict['CThostFtdcQryContractBankField'] = CThostFtdcQryContractBankField


#查询签约银行响应
CThostFtdcContractBankField = {"BrokerID": "string", "BankID": "string", "BankBrchID": "string", "BankName": "string"}
#经纪公司代码
#银行代码
#银行分中心代码
#银行名称
structDict['CThostFtdcContractBankField'] = CThostFtdcContractBankField


#投资者组合持仓明细
CThostFtdcInvestorPositionCombineDetailField = {"TradingDay": "string", "OpenDate": "string", "ExchangeID": "string",
												"SettlementID": "int", "BrokerID": "string", "InvestorID": "string",
												"ComTradeID": "string", "TradeID": "string", "InstrumentID": "string",
												"HedgeFlag": "char", "Direction": "char", "TotalAmt": "int",
												"Margin": "float", "ExchMargin": "float", "MarginRateByMoney": "float",
												"MarginRateByVolume": "float", "LegID": "int", "LegMultiple": "int",
												"CombInstrumentID": "string", "TradeGroupID": "int"}
#交易日
#开仓日期
#交易所代码
#结算编号
#经纪公司代码
#投资者代码
#组合编号
#撮合编号
#合约代码
#投机套保标志
#买卖
#持仓量
#投资者保证金
#交易所保证金
#保证金率
#保证金率(按手数)
#单腿编号
#单腿乘数
#组合持仓合约编码
#成交组号
structDict['CThostFtdcInvestorPositionCombineDetailField'] = CThostFtdcInvestorPositionCombineDetailField


#预埋单
CThostFtdcParkedOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							  "OrderRef": "string", "UserID": "string", "OrderPriceType": "char", "Direction": "char",
							  "CombOffsetFlag": "string", "CombHedgeFlag": "string", "LimitPrice": "float",
							  "VolumeTotalOriginal": "int", "TimeCondition": "char", "GTDDate": "string",
							  "VolumeCondition": "char", "MinVolume": "int", "ContingentCondition": "char",
							  "StopPrice": "float", "ForceCloseReason": "char", "IsAutoSuspend": "int",
							  "BusinessUnit": "string", "RequestID": "int", "UserForceClose": "int",
							  "ExchangeID": "string", "ParkedOrderID": "string", "UserType": "char", "Status": "char",
							  "ErrorID": "int", "ErrorMsg": "string", "IsSwapOrder": "int"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
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
#交易所代码
#预埋报单编号
#用户类型
#预埋单状态
#错误代码
#错误信息
#互换单标志
structDict['CThostFtdcParkedOrderField'] = CThostFtdcParkedOrderField


#输入预埋单操作
CThostFtdcParkedOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
									"OrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
									"ExchangeID": "string", "OrderSysID": "string", "ActionFlag": "char",
									"LimitPrice": "float", "VolumeChange": "int", "UserID": "string",
									"InstrumentID": "string", "ParkedOrderActionID": "string", "UserType": "char",
									"Status": "char", "ErrorID": "int", "ErrorMsg": "string"}
#经纪公司代码
#投资者代码
#报单操作引用
#报单引用
#请求编号
#前置编号
#会话编号
#交易所代码
#报单编号
#操作标志
#价格
#数量变化
#用户代码
#合约代码
#预埋撤单单编号
#用户类型
#预埋撤单状态
#错误代码
#错误信息
structDict['CThostFtdcParkedOrderActionField'] = CThostFtdcParkedOrderActionField


#查询预埋单
CThostFtdcQryParkedOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								 "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryParkedOrderField'] = CThostFtdcQryParkedOrderField


#查询预埋撤单
CThostFtdcQryParkedOrderActionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
									   "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CThostFtdcQryParkedOrderActionField'] = CThostFtdcQryParkedOrderActionField


#删除预埋单
CThostFtdcRemoveParkedOrderField = {"BrokerID": "string", "InvestorID": "string", "ParkedOrderID": "string"}
#经纪公司代码
#投资者代码
#预埋报单编号
structDict['CThostFtdcRemoveParkedOrderField'] = CThostFtdcRemoveParkedOrderField


#删除预埋撤单
CThostFtdcRemoveParkedOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ParkedOrderActionID": "string"}
#经纪公司代码
#投资者代码
#预埋撤单编号
structDict['CThostFtdcRemoveParkedOrderActionField'] = CThostFtdcRemoveParkedOrderActionField


#经纪公司可提资金算法表
CThostFtdcInvestorWithdrawAlgorithmField = {"BrokerID": "string", "InvestorRange": "char", "InvestorID": "string",
											"UsingRatio": "float", "CurrencyID": "string", "FundMortgageRatio": "float"}
#经纪公司代码
#投资者范围
#投资者代码
#可提资金比例
#币种代码
#货币质押比率
structDict['CThostFtdcInvestorWithdrawAlgorithmField'] = CThostFtdcInvestorWithdrawAlgorithmField


#查询组合持仓明细
CThostFtdcQryInvestorPositionCombineDetailField = {"BrokerID": "string", "InvestorID": "string",
												   "CombInstrumentID": "string"}
#经纪公司代码
#投资者代码
#组合持仓合约编码
structDict['CThostFtdcQryInvestorPositionCombineDetailField'] = CThostFtdcQryInvestorPositionCombineDetailField


#成交均价
CThostFtdcMarketDataAveragePriceField = {"AveragePrice": "float"}
#当日均价
structDict['CThostFtdcMarketDataAveragePriceField'] = CThostFtdcMarketDataAveragePriceField


#校验投资者密码
CThostFtdcVerifyInvestorPasswordField = {"BrokerID": "string", "InvestorID": "string", "Password": "string"}
#经纪公司代码
#投资者代码
#密码
structDict['CThostFtdcVerifyInvestorPasswordField'] = CThostFtdcVerifyInvestorPasswordField


#用户IP
CThostFtdcUserIPField = {"BrokerID": "string", "UserID": "string", "IPAddress": "string", "IPMask": "string",
						 "MacAddress": "string"}
#经纪公司代码
#用户代码
#IP地址
#IP地址掩码
#Mac地址
structDict['CThostFtdcUserIPField'] = CThostFtdcUserIPField


#用户事件通知信息
CThostFtdcTradingNoticeInfoField = {"BrokerID": "string", "InvestorID": "string", "SendTime": "string",
									"FieldContent": "string", "SequenceSeries": "int", "SequenceNo": "int"}
#经纪公司代码
#投资者代码
#发送时间
#消息正文
#序列系列号
#序列号
structDict['CThostFtdcTradingNoticeInfoField'] = CThostFtdcTradingNoticeInfoField


#用户事件通知
CThostFtdcTradingNoticeField = {"BrokerID": "string", "InvestorRange": "char", "InvestorID": "string",
								"SequenceSeries": "int", "UserID": "string", "SendTime": "string", "SequenceNo": "int",
								"FieldContent": "string"}
#经纪公司代码
#投资者范围
#投资者代码
#序列系列号
#用户代码
#发送时间
#序列号
#消息正文
structDict['CThostFtdcTradingNoticeField'] = CThostFtdcTradingNoticeField


#查询交易事件通知
CThostFtdcQryTradingNoticeField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQryTradingNoticeField'] = CThostFtdcQryTradingNoticeField


#查询错误报单
CThostFtdcQryErrOrderField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQryErrOrderField'] = CThostFtdcQryErrOrderField


#错误报单
CThostFtdcErrOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
						   "UserID": "string", "OrderPriceType": "char", "Direction": "char",
						   "CombOffsetFlag": "string", "CombHedgeFlag": "string", "LimitPrice": "float",
						   "VolumeTotalOriginal": "int", "TimeCondition": "char", "GTDDate": "string",
						   "VolumeCondition": "char", "MinVolume": "int", "ContingentCondition": "char",
						   "StopPrice": "float", "ForceCloseReason": "char", "IsAutoSuspend": "int",
						   "BusinessUnit": "string", "RequestID": "int", "UserForceClose": "int", "ErrorID": "int",
						   "ErrorMsg": "string", "IsSwapOrder": "int", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
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
#互换单标志
#交易所代码
structDict['CThostFtdcErrOrderField'] = CThostFtdcErrOrderField


#查询错误报单操作
CThostFtdcErrorConditionalOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
										"OrderRef": "string", "UserID": "string", "OrderPriceType": "char",
										"Direction": "char", "CombOffsetFlag": "string", "CombHedgeFlag": "string",
										"LimitPrice": "float", "VolumeTotalOriginal": "int", "TimeCondition": "char",
										"GTDDate": "string", "VolumeCondition": "char", "MinVolume": "int",
										"ContingentCondition": "char", "StopPrice": "float", "ForceCloseReason": "char",
										"IsAutoSuspend": "int", "BusinessUnit": "string", "RequestID": "int",
										"OrderLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
										"ClientID": "string", "ExchangeInstID": "string", "TraderID": "string",
										"InstallID": "int", "OrderSubmitStatus": "char", "NotifySequence": "int",
										"TradingDay": "string", "SettlementID": "int", "OrderSysID": "string",
										"OrderSource": "char", "OrderStatus": "char", "OrderType": "char",
										"VolumeTraded": "int", "VolumeTotal": "int", "InsertDate": "string",
										"InsertTime": "string", "ActiveTime": "string", "SuspendTime": "string",
										"UpdateTime": "string", "CancelTime": "string", "ActiveTraderID": "string",
										"ClearingPartID": "string", "SequenceNo": "int", "FrontID": "int",
										"SessionID": "int", "UserProductInfo": "string", "StatusMsg": "string",
										"UserForceClose": "int", "ActiveUserID": "string", "BrokerOrderSeq": "int",
										"RelativeOrderSysID": "string", "ZCETotalTradedVolume": "int", "ErrorID": "int",
										"ErrorMsg": "string", "IsSwapOrder": "int", "BranchID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
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
#交易所代码
#会员代码
#客户代码
#合约在交易所的代码
#交易所交易员代码
#安装编号
#报单提交状态
#报单提示序号
#交易日
#结算编号
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
#郑商所成交数量
#错误代码
#错误信息
#互换单标志
#营业部编号
structDict['CThostFtdcErrorConditionalOrderField'] = CThostFtdcErrorConditionalOrderField


#查询错误报单操作
CThostFtdcQryErrOrderActionField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQryErrOrderActionField'] = CThostFtdcQryErrOrderActionField


#错误报单操作
CThostFtdcErrOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
								 "OrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
								 "ExchangeID": "string", "OrderSysID": "string", "ActionFlag": "char",
								 "LimitPrice": "float", "VolumeChange": "int", "ActionDate": "string",
								 "ActionTime": "string", "TraderID": "string", "InstallID": "int",
								 "OrderLocalID": "string", "ActionLocalID": "string", "ParticipantID": "string",
								 "ClientID": "string", "BusinessUnit": "string", "OrderActionStatus": "char",
								 "UserID": "string", "StatusMsg": "string", "InstrumentID": "string",
								 "BranchID": "string", "ErrorID": "int", "ErrorMsg": "string"}
#经纪公司代码
#投资者代码
#报单操作引用
#报单引用
#请求编号
#前置编号
#会话编号
#交易所代码
#报单编号
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
#状态信息
#合约代码
#营业部编号
#错误代码
#错误信息
structDict['CThostFtdcErrOrderActionField'] = CThostFtdcErrOrderActionField


#查询交易所状态
CThostFtdcQryExchangeSequenceField = {"ExchangeID": "string"}
#交易所代码
structDict['CThostFtdcQryExchangeSequenceField'] = CThostFtdcQryExchangeSequenceField


#交易所状态
CThostFtdcExchangeSequenceField = {"ExchangeID": "string", "SequenceNo": "int", "MarketStatus": "char"}
#交易所代码
#序号
#合约交易状态
structDict['CThostFtdcExchangeSequenceField'] = CThostFtdcExchangeSequenceField


#根据价格查询最大报单数量
CThostFtdcQueryMaxOrderVolumeWithPriceField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
											   "Direction": "char", "OffsetFlag": "char", "HedgeFlag": "char",
											   "MaxVolume": "int", "Price": "float", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#买卖方向
#开平标志
#投机套保标志
#最大允许报单数量
#报单价格
#交易所代码
structDict['CThostFtdcQueryMaxOrderVolumeWithPriceField'] = CThostFtdcQueryMaxOrderVolumeWithPriceField


#查询经纪公司交易参数
CThostFtdcQryBrokerTradingParamsField = {"BrokerID": "string", "InvestorID": "string", "CurrencyID": "string"}
#经纪公司代码
#投资者代码
#币种代码
structDict['CThostFtdcQryBrokerTradingParamsField'] = CThostFtdcQryBrokerTradingParamsField


#经纪公司交易参数
CThostFtdcBrokerTradingParamsField = {"BrokerID": "string", "InvestorID": "string", "MarginPriceType": "char",
									  "Algorithm": "char", "AvailIncludeCloseProfit": "char", "CurrencyID": "string",
									  "OptionRoyaltyPriceType": "char"}
#经纪公司代码
#投资者代码
#保证金价格类型
#盈亏算法
#可用是否包含平仓盈利
#币种代码
#期权权利金价格类型
structDict['CThostFtdcBrokerTradingParamsField'] = CThostFtdcBrokerTradingParamsField


#查询经纪公司交易算法
CThostFtdcQryBrokerTradingAlgosField = {"BrokerID": "string", "ExchangeID": "string", "InstrumentID": "string"}
#经纪公司代码
#交易所代码
#合约代码
structDict['CThostFtdcQryBrokerTradingAlgosField'] = CThostFtdcQryBrokerTradingAlgosField


#经纪公司交易算法
CThostFtdcBrokerTradingAlgosField = {"BrokerID": "string", "ExchangeID": "string", "InstrumentID": "string",
									 "HandlePositionAlgoID": "char", "FindMarginRateAlgoID": "char",
									 "HandleTradingAccountAlgoID": "char"}
#经纪公司代码
#交易所代码
#合约代码
#持仓处理算法编号
#寻找保证金率算法编号
#资金处理算法编号
structDict['CThostFtdcBrokerTradingAlgosField'] = CThostFtdcBrokerTradingAlgosField


#查询经纪公司资金
CThostFtdcQueryBrokerDepositField = {"BrokerID": "string", "ExchangeID": "string"}
#经纪公司代码
#交易所代码
structDict['CThostFtdcQueryBrokerDepositField'] = CThostFtdcQueryBrokerDepositField


#经纪公司资金
CThostFtdcBrokerDepositField = {"TradingDay": "string", "BrokerID": "string", "ParticipantID": "string",
								"ExchangeID": "string", "PreBalance": "float", "CurrMargin": "float",
								"CloseProfit": "float", "Balance": "float", "Deposit": "float", "Withdraw": "float",
								"Available": "float", "Reserve": "float", "FrozenMargin": "float"}
#交易日期
#经纪公司代码
#会员代码
#交易所代码
#上次结算准备金
#当前保证金总额
#平仓盈亏
#期货结算准备金
#入金金额
#出金金额
#可提资金
#基本准备金
#冻结的保证金
structDict['CThostFtdcBrokerDepositField'] = CThostFtdcBrokerDepositField


#查询保证金监管系统经纪公司密钥
CThostFtdcQryCFMMCBrokerKeyField = {"BrokerID": "string"}
#经纪公司代码
structDict['CThostFtdcQryCFMMCBrokerKeyField'] = CThostFtdcQryCFMMCBrokerKeyField


#保证金监管系统经纪公司密钥
CThostFtdcCFMMCBrokerKeyField = {"BrokerID": "string", "ParticipantID": "string", "CreateDate": "string",
								 "CreateTime": "string", "KeyID": "int", "CurrentKey": "string", "KeyKind": "char"}
#经纪公司代码
#经纪公司统一编码
#密钥生成日期
#密钥生成时间
#密钥编号
#动态密钥
#动态密钥类型
structDict['CThostFtdcCFMMCBrokerKeyField'] = CThostFtdcCFMMCBrokerKeyField


#保证金监管系统经纪公司资金账户密钥
CThostFtdcCFMMCTradingAccountKeyField = {"BrokerID": "string", "ParticipantID": "string", "AccountID": "string",
										 "KeyID": "int", "CurrentKey": "string"}
#经纪公司代码
#经纪公司统一编码
#投资者帐号
#密钥编号
#动态密钥
structDict['CThostFtdcCFMMCTradingAccountKeyField'] = CThostFtdcCFMMCTradingAccountKeyField


#请求查询保证金监管系统经纪公司资金账户密钥
CThostFtdcQryCFMMCTradingAccountKeyField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQryCFMMCTradingAccountKeyField'] = CThostFtdcQryCFMMCTradingAccountKeyField


#用户动态令牌参数
CThostFtdcBrokerUserOTPParamField = {"BrokerID": "string", "UserID": "string", "OTPVendorsID": "string",
									 "SerialNumber": "string", "AuthKey": "string", "LastDrift": "int",
									 "LastSuccess": "int", "OTPType": "char"}
#经纪公司代码
#用户代码
#动态令牌提供商
#动态令牌序列号
#令牌密钥
#漂移值
#成功值
#动态令牌类型
structDict['CThostFtdcBrokerUserOTPParamField'] = CThostFtdcBrokerUserOTPParamField


#手工同步用户动态令牌
CThostFtdcManualSyncBrokerUserOTPField = {"BrokerID": "string", "UserID": "string", "OTPType": "char",
										  "FirstOTP": "string", "SecondOTP": "string"}
#经纪公司代码
#用户代码
#动态令牌类型
#第一个动态密码
#第二个动态密码
structDict['CThostFtdcManualSyncBrokerUserOTPField'] = CThostFtdcManualSyncBrokerUserOTPField


#投资者手续费率模板
CThostFtdcCommRateModelField = {"BrokerID": "string", "CommModelID": "string", "CommModelName": "string"}
#经纪公司代码
#手续费率模板代码
#模板名称
structDict['CThostFtdcCommRateModelField'] = CThostFtdcCommRateModelField


#请求查询投资者手续费率模板
CThostFtdcQryCommRateModelField = {"BrokerID": "string", "CommModelID": "string"}
#经纪公司代码
#手续费率模板代码
structDict['CThostFtdcQryCommRateModelField'] = CThostFtdcQryCommRateModelField


#投资者保证金率模板
CThostFtdcMarginModelField = {"BrokerID": "string", "MarginModelID": "string", "MarginModelName": "string"}
#经纪公司代码
#保证金率模板代码
#模板名称
structDict['CThostFtdcMarginModelField'] = CThostFtdcMarginModelField


#请求查询投资者保证金率模板
CThostFtdcQryMarginModelField = {"BrokerID": "string", "MarginModelID": "string"}
#经纪公司代码
#保证金率模板代码
structDict['CThostFtdcQryMarginModelField'] = CThostFtdcQryMarginModelField


#仓单折抵信息
CThostFtdcEWarrantOffsetField = {"TradingDay": "string", "BrokerID": "string", "InvestorID": "string",
								 "ExchangeID": "string", "InstrumentID": "string", "Direction": "char",
								 "HedgeFlag": "char", "Volume": "int"}
#交易日期
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
#买卖方向
#投机套保标志
#数量
structDict['CThostFtdcEWarrantOffsetField'] = CThostFtdcEWarrantOffsetField


#查询仓单折抵信息
CThostFtdcQryEWarrantOffsetField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
									"InstrumentID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
structDict['CThostFtdcQryEWarrantOffsetField'] = CThostFtdcQryEWarrantOffsetField


#查询投资者品种/跨品种保证金
CThostFtdcQryInvestorProductGroupMarginField = {"BrokerID": "string", "InvestorID": "string",
												"ProductGroupID": "string", "HedgeFlag": "char"}
#经纪公司代码
#投资者代码
#品种/跨品种标示
#投机套保标志
structDict['CThostFtdcQryInvestorProductGroupMarginField'] = CThostFtdcQryInvestorProductGroupMarginField


#投资者品种/跨品种保证金
CThostFtdcInvestorProductGroupMarginField = {"ProductGroupID": "string", "BrokerID": "string", "InvestorID": "string",
											 "TradingDay": "string", "SettlementID": "int", "FrozenMargin": "float",
											 "LongFrozenMargin": "float", "ShortFrozenMargin": "float",
											 "UseMargin": "float", "LongUseMargin": "float", "ShortUseMargin": "float",
											 "ExchMargin": "float", "LongExchMargin": "float",
											 "ShortExchMargin": "float", "CloseProfit": "float",
											 "FrozenCommission": "float", "Commission": "float", "FrozenCash": "float",
											 "CashIn": "float", "PositionProfit": "float", "OffsetAmount": "float",
											 "LongOffsetAmount": "float", "ShortOffsetAmount": "float",
											 "ExchOffsetAmount": "float", "LongExchOffsetAmount": "float",
											 "ShortExchOffsetAmount": "float", "HedgeFlag": "char"}
#品种/跨品种标示
#经纪公司代码
#投资者代码
#交易日
#结算编号
#冻结的保证金
#多头冻结的保证金
#空头冻结的保证金
#占用的保证金
#多头保证金
#空头保证金
#交易所保证金
#交易所多头保证金
#交易所空头保证金
#平仓盈亏
#冻结的手续费
#手续费
#冻结的资金
#资金差额
#持仓盈亏
#折抵总金额
#多头折抵总金额
#空头折抵总金额
#交易所折抵总金额
#交易所多头折抵总金额
#交易所空头折抵总金额
#投机套保标志
structDict['CThostFtdcInvestorProductGroupMarginField'] = CThostFtdcInvestorProductGroupMarginField


#查询监控中心用户令牌
CThostFtdcQueryCFMMCTradingAccountTokenField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CThostFtdcQueryCFMMCTradingAccountTokenField'] = CThostFtdcQueryCFMMCTradingAccountTokenField


#监控中心用户令牌
CThostFtdcCFMMCTradingAccountTokenField = {"BrokerID": "string", "ParticipantID": "string", "AccountID": "string",
										   "KeyID": "int", "Token": "string"}
#经纪公司代码
#经纪公司统一编码
#投资者帐号
#密钥编号
#动态令牌
structDict['CThostFtdcCFMMCTradingAccountTokenField'] = CThostFtdcCFMMCTradingAccountTokenField


#投资者指令权限
CThostFtdcInstructionRightField = {"BrokerID": "string", "ExchangeID": "string", "InvestorID": "string",
								   "InstructionRight": "char", "IsForbidden": "int"}
#经纪公司代码
#交易所代码
#投资者代码
#指令权限类型
#是否禁止
structDict['CThostFtdcInstructionRightField'] = CThostFtdcInstructionRightField


#查询产品组
CThostFtdcQryProductGroupField = {"ProductID": "string", "ExchangeID": "string"}
#产品代码
#交易所代码
structDict['CThostFtdcQryProductGroupField'] = CThostFtdcQryProductGroupField


#投资者品种/跨品种保证金产品组
CThostFtdcProductGroupField = {"ProductID": "string", "ExchangeID": "string", "ProductGroupID": "string"}
#产品代码
#交易所代码
#产品组代码
structDict['CThostFtdcProductGroupField'] = CThostFtdcProductGroupField


#转帐开户请求
CThostFtdcReqOpenAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								 "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								 "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								 "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
								 "CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								 "Gender": "char", "CountryCode": "string", "CustType": "char", "Address": "string",
								 "ZipCode": "string", "Telephone": "string", "MobilePhone": "string", "Fax": "string",
								 "EMail": "string", "MoneyAccountStatus": "char", "BankAccount": "string",
								 "BankPassWord": "string", "AccountID": "string", "Password": "string",
								 "InstallID": "int", "VerifyCertNoFlag": "char", "CurrencyID": "string",
								 "CashExchangeCode": "char", "Digest": "string", "BankAccType": "char",
								 "DeviceID": "string", "BankSecuAccType": "char", "BrokerIDByBank": "string",
								 "BankSecuAcc": "string", "BankPwdFlag": "char", "SecuPwdFlag": "char",
								 "OperNo": "string", "TID": "int", "UserID": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#性别
#国家代码
#客户类型
#地址
#邮编
#电话号码
#手机
#传真
#电子邮件
#资金账户状态
#银行帐号
#银行密码
#投资者帐号
#期货密码
#安装编号
#验证客户证件号码标志
#币种代码
#汇钞标志
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#交易ID
#用户标识
structDict['CThostFtdcReqOpenAccountField'] = CThostFtdcReqOpenAccountField


#转帐销户请求
CThostFtdcReqCancelAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								   "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								   "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								   "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
								   "CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								   "Gender": "char", "CountryCode": "string", "CustType": "char", "Address": "string",
								   "ZipCode": "string", "Telephone": "string", "MobilePhone": "string", "Fax": "string",
								   "EMail": "string", "MoneyAccountStatus": "char", "BankAccount": "string",
								   "BankPassWord": "string", "AccountID": "string", "Password": "string",
								   "InstallID": "int", "VerifyCertNoFlag": "char", "CurrencyID": "string",
								   "CashExchangeCode": "char", "Digest": "string", "BankAccType": "char",
								   "DeviceID": "string", "BankSecuAccType": "char", "BrokerIDByBank": "string",
								   "BankSecuAcc": "string", "BankPwdFlag": "char", "SecuPwdFlag": "char",
								   "OperNo": "string", "TID": "int", "UserID": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#性别
#国家代码
#客户类型
#地址
#邮编
#电话号码
#手机
#传真
#电子邮件
#资金账户状态
#银行帐号
#银行密码
#投资者帐号
#期货密码
#安装编号
#验证客户证件号码标志
#币种代码
#汇钞标志
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#交易ID
#用户标识
structDict['CThostFtdcReqCancelAccountField'] = CThostFtdcReqCancelAccountField


#变更银行账户请求
CThostFtdcReqChangeAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								   "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								   "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								   "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
								   "CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								   "Gender": "char", "CountryCode": "string", "CustType": "char", "Address": "string",
								   "ZipCode": "string", "Telephone": "string", "MobilePhone": "string", "Fax": "string",
								   "EMail": "string", "MoneyAccountStatus": "char", "BankAccount": "string",
								   "BankPassWord": "string", "NewBankAccount": "string", "NewBankPassWord": "string",
								   "AccountID": "string", "Password": "string", "BankAccType": "char",
								   "InstallID": "int", "VerifyCertNoFlag": "char", "CurrencyID": "string",
								   "BrokerIDByBank": "string", "BankPwdFlag": "char", "SecuPwdFlag": "char",
								   "TID": "int", "Digest": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#性别
#国家代码
#客户类型
#地址
#邮编
#电话号码
#手机
#传真
#电子邮件
#资金账户状态
#银行帐号
#银行密码
#新银行帐号
#新银行密码
#投资者帐号
#期货密码
#银行帐号类型
#安装编号
#验证客户证件号码标志
#币种代码
#期货公司银行编码
#银行密码标志
#期货资金密码核对标志
#交易ID
#摘要
structDict['CThostFtdcReqChangeAccountField'] = CThostFtdcReqChangeAccountField


#转账请求
CThostFtdcReqTransferField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							  "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							  "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							  "LastFragment": "char", "SessionID": "int", "CustomerName": "string",
							  "IdCardType": "char", "IdentifiedCardNo": "string", "CustType": "char",
							  "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
							  "Password": "string", "InstallID": "int", "FutureSerial": "int", "UserID": "string",
							  "VerifyCertNoFlag": "char", "CurrencyID": "string", "TradeAmount": "float",
							  "FutureFetchAmount": "float", "FeePayFlag": "char", "CustFee": "float",
							  "BrokerFee": "float", "Message": "string", "Digest": "string", "BankAccType": "char",
							  "DeviceID": "string", "BankSecuAccType": "char", "BrokerIDByBank": "string",
							  "BankSecuAcc": "string", "BankPwdFlag": "char", "SecuPwdFlag": "char", "OperNo": "string",
							  "RequestID": "int", "TID": "int", "TransferStatus": "char"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#客户类型
#银行帐号
#银行密码
#投资者帐号
#期货密码
#安装编号
#期货公司流水号
#用户标识
#验证客户证件号码标志
#币种代码
#转帐金额
#期货可取金额
#费用支付标志
#应收客户费用
#应收期货公司费用
#发送方给接收方的消息
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#请求编号
#交易ID
#转账交易状态
structDict['CThostFtdcReqTransferField'] = CThostFtdcReqTransferField


#银行发起银行资金转期货响应
CThostFtdcRspTransferField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							  "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							  "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							  "LastFragment": "char", "SessionID": "int", "CustomerName": "string",
							  "IdCardType": "char", "IdentifiedCardNo": "string", "CustType": "char",
							  "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
							  "Password": "string", "InstallID": "int", "FutureSerial": "int", "UserID": "string",
							  "VerifyCertNoFlag": "char", "CurrencyID": "string", "TradeAmount": "float",
							  "FutureFetchAmount": "float", "FeePayFlag": "char", "CustFee": "float",
							  "BrokerFee": "float", "Message": "string", "Digest": "string", "BankAccType": "char",
							  "DeviceID": "string", "BankSecuAccType": "char", "BrokerIDByBank": "string",
							  "BankSecuAcc": "string", "BankPwdFlag": "char", "SecuPwdFlag": "char", "OperNo": "string",
							  "RequestID": "int", "TID": "int", "TransferStatus": "char", "ErrorID": "int",
							  "ErrorMsg": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#客户类型
#银行帐号
#银行密码
#投资者帐号
#期货密码
#安装编号
#期货公司流水号
#用户标识
#验证客户证件号码标志
#币种代码
#转帐金额
#期货可取金额
#费用支付标志
#应收客户费用
#应收期货公司费用
#发送方给接收方的消息
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#请求编号
#交易ID
#转账交易状态
#错误代码
#错误信息
structDict['CThostFtdcRspTransferField'] = CThostFtdcRspTransferField


#冲正请求
CThostFtdcReqRepealField = {"RepealTimeInterval": "int", "RepealedTimes": "int", "BankRepealFlag": "char",
							"BrokerRepealFlag": "char", "PlateRepealSerial": "int", "BankRepealSerial": "string",
							"FutureRepealSerial": "int", "TradeCode": "string", "BankID": "string",
							"BankBranchID": "string", "BrokerID": "string", "BrokerBranchID": "string",
							"TradeDate": "string", "TradeTime": "string", "BankSerial": "string",
							"TradingDay": "string", "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
							"CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
							"CustType": "char", "BankAccount": "string", "BankPassWord": "string",
							"AccountID": "string", "Password": "string", "InstallID": "int", "FutureSerial": "int",
							"UserID": "string", "VerifyCertNoFlag": "char", "CurrencyID": "string",
							"TradeAmount": "float", "FutureFetchAmount": "float", "FeePayFlag": "char",
							"CustFee": "float", "BrokerFee": "float", "Message": "string", "Digest": "string",
							"BankAccType": "char", "DeviceID": "string", "BankSecuAccType": "char",
							"BrokerIDByBank": "string", "BankSecuAcc": "string", "BankPwdFlag": "char",
							"SecuPwdFlag": "char", "OperNo": "string", "RequestID": "int", "TID": "int",
							"TransferStatus": "char"}
#冲正时间间隔
#已经冲正次数
#银行冲正标志
#期商冲正标志
#被冲正平台流水号
#被冲正银行流水号
#被冲正期货流水号
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#客户类型
#银行帐号
#银行密码
#投资者帐号
#期货密码
#安装编号
#期货公司流水号
#用户标识
#验证客户证件号码标志
#币种代码
#转帐金额
#期货可取金额
#费用支付标志
#应收客户费用
#应收期货公司费用
#发送方给接收方的消息
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#请求编号
#交易ID
#转账交易状态
structDict['CThostFtdcReqRepealField'] = CThostFtdcReqRepealField


#冲正响应
CThostFtdcRspRepealField = {"RepealTimeInterval": "int", "RepealedTimes": "int", "BankRepealFlag": "char",
							"BrokerRepealFlag": "char", "PlateRepealSerial": "int", "BankRepealSerial": "string",
							"FutureRepealSerial": "int", "TradeCode": "string", "BankID": "string",
							"BankBranchID": "string", "BrokerID": "string", "BrokerBranchID": "string",
							"TradeDate": "string", "TradeTime": "string", "BankSerial": "string",
							"TradingDay": "string", "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
							"CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
							"CustType": "char", "BankAccount": "string", "BankPassWord": "string",
							"AccountID": "string", "Password": "string", "InstallID": "int", "FutureSerial": "int",
							"UserID": "string", "VerifyCertNoFlag": "char", "CurrencyID": "string",
							"TradeAmount": "float", "FutureFetchAmount": "float", "FeePayFlag": "char",
							"CustFee": "float", "BrokerFee": "float", "Message": "string", "Digest": "string",
							"BankAccType": "char", "DeviceID": "string", "BankSecuAccType": "char",
							"BrokerIDByBank": "string", "BankSecuAcc": "string", "BankPwdFlag": "char",
							"SecuPwdFlag": "char", "OperNo": "string", "RequestID": "int", "TID": "int",
							"TransferStatus": "char", "ErrorID": "int", "ErrorMsg": "string"}
#冲正时间间隔
#已经冲正次数
#银行冲正标志
#期商冲正标志
#被冲正平台流水号
#被冲正银行流水号
#被冲正期货流水号
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#客户类型
#银行帐号
#银行密码
#投资者帐号
#期货密码
#安装编号
#期货公司流水号
#用户标识
#验证客户证件号码标志
#币种代码
#转帐金额
#期货可取金额
#费用支付标志
#应收客户费用
#应收期货公司费用
#发送方给接收方的消息
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#请求编号
#交易ID
#转账交易状态
#错误代码
#错误信息
structDict['CThostFtdcRspRepealField'] = CThostFtdcRspRepealField


#查询账户信息请求
CThostFtdcReqQueryAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								  "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								  "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								  "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
								  "CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								  "CustType": "char", "BankAccount": "string", "BankPassWord": "string",
								  "AccountID": "string", "Password": "string", "FutureSerial": "int",
								  "InstallID": "int", "UserID": "string", "VerifyCertNoFlag": "char",
								  "CurrencyID": "string", "Digest": "string", "BankAccType": "char",
								  "DeviceID": "string", "BankSecuAccType": "char", "BrokerIDByBank": "string",
								  "BankSecuAcc": "string", "BankPwdFlag": "char", "SecuPwdFlag": "char",
								  "OperNo": "string", "RequestID": "int", "TID": "int"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#客户类型
#银行帐号
#银行密码
#投资者帐号
#期货密码
#期货公司流水号
#安装编号
#用户标识
#验证客户证件号码标志
#币种代码
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#请求编号
#交易ID
structDict['CThostFtdcReqQueryAccountField'] = CThostFtdcReqQueryAccountField


#查询账户信息响应
CThostFtdcRspQueryAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								  "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								  "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								  "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
								  "CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								  "CustType": "char", "BankAccount": "string", "BankPassWord": "string",
								  "AccountID": "string", "Password": "string", "FutureSerial": "int",
								  "InstallID": "int", "UserID": "string", "VerifyCertNoFlag": "char",
								  "CurrencyID": "string", "Digest": "string", "BankAccType": "char",
								  "DeviceID": "string", "BankSecuAccType": "char", "BrokerIDByBank": "string",
								  "BankSecuAcc": "string", "BankPwdFlag": "char", "SecuPwdFlag": "char",
								  "OperNo": "string", "RequestID": "int", "TID": "int", "BankUseAmount": "float",
								  "BankFetchAmount": "float"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#客户类型
#银行帐号
#银行密码
#投资者帐号
#期货密码
#期货公司流水号
#安装编号
#用户标识
#验证客户证件号码标志
#币种代码
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#请求编号
#交易ID
#银行可用金额
#银行可取金额
structDict['CThostFtdcRspQueryAccountField'] = CThostFtdcRspQueryAccountField


#期商签到签退
CThostFtdcFutureSignIOField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
							   "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
							   "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
							   "PlateSerial": "int", "LastFragment": "char", "SessionID": "int", "InstallID": "int",
							   "UserID": "string", "Digest": "string", "CurrencyID": "string", "DeviceID": "string",
							   "BrokerIDByBank": "string", "OperNo": "string", "RequestID": "int", "TID": "int"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#安装编号
#用户标识
#摘要
#币种代码
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
structDict['CThostFtdcFutureSignIOField'] = CThostFtdcFutureSignIOField


#期商签到响应
CThostFtdcRspFutureSignInField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								  "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								  "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								  "PlateSerial": "int", "LastFragment": "char", "SessionID": "int", "InstallID": "int",
								  "UserID": "string", "Digest": "string", "CurrencyID": "string", "DeviceID": "string",
								  "BrokerIDByBank": "string", "OperNo": "string", "RequestID": "int", "TID": "int",
								  "ErrorID": "int", "ErrorMsg": "string", "PinKey": "string", "MacKey": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#安装编号
#用户标识
#摘要
#币种代码
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
#错误代码
#错误信息
#PIN密钥
#MAC密钥
structDict['CThostFtdcRspFutureSignInField'] = CThostFtdcRspFutureSignInField


#期商签退请求
CThostFtdcReqFutureSignOutField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								   "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								   "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								   "PlateSerial": "int", "LastFragment": "char", "SessionID": "int", "InstallID": "int",
								   "UserID": "string", "Digest": "string", "CurrencyID": "string", "DeviceID": "string",
								   "BrokerIDByBank": "string", "OperNo": "string", "RequestID": "int", "TID": "int"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#安装编号
#用户标识
#摘要
#币种代码
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
structDict['CThostFtdcReqFutureSignOutField'] = CThostFtdcReqFutureSignOutField


#期商签退响应
CThostFtdcRspFutureSignOutField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								   "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								   "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								   "PlateSerial": "int", "LastFragment": "char", "SessionID": "int", "InstallID": "int",
								   "UserID": "string", "Digest": "string", "CurrencyID": "string", "DeviceID": "string",
								   "BrokerIDByBank": "string", "OperNo": "string", "RequestID": "int", "TID": "int",
								   "ErrorID": "int", "ErrorMsg": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#安装编号
#用户标识
#摘要
#币种代码
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
#错误代码
#错误信息
structDict['CThostFtdcRspFutureSignOutField'] = CThostFtdcRspFutureSignOutField


#查询指定流水号的交易结果请求
CThostFtdcReqQueryTradeResultBySerialField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
											  "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
											  "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
											  "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
											  "Reference": "int", "RefrenceIssureType": "char",
											  "RefrenceIssure": "string", "CustomerName": "string",
											  "IdCardType": "char", "IdentifiedCardNo": "string", "CustType": "char",
											  "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
											  "Password": "string", "CurrencyID": "string", "TradeAmount": "float",
											  "Digest": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#流水号
#本流水号发布者的机构类型
#本流水号发布者机构编码
#客户姓名
#证件类型
#证件号码
#客户类型
#银行帐号
#银行密码
#投资者帐号
#期货密码
#币种代码
#转帐金额
#摘要
structDict['CThostFtdcReqQueryTradeResultBySerialField'] = CThostFtdcReqQueryTradeResultBySerialField


#查询指定流水号的交易结果响应
CThostFtdcRspQueryTradeResultBySerialField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
											  "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
											  "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
											  "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
											  "ErrorID": "int", "ErrorMsg": "string", "Reference": "int",
											  "RefrenceIssureType": "char", "RefrenceIssure": "string",
											  "OriginReturnCode": "string", "OriginDescrInfoForReturnCode": "string",
											  "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
											  "Password": "string", "CurrencyID": "string", "TradeAmount": "float",
											  "Digest": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#错误代码
#错误信息
#流水号
#本流水号发布者的机构类型
#本流水号发布者机构编码
#原始返回代码
#原始返回码描述
#银行帐号
#银行密码
#投资者帐号
#期货密码
#币种代码
#转帐金额
#摘要
structDict['CThostFtdcRspQueryTradeResultBySerialField'] = CThostFtdcRspQueryTradeResultBySerialField


#日终文件就绪请求
CThostFtdcReqDayEndFileReadyField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
									 "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
									 "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
									 "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
									 "FileBusinessCode": "char", "Digest": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#文件业务功能
#摘要
structDict['CThostFtdcReqDayEndFileReadyField'] = CThostFtdcReqDayEndFileReadyField


#返回结果
CThostFtdcReturnResultField = {"ReturnCode": "string", "DescrInfoForReturnCode": "string"}
#返回代码
#返回码描述
structDict['CThostFtdcReturnResultField'] = CThostFtdcReturnResultField


#验证期货资金密码
CThostFtdcVerifyFuturePasswordField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
									   "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
									   "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
									   "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
									   "AccountID": "string", "Password": "string", "BankAccount": "string",
									   "BankPassWord": "string", "InstallID": "int", "TID": "int",
									   "CurrencyID": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#投资者帐号
#期货密码
#银行帐号
#银行密码
#安装编号
#交易ID
#币种代码
structDict['CThostFtdcVerifyFuturePasswordField'] = CThostFtdcVerifyFuturePasswordField


#验证客户信息
CThostFtdcVerifyCustInfoField = {"CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								 "CustType": "char"}
#客户姓名
#证件类型
#证件号码
#客户类型
structDict['CThostFtdcVerifyCustInfoField'] = CThostFtdcVerifyCustInfoField


#验证期货资金密码和客户信息
CThostFtdcVerifyFuturePasswordAndCustInfoField = {"CustomerName": "string", "IdCardType": "char",
												  "IdentifiedCardNo": "string", "CustType": "char",
												  "AccountID": "string", "Password": "string", "CurrencyID": "string"}
#客户姓名
#证件类型
#证件号码
#客户类型
#投资者帐号
#期货密码
#币种代码
structDict['CThostFtdcVerifyFuturePasswordAndCustInfoField'] = CThostFtdcVerifyFuturePasswordAndCustInfoField


#验证期货资金密码和客户信息
CThostFtdcDepositResultInformField = {"DepositSeqNo": "string", "BrokerID": "string", "InvestorID": "string",
									  "Deposit": "float", "RequestID": "int", "ReturnCode": "string",
									  "DescrInfoForReturnCode": "string"}
#出入金流水号，该流水号为银期报盘返回的流水号
#经纪公司代码
#投资者代码
#入金金额
#请求编号
#返回代码
#返回码描述
structDict['CThostFtdcDepositResultInformField'] = CThostFtdcDepositResultInformField


#交易核心向银期报盘发出密钥同步请求
CThostFtdcReqSyncKeyField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							 "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							 "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							 "LastFragment": "char", "SessionID": "int", "InstallID": "int", "UserID": "string",
							 "Message": "string", "DeviceID": "string", "BrokerIDByBank": "string", "OperNo": "string",
							 "RequestID": "int", "TID": "int"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#安装编号
#用户标识
#交易核心给银期报盘的消息
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
structDict['CThostFtdcReqSyncKeyField'] = CThostFtdcReqSyncKeyField


#交易核心向银期报盘发出密钥同步响应
CThostFtdcRspSyncKeyField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							 "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							 "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							 "LastFragment": "char", "SessionID": "int", "InstallID": "int", "UserID": "string",
							 "Message": "string", "DeviceID": "string", "BrokerIDByBank": "string", "OperNo": "string",
							 "RequestID": "int", "TID": "int", "ErrorID": "int", "ErrorMsg": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#安装编号
#用户标识
#交易核心给银期报盘的消息
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
#错误代码
#错误信息
structDict['CThostFtdcRspSyncKeyField'] = CThostFtdcRspSyncKeyField


#查询账户信息通知
CThostFtdcNotifyQueryAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
									 "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
									 "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
									 "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
									 "CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
									 "CustType": "char", "BankAccount": "string", "BankPassWord": "string",
									 "AccountID": "string", "Password": "string", "FutureSerial": "int",
									 "InstallID": "int", "UserID": "string", "VerifyCertNoFlag": "char",
									 "CurrencyID": "string", "Digest": "string", "BankAccType": "char",
									 "DeviceID": "string", "BankSecuAccType": "char", "BrokerIDByBank": "string",
									 "BankSecuAcc": "string", "BankPwdFlag": "char", "SecuPwdFlag": "char",
									 "OperNo": "string", "RequestID": "int", "TID": "int", "BankUseAmount": "float",
									 "BankFetchAmount": "float", "ErrorID": "int", "ErrorMsg": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#客户类型
#银行帐号
#银行密码
#投资者帐号
#期货密码
#期货公司流水号
#安装编号
#用户标识
#验证客户证件号码标志
#币种代码
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#请求编号
#交易ID
#银行可用金额
#银行可取金额
#错误代码
#错误信息
structDict['CThostFtdcNotifyQueryAccountField'] = CThostFtdcNotifyQueryAccountField


#银期转账交易流水表
CThostFtdcTransferSerialField = {"PlateSerial": "int", "TradeDate": "string", "TradingDay": "string",
								 "TradeTime": "string", "TradeCode": "string", "SessionID": "int", "BankID": "string",
								 "BankBranchID": "string", "BankAccType": "char", "BankAccount": "string",
								 "BankSerial": "string", "BrokerID": "string", "BrokerBranchID": "string",
								 "FutureAccType": "char", "AccountID": "string", "InvestorID": "string",
								 "FutureSerial": "int", "IdCardType": "char", "IdentifiedCardNo": "string",
								 "CurrencyID": "string", "TradeAmount": "float", "CustFee": "float",
								 "BrokerFee": "float", "AvailabilityFlag": "char", "OperatorCode": "string",
								 "BankNewAccount": "string", "ErrorID": "int", "ErrorMsg": "string"}
#平台流水号
#交易发起方日期
#交易日期
#交易时间
#交易代码
#会话编号
#银行编码
#银行分支机构编码
#银行帐号类型
#银行帐号
#银行流水号
#期货公司编码
#期商分支机构代码
#期货公司帐号类型
#投资者帐号
#投资者代码
#期货公司流水号
#证件类型
#证件号码
#币种代码
#交易金额
#应收客户费用
#应收期货公司费用
#有效标志
#操作员
#新银行帐号
#错误代码
#错误信息
structDict['CThostFtdcTransferSerialField'] = CThostFtdcTransferSerialField


#请求查询转帐流水
CThostFtdcQryTransferSerialField = {"BrokerID": "string", "AccountID": "string", "BankID": "string",
									"CurrencyID": "string"}
#经纪公司代码
#投资者帐号
#银行编码
#币种代码
structDict['CThostFtdcQryTransferSerialField'] = CThostFtdcQryTransferSerialField


#期商签到通知
CThostFtdcNotifyFutureSignInField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
									 "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
									 "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
									 "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
									 "InstallID": "int", "UserID": "string", "Digest": "string", "CurrencyID": "string",
									 "DeviceID": "string", "BrokerIDByBank": "string", "OperNo": "string",
									 "RequestID": "int", "TID": "int", "ErrorID": "int", "ErrorMsg": "string",
									 "PinKey": "string", "MacKey": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#安装编号
#用户标识
#摘要
#币种代码
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
#错误代码
#错误信息
#PIN密钥
#MAC密钥
structDict['CThostFtdcNotifyFutureSignInField'] = CThostFtdcNotifyFutureSignInField


#期商签退通知
CThostFtdcNotifyFutureSignOutField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
									  "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
									  "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
									  "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
									  "InstallID": "int", "UserID": "string", "Digest": "string",
									  "CurrencyID": "string", "DeviceID": "string", "BrokerIDByBank": "string",
									  "OperNo": "string", "RequestID": "int", "TID": "int", "ErrorID": "int",
									  "ErrorMsg": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#安装编号
#用户标识
#摘要
#币种代码
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
#错误代码
#错误信息
structDict['CThostFtdcNotifyFutureSignOutField'] = CThostFtdcNotifyFutureSignOutField


#交易核心向银期报盘发出密钥同步处理结果的通知
CThostFtdcNotifySyncKeyField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								"BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								"TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								"PlateSerial": "int", "LastFragment": "char", "SessionID": "int", "InstallID": "int",
								"UserID": "string", "Message": "string", "DeviceID": "string",
								"BrokerIDByBank": "string", "OperNo": "string", "RequestID": "int", "TID": "int",
								"ErrorID": "int", "ErrorMsg": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#安装编号
#用户标识
#交易核心给银期报盘的消息
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
#错误代码
#错误信息
structDict['CThostFtdcNotifySyncKeyField'] = CThostFtdcNotifySyncKeyField


#请求查询银期签约关系
CThostFtdcQryAccountregisterField = {"BrokerID": "string", "AccountID": "string", "BankID": "string",
									 "BankBranchID": "string", "CurrencyID": "string"}
#经纪公司代码
#投资者帐号
#银行编码
#银行分支机构编码
#币种代码
structDict['CThostFtdcQryAccountregisterField'] = CThostFtdcQryAccountregisterField


#客户开销户信息表
CThostFtdcAccountregisterField = {"TradeDay": "string", "BankID": "string", "BankBranchID": "string",
								  "BankAccount": "string", "BrokerID": "string", "BrokerBranchID": "string",
								  "AccountID": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								  "CustomerName": "string", "CurrencyID": "string", "OpenOrDestroy": "char",
								  "RegDate": "string", "OutDate": "string", "TID": "int", "CustType": "char",
								  "BankAccType": "char"}
#交易日期
#银行编码
#银行分支机构编码
#银行帐号
#期货公司编码
#期货公司分支机构编码
#投资者帐号
#证件类型
#证件号码
#客户姓名
#币种代码
#开销户类别
#签约日期
#解约日期
#交易ID
#客户类型
#银行帐号类型
structDict['CThostFtdcAccountregisterField'] = CThostFtdcAccountregisterField


#银期开户信息
CThostFtdcOpenAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							  "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							  "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							  "LastFragment": "char", "SessionID": "int", "CustomerName": "string",
							  "IdCardType": "char", "IdentifiedCardNo": "string", "Gender": "char",
							  "CountryCode": "string", "CustType": "char", "Address": "string", "ZipCode": "string",
							  "Telephone": "string", "MobilePhone": "string", "Fax": "string", "EMail": "string",
							  "MoneyAccountStatus": "char", "BankAccount": "string", "BankPassWord": "string",
							  "AccountID": "string", "Password": "string", "InstallID": "int",
							  "VerifyCertNoFlag": "char", "CurrencyID": "string", "CashExchangeCode": "char",
							  "Digest": "string", "BankAccType": "char", "DeviceID": "string",
							  "BankSecuAccType": "char", "BrokerIDByBank": "string", "BankSecuAcc": "string",
							  "BankPwdFlag": "char", "SecuPwdFlag": "char", "OperNo": "string", "TID": "int",
							  "UserID": "string", "ErrorID": "int", "ErrorMsg": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#性别
#国家代码
#客户类型
#地址
#邮编
#电话号码
#手机
#传真
#电子邮件
#资金账户状态
#银行帐号
#银行密码
#投资者帐号
#期货密码
#安装编号
#验证客户证件号码标志
#币种代码
#汇钞标志
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#交易ID
#用户标识
#错误代码
#错误信息
structDict['CThostFtdcOpenAccountField'] = CThostFtdcOpenAccountField


#银期销户信息
CThostFtdcCancelAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								"BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								"TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								"PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
								"CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								"Gender": "char", "CountryCode": "string", "CustType": "char", "Address": "string",
								"ZipCode": "string", "Telephone": "string", "MobilePhone": "string", "Fax": "string",
								"EMail": "string", "MoneyAccountStatus": "char", "BankAccount": "string",
								"BankPassWord": "string", "AccountID": "string", "Password": "string",
								"InstallID": "int", "VerifyCertNoFlag": "char", "CurrencyID": "string",
								"CashExchangeCode": "char", "Digest": "string", "BankAccType": "char",
								"DeviceID": "string", "BankSecuAccType": "char", "BrokerIDByBank": "string",
								"BankSecuAcc": "string", "BankPwdFlag": "char", "SecuPwdFlag": "char",
								"OperNo": "string", "TID": "int", "UserID": "string", "ErrorID": "int",
								"ErrorMsg": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#性别
#国家代码
#客户类型
#地址
#邮编
#电话号码
#手机
#传真
#电子邮件
#资金账户状态
#银行帐号
#银行密码
#投资者帐号
#期货密码
#安装编号
#验证客户证件号码标志
#币种代码
#汇钞标志
#摘要
#银行帐号类型
#渠道标志
#期货单位帐号类型
#期货公司银行编码
#期货单位帐号
#银行密码标志
#期货资金密码核对标志
#交易柜员
#交易ID
#用户标识
#错误代码
#错误信息
structDict['CThostFtdcCancelAccountField'] = CThostFtdcCancelAccountField


#银期变更银行账号信息
CThostFtdcChangeAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								"BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								"TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								"PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
								"CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								"Gender": "char", "CountryCode": "string", "CustType": "char", "Address": "string",
								"ZipCode": "string", "Telephone": "string", "MobilePhone": "string", "Fax": "string",
								"EMail": "string", "MoneyAccountStatus": "char", "BankAccount": "string",
								"BankPassWord": "string", "NewBankAccount": "string", "NewBankPassWord": "string",
								"AccountID": "string", "Password": "string", "BankAccType": "char", "InstallID": "int",
								"VerifyCertNoFlag": "char", "CurrencyID": "string", "BrokerIDByBank": "string",
								"BankPwdFlag": "char", "SecuPwdFlag": "char", "TID": "int", "Digest": "string",
								"ErrorID": "int", "ErrorMsg": "string"}
#业务功能码
#银行代码
#银行分支机构代码
#期商代码
#期商分支机构代码
#交易日期
#交易时间
#银行流水号
#交易系统日期
#银期平台消息流水号
#最后分片标志
#会话号
#客户姓名
#证件类型
#证件号码
#性别
#国家代码
#客户类型
#地址
#邮编
#电话号码
#手机
#传真
#电子邮件
#资金账户状态
#银行帐号
#银行密码
#新银行帐号
#新银行密码
#投资者帐号
#期货密码
#银行帐号类型
#安装编号
#验证客户证件号码标志
#币种代码
#期货公司银行编码
#银行密码标志
#期货资金密码核对标志
#交易ID
#摘要
#错误代码
#错误信息
structDict['CThostFtdcChangeAccountField'] = CThostFtdcChangeAccountField


#二级代理操作员银期权限
CThostFtdcSecAgentACIDMapField = {"BrokerID": "string", "UserID": "string", "AccountID": "string",
								  "CurrencyID": "string", "BrokerSecAgentID": "string"}
#经纪公司代码
#用户代码
#资金账户
#币种
#境外中介机构资金帐号
structDict['CThostFtdcSecAgentACIDMapField'] = CThostFtdcSecAgentACIDMapField


#二级代理操作员银期权限查询
CThostFtdcQrySecAgentACIDMapField = {"BrokerID": "string", "UserID": "string", "AccountID": "string",
									 "CurrencyID": "string"}
#经纪公司代码
#用户代码
#资金账户
#币种
structDict['CThostFtdcQrySecAgentACIDMapField'] = CThostFtdcQrySecAgentACIDMapField


#灾备中心交易权限
CThostFtdcUserRightsAssignField = {"BrokerID": "string", "UserID": "string", "DRIdentityID": "int"}
#应用单元代码
#用户代码
#交易中心代码
structDict['CThostFtdcUserRightsAssignField'] = CThostFtdcUserRightsAssignField


#经济公司是否有在本标示的交易权限
CThostFtdcBrokerUserRightAssignField = {"BrokerID": "string", "DRIdentityID": "int", "Tradeable": "int"}
#应用单元代码
#交易中心代码
#能否交易
structDict['CThostFtdcBrokerUserRightAssignField'] = CThostFtdcBrokerUserRightAssignField


#灾备交易转换报文
CThostFtdcDRTransferField = {"OrigDRIdentityID": "int", "DestDRIdentityID": "int", "OrigBrokerID": "string",
							 "DestBrokerID": "string"}
#原交易中心代码
#目标交易中心代码
#原应用单元代码
#目标易用单元代码
structDict['CThostFtdcDRTransferField'] = CThostFtdcDRTransferField


#Fens用户信息
CThostFtdcFensUserInfoField = {"BrokerID": "string", "UserID": "string", "LoginMode": "char"}
#经纪公司代码
#用户代码
#登录模式
structDict['CThostFtdcFensUserInfoField'] = CThostFtdcFensUserInfoField


#当前银期所属交易中心
CThostFtdcCurrTransferIdentityField = {"IdentityID": "int"}
#交易中心代码
structDict['CThostFtdcCurrTransferIdentityField'] = CThostFtdcCurrTransferIdentityField


#禁止登录用户
CThostFtdcLoginForbiddenUserField = {"BrokerID": "string", "UserID": "string", "IPAddress": "string"}
#经纪公司代码
#用户代码
#IP地址
structDict['CThostFtdcLoginForbiddenUserField'] = CThostFtdcLoginForbiddenUserField


#查询禁止登录用户
CThostFtdcQryLoginForbiddenUserField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CThostFtdcQryLoginForbiddenUserField'] = CThostFtdcQryLoginForbiddenUserField


#UDP组播组信息
CThostFtdcMulticastGroupInfoField = {"GroupIP": "string", "GroupPort": "int", "SourceIP": "string"}
#组播组IP地址
#组播组IP端口
#源地址
structDict['CThostFtdcMulticastGroupInfoField'] = CThostFtdcMulticastGroupInfoField


#资金账户基本准备金
CThostFtdcTradingAccountReserveField = {"BrokerID": "string", "AccountID": "string", "Reserve": "float",
										"CurrencyID": "string"}
#经纪公司代码
#投资者帐号
#基本准备金
#币种代码
structDict['CThostFtdcTradingAccountReserveField'] = CThostFtdcTradingAccountReserveField


#DBF记录
CThostFtdcDBFRecordField = {"DBFComdType": "string", "DBFComTime": "string", "DBFOComNo": "string",
							"DBFComNo": "string", "DBFFdName1": "string", "DBFFdContent1": "string",
							"DBFFdName2": "string", "DBFFdContent2": "string", "DBFFdName3": "string",
							"DBFFdContent3": "string", "DBFFdName4": "string", "DBFFdContent4": "string"}
#DBF命令类型
#DBF时间类型
#DBF原始流水号类型
#DBF流水号类型
#DBF字段类型
#DBF字段内容类型
#DBF字段类型
#DBF字段内容类型
#DBF字段类型
#DBF字段内容类型
#DBF字段类型
#DBF字段内容类型
structDict['CThostFtdcDBFRecordField'] = CThostFtdcDBFRecordField





