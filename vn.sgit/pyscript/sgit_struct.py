# encoding: UTF-8

structDict = {}

#//////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////










#信息分发
CSgitFtdcDisseminationField = {"SequenceSeries": "short", "SequenceNo": "int"}
#序列系列号
#序列号
structDict['CSgitFtdcDisseminationField'] = CSgitFtdcDisseminationField


#用户登录请求
CSgitFtdcReqUserLoginField = {"TradingDay": "string", "BrokerID": "string", "UserID": "string", "Password": "string",
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
structDict['CSgitFtdcReqUserLoginField'] = CSgitFtdcReqUserLoginField


#用户登录应答
CSgitFtdcRspUserLoginField = {"TradingDay": "string", "LoginTime": "string", "BrokerID": "string", "UserID": "string",
							  "SystemName": "string", "FrontID": "int", "SessionID": "int", "MaxOrderRef": "string",
							  "SHFETime": "string", "DCETime": "string", "CZCETime": "string", "FFEXTime": "string"}
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
structDict['CSgitFtdcRspUserLoginField'] = CSgitFtdcRspUserLoginField


#用户登出请求
CSgitFtdcUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSgitFtdcUserLogoutField'] = CSgitFtdcUserLogoutField


#强制交易员退出
CSgitFtdcForceUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSgitFtdcForceUserLogoutField'] = CSgitFtdcForceUserLogoutField


#客户端认证请求
CSgitFtdcReqAuthenticateField = {"BrokerID": "string", "UserID": "string", "UserProductInfo": "string",
								 "AuthCode": "string"}
#经纪公司代码
#用户代码
#用户端产品信息
#认证码
structDict['CSgitFtdcReqAuthenticateField'] = CSgitFtdcReqAuthenticateField


#客户端认证响应
CSgitFtdcRspAuthenticateField = {"BrokerID": "string", "UserID": "string", "UserProductInfo": "string"}
#经纪公司代码
#用户代码
#用户端产品信息
structDict['CSgitFtdcRspAuthenticateField'] = CSgitFtdcRspAuthenticateField


#客户端认证信息
CSgitFtdcAuthenticationInfoField = {"BrokerID": "string", "UserID": "string", "UserProductInfo": "string",
									"AuthInfo": "string", "IsResult": "int"}
#经纪公司代码
#用户代码
#用户端产品信息
#认证信息
#是否为认证结果
structDict['CSgitFtdcAuthenticationInfoField'] = CSgitFtdcAuthenticationInfoField


#银期转帐报文头
CSgitFtdcTransferHeaderField = {"Version": "string", "TradeCode": "string", "TradeDate": "string",
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
structDict['CSgitFtdcTransferHeaderField'] = CSgitFtdcTransferHeaderField


#银行资金转期货请求，TradeCode=202001
CSgitFtdcTransferBankToFutureReqField = {"FutureAccount": "string", "FuturePwdFlag": "char", "FutureAccPwd": "string",
										 "TradeAmt": "float", "CustFee": "float", "CurrencyCode": "string"}
#期货资金账户
#密码标志
#密码
#转账金额
#客户手续费
#币种：RMB-人民币 USD-美圆 HKD-港元
structDict['CSgitFtdcTransferBankToFutureReqField'] = CSgitFtdcTransferBankToFutureReqField


#银行资金转期货请求响应
CSgitFtdcTransferBankToFutureRspField = {"RetCode": "string", "RetInfo": "string", "FutureAccount": "string",
										 "TradeAmt": "float", "CustFee": "float", "CurrencyCode": "string"}
#响应代码
#响应信息
#资金账户
#转帐金额
#应收客户手续费
#币种
structDict['CSgitFtdcTransferBankToFutureRspField'] = CSgitFtdcTransferBankToFutureRspField


#期货资金转银行请求，TradeCode=202002
CSgitFtdcTransferFutureToBankReqField = {"FutureAccount": "string", "FuturePwdFlag": "char", "FutureAccPwd": "string",
										 "TradeAmt": "float", "CustFee": "float", "CurrencyCode": "string"}
#期货资金账户
#密码标志
#密码
#转账金额
#客户手续费
#币种：RMB-人民币 USD-美圆 HKD-港元
structDict['CSgitFtdcTransferFutureToBankReqField'] = CSgitFtdcTransferFutureToBankReqField


#期货资金转银行请求响应
CSgitFtdcTransferFutureToBankRspField = {"RetCode": "string", "RetInfo": "string", "FutureAccount": "string",
										 "TradeAmt": "float", "CustFee": "float", "CurrencyCode": "string"}
#响应代码
#响应信息
#资金账户
#转帐金额
#应收客户手续费
#币种
structDict['CSgitFtdcTransferFutureToBankRspField'] = CSgitFtdcTransferFutureToBankRspField


#查询银行资金请求，TradeCode=204002
CSgitFtdcTransferQryBankReqField = {"FutureAccount": "string", "FuturePwdFlag": "char", "FutureAccPwd": "string",
									"CurrencyCode": "string"}
#期货资金账户
#密码标志
#密码
#币种：RMB-人民币 USD-美圆 HKD-港元
structDict['CSgitFtdcTransferQryBankReqField'] = CSgitFtdcTransferQryBankReqField


#查询银行资金请求响应
CSgitFtdcTransferQryBankRspField = {"RetCode": "string", "RetInfo": "string", "FutureAccount": "string",
									"TradeAmt": "float", "UseAmt": "float", "FetchAmt": "float",
									"CurrencyCode": "string"}
#响应代码
#响应信息
#资金账户
#银行余额
#银行可用余额
#银行可取余额
#币种
structDict['CSgitFtdcTransferQryBankRspField'] = CSgitFtdcTransferQryBankRspField


#查询银行交易明细请求，TradeCode=204999
CSgitFtdcTransferQryDetailReqField = {"FutureAccount": "string"}
#期货资金账户
structDict['CSgitFtdcTransferQryDetailReqField'] = CSgitFtdcTransferQryDetailReqField


#查询银行交易明细请求响应
CSgitFtdcTransferQryDetailRspField = {"TradeDate": "string", "TradeTime": "string", "TradeCode": "string",
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
structDict['CSgitFtdcTransferQryDetailRspField'] = CSgitFtdcTransferQryDetailRspField


#响应信息
CSgitFtdcRspInfoField = {"ErrorID": "int", "ErrorMsg": "string"}
#错误代码
#错误信息
structDict['CSgitFtdcRspInfoField'] = CSgitFtdcRspInfoField


#交易所
CSgitFtdcExchangeField = {"ExchangeID": "string", "ExchangeName": "string", "ExchangeProperty": "char"}
#交易所代码
#交易所名称
#交易所属性
structDict['CSgitFtdcExchangeField'] = CSgitFtdcExchangeField


#产品
CSgitFtdcProductField = {"ProductID": "string", "ProductName": "string", "ExchangeID": "string", "ProductClass": "char",
						 "VolumeMultiple": "int", "PriceTick": "float", "MaxMarketOrderVolume": "int",
						 "MinMarketOrderVolume": "int", "MaxLimitOrderVolume": "int", "MinLimitOrderVolume": "int",
						 "PositionType": "char", "PositionDateType": "char"}
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
structDict['CSgitFtdcProductField'] = CSgitFtdcProductField


#合约
CSgitFtdcInstrumentField = {"InstrumentID": "string", "ExchangeID": "string", "InstrumentName": "string",
							"ExchangeInstID": "string", "ProductID": "string", "ProductClass": "char",
							"DeliveryYear": "int", "DeliveryMonth": "int", "MaxMarketOrderVolume": "int",
							"MinMarketOrderVolume": "int", "MaxLimitOrderVolume": "int", "MinLimitOrderVolume": "int",
							"VolumeMultiple": "int", "PriceTick": "float", "CreateDate": "string", "OpenDate": "string",
							"ExpireDate": "string", "StartDelivDate": "string", "EndDelivDate": "string",
							"InstLifePhase": "char", "IsTrading": "int", "PositionType": "char",
							"PositionDateType": "char", "LongMarginRatio": "float", "ShortMarginRatio": "float"}
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
structDict['CSgitFtdcInstrumentField'] = CSgitFtdcInstrumentField


#经纪公司
CSgitFtdcBrokerField = {"BrokerID": "string", "BrokerAbbr": "string", "BrokerName": "string", "IsActive": "int"}
#经纪公司代码
#经纪公司简称
#经纪公司名称
#是否活跃
structDict['CSgitFtdcBrokerField'] = CSgitFtdcBrokerField


#交易所交易员
CSgitFtdcTraderField = {"ExchangeID": "string", "TraderID": "string", "ParticipantID": "string", "Password": "string",
						"InstallCount": "int", "BrokerID": "string"}
#交易所代码
#交易所交易员代码
#会员代码
#密码
#安装数量
#经纪公司代码
structDict['CSgitFtdcTraderField'] = CSgitFtdcTraderField


#投资者
CSgitFtdcInvestorField = {"InvestorID": "string", "BrokerID": "string", "InvestorGroupID": "string",
						  "InvestorName": "string", "IdentifiedCardType": "char", "IdentifiedCardNo": "string",
						  "IsActive": "int", "Telephone": "string", "Address": "string", "OpenDate": "string",
						  "Mobile": "string", "CommModelID": "string"}
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
structDict['CSgitFtdcInvestorField'] = CSgitFtdcInvestorField


#交易编码
CSgitFtdcTradingCodeField = {"InvestorID": "string", "BrokerID": "string", "ExchangeID": "string", "ClientID": "string",
							 "IsActive": "int", "ClientIDType": "char"}
#投资者代码
#经纪公司代码
#交易所代码
#客户代码
#是否活跃
#交易编码类型
structDict['CSgitFtdcTradingCodeField'] = CSgitFtdcTradingCodeField


#会员编码和经纪公司编码对照表
CSgitFtdcPartBrokerField = {"BrokerID": "string", "ExchangeID": "string", "ParticipantID": "string", "IsActive": "int"}
#经纪公司代码
#交易所代码
#会员代码
#是否活跃
structDict['CSgitFtdcPartBrokerField'] = CSgitFtdcPartBrokerField


#管理用户
CSgitFtdcSuperUserField = {"UserID": "string", "UserName": "string", "Password": "string", "IsActive": "int"}
#用户代码
#用户名称
#密码
#是否活跃
structDict['CSgitFtdcSuperUserField'] = CSgitFtdcSuperUserField


#管理用户功能权限
CSgitFtdcSuperUserFunctionField = {"UserID": "string", "FunctionCode": "char"}
#用户代码
#功能代码
structDict['CSgitFtdcSuperUserFunctionField'] = CSgitFtdcSuperUserFunctionField


#投资者组
CSgitFtdcInvestorGroupField = {"BrokerID": "string", "InvestorGroupID": "string", "InvestorGroupName": "string"}
#经纪公司代码
#投资者分组代码
#投资者分组名称
structDict['CSgitFtdcInvestorGroupField'] = CSgitFtdcInvestorGroupField


#资金账户
CSgitFtdcTradingAccountField = {"BrokerID": "string", "AccountID": "string", "PreMortgage": "float",
								"PreCredit": "float", "PreDeposit": "float", "PreBalance": "float",
								"PreMargin": "float", "InterestBase": "float", "Interest": "float", "Deposit": "float",
								"Withdraw": "float", "FrozenMargin": "float", "FrozenCash": "float",
								"FrozenCommission": "float", "CurrMargin": "float", "CashIn": "float",
								"Commission": "float", "CloseProfit": "float", "PositionProfit": "float",
								"Balance": "float", "Available": "float", "WithdrawQuota": "float", "Reserve": "float",
								"TradingDay": "string", "SettlementID": "int", "Credit": "float", "Mortgage": "float",
								"ExchangeMargin": "float", "DeliveryMargin": "float", "ExchangeDeliveryMargin": "float"}
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
structDict['CSgitFtdcTradingAccountField'] = CSgitFtdcTradingAccountField


#投资者持仓
CSgitFtdcInvestorPositionField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
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
								  "CombShortFrozen": "int", "CloseProfitByDate": "float", "CloseProfitByTrade": "float",
								  "TodayPosition": "int", "MarginRateByMoney": "float", "MarginRateByVolume": "float"}
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
structDict['CSgitFtdcInvestorPositionField'] = CSgitFtdcInvestorPositionField


#合约保证金率
CSgitFtdcInstrumentMarginRateField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
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
structDict['CSgitFtdcInstrumentMarginRateField'] = CSgitFtdcInstrumentMarginRateField


#合约手续费率
CSgitFtdcInstrumentCommissionRateField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
										  "InvestorID": "string", "OpenRatioByMoney": "float",
										  "OpenRatioByVolume": "float", "CloseRatioByMoney": "float",
										  "CloseRatioByVolume": "float", "CloseTodayRatioByMoney": "float",
										  "CloseTodayRatioByVolume": "float"}
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
structDict['CSgitFtdcInstrumentCommissionRateField'] = CSgitFtdcInstrumentCommissionRateField


#深度行情
CSgitFtdcDepthMarketDataField = {"TradingDay": "string", "InstrumentID": "string", "ExchangeID": "string",
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
								 "AveragePrice": "float"}
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
structDict['CSgitFtdcDepthMarketDataField'] = CSgitFtdcDepthMarketDataField


#投资者合约交易权限
CSgitFtdcInstrumentTradingRightField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
										"InvestorID": "string", "TradingRight": "char"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#交易权限
structDict['CSgitFtdcInstrumentTradingRightField'] = CSgitFtdcInstrumentTradingRightField


#经纪公司用户
CSgitFtdcBrokerUserField = {"BrokerID": "string", "UserID": "string", "UserName": "string", "UserType": "char",
							"IsActive": "int", "IsUsingOTP": "int"}
#经纪公司代码
#用户代码
#用户名称
#用户类型
#是否活跃
#是否使用令牌
structDict['CSgitFtdcBrokerUserField'] = CSgitFtdcBrokerUserField


#经纪公司用户口令
CSgitFtdcBrokerUserPasswordField = {"BrokerID": "string", "UserID": "string", "Password": "string"}
#经纪公司代码
#用户代码
#密码
structDict['CSgitFtdcBrokerUserPasswordField'] = CSgitFtdcBrokerUserPasswordField


#经纪公司用户功能权限
CSgitFtdcBrokerUserFunctionField = {"BrokerID": "string", "UserID": "string", "BrokerFunctionCode": "char"}
#经纪公司代码
#用户代码
#经纪公司功能代码
structDict['CSgitFtdcBrokerUserFunctionField'] = CSgitFtdcBrokerUserFunctionField


#交易所交易员报盘机
CSgitFtdcTraderOfferField = {"ExchangeID": "string", "TraderID": "string", "ParticipantID": "string",
							 "Password": "string", "InstallID": "int", "OrderLocalID": "string",
							 "TraderConnectStatus": "char", "ConnectRequestDate": "string",
							 "ConnectRequestTime": "string", "LastReportDate": "string", "LastReportTime": "string",
							 "ConnectDate": "string", "ConnectTime": "string", "StartDate": "string",
							 "StartTime": "string", "TradingDay": "string", "BrokerID": "string",
							 "MaxTradeID": "string", "MaxOrderMessageReference": "string"}
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
structDict['CSgitFtdcTraderOfferField'] = CSgitFtdcTraderOfferField


#投资者结算结果
CSgitFtdcSettlementInfoField = {"TradingDay": "string", "SettlementID": "int", "BrokerID": "string",
								"InvestorID": "string", "SequenceNo": "int", "Content": "string"}
#交易日
#结算编号
#经纪公司代码
#投资者代码
#序号
#消息正文
structDict['CSgitFtdcSettlementInfoField'] = CSgitFtdcSettlementInfoField


#合约保证金率调整
CSgitFtdcInstrumentMarginRateAdjustField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
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
structDict['CSgitFtdcInstrumentMarginRateAdjustField'] = CSgitFtdcInstrumentMarginRateAdjustField


#交易所保证金率
CSgitFtdcExchangeMarginRateField = {"BrokerID": "string", "InstrumentID": "string", "HedgeFlag": "char",
									"LongMarginRatioByMoney": "float", "LongMarginRatioByVolume": "float",
									"ShortMarginRatioByMoney": "float", "ShortMarginRatioByVolume": "float"}
#经纪公司代码
#合约代码
#投机套保标志
#多头保证金率
#多头保证金费
#空头保证金率
#空头保证金费
structDict['CSgitFtdcExchangeMarginRateField'] = CSgitFtdcExchangeMarginRateField


#交易所保证金率调整
CSgitFtdcExchangeMarginRateAdjustField = {"BrokerID": "string", "InstrumentID": "string", "HedgeFlag": "char",
										  "LongMarginRatioByMoney": "float", "LongMarginRatioByVolume": "float",
										  "ShortMarginRatioByMoney": "float", "ShortMarginRatioByVolume": "float",
										  "ExchLongMarginRatioByMoney": "float", "ExchLongMarginRatioByVolume": "float",
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
structDict['CSgitFtdcExchangeMarginRateAdjustField'] = CSgitFtdcExchangeMarginRateAdjustField


#结算引用
CSgitFtdcSettlementRefField = {"TradingDay": "string", "SettlementID": "int"}
#交易日
#结算编号
structDict['CSgitFtdcSettlementRefField'] = CSgitFtdcSettlementRefField


#当前时间
CSgitFtdcCurrentTimeField = {"CurrDate": "string", "CurrTime": "string", "CurrMillisec": "int"}
#当前日期
#当前时间
#当前时间（毫秒）
structDict['CSgitFtdcCurrentTimeField'] = CSgitFtdcCurrentTimeField


#通讯阶段
CSgitFtdcCommPhaseField = {"TradingDay": "string", "CommPhaseNo": "short"}
#交易日
#通讯时段编号
structDict['CSgitFtdcCommPhaseField'] = CSgitFtdcCommPhaseField


#登录信息
CSgitFtdcLoginInfoField = {"FrontID": "int", "SessionID": "int", "BrokerID": "string", "UserID": "string",
						   "LoginDate": "string", "LoginTime": "string", "IPAddress": "string",
						   "UserProductInfo": "string", "InterfaceProductInfo": "string", "ProtocolInfo": "string",
						   "SystemName": "string", "Password": "string", "MaxOrderRef": "string", "SHFETime": "string",
						   "DCETime": "string", "CZCETime": "string", "FFEXTime": "string", "MacAddress": "string",
						   "OneTimePassword": "string"}
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
structDict['CSgitFtdcLoginInfoField'] = CSgitFtdcLoginInfoField


#登录信息
CSgitFtdcLogoutAllField = {"FrontID": "int", "SessionID": "int", "SystemName": "string"}
#前置编号
#会话编号
#系统名称
structDict['CSgitFtdcLogoutAllField'] = CSgitFtdcLogoutAllField


#前置状态
CSgitFtdcFrontStatusField = {"FrontID": "int", "LastReportDate": "string", "LastReportTime": "string",
							 "IsActive": "int"}
#前置编号
#上次报告日期
#上次报告时间
#是否活跃
structDict['CSgitFtdcFrontStatusField'] = CSgitFtdcFrontStatusField


#用户口令变更
CSgitFtdcUserPasswordUpdateField = {"BrokerID": "string", "UserID": "string", "OldPassword": "string",
									"NewPassword": "string"}
#经纪公司代码
#用户代码
#原来的口令
#新的口令
structDict['CSgitFtdcUserPasswordUpdateField'] = CSgitFtdcUserPasswordUpdateField


#输入报单
CSgitFtdcInputOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							"OrderRef": "string", "UserID": "string", "OrderPriceType": "char", "Direction": "char",
							"CombOffsetFlag": "string", "CombHedgeFlag": "string", "LimitPrice": "float",
							"VolumeTotalOriginal": "int", "TimeCondition": "char", "GTDDate": "string",
							"VolumeCondition": "char", "MinVolume": "int", "ContingentCondition": "char",
							"StopPrice": "float", "ForceCloseReason": "char", "IsAutoSuspend": "int",
							"BusinessUnit": "string", "RequestID": "int", "UserForceClose": "int"}
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
structDict['CSgitFtdcInputOrderField'] = CSgitFtdcInputOrderField


#报单
CSgitFtdcOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
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
					   "BrokerOrderSeq": "int", "RelativeOrderSysID": "string"}
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
structDict['CSgitFtdcOrderField'] = CSgitFtdcOrderField


