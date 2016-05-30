# encoding: UTF-8

structDict = {}

#//////////////////////////////////////////////////////////////////////
#@system 风控前置系统
#@company CFFEX
#@file USTPFtdcUserApiStruct.h
#@brief 定义了客户端接口使用的业务数据结构
#@history 
#//////////////////////////////////////////////////////////////////////










#系统用户登录请求
CUstpFtdcReqUserLoginField = {"TradingDay": "string", "UserID": "string", "BrokerID": "string", "Password": "string",
							  "UserProductInfo": "string", "InterfaceProductInfo": "string", "ProtocolInfo": "string",
							  "IPAddress": "string", "MacAddress": "string", "DataCenterID": "int"}
#交易日
#交易用户代码
#经纪公司编号
#密码
#用户端产品信息
#接口端产品信息
#协议信息
#IP地址
#Mac地址
#数据中心代码
structDict['CUstpFtdcReqUserLoginField'] = CUstpFtdcReqUserLoginField

#系统用户登录应答
CUstpFtdcRspUserLoginField = {"TradingDay": "string", "BrokerID": "string", "UserID": "string", "LoginTime": "string",
							  "MaxOrderLocalID": "string", "TradingSystemName": "string", "DataCenterID": "int",
							  "PrivateFlowSize": "int", "UserFlowSize": "int"}
#交易日
#经纪公司编号
#交易用户代码
#登录成功时间
#用户最大本地报单号
#交易系统名称
#数据中心代码
#会员私有流当前长度
#交易员私有流当前长度
structDict['CUstpFtdcRspUserLoginField'] = CUstpFtdcRspUserLoginField

#用户登出请求
CUstpFtdcReqUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司编号
#交易用户代码
structDict['CUstpFtdcReqUserLogoutField'] = CUstpFtdcReqUserLogoutField

#用户登出请求
CUstpFtdcRspUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司编号
#交易用户代码
structDict['CUstpFtdcRspUserLogoutField'] = CUstpFtdcRspUserLogoutField

#强制用户退出
CUstpFtdcForceUserExitField = {"BrokerID": "string", "UserID": "string"}
#经纪公司编号
#交易用户代码
structDict['CUstpFtdcForceUserExitField'] = CUstpFtdcForceUserExitField

#用户口令修改
CUstpFtdcUserPasswordUpdateField = {"BrokerID": "string", "UserID": "string", "OldPassword": "string",
									"NewPassword": "string"}
#经纪公司编号
#交易用户代码
#旧密码
#新密码
structDict['CUstpFtdcUserPasswordUpdateField'] = CUstpFtdcUserPasswordUpdateField

#输入报单
CUstpFtdcInputOrderField = {"BrokerID": "string", "ExchangeID": "string", "OrderSysID": "string",
							"InvestorID": "string", "UserID": "string", "InstrumentID": "string",
							"UserOrderLocalID": "string", "OrderPriceType": "string", "Direction": "string",
							"OffsetFlag": "string", "HedgeFlag": "string", "LimitPrice": "float", "Volume": "int",
							"TimeCondition": "string", "GTDDate": "string", "VolumeCondition": "string",
							"MinVolume": "int", "StopPrice": "float", "ForceCloseReason": "string",
							"IsAutoSuspend": "int", "BusinessUnit": "string", "UserCustom": "string"}
#经纪公司编号
#交易所代码
#系统报单编号
#投资者编号
#用户代码
#合约代码
#用户本地报单号
#报单类型
#买卖方向
#开平标志
#投机套保标志
#价格
#数量
#有效期类型
#GTD日期
#成交量类型
#最小成交量
#止损价
#强平原因
#自动挂起标志
#业务单元
#用户自定义域
structDict['CUstpFtdcInputOrderField'] = CUstpFtdcInputOrderField

#报单操作
CUstpFtdcOrderActionField = {"ExchangeID": "string", "OrderSysID": "string", "BrokerID": "string",
							 "InvestorID": "string", "UserID": "string", "UserOrderActionLocalID": "string",
							 "UserOrderLocalID": "string", "ActionFlag": "string", "LimitPrice": "float",
							 "VolumeChange": "int"}
