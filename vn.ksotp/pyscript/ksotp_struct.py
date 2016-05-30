# encoding: UTF-8

structDict = {}











#响应信息
CKSOTPRspInfoField = {"ErrorID": "int", "ErrorMsg": "string"}
#错误代码
#错误信息
structDict['CKSOTPRspInfoField'] = CKSOTPRspInfoField


#用户登录请求
CKSOTPReqUserLoginField = {"BrokerID": "string", "UserID": "string", "Password": "string", "UserProductInfo": "string",
						   "MacAddress": "string", "ClientIPAddress": "string"}
#经纪公司代码
#用户代码
#密码
#用户端产品信息
#Mac地址
#终端IP地址
structDict['CKSOTPReqUserLoginField'] = CKSOTPReqUserLoginField


#用户登录应答
CKSOTPRspUserLoginField = {"BrokerID": "string", "TradingDay": "string", "LoginTime": "string", "UserID": "string",
						   "SystemName": "string", "FrontID": "int", "SessionID": "int", "MaxOrderRef": "string",
						   "SSETime": "string"}
#经纪公司代码
#交易日
#登录成功时间
#用户代码
#交易系统名称
#前置编号
#会话编号
#最大报单引用
#上证所时间
structDict['CKSOTPRspUserLoginField'] = CKSOTPRspUserLoginField


#用户登出请求
CKSOTPUserLogoutField = {"BrokerID": "string", "UserID": "string"}
#经纪公司代码
#用户代码
structDict['CKSOTPUserLogoutField'] = CKSOTPUserLogoutField


#用户口令变更
CKSOTPUserPasswordUpdateField = {"BrokerID": "string", "UserID": "string", "OldPassword": "string",
								 "NewPassword": "string"}
#经纪公司代码
#用户代码
#原来的口令
#新的口令
structDict['CKSOTPUserPasswordUpdateField'] = CKSOTPUserPasswordUpdateField


#资金账户口令变更域
CKSOTPTradingAccountPasswordUpdateField = {"BrokerID": "string", "AccountID": "string", "OldPassword": "string",
										   "NewPassword": "string"}
#经纪公司代码
#投资者帐号
#原来的口令
#新的口令
structDict['CKSOTPTradingAccountPasswordUpdateField'] = CKSOTPTradingAccountPasswordUpdateField


#输入报单
CKSOTPInputOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
						 "UserID": "string", "OrderPriceType": "string", "Direction": "string", "OffsetFlag": "string",
						 "HedgeFlag": "string", "LimitPrice": "float", "VolumeTotalOriginal": "int",
						 "TimeCondition": "string", "GTDDate": "string", "VolumeCondition": "string",
						 "MinVolume": "int", "ContingentCondition": "string", "StopPrice": "float",
						 "ForceCloseReason": "string", "IsAutoSuspend": "int", "BusinessUnit": "string",
						 "RequestID": "int", "UserForceClose": "int", "IsSwapOrder": "int", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
#报单价格条件
#买卖方向
#开平标志
#备兑标志
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
structDict['CKSOTPInputOrderField'] = CKSOTPInputOrderField


#输入报单操作
CKSOTPInputOrderActionField = {"BrokerID": "string", "InvestorID": "string", "OrderRef": "string", "RequestID": "int",
							   "FrontID": "int", "SessionID": "int", "ExchangeID": "string", "OrderSysID": "string",
							   "ActionFlag": "string", "LimitPrice": "float", "VolumeChange": "int", "UserID": "string",
							   "InstrumentID": "string"}
#经纪公司代码
#投资者代码
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
structDict['CKSOTPInputOrderActionField'] = CKSOTPInputOrderActionField


#查询报单
CKSOTPQryOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "ExchangeID": "string",
					   "OrderSysID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#报单编号
structDict['CKSOTPQryOrderField'] = CKSOTPQryOrderField


#查询成交
CKSOTPQryTradeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "ExchangeID": "string",
					   "TradeTimeStart": "string", "TradeTimeEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#开始时间
#结束时间
structDict['CKSOTPQryTradeField'] = CKSOTPQryTradeField


#查询投资者持仓
CKSOTPQryInvestorPositionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								  "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CKSOTPQryInvestorPositionField'] = CKSOTPQryInvestorPositionField


#投资者持仓
CKSOTPInvestorPositionField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
							   "PosiDirection": "string", "HedgeFlag": "string", "PositionDate": "string",
							   "YdPosition": "int", "Position": "int", "LongFrozen": "int", "ShortFrozen": "int",
							   "LongFrozenAmount": "float", "ShortFrozenAmount": "float", "OpenVolume": "int",
							   "OpenAmount": "float", "CloseAmount": "float", "PositionCost": "float",
							   "UseMargin": "float", "FrozenMargin": "float", "FrozenCash": "float",
							   "FrozenCommission": "float", "CashIn": "float", "Commission": "float",
							   "CloseProfit": "float", "PositionProfit": "float", "PreSettlementPrice": "float",
							   "SettlementPrice": "float", "TradingDay": "string", "SettlementID": "int",
							   "OpenCost": "float", "ExchangeMargin": "float", "CloseProfitByDate": "float",
							   "CloseProfitByTrade": "float", "TodayPosition": "int", "MarginRateByMoney": "float",
							   "MarginRateByVolume": "float", "StrikeFrozen": "int", "StrikeFrozenAmount": "float",
							   "ExchangeID": "string"}
#合约代码
#经纪公司代码
#投资者代码
#持仓多空方向
#备兑标志
#持仓日期
#上日持仓
#今日持仓
#多头冻结
#空头冻结
#开仓冻结金额
#开仓冻结金额
#开仓量
#开仓金额
#平仓金额
#持仓成本
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
#逐日盯市平仓盈亏
#逐笔对冲平仓盈亏
#今日持仓
#保证金率
#保证金率(按手数)
#执行冻结
#执行冻结金额
#交易所代码
structDict['CKSOTPInvestorPositionField'] = CKSOTPInvestorPositionField


#查询资金账户
CKSOTPQryTradingAccountField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CKSOTPQryTradingAccountField'] = CKSOTPQryTradingAccountField


#资金账户
CKSOTPTradingAccountField = {"BrokerID": "string", "AccountID": "string", "PreBalance": "float", "PreMargin": "float",
							 "Deposit": "float", "Withdraw": "float", "FrozenMargin": "float", "FrozenCash": "float",
							 "FrozenCommission": "float", "CurrMargin": "float", "CashIn": "float",
							 "Commission": "float", "CloseProfit": "float", "PositionProfit": "float",
							 "Balance": "float", "Available": "float", "WithdrawQuota": "float", "Reserve": "float",
							 "TradingDay": "string", "SettlementID": "int", "Credit": "float", "Mortgage": "float",
							 "ExchangeMargin": "float", "DeliveryMargin": "float", "ExchangeDeliveryMargin": "float"}