#交易所报单
CSgitFtdcExchangeOrderField = {"OrderPriceType": "char", "Direction": "char", "CombOffsetFlag": "string",
							   "CombHedgeFlag": "string", "LimitPrice": "float", "VolumeTotalOriginal": "int",
							   "TimeCondition": "char", "GTDDate": "string", "VolumeCondition": "char",
							   "MinVolume": "int", "ContingentCondition": "char", "StopPrice": "float",
							   "ForceCloseReason": "char", "IsAutoSuspend": "int", "BusinessUnit": "string",
							   "RequestID": "int", "OrderLocalID": "string", "ExchangeID": "string",
							   "ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string",
							   "TraderID": "string", "InstallID": "int", "OrderSubmitStatus": "char",
							   "NotifySequence": "int", "TradingDay": "string", "SettlementID": "int",
							   "OrderSysID": "string", "OrderSource": "char", "OrderStatus": "char",
							   "OrderType": "char", "VolumeTraded": "int", "VolumeTotal": "int", "InsertDate": "string",
							   "InsertTime": "string", "ActiveTime": "string", "SuspendTime": "string",
							   "UpdateTime": "string", "CancelTime": "string", "ActiveTraderID": "string",
							   "ClearingPartID": "string", "SequenceNo": "int"}
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
structDict['CSgitFtdcExchangeOrderField'] = CSgitFtdcExchangeOrderField