#交易所代码
#报单编号
#经纪公司编号
#投资者编号
#用户代码
#本次撤单操作的本地编号
#被撤订单的本地报单编号
#报单操作标志
#价格
#数量变化
structDict['CUstpFtdcOrderActionField'] = CUstpFtdcOrderActionField

#内存表导出
CUstpFtdcMemDbField = {"MemTableName": "string"}
#内存表名
structDict['CUstpFtdcMemDbField'] = CUstpFtdcMemDbField

#响应信息
CUstpFtdcRspInfoField = {"ErrorID": "int", "ErrorMsg": "string"}
#错误代码
#错误信息
structDict['CUstpFtdcRspInfoField'] = CUstpFtdcRspInfoField

#报单查询
CUstpFtdcQryOrderField = {"BrokerID": "string", "UserID": "string", "ExchangeID": "string", "InvestorID": "string",
						  "OrderSysID": "string", "InstrumentID": "string"}
#经纪公司编号
#用户代码
#交易所代码
#投资者编号
#报单编号
#合约代码
structDict['CUstpFtdcQryOrderField'] = CUstpFtdcQryOrderField

#成交查询
CUstpFtdcQryTradeField = {"BrokerID": "string", "UserID": "string", "ExchangeID": "string", "InvestorID": "string",
						  "TradeID": "string", "InstrumentID": "string"}
#经纪公司编号
#用户代码
#交易所代码
#投资者编号
#成交编号
#合约代码
structDict['CUstpFtdcQryTradeField'] = CUstpFtdcQryTradeField

#合约查询
CUstpFtdcQryInstrumentField = {"ExchangeID": "string", "ProductID": "string", "InstrumentID": "string"}
#交易所代码
#产品代码
#合约代码
structDict['CUstpFtdcQryInstrumentField'] = CUstpFtdcQryInstrumentField

#合约查询应答
CUstpFtdcRspInstrumentField = {"ExchangeID": "string", "ProductID": "string", "ProductName": "string",
							   "InstrumentID": "string", "InstrumentName": "string", "DeliveryYear": "int",
							   "DeliveryMonth": "int", "MaxLimitOrderVolume": "int", "MinLimitOrderVolume": "int",
							   "MaxMarketOrderVolume": "int", "MinMarketOrderVolume": "int", "VolumeMultiple": "int",
							   "PriceTick": "float", "Currency": "string", "LongPosLimit": "int",
							   "ShortPosLimit": "int", "LowerLimitPrice": "float", "UpperLimitPrice": "float",
							   "PreSettlementPrice": "float", "InstrumentStatus": "string", "CreateDate": "string",
							   "OpenDate": "string", "ExpireDate": "string", "StartDelivDate": "string",
							   "EndDelivDate": "string", "BasisPrice": "float", "IsTrading": "int",
							   "UnderlyingInstrID": "string", "UnderlyingMultiple": "int", "PositionType": "string",
							   "StrikePrice": "float", "OptionsType": "string"}
#交易所代码
#品种代码
#品种名称
#合约代码
#合约名称
#交割年份
#交割月
#限价单最大下单量
#限价单最小下单量
#市价单最大下单量
#市价单最小下单量
#数量乘数
#报价单位
#币种
#多头限仓
#空头限仓
#跌停板价
#涨停板价
#昨结算
#合约交易状态
#创建日
#上市日
#到期日
#开始交割日
#最后交割日
#挂牌基准价
#当前是否交易
#基础商品代码
#基础商品乘数
#持仓类型
#执行价
#期权类型
structDict['CUstpFtdcRspInstrumentField'] = CUstpFtdcRspInstrumentField