#经纪公司代码
#投资者帐号
#上次结算准备金
#上次占用的保证金
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
#证券结算准备金
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
structDict['CKSOTPTradingAccountField'] = CKSOTPTradingAccountField


#查询投资者
CKSOTPQryInvestorField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CKSOTPQryInvestorField'] = CKSOTPQryInvestorField


#投资者
CKSOTPInvestorField = {"InvestorID": "string", "BrokerID": "string", "InvestorName": "string",
					   "IdentifiedCardType": "string", "IdentifiedCardNo": "string", "IsActive": "int",
					   "Telephone": "string", "Address": "string", "OpenDate": "string", "Mobile": "string"}
#投资者代码
#经纪公司代码
#投资者名称
#证件类型
#证件号码
#是否活跃
#联系电话
#通讯地址
#开户日期
#手机
structDict['CKSOTPInvestorField'] = CKSOTPInvestorField


#查询合约账号
CKSOTPQryTradingCodeField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
structDict['CKSOTPQryTradingCodeField'] = CKSOTPQryTradingCodeField


#交易编码
CKSOTPTradingCodeField = {"InvestorID": "string", "BrokerID": "string", "ExchangeID": "string", "ClientID": "string",
						  "IsActive": "int", "ClientIDType": "string"}
#投资者代码
#经纪公司代码
#交易所代码
#合约账号
#是否活跃
#交易编码类型
structDict['CKSOTPTradingCodeField'] = CKSOTPTradingCodeField


#查询交易所
CKSOTPQryExchangeField = {"ExchangeID": "string"}
#交易所代码
structDict['CKSOTPQryExchangeField'] = CKSOTPQryExchangeField


#交易所
CKSOTPExchangeField = {"ExchangeID": "string", "ExchangeName": "string"}
#交易所代码
#交易所名称
structDict['CKSOTPExchangeField'] = CKSOTPExchangeField


#查询合约
CKSOTPQryInstrumentField = {"InstrumentID": "string", "ExchangeID": "string"}
#合约代码
#交易所代码
structDict['CKSOTPQryInstrumentField'] = CKSOTPQryInstrumentField


#合约
CKSOTPInstrumentField = {"InstrumentID": "string", "ExchangeID": "string", "InstrumentName": "string",
						 "ExchangeInstID": "string", "ProductID": "string", "ProductClass": "string",
						 "DeliveryYear": "int", "DeliveryMonth": "int", "MaxMarketOrderVolume": "int",
						 "MinMarketOrderVolume": "int", "MaxLimitOrderVolume": "int", "MinLimitOrderVolume": "int",
						 "VolumeMultiple": "int", "PriceTick": "float", "CreateDate": "string", "OpenDate": "string",
						 "ExpireDate": "string", "StartDelivDate": "string", "EndDelivDate": "string",
						 "InstLifePhase": "string", "IsTrading": "int", "PositionType": "string",
						 "PositionDateType": "string", "LongMarginRatio": "float", "ShortMarginRatio": "float",
						 "UnderlyingInstrID": "string", "StrikePrice": "float", "OptionsType": "string",
						 "UnderlyingMultiple": "float", "InstrumentCode": "string"}
#合约代码
#交易所代码
#合约名称
#合约在交易所的代码
#品种代码
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
#基础商品代码
#执行价
#期权类型
#合约基础商品乘数
#合约标识码
structDict['CKSOTPInstrumentField'] = CKSOTPInstrumentField


#查询投资者持仓明细
CKSOTPQryInvestorPositionDetailField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
										"ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CKSOTPQryInvestorPositionDetailField'] = CKSOTPQryInvestorPositionDetailField


#投资者持仓明细
CKSOTPInvestorPositionDetailField = {"InstrumentID": "string", "BrokerID": "string", "InvestorID": "string",
									 "HedgeFlag": "string", "Direction": "string", "OpenDate": "string",
									 "TradeID": "string", "Volume": "int", "OpenPrice": "float", "TradingDay": "string",
									 "SettlementID": "int", "TradeType": "string", "ExchangeID": "string",
									 "CloseProfitByDate": "float", "CloseProfitByTrade": "float",
									 "PositionProfitByDate": "float", "PositionProfitByTrade": "float",
									 "Margin": "float", "ExchMargin": "float", "MarginRateByMoney": "float",
									 "MarginRateByVolume": "float", "LastSettlementPrice": "float",
									 "SettlementPrice": "float"}
#合约代码
#经纪公司代码
#投资者代码
#备兑标志
#买卖
#开仓日期
#成交编号
#数量
#开仓价
#交易日
#结算编号
#成交类型
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
structDict['CKSOTPInvestorPositionDetailField'] = CKSOTPInvestorPositionDetailField


#查询交易事件通知
CKSOTPQryTradingNoticeField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CKSOTPQryTradingNoticeField'] = CKSOTPQryTradingNoticeField


#用户事件通知
CKSOTPTradingNoticeField = {"BrokerID": "string", "InvestorID": "string", "SequenceSeries": "int", "UserID": "string",
							"SendTime": "string", "SequenceNo": "int", "FieldContent": "string"}
#经纪公司代码
#投资者代码
#序列系列号
#用户代码
#发送时间
#序列号
#消息正文
structDict['CKSOTPTradingNoticeField'] = CKSOTPTradingNoticeField


#用户事件通知信息
CKSOTPTradingNoticeInfoField = {"BrokerID": "string", "InvestorID": "string", "SendTime": "string",
								"FieldContent": "string", "SequenceSeries": "int", "SequenceNo": "int"}
#经纪公司代码
#投资者代码
#发送时间
#消息正文
#序列系列号
#序列号
structDict['CKSOTPTradingNoticeInfoField'] = CKSOTPTradingNoticeInfoField


#输入的执行宣告
CKSOTPInputExecOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							 "ExecOrderRef": "string", "UserID": "string", "Volume": "int", "RequestID": "int",
							 "BusinessUnit": "string", "OffsetFlag": "string", "HedgeFlag": "string",
							 "ActionType": "string", "PosiDirection": "string", "ReservePositionFlag": "string",
							 "CloseFlag": "string", "ExchangeID": "string"}
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
structDict['CKSOTPInputExecOrderField'] = CKSOTPInputExecOrderField