#交易所报单插入失败
CSgitFtdcExchangeOrderInsertErrorField = {"ExchangeID": "string", "ParticipantID": "string", "TraderID": "string",
										  "InstallID": "int", "OrderLocalID": "string", "ErrorID": "int",
										  "ErrorMsg": "string"}
#交易所代码
#会员代码
#交易所交易员代码
#安装编号
#本地报单编号
#错误代码
#错误信息
structDict['CSgitFtdcExchangeOrderInsertErrorField'] = CSgitFtdcExchangeOrderInsertErrorField


#输入报单操作
CSgitFtdcInputOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
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
structDict['CSgitFtdcInputOrderActionField'] = CSgitFtdcInputOrderActionField


#报单操作
CSgitFtdcOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
							 "OrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
							 "ExchangeID": "string", "OrderSysID": "string", "ActionFlag": "char",
							 "LimitPrice": "float", "VolumeChange": "int", "ActionDate": "string",
							 "ActionTime": "string", "TraderID": "string", "InstallID": "int", "OrderLocalID": "string",
							 "ActionLocalID": "string", "ParticipantID": "string", "ClientID": "string",
							 "BusinessUnit": "string", "OrderActionStatus": "char", "UserID": "string",
							 "StatusMsg": "string", "InstrumentID": "string"}
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
structDict['CSgitFtdcOrderActionField'] = CSgitFtdcOrderActionField


#交易所报单操作
CSgitFtdcExchangeOrderActionField = {"ExchangeID": "string", "OrderSysID": "string", "ActionFlag": "char",
									 "LimitPrice": "float", "VolumeChange": "int", "ActionDate": "string",
									 "ActionTime": "string", "TraderID": "string", "InstallID": "int",
									 "OrderLocalID": "string", "ActionLocalID": "string", "ParticipantID": "string",
									 "ClientID": "string", "BusinessUnit": "string", "OrderActionStatus": "char",
									 "UserID": "string"}
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
structDict['CSgitFtdcExchangeOrderActionField'] = CSgitFtdcExchangeOrderActionField


#交易所报单操作失败
CSgitFtdcExchangeOrderActionErrorField = {"ExchangeID": "string", "OrderSysID": "string", "TraderID": "string",
										  "InstallID": "int", "OrderLocalID": "string", "ActionLocalID": "string",
										  "ErrorID": "int", "ErrorMsg": "string"}
#交易所代码
#报单编号
#交易所交易员代码
#安装编号
#本地报单编号
#操作本地编号
#错误代码
#错误信息
structDict['CSgitFtdcExchangeOrderActionErrorField'] = CSgitFtdcExchangeOrderActionErrorField


#交易所成交
CSgitFtdcExchangeTradeField = {"ExchangeID": "string", "TradeID": "string", "Direction": "char", "OrderSysID": "string",
							   "ParticipantID": "string", "ClientID": "string", "TradingRole": "char",
							   "ExchangeInstID": "string", "OffsetFlag": "char", "HedgeFlag": "char", "Price": "float",
							   "Volume": "int", "TradeDate": "string", "TradeTime": "string", "TradeType": "char",
							   "PriceSource": "char", "TraderID": "string", "OrderLocalID": "string",
							   "ClearingPartID": "string", "BusinessUnit": "string", "SequenceNo": "int",
							   "TradeSource": "char"}
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
structDict['CSgitFtdcExchangeTradeField'] = CSgitFtdcExchangeTradeField


#成交
CSgitFtdcTradeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
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
structDict['CSgitFtdcTradeField'] = CSgitFtdcTradeField


#用户会话
CSgitFtdcUserSessionField = {"FrontID": "int", "SessionID": "int", "BrokerID": "string", "UserID": "string",
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
structDict['CSgitFtdcUserSessionField'] = CSgitFtdcUserSessionField


#查询最大报单数量
CSgitFtdcQueryMaxOrderVolumeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
									 "Direction": "char", "OffsetFlag": "char", "HedgeFlag": "char", "MaxVolume": "int"}
#经纪公司代码
#投资者代码
#合约代码
#买卖方向
#开平标志
#投机套保标志
#最大允许报单数量
structDict['CSgitFtdcQueryMaxOrderVolumeField'] = CSgitFtdcQueryMaxOrderVolumeField


#投资者结算结果确认信息
CSgitFtdcSettlementInfoConfirmField = {"BrokerID": "string", "InvestorID": "string", "ConfirmDate": "string",
									   "ConfirmTime": "string"}
#经纪公司代码
#投资者代码
#确认日期
#确认时间
structDict['CSgitFtdcSettlementInfoConfirmField'] = CSgitFtdcSettlementInfoConfirmField


#出入金同步
CSgitFtdcSyncDepositField = {"DepositSeqNo": "string", "BrokerID": "string", "InvestorID": "string", "Deposit": "float",
							 "IsForce": "int"}
#出入金流水号
#经纪公司代码
#投资者代码
#入金金额
#是否强制进行
structDict['CSgitFtdcSyncDepositField'] = CSgitFtdcSyncDepositField


#经纪公司同步
CSgitFtdcBrokerSyncField = {"BrokerID": "string"}
#经纪公司代码
structDict['CSgitFtdcBrokerSyncField'] = CSgitFtdcBrokerSyncField


#正在同步中的投资者
CSgitFtdcSyncingInvestorField = {"InvestorID": "string", "BrokerID": "string", "InvestorGroupID": "string",
								 "InvestorName": "string", "IdentifiedCardType": "char", "IdentifiedCardNo": "string",
								 "IsActive": "int", "Telephone": "string", "Address": "string", "OpenDate": "string",
								 "Mobile": "string", "CommModelID": "string"}
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
structDict['CSgitFtdcSyncingInvestorField'] = CSgitFtdcSyncingInvestorField


#正在同步中的交易代码
CSgitFtdcSyncingTradingCodeField = {"InvestorID": "string", "BrokerID": "string", "ExchangeID": "string",
									"ClientID": "string", "IsActive": "int", "ClientIDType": "char"}
#投资者代码
#经纪公司代码
#交易所代码
#客户代码
#是否活跃
#交易编码类型
structDict['CSgitFtdcSyncingTradingCodeField'] = CSgitFtdcSyncingTradingCodeField


#正在同步中的投资者分组
CSgitFtdcSyncingInvestorGroupField = {"BrokerID": "string", "InvestorGroupID": "string", "InvestorGroupName": "string"}
#经纪公司代码
#投资者分组代码
#投资者分组名称
structDict['CSgitFtdcSyncingInvestorGroupField'] = CSgitFtdcSyncingInvestorGroupField


#正在同步中的交易账号
CSgitFtdcSyncingTradingAccountField = {"BrokerID": "string", "AccountID": "string", "PreMortgage": "float",
									   "PreCredit": "float", "PreDeposit": "float", "PreBalance": "float",
									   "PreMargin": "float", "InterestBase": "float", "Interest": "float",
									   "Deposit": "float", "Withdraw": "float", "FrozenMargin": "float",
									   "FrozenCash": "float", "FrozenCommission": "float", "CurrMargin": "float",
									   "CashIn": "float", "Commission": "float", "CloseProfit": "float",
									   "PositionProfit": "float", "Balance": "float", "Available": "float",
									   "WithdrawQuota": "float", "Reserve": "float", "TradingDay": "string",
									   "SettlementID": "int", "Credit": "float", "Mortgage": "float",
									   "ExchangeMargin": "float", "DeliveryMargin": "float",
									   "ExchangeDeliveryMargin": "float"}
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
structDict['CSgitFtdcSyncingTradingAccountField'] = CSgitFtdcSyncingTradingAccountField


#正在同步中的投资者持仓
CSgitFtdcSyncingInvestorPositionField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
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
										 "MarginRateByMoney": "float", "MarginRateByVolume": "float"}
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
structDict['CSgitFtdcSyncingInvestorPositionField'] = CSgitFtdcSyncingInvestorPositionField


#正在同步中的合约保证金率
CSgitFtdcSyncingInstrumentMarginRateField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
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
structDict['CSgitFtdcSyncingInstrumentMarginRateField'] = CSgitFtdcSyncingInstrumentMarginRateField


#正在同步中的合约手续费率
CSgitFtdcSyncingInstrumentCommissionRateField = {"InstrumentID": "string", "InvestorRange": "char",
												 "BrokerID": "string", "InvestorID": "string",
												 "OpenRatioByMoney": "float", "OpenRatioByVolume": "float",
												 "CloseRatioByMoney": "float", "CloseRatioByVolume": "float",
												 "CloseTodayRatioByMoney": "float", "CloseTodayRatioByVolume": "float"}
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
structDict['CSgitFtdcSyncingInstrumentCommissionRateField'] = CSgitFtdcSyncingInstrumentCommissionRateField


#正在同步中的合约交易权限
CSgitFtdcSyncingInstrumentTradingRightField = {"InstrumentID": "string", "InvestorRange": "char", "BrokerID": "string",
											   "InvestorID": "string", "TradingRight": "char"}
#合约代码
#投资者范围
#经纪公司代码
#投资者代码
#交易权限
structDict['CSgitFtdcSyncingInstrumentTradingRightField'] = CSgitFtdcSyncingInstrumentTradingRightField


#查询报单
CSgitFtdcQryOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						  "ExchangeID": "string", "OrderSysID": "string", "InsertTimeStart": "string",
						  "InsertTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#报单编号
#开始时间
#结束时间
structDict['CSgitFtdcQryOrderField'] = CSgitFtdcQryOrderField


#查询成交
CSgitFtdcQryTradeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						  "ExchangeID": "string", "TradeID": "string", "TradeTimeStart": "string",
						  "TradeTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#成交编号
#开始时间
#结束时间
structDict['CSgitFtdcQryTradeField'] = CSgitFtdcQryTradeField