#合约状态
CUstpFtdcInstrumentStatusField = {"ExchangeID": "string", "ProductID": "string", "ProductName": "string",
								  "InstrumentID": "string", "InstrumentName": "string", "DeliveryYear": "int",
								  "DeliveryMonth": "int", "MaxLimitOrderVolume": "int", "MinLimitOrderVolume": "int",
								  "MaxMarketOrderVolume": "int", "MinMarketOrderVolume": "int", "VolumeMultiple": "int",
								  "PriceTick": "float", "Currency": "string", "LongPosLimit": "int",
								  "ShortPosLimit": "int", "LowerLimitPrice": "float", "UpperLimitPrice": "float",
								  "PreSettlementPrice": "float", "InstrumentStatus": "string", "CreateDate": "string",
								  "OpenDate": "string", "ExpireDate": "string", "StartDelivDate": "string",
								  "EndDelivDate": "string", "BasisPrice": "float", "IsTrading": "int",
								  "UnderlyingInstrID": "string", "UnderlyingMultiple": "int", "PositionType": "string",
								  "StrikePrice": "float", "OptionsType": "string"}
#交易所代码
#品种代码
#品种名称
#合约代码
#合约名称
#交割年份
#交割月
#限价单最大下单量
#限价单最小下单量
#市价单最大下单量
#市价单最小下单量
#数量乘数
#报价单位
#币种
#多头限仓
#空头限仓
#跌停板价
#涨停板价
#昨结算
#合约交易状态
#创建日
#上市日
#到期日
#开始交割日
#最后交割日
#挂牌基准价
#当前是否交易
#基础商品代码
#基础商品乘数
#持仓类型
#执行价
#期权类型
structDict['CUstpFtdcInstrumentStatusField'] = CUstpFtdcInstrumentStatusField

#投资者资金查询
CUstpFtdcQryInvestorAccountField = {"BrokerID": "string", "UserID": "string", "InvestorID": "string"}
#经纪公司编号
#用户代码
#投资者编号
structDict['CUstpFtdcQryInvestorAccountField'] = CUstpFtdcQryInvestorAccountField

#投资者资金应答
CUstpFtdcRspInvestorAccountField = {"BrokerID": "string", "InvestorID": "string", "AccountID": "string",
									"PreBalance": "float", "Deposit": "float", "Withdraw": "float",
									"FrozenMargin": "float", "FrozenFee": "float", "FrozenPremium": "float",
									"Fee": "float", "CloseProfit": "float", "PositionProfit": "float",
									"Available": "float", "LongFrozenMargin": "float", "ShortFrozenMargin": "float",
									"LongMargin": "float", "ShortMargin": "float", "ReleaseMargin": "float",
									"DynamicRights": "float", "TodayInOut": "float", "Margin": "float",
									"Premium": "float", "Risk": "float"}
#经纪公司编号
#投资者编号
#资金帐号
#上次结算准备金
#入金金额
#出金金额
#冻结的保证金
#冻结手续费
#冻结权利金
#手续费
#平仓盈亏
#持仓盈亏
#可用资金
#多头冻结的保证金
#空头冻结的保证金
#多头占用保证金
#空头占用保证金
#当日释放保证金
#动态权益
#今日出入金
#占用保证金
#期权权利金收支
#风险度
structDict['CUstpFtdcRspInvestorAccountField'] = CUstpFtdcRspInvestorAccountField

#可用投资者查询
CUstpFtdcQryUserInvestorField = {"BrokerID": "string", "UserID": "string"}
#经纪公司编号
#用户代码
structDict['CUstpFtdcQryUserInvestorField'] = CUstpFtdcQryUserInvestorField

#可用投资者
CUstpFtdcRspUserInvestorField = {"BrokerID": "string", "UserID": "string", "InvestorID": "string"}
#经纪公司编号
#交易用户代码
#投资者编号
structDict['CUstpFtdcRspUserInvestorField'] = CUstpFtdcRspUserInvestorField

#交易编码查询
CUstpFtdcQryTradingCodeField = {"BrokerID": "string", "UserID": "string", "InvestorID": "string",
								"ExchangeID": "string"}
#经纪公司编号
#用户代码
#投资者编号
#交易所代码
structDict['CUstpFtdcQryTradingCodeField'] = CUstpFtdcQryTradingCodeField

#交易编码查询
CUstpFtdcRspTradingCodeField = {"BrokerID": "string", "ExchangeID": "string", "InvestorID": "string",
								"ClientID": "string", "ClientRight": "string", "IsActive": "string"}