#输入执行宣告操作
CKSOTPInputExecOrderActionField = {"BrokerID": "string", "InvestorID": "string", "ExecOrderActionRef": "int",
								   "ExecOrderRef": "string", "RequestID": "int", "FrontID": "int", "SessionID": "int",
								   "ExchangeID": "string", "ExecOrderSysID": "string", "ActionFlag": "string",
								   "UserID": "string", "InstrumentID": "string"}
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
structDict['CKSOTPInputExecOrderActionField'] = CKSOTPInputExecOrderActionField


#录入锁定
CKSOTPInputLockField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "LockRef": "string",
						"UserID": "string", "Volume": "int", "RequestID": "int", "BusinessUnit": "string",
						"LockType": "string", "ExchangeID": "string"}
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
structDict['CKSOTPInputLockField'] = CKSOTPInputLockField


#锁定
CKSOTPLockField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "LockRef": "string",
				   "UserID": "string", "Volume": "int", "RequestID": "int", "BusinessUnit": "string",
				   "LockType": "string", "LockLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
				   "ClientID": "string", "ExchangeInstID": "string", "TraderID": "string", "InstallID": "int",
				   "OrderSubmitStatus": "string", "NotifySequence": "int", "TradingDay": "string",
				   "SettlementID": "int", "LockSysID": "string", "InsertDate": "string", "InsertTime": "string",
				   "CancelTime": "string", "LockStatus": "string", "ClearingPartID": "string", "SequenceNo": "int",
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
structDict['CKSOTPLockField'] = CKSOTPLockField


#查询锁定
CKSOTPQryLockField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "ExchangeID": "string",
					  "LockSysID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#锁定编号
structDict['CKSOTPQryLockField'] = CKSOTPQryLockField


#执行宣告查询
CKSOTPQryExecOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						   "ExchangeID": "string", "ExecOrderSysID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#执行宣告编号
structDict['CKSOTPQryExecOrderField'] = CKSOTPQryExecOrderField


#输入查询宣告数量
CKSOTPQryExecOrderVolumeField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
								 "InstrumentID": "string", "ProductID": "string", "HedgeFlag": "string",
								 "Direction": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
#产品代码
#投机套保标志
#买卖标志
structDict['CKSOTPQryExecOrderVolumeField'] = CKSOTPQryExecOrderVolumeField


#输出查询宣告数量
CKSOTPExecOrderVolumeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							  "ProductID": "string", "HedgeFlag": "string", "ExecVolume": "int", "ActionVolume": "int",
							  "ExecedVolume": "int", "ActionedVolume": "int", "Direction": "string"}
#经纪公司代码
#投资者代码
#合约代码
#产品代码
#投机套保标志
#可申请执行量
#可申请放弃量
#已申请执行量
#已申请放弃量
#买卖标志
structDict['CKSOTPExecOrderVolumeField'] = CKSOTPExecOrderVolumeField


#查询锁定证券仓位
CKSOTPQryLockPositionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							  "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CKSOTPQryLockPositionField'] = CKSOTPQryLockPositionField


#锁定证券仓位
CKSOTPLockPositionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						   "ExchangeID": "string", "Volume": "int", "FrozenVolume": "int"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
#数量
#已锁定数量
structDict['CKSOTPLockPositionField'] = CKSOTPLockPositionField


#输入查询标的券信息请求
CKSOTPQryUnderlyingStockInfoField = {"BrokerID": "string", "ExchangeID": "string", "ProductID": "string"}
#经纪公司代码
#交易所代码
#品种代码
structDict['CKSOTPQryUnderlyingStockInfoField'] = CKSOTPQryUnderlyingStockInfoField


#输出查询标的券信息请求
CKSOTPUnderlyingStockInfoField = {"BrokerID": "string", "ExchangeID": "string", "ProductID": "string",
								  "PreClosePrice": "float", "GuarantRatio": "float"}
#经纪公司代码
#交易所代码
#品种代码
#昨收盘
#安全系数
structDict['CKSOTPUnderlyingStockInfoField'] = CKSOTPUnderlyingStockInfoField


#输入查询个股期权手续费率请求
CKSOTPQryOTPInsCommRateField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
								"ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#交易所代码
structDict['CKSOTPQryOTPInsCommRateField'] = CKSOTPQryOTPInsCommRateField


#输出查询个股期权合约手续费率
CKSOTPOTPInsCommRateField = {"InstrumentID": "string", "InvestorRange": "string", "BrokerID": "string",
							 "InvestorID": "string", "OpenRatioByMoney": "float", "OpenRatioByVolume": "float",
							 "CloseRatioByMoney": "float", "CloseRatioByVolume": "float",
							 "CloseTodayRatioByMoney": "float", "CloseTodayRatioByVolume": "float",
							 "StrikeRatioByMoney": "float", "StrikeRatioByVolume": "float", "ExchangeID": "string"}
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
structDict['CKSOTPOTPInsCommRateField'] = CKSOTPOTPInsCommRateField


#输入查询个股期权合约保证金率请求
CKSOTPQryInstrumentMarginRateField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
									  "HedgeFlag": "string", "ExchangeID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#投机套保标志
#交易所代码
structDict['CKSOTPQryInstrumentMarginRateField'] = CKSOTPQryInstrumentMarginRateField


#输出查询个股期权合约保证金率
CKSOTPInstrumentMarginRateField = {"InstrumentID": "string", "InvestorRange": "string", "BrokerID": "string",
								   "InvestorID": "string", "HedgeFlag": "string", "LongMarginRatioByMoney": "float",
								   "LongMarginRatioByVolume": "float", "ShortMarginRatioByMoney": "float",
								   "ShortMarginRatioByVolume": "float", "IsRelative": "int", "ExchangeID": "string"}
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
#交易所代码
structDict['CKSOTPInstrumentMarginRateField'] = CKSOTPInstrumentMarginRateField


#输入个股行权指派信息
CKSOTPQryOTPAssignmentField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
							   "InstrumentID": "string", "Direction": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#合约代码
#买卖
structDict['CKSOTPQryOTPAssignmentField'] = CKSOTPQryOTPAssignmentField


#输出个股行权指派信息
CKSOTPOTPAssignmentField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							"Direction": "string", "ExchangeID": "string", "InstrumentName": "string",
							"ProductID": "string", "HedgeFlag": "string", "YdPosition": "int", "AssInsVo": "int",
							"AssProVol": "int", "FeePay": "float", "OptionsType": "string", "DeliveryDay": "string",
							"StockID": "string"}