#查询投资者持仓
CSgitFtdcQryInvestorPositionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#合约代码
structDict['CSgitFtdcQryInvestorPositionField'] = CSgitFtdcQryInvestorPositionField


#查询资金账户
CSgitFtdcQryTradingAccountField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSgitFtdcQryTradingAccountField'] = CSgitFtdcQryTradingAccountField


#查询投资者
CSgitFtdcQryInvestorField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSgitFtdcQryInvestorField'] = CSgitFtdcQryInvestorField


#查询交易编码
CSgitFtdcQryTradingCodeField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
								"ClientID": "string", "ClientIDType": "char"}
#经纪公司代码
#投资者代码
#交易所代码
#客户代码
#交易编码类型
structDict['CSgitFtdcQryTradingCodeField'] = CSgitFtdcQryTradingCodeField


#查询交易编码
CSgitFtdcQryInvestorGroupField = {"BrokerID": "string"}
#经纪公司代码
structDict['CSgitFtdcQryInvestorGroupField'] = CSgitFtdcQryInvestorGroupField


#查询交易编码
CSgitFtdcQryInstrumentMarginRateField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
										 "HedgeFlag": "char"}
#经纪公司代码
#投资者代码
#合约代码
#投机套保标志
structDict['CSgitFtdcQryInstrumentMarginRateField'] = CSgitFtdcQryInstrumentMarginRateField


#查询交易编码
CSgitFtdcQryInstrumentCommissionRateField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#合约代码
structDict['CSgitFtdcQryInstrumentCommissionRateField'] = CSgitFtdcQryInstrumentCommissionRateField


#查询交易编码
CSgitFtdcQryInstrumentTradingRightField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#合约代码
structDict['CSgitFtdcQryInstrumentTradingRightField'] = CSgitFtdcQryInstrumentTradingRightField


#查询经纪公司
CSgitFtdcQryBrokerField = {"BrokerID": "string"}
#经纪公司代码
structDict['CSgitFtdcQryBrokerField'] = CSgitFtdcQryBrokerField


#查询交易员
CSgitFtdcQryTraderField = {"ExchangeID": "string", "ParticipantID": "string", "TraderID": "string"}
#交易所代码
#会员代码
#交易所交易员代码
structDict['CSgitFtdcQryTraderField'] = CSgitFtdcQryTraderField


#查询经纪公司会员代码
CSgitFtdcQryPartBrokerField = {"ExchangeID": "string", "BrokerID": "string", "ParticipantID": "string"}
#交易所代码
#经纪公司代码
#会员代码
structDict['CSgitFtdcQryPartBrokerField'] = CSgitFtdcQryPartBrokerField


#查询管理用户功能权限
CSgitFtdcQrySuperUserFunctionField = {"UserID": "string"}
#用户代码
structDict['CSgitFtdcQrySuperUserFunctionField'] = CSgitFtdcQrySuperUserFunctionField


#查询用户会话
CSgitFtdcQryUserSessionField = {"FrontID": "int", "SessionID": "int", "BrokerID": "string", "UserID": "string"}
#前置编号
#会话编号
#经纪公司代码
#用户代码
structDict['CSgitFtdcQryUserSessionField'] = CSgitFtdcQryUserSessionField


#查询前置状态
CSgitFtdcQryFrontStatusField = {"FrontID": "int"}
#前置编号
structDict['CSgitFtdcQryFrontStatusField'] = CSgitFtdcQryFrontStatusField


#查询交易所报单
CSgitFtdcQryExchangeOrderField = {"ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string",
								  "ExchangeID": "string", "TraderID": "string"}
#会员代码
#客户代码
#合约在交易所的代码
#交易所代码
#交易所交易员代码
structDict['CSgitFtdcQryExchangeOrderField'] = CSgitFtdcQryExchangeOrderField


#查询报单操作
CSgitFtdcQryOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CSgitFtdcQryOrderActionField'] = CSgitFtdcQryOrderActionField


#查询交易所报单操作
CSgitFtdcQryExchangeOrderActionField = {"ParticipantID": "string", "ClientID": "string", "ExchangeID": "string",
										"TraderID": "string"}
#会员代码
#客户代码
#交易所代码
#交易所交易员代码
structDict['CSgitFtdcQryExchangeOrderActionField'] = CSgitFtdcQryExchangeOrderActionField


#查询管理用户
CSgitFtdcQrySuperUserField = {"UserID": "string"}
#用户代码
structDict['CSgitFtdcQrySuperUserField'] = CSgitFtdcQrySuperUserField


#查询交易所
CSgitFtdcQryExchangeField = {"ExchangeID": "string"}
#交易所代码
structDict['CSgitFtdcQryExchangeField'] = CSgitFtdcQryExchangeField


#查询产品
CSgitFtdcQryProductField = {"ProductID": "string"}
#产品代码
structDict['CSgitFtdcQryProductField'] = CSgitFtdcQryProductField


#查询合约
CSgitFtdcQryInstrumentField = {"InstrumentID": "string", "ExchangeID": "string", "ExchangeInstID": "string",
							   "ProductID": "string"}
#合约代码
#交易所代码
#合约在交易所的代码
#产品代码
structDict['CSgitFtdcQryInstrumentField'] = CSgitFtdcQryInstrumentField


#查询行情
CSgitFtdcQryDepthMarketDataField = {"InstrumentID": "string"}
#合约代码
structDict['CSgitFtdcQryDepthMarketDataField'] = CSgitFtdcQryDepthMarketDataField


#查询经纪公司用户
CSgitFtdcQryBrokerUserField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSgitFtdcQryBrokerUserField'] = CSgitFtdcQryBrokerUserField


#查询经纪公司用户权限
CSgitFtdcQryBrokerUserFunctionField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CSgitFtdcQryBrokerUserFunctionField'] = CSgitFtdcQryBrokerUserFunctionField


#查询交易员报盘机
CSgitFtdcQryTraderOfferField = {"ExchangeID": "string", "ParticipantID": "string", "TraderID": "string"}
#交易所代码
#会员代码
#交易所交易员代码
structDict['CSgitFtdcQryTraderOfferField'] = CSgitFtdcQryTraderOfferField


#查询出入金流水
CSgitFtdcQrySyncDepositField = {"BrokerID": "string", "DepositSeqNo": "string"}
#经纪公司代码
#出入金流水号
structDict['CSgitFtdcQrySyncDepositField'] = CSgitFtdcQrySyncDepositField


#查询投资者结算结果
CSgitFtdcQrySettlementInfoField = {"BrokerID": "string", "InvestorID": "string", "TradingDay": "string"}
#经纪公司代码
#投资者代码
#交易日
structDict['CSgitFtdcQrySettlementInfoField'] = CSgitFtdcQrySettlementInfoField


#查询报单
CSgitFtdcQryHisOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
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
structDict['CSgitFtdcQryHisOrderField'] = CSgitFtdcQryHisOrderField


#市场行情
CSgitFtdcMarketDataField = {"TradingDay": "string", "InstrumentID": "string", "ExchangeID": "string",
							"ExchangeInstID": "string", "LastPrice": "float", "PreSettlementPrice": "float",
							"PreClosePrice": "float", "PreOpenInterest": "float", "OpenPrice": "float",
							"HighestPrice": "float", "LowestPrice": "float", "Volume": "int", "Turnover": "float",
							"OpenInterest": "float", "ClosePrice": "float", "SettlementPrice": "float",
							"UpperLimitPrice": "float", "LowerLimitPrice": "float", "PreDelta": "float",
							"CurrDelta": "float", "UpdateTime": "string", "UpdateMillisec": "int"}
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
structDict['CSgitFtdcMarketDataField'] = CSgitFtdcMarketDataField


#行情基础属性
CSgitFtdcMarketDataBaseField = {"TradingDay": "string", "PreSettlementPrice": "float", "PreClosePrice": "float",
								"PreOpenInterest": "float", "PreDelta": "float"}
#交易日
#上次结算价
#昨收盘
#昨持仓量
#昨虚实度
structDict['CSgitFtdcMarketDataBaseField'] = CSgitFtdcMarketDataBaseField