#经纪公司编号
#交易所代码
#投资者编号
#客户代码
#客户代码权限
#是否活跃
structDict['CUstpFtdcRspTradingCodeField'] = CUstpFtdcRspTradingCodeField

#交易所查询请求
CUstpFtdcQryExchangeField = {"ExchangeID": "string"}
#交易所代码
structDict['CUstpFtdcQryExchangeField'] = CUstpFtdcQryExchangeField

#交易所查询应答
CUstpFtdcRspExchangeField = {"ExchangeID": "string", "ExchangeName": "string"}
#交易所代码
#交易所名称
structDict['CUstpFtdcRspExchangeField'] = CUstpFtdcRspExchangeField

#投资者持仓查询请求
CUstpFtdcQryInvestorPositionField = {"BrokerID": "string", "UserID": "string", "ExchangeID": "string",
									 "InvestorID": "string", "InstrumentID": "string"}
#经纪公司编号
#用户代码
#交易所代码
#投资者编号
#合约代码
structDict['CUstpFtdcQryInvestorPositionField'] = CUstpFtdcQryInvestorPositionField

#投资者持仓查询应答
CUstpFtdcRspInvestorPositionField = {"InvestorID": "string", "BrokerID": "string", "ExchangeID": "string",
									 "ClientID": "string", "InstrumentID": "string", "Direction": "string",
									 "HedgeFlag": "string", "UsedMargin": "float", "Position": "int",
									 "PositionCost": "float", "YdPosition": "int", "YdPositionCost": "float",
									 "FrozenMargin": "float", "FrozenPosition": "int", "FrozenClosing": "int",
									 "FrozenPremium": "float", "LastTradeID": "string", "LastOrderLocalID": "string",
									 "Currency": "string"}
#投资者编号
#经纪公司编号
#交易所代码
#客户代码
#合约代码
#买卖方向
#投机套保标志
#占用保证金
#今持仓量
#今日持仓成本
#昨持仓量
#昨日持仓成本
#冻结的保证金
#开仓冻结持仓
#平仓冻结持仓
#冻结的权利金
#最后一笔成交编号
#最后一笔本地报单编号
#币种
structDict['CUstpFtdcRspInvestorPositionField'] = CUstpFtdcRspInvestorPositionField

#合规参数查询请求
CUstpFtdcQryComplianceParamField = {"BrokerID": "string", "UserID": "string", "InvestorID": "string",
									"ExchangeID": "string"}
#经纪公司编号
#用户代码
#投资者编号
#交易所代码
structDict['CUstpFtdcQryComplianceParamField'] = CUstpFtdcQryComplianceParamField

#合规参数查询应答
CUstpFtdcRspComplianceParamField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
									"ClientID": "string", "DailyMaxOrder": "int", "DailyMaxOrderAction": "int",
									"DailyMaxErrorOrder": "int", "DailyMaxOrderVolume": "int",
									"DailyMaxOrderActionVolume": "int"}
#经纪公司编号
#投资者编号
#交易所代码
#客户号
#每日最大报单笔
#每日最大撤单笔
#每日最大错单笔
#每日最大报单手
#每日最大撤单手
structDict['CUstpFtdcRspComplianceParamField'] = CUstpFtdcRspComplianceParamField

#用户查询
CUstpFtdcQryUserField = {"StartUserID": "string", "EndUserID": "string"}
#交易用户代码
#交易用户代码
structDict['CUstpFtdcQryUserField'] = CUstpFtdcQryUserField

#用户
CUstpFtdcUserField = {"BrokerID": "string", "UserID": "string", "Password": "string", "IsActive": "string",
					  "UserName": "string", "UserType": "string", "Department": "string", "GrantFuncSet": "string",
					  "SetUserID": "string", "CommandDate": "string", "CommandTime": "string"}
#经纪公司编号
#用户代码
#用户登录密码
#是否活跃
#用户名称
#用户类型
#营业部
#授权功能集
#修改用户编号
#操作日期
#操作时间
structDict['CUstpFtdcUserField'] = CUstpFtdcUserField