#经纪公司代码
#投资者代码
#合约代码
#买卖
#交易所代码
#合约名称
#产品代码
#投机套保标志
#上日持仓
#行权指派合约数量
#行权标的证券数量
#行权指派应付金额
#期权C/P标志
#行权交收日
#个股合约标识码
structDict['CKSOTPOTPAssignmentField'] = CKSOTPOTPAssignmentField


#查询行情
CKSOTPQryDepthMarketDataField = {"InstrumentID": "string", "ExchangeID": "string"}
#合约代码
#交易所代码
structDict['CKSOTPQryDepthMarketDataField'] = CKSOTPQryDepthMarketDataField


#深度行情
CKSOTPDepthMarketDataField = {"TradingDay": "string", "InstrumentID": "string", "ExchangeID": "string",
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
structDict['CKSOTPDepthMarketDataField'] = CKSOTPDepthMarketDataField


#发给做市商的询价请求
CKSOTPForQuoteRspField = {"TradingDay": "string", "InstrumentID": "string", "ForQuoteSysID": "string",
						  "ForQuoteTime": "string", "ActionDay": "string", "ExchangeID": "string"}
#交易日
#合约代码
#询价编号
#询价时间
#业务日期
#交易所代码
structDict['CKSOTPForQuoteRspField'] = CKSOTPForQuoteRspField


#报单
CKSOTPOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
					"UserID": "string", "OrderPriceType": "string", "Direction": "string", "OffsetFlag": "string",
					"LimitPrice": "float", "HedgeFlag": "string", "VolumeTotalOriginal": "int",
					"TimeCondition": "string", "GTDDate": "string", "VolumeCondition": "string", "MinVolume": "int",
					"ContingentCondition": "string", "StopPrice": "float", "ForceCloseReason": "string",
					"BusinessUnit": "string", "RequestID": "int", "OrderLocalID": "string", "ExchangeID": "string",
					"ParticipantID": "string", "ClientID": "string", "ExchangeInstID": "string", "TraderID": "string",
					"OrderSubmitStatus": "string", "NotifySequence": "int", "TradingDay": "string",
					"SettlementID": "int", "OrderSysID": "string", "OrderSource": "string", "OrderStatus": "string",
					"OrderType": "string", "VolumeTraded": "int", "VolumeTotal": "int", "InsertDate": "string",
					"InsertTime": "string", "ActiveTime": "string", "UpdateTime": "string", "CancelTime": "string",
					"SequenceNo": "int", "FrontID": "int", "SessionID": "int", "UserProductInfo": "string",
					"StatusMsg": "string", "UserForceClose": "int", "ActiveUserID": "string", "BrokerOrderSeq": "int"}
#经纪公司代码
#投资者代码
#合约代码
#报单引用
#用户代码
#报单价格条件
#买卖方向
#开平标志
#价格
#备兑标志
#数量
#有效期类型
#GTD日期
#成交量类型
#最小成交量
#触发条件
#止损价
#强平原因
#业务单元
#请求编号
#本地报单编号
#交易所代码
#会员代码
#合约账号
#合约在交易所的代码
#交易所交易员代码
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
#最后修改时间
#撤销时间
#序号
#前置编号
#会话编号
#用户端产品信息
#状态信息
#用户强评标志
#操作用户代码
#经纪公司报单编号
structDict['CKSOTPOrderField'] = CKSOTPOrderField


#成交
CKSOTPTradeField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "OrderRef": "string",
					"UserID": "string", "ExchangeID": "string", "TradeID": "string", "Direction": "string",
					"OrderSysID": "string", "ParticipantID": "string", "ClientID": "string", "TradingRole": "string",
					"ExchangeInstID": "string", "OffsetFlag": "string", "HedgeFlag": "string", "Price": "float",
					"Volume": "int", "TradeDate": "string", "TradeTime": "string", "TradeType": "string",
					"PriceSource": "string", "TraderID": "string", "OrderLocalID": "string", "ClearingPartID": "string",
					"BusinessUnit": "string", "SequenceNo": "int", "TradingDay": "string", "BrokerOrderSeq": "int",
					"TradeSource": "string"}
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
#合约账号
#交易角色
#合约在交易所的代码
#开平标志
#备兑标志
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
#经纪公司报单编号
#成交来源
structDict['CKSOTPTradeField'] = CKSOTPTradeField


#执行宣告
CKSOTPExecOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
						"ExecOrderRef": "string", "UserID": "string", "Volume": "int", "RequestID": "int",
						"BusinessUnit": "string", "OffsetFlag": "string", "HedgeFlag": "string", "ActionType": "string",
						"PosiDirection": "string", "ReservePositionFlag": "string", "CloseFlag": "string",
						"ExecOrderLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
						"ClientID": "string", "ExchangeInstID": "string", "TraderID": "string", "InstallID": "int",
						"OrderSubmitStatus": "string", "NotifySequence": "int", "TradingDay": "string",
						"SettlementID": "int", "ExecOrderSysID": "string", "InsertDate": "string",
						"InsertTime": "string", "CancelTime": "string", "ExecResult": "string",
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
structDict['CKSOTPExecOrderField'] = CKSOTPExecOrderField


#合约状态
CKSOTPInstrumentStatusField = {"ExchangeID": "string", "ExchangeInstID": "string", "InstrumentID": "string",
							   "InstrumentStatus": "string", "TradingSegmentSN": "int", "EnterTime": "string",
							   "EnterReason": "string"}
#交易所代码
#合约在交易所的代码
#合约代码
#合约交易状态
#交易阶段编号
#进入本状态时间
#进入本状态原因
structDict['CKSOTPInstrumentStatusField'] = CKSOTPInstrumentStatusField


#转账请求
CKSOTPReqTransferField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
						  "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
						  "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
						  "LastFragment": "string", "SessionID": "int", "CustomerName": "string",
						  "IdCardType": "string", "IdentifiedCardNo": "string", "CustType": "string",
						  "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
						  "Password": "string", "InstallID": "int", "FutureSerial": "int", "UserID": "string",
						  "VerifyCertNoFlag": "string", "CurrencyID": "string", "TradeAmount": "float",
						  "FutureFetchAmount": "float", "FeePayFlag": "string", "CustFee": "float",
						  "BrokerFee": "float", "Message": "string", "Digest": "string", "BankAccType": "string",
						  "DeviceID": "string", "BankSecuAccType": "string", "BrokerIDByBank": "string",
						  "BankSecuAcc": "string", "BankPwdFlag": "string", "SecuPwdFlag": "string", "OperNo": "string",
						  "RequestID": "int", "TID": "int", "TransferStatus": "string"}
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
#证券密码
#安装编号
#证券公司流水号
#用户标识
#验证客户证件号码标志
#币种代码
#转帐金额
#证券可取金额
#费用支付标志
#应收客户费用
#应收证券公司费用
#发送方给接收方的消息
#摘要
#银行帐号类型
#渠道标志
#证券单位帐号类型
#证券公司银行编码
#证券单位帐号
#银行密码标志
#证券资金密码核对标志
#交易柜员
#请求编号
#交易ID
#转账交易状态
structDict['CKSOTPReqTransferField'] = CKSOTPReqTransferField