#行情静态属性
CSgitFtdcMarketDataStaticField = {"OpenPrice": "float", "HighestPrice": "float", "LowestPrice": "float",
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
structDict['CSgitFtdcMarketDataStaticField'] = CSgitFtdcMarketDataStaticField


#行情最新成交属性
CSgitFtdcMarketDataLastMatchField = {"LastPrice": "float", "Volume": "int", "Turnover": "float",
									 "OpenInterest": "float"}
#最新价
#数量
#成交金额
#持仓量
structDict['CSgitFtdcMarketDataLastMatchField'] = CSgitFtdcMarketDataLastMatchField


#行情最优价属性
CSgitFtdcMarketDataBestPriceField = {"BidPrice1": "float", "BidVolume1": "int", "AskPrice1": "float",
									 "AskVolume1": "int"}
#申买价一
#申买量一
#申卖价一
#申卖量一
structDict['CSgitFtdcMarketDataBestPriceField'] = CSgitFtdcMarketDataBestPriceField


#行情申买二、三属性
CSgitFtdcMarketDataBid23Field = {"BidPrice2": "float", "BidVolume2": "int", "BidPrice3": "float", "BidVolume3": "int"}
#申买价二
#申买量二
#申买价三
#申买量三
structDict['CSgitFtdcMarketDataBid23Field'] = CSgitFtdcMarketDataBid23Field


#行情申卖二、三属性
CSgitFtdcMarketDataAsk23Field = {"AskPrice2": "float", "AskVolume2": "int", "AskPrice3": "float", "AskVolume3": "int"}
#申卖价二
#申卖量二
#申卖价三
#申卖量三
structDict['CSgitFtdcMarketDataAsk23Field'] = CSgitFtdcMarketDataAsk23Field


#行情申买四、五属性
CSgitFtdcMarketDataBid45Field = {"BidPrice4": "float", "BidVolume4": "int", "BidPrice5": "float", "BidVolume5": "int"}
#申买价四
#申买量四
#申买价五
#申买量五
structDict['CSgitFtdcMarketDataBid45Field'] = CSgitFtdcMarketDataBid45Field


#行情申卖四、五属性
CSgitFtdcMarketDataAsk45Field = {"AskPrice4": "float", "AskVolume4": "int", "AskPrice5": "float", "AskVolume5": "int"}
#申卖价四
#申卖量四
#申卖价五
#申卖量五
structDict['CSgitFtdcMarketDataAsk45Field'] = CSgitFtdcMarketDataAsk45Field


#行情更新时间属性
CSgitFtdcMarketDataUpdateTimeField = {"InstrumentID": "string", "UpdateTime": "string", "UpdateMillisec": "int"}
#合约代码
#最后修改时间
#最后修改毫秒
structDict['CSgitFtdcMarketDataUpdateTimeField'] = CSgitFtdcMarketDataUpdateTimeField


#行情交易所代码属性
CSgitFtdcMarketDataExchangeField = {"ExchangeID": "float"}
#交易所代码
structDict['CSgitFtdcMarketDataExchangeField'] = CSgitFtdcMarketDataExchangeField


#指定的合约
CSgitFtdcSpecificInstrumentField = {"InstrumentID": "string"}
#合约代码
structDict['CSgitFtdcSpecificInstrumentField'] = CSgitFtdcSpecificInstrumentField


#合约状态
CSgitFtdcInstrumentStatusField = {"ExchangeID": "string", "ExchangeInstID": "string", "SettlementGroupID": "string",
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
structDict['CSgitFtdcInstrumentStatusField'] = CSgitFtdcInstrumentStatusField


#查询合约状态
CSgitFtdcQryInstrumentStatusField = {"ExchangeID": "string", "ExchangeInstID": "string"}
#交易所代码
#合约在交易所的代码
structDict['CSgitFtdcQryInstrumentStatusField'] = CSgitFtdcQryInstrumentStatusField


#投资者账户
CSgitFtdcInvestorAccountField = {"BrokerID": "string", "InvestorID": "string", "AccountID": "string"}
#经纪公司代码
#投资者代码
#投资者帐号
structDict['CSgitFtdcInvestorAccountField'] = CSgitFtdcInvestorAccountField


#浮动盈亏算法
CSgitFtdcPositionProfitAlgorithmField = {"BrokerID": "string", "AccountID": "string", "Algorithm": "char",
										 "Memo": "string"}
#经纪公司代码
#投资者帐号
#盈亏算法
#备注
structDict['CSgitFtdcPositionProfitAlgorithmField'] = CSgitFtdcPositionProfitAlgorithmField


#会员资金折扣
CSgitFtdcDiscountField = {"BrokerID": "string", "InvestorRange": "char", "InvestorID": "string", "Discount": "float"}
#经纪公司代码
#投资者范围
#投资者代码
#资金折扣比例
structDict['CSgitFtdcDiscountField'] = CSgitFtdcDiscountField


#查询转帐银行
CSgitFtdcQryTransferBankField = {"BankID": "string", "BankBrchID": "string"}
#银行代码
#银行分中心代码
structDict['CSgitFtdcQryTransferBankField'] = CSgitFtdcQryTransferBankField


#转帐银行
CSgitFtdcTransferBankField = {"BankID": "string", "BankBrchID": "string", "BankName": "string", "IsActive": "int"}
#银行代码
#银行分中心代码
#银行名称
#是否活跃
structDict['CSgitFtdcTransferBankField'] = CSgitFtdcTransferBankField


#查询投资者持仓明细
CSgitFtdcQryInvestorPositionDetailField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#合约代码
structDict['CSgitFtdcQryInvestorPositionDetailField'] = CSgitFtdcQryInvestorPositionDetailField


#投资者持仓明细
CSgitFtdcInvestorPositionDetailField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
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
structDict['CSgitFtdcInvestorPositionDetailField'] = CSgitFtdcInvestorPositionDetailField


#资金账户口令域
CSgitFtdcTradingAccountPasswordField = {"BrokerID": "string", "AccountID": "string", "Password": "string"}
#经纪公司代码
#投资者帐号
#密码
structDict['CSgitFtdcTradingAccountPasswordField'] = CSgitFtdcTradingAccountPasswordField


#交易所行情报盘机
CSgitFtdcMDTraderOfferField = {"ExchangeID": "string", "TraderID": "string", "ParticipantID": "string",
							   "Password": "string", "InstallID": "int", "OrderLocalID": "string",
							   "TraderConnectStatus": "char", "ConnectRequestDate": "string",
							   "ConnectRequestTime": "string", "LastReportDate": "string", "LastReportTime": "string",
							   "ConnectDate": "string", "ConnectTime": "string", "StartDate": "string",
							   "StartTime": "string", "TradingDay": "string", "BrokerID": "string",
							   "MaxTradeID": "string", "MaxOrderMessageReference": "string"}
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
structDict['CSgitFtdcMDTraderOfferField'] = CSgitFtdcMDTraderOfferField


#查询行情报盘机
CSgitFtdcQryMDTraderOfferField = {"ExchangeID": "string", "ParticipantID": "string", "TraderID": "string"}
#交易所代码
#会员代码
#交易所交易员代码
structDict['CSgitFtdcQryMDTraderOfferField'] = CSgitFtdcQryMDTraderOfferField


#查询客户通知
CSgitFtdcQryNoticeField = {"BrokerID": "string"}
#经纪公司代码
structDict['CSgitFtdcQryNoticeField'] = CSgitFtdcQryNoticeField


#客户通知
CSgitFtdcNoticeField = {"BrokerID": "string", "Content": "string", "SequenceLabel": "string"}
#经纪公司代码
#消息正文
#经纪公司通知内容序列号
structDict['CSgitFtdcNoticeField'] = CSgitFtdcNoticeField


#用户权限
CSgitFtdcUserRightField = {"BrokerID": "string", "UserID": "string", "UserRightType": "char", "IsForbidden": "int"}
#经纪公司代码
#用户代码
#客户权限类型
#是否禁止
structDict['CSgitFtdcUserRightField'] = CSgitFtdcUserRightField


#查询结算信息确认域
CSgitFtdcQrySettlementInfoConfirmField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSgitFtdcQrySettlementInfoConfirmField'] = CSgitFtdcQrySettlementInfoConfirmField


#装载结算信息
CSgitFtdcLoadSettlementInfoField = {"BrokerID": "string"}
#经纪公司代码
structDict['CSgitFtdcLoadSettlementInfoField'] = CSgitFtdcLoadSettlementInfoField


#经纪公司可提资金算法表
CSgitFtdcBrokerWithdrawAlgorithmField = {"BrokerID": "string", "WithdrawAlgorithm": "char", "UsingRatio": "float",
										 "IncludeCloseProfit": "char", "AllWithoutTrade": "char",
										 "AvailIncludeCloseProfit": "char", "IsBrokerUserEvent": "int"}
#经纪公司代码
#可提资金算法
#资金使用率
#可提是否包含平仓盈利
#本日无仓且无成交客户是否受可提比例限制
#可用是否包含平仓盈利
#是否启用用户事件
structDict['CSgitFtdcBrokerWithdrawAlgorithmField'] = CSgitFtdcBrokerWithdrawAlgorithmField


#资金账户口令变更域
CSgitFtdcTradingAccountPasswordUpdateV1Field = {"BrokerID": "string", "InvestorID": "string", "OldPassword": "string",
												"NewPassword": "string"}
#经纪公司代码
#投资者代码
#原来的口令
#新的口令
structDict['CSgitFtdcTradingAccountPasswordUpdateV1Field'] = CSgitFtdcTradingAccountPasswordUpdateV1Field


#资金账户口令变更域
CSgitFtdcTradingAccountPasswordUpdateField = {"BrokerID": "string", "AccountID": "string", "OldPassword": "string",
											  "NewPassword": "string"}
#经纪公司代码
#投资者帐号
#原来的口令
#新的口令
structDict['CSgitFtdcTradingAccountPasswordUpdateField'] = CSgitFtdcTradingAccountPasswordUpdateField


#查询组合合约分腿
CSgitFtdcQryCombinationLegField = {"CombInstrumentID": "string", "LegID": "int", "LegInstrumentID": "string"}
#组合合约代码
#单腿编号
#单腿合约代码
structDict['CSgitFtdcQryCombinationLegField'] = CSgitFtdcQryCombinationLegField


#查询组合合约分腿
CSgitFtdcQrySyncStatusField = {"TradingDay": "string"}
#交易日
structDict['CSgitFtdcQrySyncStatusField'] = CSgitFtdcQrySyncStatusField


#组合交易合约的单腿
CSgitFtdcCombinationLegField = {"CombInstrumentID": "string", "LegID": "int", "LegInstrumentID": "string",
								"Direction": "char", "LegMultiple": "int", "ImplyLevel": "int"}
#组合合约代码
#单腿编号
#单腿合约代码
#买卖方向
#单腿乘数
#派生层数
structDict['CSgitFtdcCombinationLegField'] = CSgitFtdcCombinationLegField


#数据同步状态
CSgitFtdcSyncStatusField = {"TradingDay": "string", "DataSyncStatus": "char"}
#交易日
#数据同步状态
structDict['CSgitFtdcSyncStatusField'] = CSgitFtdcSyncStatusField


#查询联系人
CSgitFtdcQryLinkManField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSgitFtdcQryLinkManField'] = CSgitFtdcQryLinkManField


#联系人
CSgitFtdcLinkManField = {"BrokerID": "string", "InvestorID": "string", "PersonType": "char",
						 "IdentifiedCardType": "char", "IdentifiedCardNo": "string", "PersonName": "string",
						 "Telephone": "string", "Address": "string", "ZipCode": "string", "Priority": "int"}
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
structDict['CSgitFtdcLinkManField'] = CSgitFtdcLinkManField


#查询经纪公司用户事件
CSgitFtdcQryBrokerUserEventField = {"BrokerID": "string", "UserID": "string", "UserEventType": "char"}
#经纪公司代码
#用户代码
#用户事件类型
structDict['CSgitFtdcQryBrokerUserEventField'] = CSgitFtdcQryBrokerUserEventField


#查询经纪公司用户事件
CSgitFtdcBrokerUserEventField = {"BrokerID": "string", "UserID": "string", "UserEventType": "char",
								 "EventSequenceNo": "int", "EventDate": "string", "EventTime": "string",
								 "UserEventInfo": "string", "InvestorID": "string", "InstrumentID": "string"}
#经纪公司代码
#用户代码
#用户事件类型
#用户事件序号
#事件发生日期
#事件发生时间
#用户事件信息
#投资者代码
#合约代码
structDict['CSgitFtdcBrokerUserEventField'] = CSgitFtdcBrokerUserEventField


#查询签约银行请求
CSgitFtdcQryContractBankField = {"BrokerID": "string", "BankID": "string", "BankBrchID": "string"}
#经纪公司代码
#银行代码
#银行分中心代码
structDict['CSgitFtdcQryContractBankField'] = CSgitFtdcQryContractBankField


#查询签约银行响应
CSgitFtdcContractBankField = {"BrokerID": "string", "BankID": "string", "BankBrchID": "string", "BankName": "string"}
#经纪公司代码
#银行代码
#银行分中心代码
#银行名称
structDict['CSgitFtdcContractBankField'] = CSgitFtdcContractBankField


#投资者组合持仓明细
CSgitFtdcInvestorPositionCombineDetailField = {"TradingDay": "string", "OpenDate": "string", "ExchangeID": "string",
											   "SettlementID": "int", "BrokerID": "string", "InvestorID": "string",
											   "ComTradeID": "string", "TradeID": "string", "InstrumentID": "string",
											   "HedgeFlag": "char", "Direction": "char", "TotalAmt": "int",
											   "Margin": "float", "ExchMargin": "float", "MarginRateByMoney": "float",
											   "MarginRateByVolume": "float", "LegID": "int", "LegMultiple": "int",
											   "CombInstrumentID": "string"}
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
structDict['CSgitFtdcInvestorPositionCombineDetailField'] = CSgitFtdcInvestorPositionCombineDetailField


#预埋单
CSgitFtdcParkedOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							 "OrderRef": "string", "UserID": "string", "OrderPriceType": "char", "Direction": "char",
							 "CombOffsetFlag": "string", "CombHedgeFlag": "string", "LimitPrice": "float",
							 "VolumeTotalOriginal": "int", "TimeCondition": "char", "GTDDate": "string",
							 "VolumeCondition": "char", "MinVolume": "int", "ContingentCondition": "char",
							 "StopPrice": "float", "ForceCloseReason": "char", "IsAutoSuspend": "int",
							 "BusinessUnit": "string", "RequestID": "int", "UserForceClose": "int",
							 "ExchangeID": "string", "ParkedOrderID": "string", "UserType": "char", "Status": "char",
							 "ErrorID": "int", "ErrorMsg": "string"}
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
structDict['CSgitFtdcParkedOrderField'] = CSgitFtdcParkedOrderField


#输入预埋单操作
CSgitFtdcParkedOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
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
structDict['CSgitFtdcParkedOrderActionField'] = CSgitFtdcParkedOrderActionField


#查询预埋单
CSgitFtdcQryParkedOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								"ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CSgitFtdcQryParkedOrderField'] = CSgitFtdcQryParkedOrderField


#查询预埋撤单
CSgitFtdcQryParkedOrderActionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
									  "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CSgitFtdcQryParkedOrderActionField'] = CSgitFtdcQryParkedOrderActionField


#删除预埋单
CSgitFtdcRemoveParkedOrderField = {"BrokerID": "string", "InvestorID": "string", "ParkedOrderID": "string"}
#经纪公司代码
#投资者代码
#预埋报单编号
structDict['CSgitFtdcRemoveParkedOrderField'] = CSgitFtdcRemoveParkedOrderField


#删除预埋撤单
CSgitFtdcRemoveParkedOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ParkedOrderActionID": "string"}
#经纪公司代码
#投资者代码
#预埋撤单编号
structDict['CSgitFtdcRemoveParkedOrderActionField'] = CSgitFtdcRemoveParkedOrderActionField


#经纪公司可提资金算法表
CSgitFtdcInvestorWithdrawAlgorithmField = {"BrokerID": "string", "InvestorRange": "char", "InvestorID": "string",
										   "UsingRatio": "float"}
#经纪公司代码
#投资者范围
#投资者代码
#可提资金比例
structDict['CSgitFtdcInvestorWithdrawAlgorithmField'] = CSgitFtdcInvestorWithdrawAlgorithmField


#查询组合持仓明细
CSgitFtdcQryInvestorPositionCombineDetailField = {"BrokerID": "string", "InvestorID": "string",
												  "CombInstrumentID": "string"}
#经纪公司代码
#投资者代码
#组合持仓合约编码
structDict['CSgitFtdcQryInvestorPositionCombineDetailField'] = CSgitFtdcQryInvestorPositionCombineDetailField


#成交均价
CSgitFtdcMarketDataAveragePriceField = {"AveragePrice": "float"}
#当日均价
structDict['CSgitFtdcMarketDataAveragePriceField'] = CSgitFtdcMarketDataAveragePriceField


#校验投资者密码
CSgitFtdcVerifyInvestorPasswordField = {"BrokerID": "string", "InvestorID": "string", "Password": "string"}
#经纪公司代码
#投资者代码
#密码
structDict['CSgitFtdcVerifyInvestorPasswordField'] = CSgitFtdcVerifyInvestorPasswordField


#用户IP
CSgitFtdcUserIPField = {"BrokerID": "string", "UserID": "string", "IPAddress": "string", "IPMask": "string",
						"MacAddress": "string"}
#经纪公司代码
#用户代码
#IP地址
#IP地址掩码
#Mac地址
structDict['CSgitFtdcUserIPField'] = CSgitFtdcUserIPField


#用户事件通知信息
CSgitFtdcTradingNoticeInfoField = {"BrokerID": "string", "InvestorID": "string", "SendTime": "string",
								   "FieldContent": "string", "SequenceSeries": "short", "SequenceNo": "int"}
#经纪公司代码
#投资者代码
#发送时间
#消息正文
#序列系列号
#序列号
structDict['CSgitFtdcTradingNoticeInfoField'] = CSgitFtdcTradingNoticeInfoField


#用户事件通知
CSgitFtdcTradingNoticeField = {"BrokerID": "string", "InvestorRange": "char", "InvestorID": "string",
							   "SequenceSeries": "short", "UserID": "string", "SendTime": "string", "SequenceNo": "int",
							   "FieldContent": "string"}
#经纪公司代码
#投资者范围
#投资者代码
#序列系列号
#用户代码
#发送时间
#序列号
#消息正文
structDict['CSgitFtdcTradingNoticeField'] = CSgitFtdcTradingNoticeField


#查询交易事件通知
CSgitFtdcQryTradingNoticeField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSgitFtdcQryTradingNoticeField'] = CSgitFtdcQryTradingNoticeField


#查询错误报单
CSgitFtdcQryErrOrderField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSgitFtdcQryErrOrderField'] = CSgitFtdcQryErrOrderField


#错误报单
CSgitFtdcErrOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
						  "UserID": "string", "OrderPriceType": "char", "Direction": "char", "CombOffsetFlag": "string",
						  "CombHedgeFlag": "string", "LimitPrice": "float", "VolumeTotalOriginal": "int",
						  "TimeCondition": "char", "GTDDate": "string", "VolumeCondition": "char", "MinVolume": "int",
						  "ContingentCondition": "char", "StopPrice": "float", "ForceCloseReason": "char",
						  "IsAutoSuspend": "int", "BusinessUnit": "string", "RequestID": "int", "UserForceClose": "int",
						  "ErrorID": "int", "ErrorMsg": "string"}
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
structDict['CSgitFtdcErrOrderField'] = CSgitFtdcErrOrderField