#投资者手续费率查询
CUstpFtdcQryInvestorFeeField = {"BrokerID": "string", "UserID": "string", "InvestorID": "string",
								"ExchangeID": "string", "InstrumentID": "string"}
#经纪公司编号
#用户代码
#投资者编号
#交易所代码
#合约代码
structDict['CUstpFtdcQryInvestorFeeField'] = CUstpFtdcQryInvestorFeeField

#投资者手续费率
CUstpFtdcInvestorFeeField = {"BrokerID": "string", "ClientID": "string", "ExchangeID": "string",
							 "InstrumentID": "string", "ProductID": "string", "OpenFeeRate": "float",
							 "OpenFeeAmt": "float", "OffsetFeeRate": "float", "OffsetFeeAmt": "float",
							 "OTFeeRate": "float", "OTFeeAmt": "float"}
#经纪公司编号
#客户号
#交易所代码
#合约代码
#品种代码
#开仓手续费按比例
#开仓手续费按手数
#平仓手续费按比例
#平仓手续费按手数
#平今仓手续费按比例
#平今仓手续费按手数
structDict['CUstpFtdcInvestorFeeField'] = CUstpFtdcInvestorFeeField

#投资者保证金率查询
CUstpFtdcQryInvestorMarginField = {"BrokerID": "string", "UserID": "string", "InvestorID": "string",
								   "ExchangeID": "string", "InstrumentID": "string"}
#经纪公司编号
#用户代码
#投资者编号
#交易所代码
#合约代码
structDict['CUstpFtdcQryInvestorMarginField'] = CUstpFtdcQryInvestorMarginField

#投资者保证金率
CUstpFtdcInvestorMarginField = {"BrokerID": "string", "ClientID": "string", "ExchangeID": "string",
								"InstrumentID": "string", "ProductID": "string", "LongMarginRate": "float",
								"LongMarginAmt": "float", "ShortMarginRate": "float", "ShortMarginAmt": "float"}
#经纪公司编号
#客户号
#交易所代码
#合约代码
#品种代码
#多头占用保证金按比例
#多头保证金按手数
#空头占用保证金按比例
#空头保证金按手数
structDict['CUstpFtdcInvestorMarginField'] = CUstpFtdcInvestorMarginField

#成交
CUstpFtdcTradeField = {"BrokerID": "string", "ExchangeID": "string", "TradingDay": "string", "ParticipantID": "string",
					   "SeatID": "string", "InvestorID": "string", "ClientID": "string", "UserID": "string",
					   "TradeID": "string", "OrderSysID": "string", "UserOrderLocalID": "string",
					   "InstrumentID": "string", "Direction": "string", "OffsetFlag": "string", "HedgeFlag": "string",
					   "TradePrice": "float", "TradeVolume": "int", "TradeTime": "string", "ClearingPartID": "string"}
#经纪公司编号
#交易所代码
#交易日
#会员编号
#下单席位号
#投资者编号
#客户号
#用户编号
#成交编号
#报单编号
#本地报单编号
#合约代码
#买卖方向
#开平标志
#投机套保标志
#成交价格
#成交数量
#成交时间
#清算会员编号
structDict['CUstpFtdcTradeField'] = CUstpFtdcTradeField

#报单
CUstpFtdcOrderField = {"BrokerID": "string", "ExchangeID": "string", "OrderSysID": "string", "InvestorID": "string",
					   "UserID": "string", "InstrumentID": "string", "UserOrderLocalID": "string",
					   "OrderPriceType": "string", "Direction": "string", "OffsetFlag": "string", "HedgeFlag": "string",
					   "LimitPrice": "float", "Volume": "int", "TimeCondition": "string", "GTDDate": "string",
					   "VolumeCondition": "string", "MinVolume": "int", "StopPrice": "float",
					   "ForceCloseReason": "string", "IsAutoSuspend": "int", "BusinessUnit": "string",
					   "UserCustom": "string", "TradingDay": "string", "ParticipantID": "string", "ClientID": "string",
					   "SeatID": "string", "InsertTime": "string", "OrderLocalID": "string", "OrderSource": "string",
					   "OrderStatus": "string", "CancelTime": "string", "CancelUserID": "string", "VolumeTraded": "int",
					   "VolumeRemain": "int"}