#银行资金转证券响应
CKSOTPRspTransferField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
						  "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
						  "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
						  "LastFragment": "string", "SessionID": "int", "CustomerName": "string",
						  "IdCardType": "string", "IdentifiedCardNo": "string", "CustType": "string",
						  "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
						  "Password": "string", "InstallID": "int", "FutureSerial": "int", "UserID": "string",
						  "VerifyCertNoFlag": "string", "CurrencyID": "string", "TradeAmount": "float",
						  "FutureFetchAmount": "float", "FeePayFlag": "string", "CustFee": "float",
						  "BrokerFee": "float", "Message": "string", "Digest": "string", "BankAccType": "string",
						  "DeviceID": "string", "BankSecuAccType": "string", "BrokerIDByBank": "string",
						  "BankSecuAcc": "string", "BankPwdFlag": "string", "SecuPwdFlag": "string", "OperNo": "string",
						  "RequestID": "int", "TID": "int", "TransferStatus": "string", "ErrorID": "int",
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
#证券密码
#安装编号
#证券公司流水号
#用户标识
#验证客户证件号码标志
#币种代码
#转帐金额
#证券可取金额
#费用支付标志
#应收客户费用
#应收证券公司费用
#发送方给接收方的消息
#摘要
#银行帐号类型
#渠道标志
#证券单位帐号类型
#证券公司银行编码
#证券单位帐号
#银行密码标志
#证券资金密码核对标志
#交易柜员
#请求编号
#交易ID
#转账交易状态
#错误代码
#错误信息
structDict['CKSOTPRspTransferField'] = CKSOTPRspTransferField


#查询签约银行请求
CKSOTPQryContractBankField = {"BrokerID": "string", "BankID": "string", "BankBrchID": "string"}
#经纪公司代码
#银行代码
#银行分中心代码
structDict['CKSOTPQryContractBankField'] = CKSOTPQryContractBankField


#查询签约银行响应
CKSOTPContractBankField = {"BrokerID": "string", "BankID": "string", "BankBrchID": "string", "BankName": "string"}
#经纪公司代码
#银行代码
#银行分中心代码
#银行名称
structDict['CKSOTPContractBankField'] = CKSOTPContractBankField


#查询账户信息请求
CKSOTPReqQueryAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							  "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							  "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							  "LastFragment": "string", "SessionID": "int", "CustomerName": "string",
							  "IdCardType": "string", "IdentifiedCardNo": "string", "CustType": "string",
							  "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
							  "Password": "string", "FutureSerial": "int", "InstallID": "int", "UserID": "string",
							  "VerifyCertNoFlag": "string", "CurrencyID": "string", "Digest": "string",
							  "BankAccType": "string", "DeviceID": "string", "BankSecuAccType": "string",
							  "BrokerIDByBank": "string", "BankSecuAcc": "string", "BankPwdFlag": "string",
							  "SecuPwdFlag": "string", "OperNo": "string", "RequestID": "int", "TID": "int"}
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
#证券密码
#证券公司流水号
#安装编号
#用户标识
#验证客户证件号码标志
#币种代码
#摘要
#银行帐号类型
#渠道标志
#证券单位帐号类型
#证券公司银行编码
#证券单位帐号
#银行密码标志
#证券资金密码核对标志
#交易柜员
#请求编号
#交易ID
structDict['CKSOTPReqQueryAccountField'] = CKSOTPReqQueryAccountField


#查询账户信息响应
CKSOTPRspQueryAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string", "BrokerID": "string",
							  "BrokerBranchID": "string", "TradeDate": "string", "TradeTime": "string",
							  "BankSerial": "string", "TradingDay": "string", "PlateSerial": "int",
							  "LastFragment": "string", "SessionID": "int", "CustomerName": "string",
							  "IdCardType": "string", "IdentifiedCardNo": "string", "CustType": "string",
							  "BankAccount": "string", "BankPassWord": "string", "AccountID": "string",
							  "Password": "string", "FutureSerial": "int", "InstallID": "int", "UserID": "string",
							  "VerifyCertNoFlag": "string", "CurrencyID": "string", "Digest": "string",
							  "BankAccType": "string", "DeviceID": "string", "BankSecuAccType": "string",
							  "BrokerIDByBank": "string", "BankSecuAcc": "string", "BankPwdFlag": "string",
							  "SecuPwdFlag": "string", "OperNo": "string", "RequestID": "int", "TID": "int",
							  "BankUseAmount": "float", "BankFetchAmount": "float"}
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
#证券密码
#证券公司流水号
#安装编号
#用户标识
#验证客户证件号码标志
#币种代码
#摘要
#银行帐号类型
#渠道标志
#证券单位帐号类型
#证券公司银行编码
#证券单位帐号
#银行密码标志
#证券资金密码核对标志
#交易柜员
#请求编号
#交易ID
#银行可用金额
#银行可取金额
structDict['CKSOTPRspQueryAccountField'] = CKSOTPRspQueryAccountField


#请求查询转帐流水
CKSOTPQryTransferSerialField = {"BrokerID": "string", "AccountID": "string", "BankID": "string", "CurrencyID": "string"}
#经纪公司代码
#投资者帐号
#银行编码
#币种代码
structDict['CKSOTPQryTransferSerialField'] = CKSOTPQryTransferSerialField