#查询错误报单操作
CSgitFtdcErrorConditionalOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
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
									   "RelativeOrderSysID": "string", "ErrorID": "int", "ErrorMsg": "string"}
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
#错误代码
#错误信息
structDict['CSgitFtdcErrorConditionalOrderField'] = CSgitFtdcErrorConditionalOrderField


#查询错误报单操作
CSgitFtdcQryErrOrderActionField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSgitFtdcQryErrOrderActionField'] = CSgitFtdcQryErrOrderActionField


#错误报单操作
CSgitFtdcErrOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderActionRef": "int",
								"OrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
								"ExchangeID": "string", "OrderSysID": "string", "ActionFlag": "char",
								"LimitPrice": "float", "VolumeChange": "int", "ActionDate": "string",
								"ActionTime": "string", "TraderID": "string", "InstallID": "int",
								"OrderLocalID": "string", "ActionLocalID": "string", "ParticipantID": "string",
								"ClientID": "string", "BusinessUnit": "string", "OrderActionStatus": "char",
								"UserID": "string", "StatusMsg": "string", "InstrumentID": "string", "ErrorID": "int",
								"ErrorMsg": "string"}
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
#错误代码
#错误信息
structDict['CSgitFtdcErrOrderActionField'] = CSgitFtdcErrOrderActionField


#查询交易所状态
CSgitFtdcQryExchangeSequenceField = {"ExchangeID": "string"}
#交易所代码
structDict['CSgitFtdcQryExchangeSequenceField'] = CSgitFtdcQryExchangeSequenceField


#交易所状态
CSgitFtdcExchangeSequenceField = {"ExchangeID": "string", "SequenceNo": "int", "MarketStatus": "char"}
#交易所代码
#序号
#合约交易状态
structDict['CSgitFtdcExchangeSequenceField'] = CSgitFtdcExchangeSequenceField


#根据价格查询最大报单数量
CSgitFtdcQueryMaxOrderVolumeWithPriceField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
											  "Direction": "char", "OffsetFlag": "char", "HedgeFlag": "char",
											  "MaxVolume": "int", "Price": "float"}
#经纪公司代码
#投资者代码
#合约代码
#买卖方向
#开平标志
#投机套保标志
#最大允许报单数量
#报单价格
structDict['CSgitFtdcQueryMaxOrderVolumeWithPriceField'] = CSgitFtdcQueryMaxOrderVolumeWithPriceField


#查询经纪公司交易参数
CSgitFtdcQryBrokerTradingParamsField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSgitFtdcQryBrokerTradingParamsField'] = CSgitFtdcQryBrokerTradingParamsField


#经纪公司交易参数
CSgitFtdcBrokerTradingParamsField = {"BrokerID": "string", "InvestorID": "string", "MarginPriceType": "char",
									 "Algorithm": "char", "AvailIncludeCloseProfit": "char"}
#经纪公司代码
#投资者代码
#保证金价格类型
#盈亏算法
#可用是否包含平仓盈利
structDict['CSgitFtdcBrokerTradingParamsField'] = CSgitFtdcBrokerTradingParamsField


#查询经纪公司交易算法
CSgitFtdcQryBrokerTradingAlgosField = {"BrokerID": "string", "ExchangeID": "string", "InstrumentID": "string"}
#经纪公司代码
#交易所代码
#合约代码
structDict['CSgitFtdcQryBrokerTradingAlgosField'] = CSgitFtdcQryBrokerTradingAlgosField


#经纪公司交易算法
CSgitFtdcBrokerTradingAlgosField = {"BrokerID": "string", "ExchangeID": "string", "InstrumentID": "string",
									"HandlePositionAlgoID": "char", "FindMarginRateAlgoID": "char",
									"HandleTradingAccountAlgoID": "char"}
#经纪公司代码
#交易所代码
#合约代码
#持仓处理算法编号
#寻找保证金率算法编号
#资金处理算法编号
structDict['CSgitFtdcBrokerTradingAlgosField'] = CSgitFtdcBrokerTradingAlgosField