#经纪公司编号
#交易所代码
#系统报单编号
#投资者编号
#用户代码
#合约代码
#用户本地报单号
#报单类型
#买卖方向
#开平标志
#投机套保标志
#价格
#数量
#有效期类型
#GTD日期
#成交量类型
#最小成交量
#止损价
#强平原因
#自动挂起标志
#业务单元
#用户自定义域
#交易日
#会员编号
#客户号
#下单席位号
#插入时间
#本地报单编号
#报单来源
#报单状态
#撤销时间
#撤单用户编号
#今成交数量
#剩余数量
structDict['CUstpFtdcOrderField'] = CUstpFtdcOrderField

#数据流回退
CUstpFtdcFlowMessageCancelField = {"SequenceSeries": "int", "TradingDay": "string", "DataCenterID": "int",
								   "StartSequenceNo": "int", "EndSequenceNo": "int"}
#序列系列号
#交易日
#数据中心代码
#回退起始序列号
#回退结束序列号
structDict['CUstpFtdcFlowMessageCancelField'] = CUstpFtdcFlowMessageCancelField

#信息分发
CUstpFtdcDisseminationField = {"SequenceSeries": "int", "SequenceNo": "int"}
#序列系列号
#序列号
structDict['CUstpFtdcDisseminationField'] = CUstpFtdcDisseminationField

#出入金结果
CUstpFtdcInvestorAccountDepositResField = {"BrokerID": "string", "UserID": "string", "InvestorID": "string",
										   "AccountID": "string", "AccountSeqNo": "string", "Amount": "float",
										   "AmountDirection": "string", "Available": "float", "Balance": "float"}
#经纪公司编号
#用户代码
#投资者编号
#资金帐号
#资金流水号
#金额
#出入金方向
#可用资金
#结算准备金
structDict['CUstpFtdcInvestorAccountDepositResField'] = CUstpFtdcInvestorAccountDepositResField

#行情基础属性
CUstpFtdcMarketDataBaseField = {"TradingDay": "string", "SettlementGroupID": "string", "SettlementID": "int",
								"PreSettlementPrice": "float", "PreClosePrice": "float", "PreOpenInterest": "float",
								"PreDelta": "float"}
#交易日
#结算组代码
#结算编号
#昨结算
#昨收盘
#昨持仓量
#昨虚实度
structDict['CUstpFtdcMarketDataBaseField'] = CUstpFtdcMarketDataBaseField

#行情静态属性
CUstpFtdcMarketDataStaticField = {"OpenPrice": "float", "HighestPrice": "float", "LowestPrice": "float",
								  "ClosePrice": "float", "UpperLimitPrice": "float", "LowerLimitPrice": "float",
								  "SettlementPrice": "float", "CurrDelta": "float"}
#今开盘
#最高价
#最低价
#今收盘
#涨停板价
#跌停板价
#今结算
#今虚实度
structDict['CUstpFtdcMarketDataStaticField'] = CUstpFtdcMarketDataStaticField

#行情最新成交属性
CUstpFtdcMarketDataLastMatchField = {"LastPrice": "float", "Volume": "int", "Turnover": "float",
									 "OpenInterest": "float"}
#最新价
#数量
#成交金额
#持仓量
structDict['CUstpFtdcMarketDataLastMatchField'] = CUstpFtdcMarketDataLastMatchField

#行情最优价属性
CUstpFtdcMarketDataBestPriceField = {"BidPrice1": "float", "BidVolume1": "int", "AskPrice1": "float",
									 "AskVolume1": "int"}
#申买价一
#申买量一
#申卖价一
#申卖量一
structDict['CUstpFtdcMarketDataBestPriceField'] = CUstpFtdcMarketDataBestPriceField