#查询账户信息通知
CKSOTPNotifyQueryAccountField = {"TradeCode": "string", "BankID": "string", "BankBranchID": "string",
								 "BrokerID": "string", "BrokerBranchID": "string", "TradeDate": "string",
								 "TradeTime": "string", "BankSerial": "string", "TradingDay": "string",
								 "PlateSerial": "int", "LastFragment": "string", "SessionID": "int",
								 "CustomerName": "string", "IdCardType": "string", "IdentifiedCardNo": "string",
								 "CustType": "string", "BankAccount": "string", "BankPassWord": "string",
								 "AccountID": "string", "Password": "string", "FutureSerial": "int", "InstallID": "int",
								 "UserID": "string", "VerifyCertNoFlag": "string", "CurrencyID": "string",
								 "Digest": "string", "BankAccType": "string", "DeviceID": "string",
								 "BankSecuAccType": "string", "BrokerIDByBank": "string", "BankSecuAcc": "string",
								 "BankPwdFlag": "string", "SecuPwdFlag": "string", "OperNo": "string",
								 "RequestID": "int", "TID": "int", "BankUseAmount": "float", "BankFetchAmount": "float",
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
#客户类型
#银行帐号
#银行密码
#投资者帐号
#证券密码
#证券公司流水号
#安装编号
#用户标识
#验证客户证件号码标志
#币种代码
#摘要
#银行帐号类型
#渠道标志
#证券单位帐号类型
#证券公司银行编码
#证券单位帐号
#银行密码标志
#证券资金密码核对标志
#交易柜员
#请求编号
#交易ID
#银行可用金额
#银行可取金额
#错误代码
#错误信息
structDict['CKSOTPNotifyQueryAccountField'] = CKSOTPNotifyQueryAccountField


#银期转账交易流水表
CKSOTPTransferSerialField = {"PlateSerial": "int", "TradeDate": "string", "TradingDay": "string", "TradeTime": "string",
							 "TradeCode": "string", "SessionID": "int", "BankID": "string", "BankBranchID": "string",
							 "BankAccType": "string", "BankAccount": "string", "BankSerial": "string",
							 "BrokerID": "string", "BrokerBranchID": "string", "FutureAccType": "string",
							 "AccountID": "string", "InvestorID": "string", "FutureSerial": "int",
							 "IdCardType": "string", "IdentifiedCardNo": "string", "CurrencyID": "string",
							 "TradeAmount": "float", "CustFee": "float", "BrokerFee": "float",
							 "AvailabilityFlag": "string", "OperatorCode": "string", "BankNewAccount": "string",
							 "ErrorID": "int", "ErrorMsg": "string"}
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
#证券公司编码
#期商分支机构代码
#证券公司帐号类型
#投资者帐号
#投资者代码
#证券公司流水号
#证件类型
#证件号码
#币种代码
#交易金额
#应收客户费用
#应收证券公司费用
#有效标志
#操作员
#新银行帐号
#错误代码
#错误信息
structDict['CKSOTPTransferSerialField'] = CKSOTPTransferSerialField


#指定的合约
CKSOTPSpecificInstrumentField = {"InstrumentID": "string", "ExchangeID": "string"}
#合约代码
#交易所代码
structDict['CKSOTPSpecificInstrumentField'] = CKSOTPSpecificInstrumentField


#查询客户交易级别
CKSOTPQryInvestorTradeLevelField = {"BrokerID": "string", "ExchangeID": "string", "ProductID": "string"}
#经纪公司代码
#交易所代码
#产品代码
structDict['CKSOTPQryInvestorTradeLevelField'] = CKSOTPQryInvestorTradeLevelField


#客户交易级别
CKSOTPInvestorTradeLevelField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
								 "ProductID": "string", "TradeLevel": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#产品代码
#交易级别
structDict['CKSOTPInvestorTradeLevelField'] = CKSOTPInvestorTradeLevelField


#查询个股限购额度
CKSOTPQryPurchaseLimitAmtField = {"BrokerID": "string", "ExchangeID": "string"}
#经纪公司代码
#交易所代码
structDict['CKSOTPQryPurchaseLimitAmtField'] = CKSOTPQryPurchaseLimitAmtField


#个股限购额度
CKSOTPPurchaseLimitAmtField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
							   "PurLimitAmt": "float"}
#经纪公司代码
#投资者代码
#交易所代码
#限购额度
structDict['CKSOTPPurchaseLimitAmtField'] = CKSOTPPurchaseLimitAmtField


#查询个股限仓额度
CKSOTPQryPositionLimitVolField = {"BrokerID": "string", "ExchangeID": "string", "ProductID": "string",
								  "ProtectFlag": "string", "OptionsType": "string", "ControlRange": "string"}
#经纪公司代码
#交易所代码
#产品代码
#保护性标志
#期权C/P标志
#控制范围
structDict['CKSOTPQryPositionLimitVolField'] = CKSOTPQryPositionLimitVolField


#查询个股限仓额度
CKSOTPPositionLimitVolField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
							   "ProductID": "string", "ProtectFlag": "string", "OptionsType": "string",
							   "ControlRange": "string", "PosiLimitVol": "int"}
#经纪公司代码
#投资者代码
#交易所代码
#产品代码
#保护性标志
#期权C/P标志
#控制范围
#限仓额度
structDict['CKSOTPPositionLimitVolField'] = CKSOTPPositionLimitVolField


#查询投资者结算结果
CKSOTPQrySettlementInfoField = {"BrokerID": "string", "InvestorID": "string", "TradingDay": "string"}
#经纪公司代码
#投资者代码
#交易日
structDict['CKSOTPQrySettlementInfoField'] = CKSOTPQrySettlementInfoField


#查询结算信息确认域
CKSOTPQrySettlementInfoConfirmField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CKSOTPQrySettlementInfoConfirmField'] = CKSOTPQrySettlementInfoConfirmField


#投资者结算结果确认信息
CKSOTPSettlementInfoConfirmField = {"BrokerID": "string", "InvestorID": "string", "ConfirmDate": "string",
									"ConfirmTime": "string"}
#经纪公司代码
#投资者代码
#确认日期
#确认时间
structDict['CKSOTPSettlementInfoConfirmField'] = CKSOTPSettlementInfoConfirmField


#投资者结算结果
CKSOTPSettlementInfoField = {"TradingDay": "string", "SettlementID": "int", "BrokerID": "string",
							 "InvestorID": "string", "SequenceNo": "int", "Content": "string"}
#交易日
#结算编号
#经纪公司代码
#投资者代码
#序号
#消息正文
structDict['CKSOTPSettlementInfoField'] = CKSOTPSettlementInfoField


#查询历史报单
CKSOTPQryHistoryOrderField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string",
							  "OrderLocalID": "string", "ProductID": "string", "OrderDataStart": "string",
							  "OrderDataEnd": "string"}
#经纪公司代码
#投资者代码
#合约代码
#本地报单编号
#品种代码
#开始日期
#结束日期
structDict['CKSOTPQryHistoryOrderField'] = CKSOTPQryHistoryOrderField


#查询历史成交
CKSOTPQryHistoryTradeField = {"BrokerID": "string", "InvestorID": "string", "ProductID": "string",
							  "TradeDataStart": "string", "TradeDataEnd": "string"}