#查询经纪公司资金
CSgitFtdcQueryBrokerDepositField = {"BrokerID": "string", "ExchangeID": "string"}
#经纪公司代码
#交易所代码
structDict['CSgitFtdcQueryBrokerDepositField'] = CSgitFtdcQueryBrokerDepositField


#经纪公司资金
CSgitFtdcBrokerDepositField = {"TradingDay": "string", "BrokerID": "string", "ParticipantID": "string",
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
structDict['CSgitFtdcBrokerDepositField'] = CSgitFtdcBrokerDepositField


#查询保证金监管系统经纪公司密钥
CSgitFtdcQryCFMMCBrokerKeyField = {"BrokerID": "string"}
#经纪公司代码
structDict['CSgitFtdcQryCFMMCBrokerKeyField'] = CSgitFtdcQryCFMMCBrokerKeyField


#保证金监管系统经纪公司密钥
CSgitFtdcCFMMCBrokerKeyField = {"BrokerID": "string", "ParticipantID": "string", "CreateDate": "string",
								"CreateTime": "string", "KeyID": "int", "CurrentKey": "string", "KeyKind": "char"}
#经纪公司代码
#经纪公司统一编码
#密钥生成日期
#密钥生成时间
#密钥编号
#动态密钥
#动态密钥类型
structDict['CSgitFtdcCFMMCBrokerKeyField'] = CSgitFtdcCFMMCBrokerKeyField


#保证金监管系统经纪公司资金账户密钥
CSgitFtdcCFMMCTradingAccountKeyField = {"BrokerID": "string", "ParticipantID": "string", "AccountID": "string",
										"KeyID": "int", "CurrentKey": "string"}
#经纪公司代码
#经纪公司统一编码
#投资者帐号
#密钥编号
#动态密钥
structDict['CSgitFtdcCFMMCTradingAccountKeyField'] = CSgitFtdcCFMMCTradingAccountKeyField


#请求查询保证金监管系统经纪公司资金账户密钥
CSgitFtdcQryCFMMCTradingAccountKeyField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CSgitFtdcQryCFMMCTradingAccountKeyField'] = CSgitFtdcQryCFMMCTradingAccountKeyField


#用户动态令牌参数
CSgitFtdcBrokerUserOTPParamField = {"BrokerID": "string", "UserID": "string", "OTPVendorsID": "string",
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
structDict['CSgitFtdcBrokerUserOTPParamField'] = CSgitFtdcBrokerUserOTPParamField


#手工同步用户动态令牌
CSgitFtdcManualSyncBrokerUserOTPField = {"BrokerID": "string", "UserID": "string", "OTPType": "char",
										 "FirstOTP": "string", "SecondOTP": "string"}
#经纪公司代码
#用户代码
#动态令牌类型
#第一个动态密码
#第二个动态密码
structDict['CSgitFtdcManualSyncBrokerUserOTPField'] = CSgitFtdcManualSyncBrokerUserOTPField


#投资者手续费率模板
CSgitFtdcCommRateModelField = {"BrokerID": "string", "CommModelID": "string", "CommModelName": "string"}
#经纪公司代码
#手续费率模板代码
#模板名称
structDict['CSgitFtdcCommRateModelField'] = CSgitFtdcCommRateModelField


#请求查询投资者手续费率模板
CSgitFtdcQryCommRateModelField = {"BrokerID": "string", "CommModelID": "string"}
#经纪公司代码
#手续费率模板代码
structDict['CSgitFtdcQryCommRateModelField'] = CSgitFtdcQryCommRateModelField


#仓单折抵信息
CSgitFtdcEWarrantOffsetField = {"TradingDay": "string", "BrokerID": "string", "InvestorID": "string",
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
structDict['CSgitFtdcEWarrantOffsetField'] = CSgitFtdcEWarrantOffsetField


#查询仓单折抵信息
CSgitFtdcQryEWarrantOffsetField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
								   "InstrumentID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
structDict['CSgitFtdcQryEWarrantOffsetField'] = CSgitFtdcQryEWarrantOffsetField


#转帐开户请求
CSgitFtdcReqOpenAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
								"OperNo": "string", "TID": "int"}
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
structDict['CSgitFtdcReqOpenAccountField'] = CSgitFtdcReqOpenAccountField


#转帐销户请求
CSgitFtdcReqCancelAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
								  "OperNo": "string", "TID": "int"}
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
structDict['CSgitFtdcReqCancelAccountField'] = CSgitFtdcReqCancelAccountField


#变更银行账户请求
CSgitFtdcReqChangeAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcReqChangeAccountField'] = CSgitFtdcReqChangeAccountField


#转账请求
CSgitFtdcReqTransferField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							 "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							 "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							 "LastFragment": "char", "SessionID": "int", "CustomerName": "string", "IdCardType": "char",
							 "IdentifiedCardNo": "string", "CustType": "char", "BankAccount": "string",
							 "BankPassWord": "string", "AccountID": "string", "Password": "string", "InstallID": "int",
							 "FutureSerial": "int", "UserID": "string", "VerifyCertNoFlag": "char",
							 "CurrencyID": "string", "TradeAmount": "float", "FutureFetchAmount": "float",
							 "FeePayFlag": "char", "CustFee": "float", "BrokerFee": "float", "Message": "string",
							 "Digest": "string", "BankAccType": "char", "DeviceID": "string", "BankSecuAccType": "char",
							 "BrokerIDByBank": "string", "BankSecuAcc": "string", "BankPwdFlag": "char",
							 "SecuPwdFlag": "char", "OperNo": "string", "RequestID": "int", "TID": "int",
							 "TransferStatus": "char"}
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
structDict['CSgitFtdcReqTransferField'] = CSgitFtdcReqTransferField


#银行发起银行资金转期货响应
CSgitFtdcRspTransferField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							 "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							 "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							 "LastFragment": "char", "SessionID": "int", "CustomerName": "string", "IdCardType": "char",
							 "IdentifiedCardNo": "string", "CustType": "char", "BankAccount": "string",
							 "BankPassWord": "string", "AccountID": "string", "Password": "string", "InstallID": "int",
							 "FutureSerial": "int", "UserID": "string", "VerifyCertNoFlag": "char",
							 "CurrencyID": "string", "TradeAmount": "float", "FutureFetchAmount": "float",
							 "FeePayFlag": "char", "CustFee": "float", "BrokerFee": "float", "Message": "string",
							 "Digest": "string", "BankAccType": "char", "DeviceID": "string", "BankSecuAccType": "char",
							 "BrokerIDByBank": "string", "BankSecuAcc": "string", "BankPwdFlag": "char",
							 "SecuPwdFlag": "char", "OperNo": "string", "RequestID": "int", "TID": "int",
							 "TransferStatus": "char", "ErrorID": "int", "ErrorMsg": "string"}
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
structDict['CSgitFtdcRspTransferField'] = CSgitFtdcRspTransferField


#冲正请求
CSgitFtdcReqRepealField = {"RepealTimeInterval": "int", "RepealedTimes": "int", "BankRepealFlag": "char",
						   "BrokerRepealFlag": "char", "PlateRepealSerial": "int", "BankRepealSerial": "string",
						   "FutureRepealSerial": "int", "TradeCode": "string", "BankID": "string",
						   "BankBranchID": "string", "BrokerID": "string", "BrokerBranchID": "string",
						   "TradeDate": "string", "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
						   "PlateSerial": "int", "LastFragment": "char", "SessionID": "int", "CustomerName": "string",
						   "IdCardType": "char", "IdentifiedCardNo": "string", "CustType": "char",
						   "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
						   "Password": "string", "InstallID": "int", "FutureSerial": "int", "UserID": "string",
						   "VerifyCertNoFlag": "char", "CurrencyID": "string", "TradeAmount": "float",
						   "FutureFetchAmount": "float", "FeePayFlag": "char", "CustFee": "float", "BrokerFee": "float",
						   "Message": "string", "Digest": "string", "BankAccType": "char", "DeviceID": "string",
						   "BankSecuAccType": "char", "BrokerIDByBank": "string", "BankSecuAcc": "string",
						   "BankPwdFlag": "char", "SecuPwdFlag": "char", "OperNo": "string", "RequestID": "int",
						   "TID": "int", "TransferStatus": "char"}
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
structDict['CSgitFtdcReqRepealField'] = CSgitFtdcReqRepealField


#冲正响应
CSgitFtdcRspRepealField = {"RepealTimeInterval": "int", "RepealedTimes": "int", "BankRepealFlag": "char",
						   "BrokerRepealFlag": "char", "PlateRepealSerial": "int", "BankRepealSerial": "string",
						   "FutureRepealSerial": "int", "TradeCode": "string", "BankID": "string",
						   "BankBranchID": "string", "BrokerID": "string", "BrokerBranchID": "string",
						   "TradeDate": "string", "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
						   "PlateSerial": "int", "LastFragment": "char", "SessionID": "int", "CustomerName": "string",
						   "IdCardType": "char", "IdentifiedCardNo": "string", "CustType": "char",
						   "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
						   "Password": "string", "InstallID": "int", "FutureSerial": "int", "UserID": "string",
						   "VerifyCertNoFlag": "char", "CurrencyID": "string", "TradeAmount": "float",
						   "FutureFetchAmount": "float", "FeePayFlag": "char", "CustFee": "float", "BrokerFee": "float",
						   "Message": "string", "Digest": "string", "BankAccType": "char", "DeviceID": "string",
						   "BankSecuAccType": "char", "BrokerIDByBank": "string", "BankSecuAcc": "string",
						   "BankPwdFlag": "char", "SecuPwdFlag": "char", "OperNo": "string", "RequestID": "int",
						   "TID": "int", "TransferStatus": "char", "ErrorID": "int", "ErrorMsg": "string"}
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
structDict['CSgitFtdcRspRepealField'] = CSgitFtdcRspRepealField


#查询账户信息请求
CSgitFtdcReqQueryAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								 "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								 "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								 "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
								 "CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								 "CustType": "char", "BankAccount": "string", "BankPassWord": "string",
								 "AccountID": "string", "Password": "string", "FutureSerial": "int", "InstallID": "int",
								 "UserID": "string", "VerifyCertNoFlag": "char", "CurrencyID": "string",
								 "Digest": "string", "BankAccType": "char", "DeviceID": "string",
								 "BankSecuAccType": "char", "BrokerIDByBank": "string", "BankSecuAcc": "string",
								 "BankPwdFlag": "char", "SecuPwdFlag": "char", "OperNo": "string", "RequestID": "int",
								 "TID": "int"}
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
structDict['CSgitFtdcReqQueryAccountField'] = CSgitFtdcReqQueryAccountField