#行情申买二、三属性
CUstpFtdcMarketDataBid23Field = {"BidPrice2": "float", "BidVolume2": "int", "BidPrice3": "float", "BidVolume3": "int"}
#申买价二
#申买量二
#申买价三
#申买量三
structDict['CUstpFtdcMarketDataBid23Field'] = CUstpFtdcMarketDataBid23Field

#行情申卖二、三属性
CUstpFtdcMarketDataAsk23Field = {"AskPrice2": "float", "AskVolume2": "int", "AskPrice3": "float", "AskVolume3": "int"}
#申卖价二
#申卖量二
#申卖价三
#申卖量三
structDict['CUstpFtdcMarketDataAsk23Field'] = CUstpFtdcMarketDataAsk23Field

#行情申买四、五属性
CUstpFtdcMarketDataBid45Field = {"BidPrice4": "float", "BidVolume4": "int", "BidPrice5": "float", "BidVolume5": "int"}
#申买价四
#申买量四
#申买价五
#申买量五
structDict['CUstpFtdcMarketDataBid45Field'] = CUstpFtdcMarketDataBid45Field

#行情申卖四、五属性
CUstpFtdcMarketDataAsk45Field = {"AskPrice4": "float", "AskVolume4": "int", "AskPrice5": "float", "AskVolume5": "int"}
#申卖价四
#申卖量四
#申卖价五
#申卖量五
structDict['CUstpFtdcMarketDataAsk45Field'] = CUstpFtdcMarketDataAsk45Field

#行情更新时间属性
CUstpFtdcMarketDataUpdateTimeField = {"InstrumentID": "string", "UpdateTime": "string", "UpdateMillisec": "int"}
#合约代码
#最后修改时间
#最后修改毫秒
structDict['CUstpFtdcMarketDataUpdateTimeField'] = CUstpFtdcMarketDataUpdateTimeField

#深度行情
CUstpFtdcDepthMarketDataField = {"TradingDay": "string", "SettlementGroupID": "string", "SettlementID": "int",
								 "PreSettlementPrice": "float", "PreClosePrice": "float", "PreOpenInterest": "float",
								 "PreDelta": "float", "OpenPrice": "float", "HighestPrice": "float",
								 "LowestPrice": "float", "ClosePrice": "float", "UpperLimitPrice": "float",
								 "LowerLimitPrice": "float", "SettlementPrice": "float", "CurrDelta": "float",
								 "LastPrice": "float", "Volume": "int", "Turnover": "float", "OpenInterest": "float",
								 "BidPrice1": "float", "BidVolume1": "int", "AskPrice1": "float", "AskVolume1": "int",
								 "BidPrice2": "float", "BidVolume2": "int", "BidPrice3": "float", "BidVolume3": "int",
								 "AskPrice2": "float", "AskVolume2": "int", "AskPrice3": "float", "AskVolume3": "int",
								 "BidPrice4": "float", "BidVolume4": "int", "BidPrice5": "float", "BidVolume5": "int",
								 "AskPrice4": "float", "AskVolume4": "int", "AskPrice5": "float", "AskVolume5": "int",
								 "InstrumentID": "string", "UpdateTime": "string", "UpdateMillisec": "int"}
#交易日
#结算组代码
#结算编号
#昨结算
#昨收盘
#昨持仓量
#昨虚实度
#今开盘
#最高价
#最低价
#今收盘
#涨停板价
#跌停板价
#今结算
#今虚实度
#最新价
#数量
#成交金额
#持仓量
#申买价一
#申买量一
#申卖价一
#申卖量一
#申买价二
#申买量二
#申买价三
#申买量三
#申卖价二
#申卖量二
#申卖价三
#申卖量三
#申买价四
#申买量四
#申买价五
#申买量五
#申卖价四
#申卖量四
#申卖价五
#申卖量五
#合约代码
#最后修改时间
#最后修改毫秒
structDict['CUstpFtdcDepthMarketDataField'] = CUstpFtdcDepthMarketDataField

#订阅合约的相关信息
CUstpFtdcSpecificInstrumentField = {"InstrumentID": "string"}
#合约代码
structDict['CUstpFtdcSpecificInstrumentField'] = CUstpFtdcSpecificInstrumentField