#经纪公司代码
#投资者代码
#品种代码
#开始日期
#结束日期
structDict['CKSOTPQryHistoryTradeField'] = CKSOTPQryHistoryTradeField


#查询历史行权指派明细
CKSOTPQryHistoryAssignmentField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
								   "ProductID": "string", "InstrumentID": "string", "HedgeFlag": "string",
								   "OptionsType": "string", "DeliveryMonth": "string", "PosiDirection": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#产品代码
#合约代码
#投保标记
#期权类型
#交割月
#持仓方向
structDict['CKSOTPQryHistoryAssignmentField'] = CKSOTPQryHistoryAssignmentField


#查询行权交割明细
CKSOTPQryDelivDetailField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
							 "ProductID": "string", "DeliveryMonth": "string", "DelivMode": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#产品代码
#交割月
#个股交收查询类型
structDict['CKSOTPQryDelivDetailField'] = CKSOTPQryDelivDetailField


#自动行权执行操作
CKSOTPAutoExecOrderActionField = {"BrokerID": "string", "InvestorID": "string", "RangeVol": "int"}
#经纪公司代码
#投资者代码
#自动行权阈值(0-不自动行权,非0-代表超过阀值会自动行权(20代表20%))
structDict['CKSOTPAutoExecOrderActionField'] = CKSOTPAutoExecOrderActionField


#历史行权指派明细
CKSOTPHistoryAssignmentField = {"BrokerID": "string", "InvestorID": "string", "TradingDay": "string",
								"ProductID": "string", "InstrumentID": "string", "ClientID": "string",
								"StockInstr": "string", "HedgeFlag": "string", "OptionsType": "string",
								"PosiDirection": "string", "StrikePrice": "float", "ExecVol": "int", "IOVol": "int",
								"IOAmt": "float", "DelivDate": "string"}
#经纪公司代码
#投资者代码
#交易日期
#产品代码
#合约代码
#客户代码
#标的证券代码
#投保标记
#期权类型
#持仓方向
#执行价
#行权指派数量
#标的证券应收付数量
#应收付金额
#行权交收日
structDict['CKSOTPHistoryAssignmentField'] = CKSOTPHistoryAssignmentField


#行权交割明细
CKSOTPDelivDetailField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string", "StockInstr": "string",
						  "IOVol": "int", "IOVolInFact": "int", "SettlementPrice": "float", "SettlementAmt": "float",
						  "DelivDate": "string", "FunctionName": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#标的证券代码
#应收/应付/扣券证券数量
#实收付数量
#结算价
#扣券面值/结算金额
#行权交收日
#业务类型名称
structDict['CKSOTPDelivDetailField'] = CKSOTPDelivDetailField


#历史报单
CKSOTPHistoryOrderField = {"BrokerID": "string", "InvestorID": "string", "CustomerName": "string",
						   "InstrumentID": "string", "OrderLocalID": "string", "InsertTime": "string",
						   "BusinessUnit": "string", "TradePrice": "float", "TradeAmount": "float",
						   "VolumeTraded": "int", "FrozenAmount": "float", "CurrencyID": "string", "SequenceNo": "int",
						   "Direction": "string", "ExchangeID": "string", "UserProductInfo": "string",
						   "RequestID": "int", "OrderRef": "string", "FrontID": "int", "SessionID": "int",
						   "OrderPrice": "float", "OrderSource": "string", "InsertDate": "string",
						   "OrderTime": "string", "VolumeTotalOriginal": "int", "OrderStatus": "string",
						   "ProductID": "string", "ProductName": "string", "ProductClass": "string",
						   "OffsetFlag": "string", "FunctionName": "string"}
#经纪公司代码
#投资者代码
#客户姓名
#合约代码
#本地报单编号
#申报时间
#业务单元
#成交价格
#成交金额
#成交数量
#冻结解冻金额
#币种代码
#序号
#买卖方向
#交易所代码
#用户端产品信息
#请求编号
#报单引用
#前置编号
#会话编号
#委托价格
#委托来源
#委托日期
#委托时间
#委托数量
#委托状态
#产品代码
#产品名称
#产品类型
#投保买卖开平标志
#业务类型名称
structDict['CKSOTPHistoryOrderField'] = CKSOTPHistoryOrderField


#历史成交
CKSOTPHistoryTradeField = {"BrokerID": "string", "InvestorID": "string", "CustomerName": "string",
						   "OrderLocalID": "string", "CurrencyID": "string", "ExchangeID": "string",
						   "ProductID": "string", "ProductName": "string", "VolumeTraded": "int",
						   "TradeAmount": "float", "TradeDate": "string", "TradeTime": "string", "OffsetFlag": "string",
						   "BusinessUnit": "string", "Commission": "float", "Memo": "string",
						   "TraderOfferTime": "string", "TradePrice;": "float", "ClientID": "string",
						   "OptionsType": "string", "HedgeFlag": "string", "RoyaltyVolume": "int",
						   "ObligationVolume": "int", "RoyaltyAmount": "float", "ObligationAmount": "float",
						   "TradeID": "string", "FunctionName": "string"}
#经纪公司代码
#投资者代码
#客户姓名
#本地报单编号
#币种代码
#交易所代码
#产品代码
#产品名称
#成交数量
#成交金额
#成交日期
#成交时间
#投保买卖开平标志
#业务单元
#手续费
#备注
#报盘时间
#成交价格
#期权交易编码
#期权类型
#备兑标志
#权利仓数量
#义务仓数量
#权利仓金额
#义务仓金额
#成交编号
#业务类型名称
structDict['CKSOTPHistoryTradeField'] = CKSOTPHistoryTradeField


#个股组合拆分委托
CKSOTPInputCombActionField = {"BrokerID": "string", "InvestorID": "string", "StrategyID": "string",
							  "InstrumentID1": "string", "InstrumentID2": "string", "InstrumentID3": "string",
							  "InstrumentID4": "string", "CombActionRef": "string", "UserID": "string",
							  "Direction1": "string", "Direction2": "string", "Direction3": "string",
							  "Direction4": "string", " CombActionFlag": "string", "Volume": "int",
							  "CombDirection": "string", "HedgeFlag": "string", "ExchangeID": "string",
							  "ComTradeID": "string"}
#经纪公司代码
#投资者代码
#策略代码
#合约代码1
#合约代码2
#合约代码3
#合约代码4
#组合引用
#用户代码
#买卖方向1
#买卖方向2
#买卖方向3
#买卖方向4
#强拆标记
#数量
#组合拆分标记
#投机套保标志
#交易所代码
#交易所组合编号
structDict['CKSOTPInputCombActionField'] = CKSOTPInputCombActionField