#查询账户信息响应
CSgitFtdcRspQueryAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								 "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								 "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								 "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
								 "CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								 "CustType": "char", "BankAccount": "string", "BankPassWord": "string",
								 "AccountID": "string", "Password": "string", "FutureSerial": "int", "InstallID": "int",
								 "UserID": "string", "VerifyCertNoFlag": "char", "CurrencyID": "string",
								 "Digest": "string", "BankAccType": "char", "DeviceID": "string",
								 "BankSecuAccType": "char", "BrokerIDByBank": "string", "BankSecuAcc": "string",
								 "BankPwdFlag": "char", "SecuPwdFlag": "char", "OperNo": "string", "RequestID": "int",
								 "TID": "int", "BankUseAmount": "float", "BankFetchAmount": "float"}
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
structDict['CSgitFtdcRspQueryAccountField'] = CSgitFtdcRspQueryAccountField


#期商签到签退
CSgitFtdcFutureSignIOField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							  "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							  "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							  "LastFragment": "char", "SessionID": "int", "InstallID": "int", "UserID": "string",
							  "Digest": "string", "CurrencyID": "string", "DeviceID": "string",
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
structDict['CSgitFtdcFutureSignIOField'] = CSgitFtdcFutureSignIOField


#期商签到响应
CSgitFtdcRspFutureSignInField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcRspFutureSignInField'] = CSgitFtdcRspFutureSignInField


#期商签退请求
CSgitFtdcReqFutureSignOutField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcReqFutureSignOutField'] = CSgitFtdcReqFutureSignOutField


#期商签退响应
CSgitFtdcRspFutureSignOutField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcRspFutureSignOutField'] = CSgitFtdcRspFutureSignOutField


#查询指定流水号的交易结果请求
CSgitFtdcReqQueryTradeResultBySerialField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
											 "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
											 "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
											 "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
											 "Reference": "int", "RefrenceIssureType": "char",
											 "RefrenceIssure": "string", "CustomerName": "string", "IdCardType": "char",
											 "IdentifiedCardNo": "string", "CustType": "char", "BankAccount": "string",
											 "BankPassWord": "string", "AccountID": "string", "Password": "string",
											 "CurrencyID": "string", "TradeAmount": "float", "Digest": "string"}
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
structDict['CSgitFtdcReqQueryTradeResultBySerialField'] = CSgitFtdcReqQueryTradeResultBySerialField


#查询指定流水号的交易结果响应
CSgitFtdcRspQueryTradeResultBySerialField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcRspQueryTradeResultBySerialField'] = CSgitFtdcRspQueryTradeResultBySerialField


#日终文件就绪请求
CSgitFtdcReqDayEndFileReadyField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcReqDayEndFileReadyField'] = CSgitFtdcReqDayEndFileReadyField


#返回结果
CSgitFtdcReturnResultField = {"ReturnCode": "string", "DescrInfoForReturnCode": "string"}
#返回代码
#返回码描述
structDict['CSgitFtdcReturnResultField'] = CSgitFtdcReturnResultField


#验证期货资金密码
CSgitFtdcVerifyFuturePasswordField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
									  "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
									  "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
									  "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
									  "AccountID": "string", "Password": "string", "BankAccount": "string",
									  "BankPassWord": "string", "InstallID": "int", "TID": "int"}
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
structDict['CSgitFtdcVerifyFuturePasswordField'] = CSgitFtdcVerifyFuturePasswordField


#验证客户信息
CSgitFtdcVerifyCustInfoField = {"CustomerName": "string", "IdCardType": "char", "IdentifiedCardNo": "string",
								"CustType": "char"}
#客户姓名
#证件类型
#证件号码
#客户类型
structDict['CSgitFtdcVerifyCustInfoField'] = CSgitFtdcVerifyCustInfoField


#验证期货资金密码和客户信息
CSgitFtdcVerifyFuturePasswordAndCustInfoField = {"CustomerName": "string", "IdCardType": "char",
												 "IdentifiedCardNo": "string", "CustType": "char",
												 "AccountID": "string", "Password": "string"}
#客户姓名
#证件类型
#证件号码
#客户类型
#投资者帐号
#期货密码
structDict['CSgitFtdcVerifyFuturePasswordAndCustInfoField'] = CSgitFtdcVerifyFuturePasswordAndCustInfoField


#验证期货资金密码和客户信息
CSgitFtdcDepositResultInformField = {"DepositSeqNo": "string", "BrokerID": "string", "InvestorID": "string",
									 "Deposit": "float", "RequestID": "int", "ReturnCode": "string",
									 "DescrInfoForReturnCode": "string"}
#出入金流水号，该流水号为银期报盘返回的流水号
#经纪公司代码
#投资者代码
#入金金额
#请求编号
#返回代码
#返回码描述
structDict['CSgitFtdcDepositResultInformField'] = CSgitFtdcDepositResultInformField


#交易核心向银期报盘发出密钥同步请求
CSgitFtdcReqSyncKeyField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
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
structDict['CSgitFtdcReqSyncKeyField'] = CSgitFtdcReqSyncKeyField


#交易核心向银期报盘发出密钥同步响应
CSgitFtdcRspSyncKeyField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
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
structDict['CSgitFtdcRspSyncKeyField'] = CSgitFtdcRspSyncKeyField


#查询账户信息通知
CSgitFtdcNotifyQueryAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcNotifyQueryAccountField'] = CSgitFtdcNotifyQueryAccountField


#银期转账交易流水表
CSgitFtdcTransferSerialField = {"PlateSerial": "int", "TradeDate": "string", "TradingDay": "string",
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
structDict['CSgitFtdcTransferSerialField'] = CSgitFtdcTransferSerialField


#请求查询转帐流水
CSgitFtdcQryTransferSerialField = {"BrokerID": "string", "AccountID": "string", "BankID": "string"}
#经纪公司代码
#投资者帐号
#银行编码
structDict['CSgitFtdcQryTransferSerialField'] = CSgitFtdcQryTransferSerialField


#期商签到通知
CSgitFtdcNotifyFutureSignInField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcNotifyFutureSignInField'] = CSgitFtdcNotifyFutureSignInField


#期商签退通知
CSgitFtdcNotifyFutureSignOutField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
									 "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
									 "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
									 "PlateSerial": "int", "LastFragment": "char", "SessionID": "int",
									 "InstallID": "int", "UserID": "string", "Digest": "string", "CurrencyID": "string",
									 "DeviceID": "string", "BrokerIDByBank": "string", "OperNo": "string",
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
#摘要
#币种代码
#渠道标志
#期货公司银行编码
#交易柜员
#请求编号
#交易ID
#错误代码
#错误信息
structDict['CSgitFtdcNotifyFutureSignOutField'] = CSgitFtdcNotifyFutureSignOutField


#交易核心向银期报盘发出密钥同步处理结果的通知
CSgitFtdcNotifySyncKeyField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcNotifySyncKeyField'] = CSgitFtdcNotifySyncKeyField


#请求查询银期签约关系
CSgitFtdcQryAccountregisterField = {"BrokerID": "string", "AccountID": "string", "BankID": "string"}
#经纪公司代码
#投资者帐号
#银行编码
structDict['CSgitFtdcQryAccountregisterField'] = CSgitFtdcQryAccountregisterField


#客户开销户信息表
CSgitFtdcAccountregisterField = {"TradeDay": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcAccountregisterField'] = CSgitFtdcAccountregisterField


#银期开户信息
CSgitFtdcOpenAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							 "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							 "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							 "LastFragment": "char", "SessionID": "int", "CustomerName": "string", "IdCardType": "char",
							 "IdentifiedCardNo": "string", "Gender": "char", "CountryCode": "string",
							 "CustType": "char", "Address": "string", "ZipCode": "string", "Telephone": "string",
							 "MobilePhone": "string", "Fax": "string", "EMail": "string", "MoneyAccountStatus": "char",
							 "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
							 "Password": "string", "InstallID": "int", "VerifyCertNoFlag": "char",
							 "CurrencyID": "string", "CashExchangeCode": "char", "Digest": "string",
							 "BankAccType": "char", "DeviceID": "string", "BankSecuAccType": "char",
							 "BrokerIDByBank": "string", "BankSecuAcc": "string", "BankPwdFlag": "char",
							 "SecuPwdFlag": "char", "OperNo": "string", "TID": "int", "ErrorID": "int",
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
#错误代码
#错误信息
structDict['CSgitFtdcOpenAccountField'] = CSgitFtdcOpenAccountField


#银期销户信息
CSgitFtdcCancelAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
							   "OperNo": "string", "TID": "int", "ErrorID": "int", "ErrorMsg": "string"}
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
#错误代码
#错误信息
structDict['CSgitFtdcCancelAccountField'] = CSgitFtdcCancelAccountField


#银期变更银行账号信息
CSgitFtdcChangeAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
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
structDict['CSgitFtdcChangeAccountField'] = CSgitFtdcChangeAccountField


#灾备中心交易权限
CSgitFtdcUserRightsAssignField = {"BrokerID": "string", "UserID": "string", "DRIdentityID": "int"}
#应用单元代码
#用户代码
#交易中心代码
structDict['CSgitFtdcUserRightsAssignField'] = CSgitFtdcUserRightsAssignField


#经济公司是否有在本标示的交易权限
CSgitFtdcBrokerUserRightAssignField = {"BrokerID": "string", "DRIdentityID": "int", "Tradeable": "int"}
#应用单元代码
#交易中心代码
#能否交易
structDict['CSgitFtdcBrokerUserRightAssignField'] = CSgitFtdcBrokerUserRightAssignField


#灾备交易转换报文
CSgitFtdcDRTransferField = {"OrigDRIdentityID": "int", "DestDRIdentityID": "int", "OrigBrokerID": "string",
							"DestBrokerID": "string"}
#原交易中心代码
#目标交易中心代码
#原应用单元代码
#目标易用单元代码
structDict['CSgitFtdcDRTransferField'] = CSgitFtdcDRTransferField



CSgitMBLQuotReq = {"StartContractID": "string", "EndContractID": "string", "BsFlag": "char"}
structDict['CSgitMBLQuotReq'] = CSgitMBLQuotReq



CSgitMBLQuotData = {"ContractID": "string", "BsFlag": "char", "Price": "float", "Qty": "int"}
structDict['CSgitMBLQuotData'] = CSgitMBLQuotData



CSgitSubQuotField = {"ContractID": "string"}
structDict['CSgitSubQuotField'] = CSgitSubQuotField