#个股组合拆分
CKSOTPCombActionField = {"BrokerID": "string", "InvestorID": "string", "InstrumentID": "string", "StrategyID": "string",
						 "InstrumentID1": "string", "InstrumentID2": "string", "InstrumentID3": "string",
						 "InstrumentID4": "string", "CombActionRef": "string", "UserID": "string",
						 "Direction1": "string", "Direction2": "string", "Direction3": "string", "Direction4": "string",
						 " CombActionFlag": "string", "Volume": "int", "CombDirection": "string", "HedgeFlag": "string",
						 "ActionLocalID": "string", "ExchangeID": "string", "ParticipantID": "string",
						 "ClientID": "string", "ExchangeInstID": "string", "TraderID": "string", "InstallID": "int",
						 "ActionStatus": "string", "NotifySequence": "int", "TradingDay": "string",
						 "SettlementID": "int", "SequenceNo": "int", "FrontID": "int", "SessionID": "int",
						 "UserProductInfo": "string", "StatusMsg": "string", "ComTradeID": "string",
						 "OrderSource": "string"}
#经纪公司代码
#投资者代码
#完整合约代码
#策略代码
#合约代码1
#合约代码2
#合约代码3
#合约代码4
#组合引用
#用户代码
#买卖方向1
#买卖方向2
#买卖方向3
#买卖方向4
#强拆标记
#数量
#组合拆分标记
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
#交易所组合编号
#报单来源
structDict['CKSOTPCombActionField'] = CKSOTPCombActionField


#查询个股组合持仓明细
CKSOTPQryInvestorPositionCombineDetailField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
											   "ProductID": "string", "ComTradeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#产品代码
#交易所组合编号
structDict['CKSOTPQryInvestorPositionCombineDetailField'] = CKSOTPQryInvestorPositionCombineDetailField


#个股组合持仓明细
CKSOTPInvestorPositionCombineDetailField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
											"ClientID": "string", "ComTradeID": "string", "StrategyID": "string",
											"InstrumentID1": "string", "InstrumentID2": "string",
											"InstrumentID3": "string", "InstrumentID4": "string", "Margin": "float",
											"CombActionVolume": "int", "HedgeFlag": "string", "TotalAmt": "int",
											"Direction1": "string", "Direction2": "string", "Direction3": "string",
											"Direction4": "string", "CombDirection": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#交易编码
#组合编号
#策略代码
#合约代码1
#合约代码2
#合约代码3
#合约代码4
#保证金
#距离自动拆分日天数
#投保标记
#持仓量
#买卖方向1
#买卖方向2
#买卖方向3
#买卖方向4
#组合买卖方向
structDict['CKSOTPInvestorPositionCombineDetailField'] = CKSOTPInvestorPositionCombineDetailField


#个股可组合可拆分手数查询请求
CKSOTPQryCombActionVolumeField = {"BrokerID": "string", "InvestorID": "string", "ExchangeID": "string",
								  "StrategyID": "string", "InstrumentID1": "string", "InstrumentID2": "string",
								  "InstrumentID3": "string", "InstrumentID4": "string", "HedgeFlag": "string",
								  "Direction1": "string", "Direction2": "string", "Direction3": "string",
								  "Direction4": "string", " CombActionFlag": "string", "CombDirection": "string",
								  "ComTradeID": "string"}
#经纪公司代码
#投资者代码
#交易所代码
#策略代码
#合约代码1
#合约代码2
#合约代码3
#合约代码4
#投保标记
#买卖方向1
#买卖方向2
#买卖方向3
#买卖方向4
#强拆标记
#组合拆分标记
#组合编号
structDict['CKSOTPQryCombActionVolumeField'] = CKSOTPQryCombActionVolumeField


#个股可组合可拆分手数
CKSOTPCombActionVolumeField = {"BrokerID": "string", "InvestorID": "string", "MaxCombVolume": "int",
							   "MaxActionVolume": "int"}
#经纪公司代码
#投资者代码
#最大可组合数量
#最大可拆分数量
structDict['CKSOTPCombActionVolumeField'] = CKSOTPCombActionVolumeField


#客户每日出金额度申请请求
CKSOTPInputFundOutCreditApplyField = {"BrokerID": "string", "InvestorID": "string", "FundOutCredit": "float",
									  "CreditApplyFlag": "string", "CreditSerial": "int"}
#经纪公司代码
#投资者代码
#当日出金额度
#当日出金额度操作类型
#流水号
structDict['CKSOTPInputFundOutCreditApplyField'] = CKSOTPInputFundOutCreditApplyField


#客户每日出金额度查询请求
CKSOTPQryFundOutCreditField = {"BrokerID": "string", "InvestorID": "string"}
#经纪公司代码
#投资者代码
structDict['CKSOTPQryFundOutCreditField'] = CKSOTPQryFundOutCreditField


#客户每日出金额度查询
CKSOTPRspQryFundOutCreditField = {"BrokerID": "string", "InvestorID": "string", "FundOutCredit": "float",
								  "FundOutedCredit": "float", "UpdateDate": "string", "SetDate": "string",
								  "SetTime": "string"}
#经纪公司代码
#投资者代码
#当日出金额度
#当日已出金额度
#最后更新日期
#设置日期
#设置时间
structDict['CKSOTPRspQryFundOutCreditField'] = CKSOTPRspQryFundOutCreditField


#客户每日出金额度申请查询请求
CKSOTPQryFundOutCreditApplyField = {"BrokerID": "string", "InvestorID": "string", "QryCreditStart": "string",
									"QryCreditEnd": "string", "DealStatus": "string"}
#经纪公司代码
#投资者代码
#查询开始日期
#查询结束日期
#当日出金额度处理状态
structDict['CKSOTPQryFundOutCreditApplyField'] = CKSOTPQryFundOutCreditApplyField


#客户每日出金额度申请查询
CKSOTPRspQryFundOutCreditApplyField = {"BrokerID": "string", "InvestorID": "string", "CreditSerial": "int",
									   "FundOutCredit": "float", "DealStatus": "string", "ApplyDate": "string",
									   "ApplyTime": "string", "ConfirmDate": "string", "ConfirmTime": "string"}
#经纪公司代码
#投资者代码
#流水号
#申请出金额度
#当日出金额度处理状态
#申请日期
#申请时间
#审核日期
#审核时间
structDict['CKSOTPRspQryFundOutCreditApplyField'] = CKSOTPRspQryFundOutCreditApplyField

structDict['CKSOTPRspQryFundOutCreditApplyField'] = CKSOTPRspQryFundOutCreditApplyField



