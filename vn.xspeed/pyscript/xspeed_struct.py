# encoding: UTF-8

structDict = {}

















#心跳包
DFITCTimeOutField = {"lRequestID": "long"}
structDict['DFITCTimeOutField'] = DFITCTimeOutField



#请求报单数据类型(基本报单)
DFITCInsertOrderField = {"accountID": "string", "localOrderID": "long", "instrumentID": "string",
						 "insertPrice": "float", "orderAmount": "long", "buySellType": "short", "openCloseType": "int",
						 "speculator": "int", "insertType": "int", "orderType": "int", "orderProperty": "char",
						 "instrumentType": "int", "minMatchAmount": "long", "reservedType2": "int",
						 "lRequestID": "long", "customCategory": "string", "profitLossPrice": "float"}
structDict['DFITCInsertOrderField'] = DFITCInsertOrderField



#撤单数据类型
DFITCCancelOrderField = {"accountID": "string", "spdOrderID": "long", "localOrderID": "long", "instrumentID": "string",
						 "lRequestID": "long"}
structDict['DFITCCancelOrderField'] = DFITCCancelOrderField



#委托响应类型
DFITCOrderRspDataRtnField = {"localOrderID": "long", "spdOrderID": "long", "orderStatus": "short", "lRequestID": "long",
							 "fee": "float", "margin": "float", "customCategory": "string", "accountID": "string",
							 "instrumentID": "string", "sessionID": "long", "exchangeID": "string",
							 "buySellType": "short", "openCloseType": "int", "instrumentType": "int",
							 "speculator": "int", "insertPrice": "float", "profitLossPrice": "float",
							 "minMatchAmount": "long", "orderAmount": "long", "insertType": "int", "orderType": "int",
							 "orderProperty": "char", "clientID": "string"}
structDict['DFITCOrderRspDataRtnField'] = DFITCOrderRspDataRtnField




#查询资金数据类型
DFITCCapitalField = {"lRequestID": "long", "accountID": "string"}
structDict['DFITCCapitalField'] = DFITCCapitalField



#查询持仓数据类型
DFITCPositionField = {"lRequestID": "long", "accountID": "string", "instrumentID": "string", "instrumentType": "int"}
structDict['DFITCPositionField'] = DFITCPositionField



#交易所合约
DFITCExchangeInstrumentField = {"lRequestID": "long", "accountID": "string", "exchangeID": "string",
								"instrumentType": "int"}
structDict['DFITCExchangeInstrumentField'] = DFITCExchangeInstrumentField



#用户登录数据类型
DFITCUserLoginField = {"lRequestID": "long", "accountID": "string", "passwd": "string", "companyID": "short"}
structDict['DFITCUserLoginField'] = DFITCUserLoginField



#用户退出类型
DFITCUserLogoutField = {"lRequestID": "long", "accountID": "string", "sessionID": "long"}
structDict['DFITCUserLogoutField'] = DFITCUserLogoutField



#委托回报
DFITCOrderRtnField = {"localOrderID": "long", "spdOrderID": "long", "OrderSysID": "string", "orderStatus": "short",
					  "sessionID": "long", "SuspendTime": "string", "instrumentID": "string", "exchangeID": "string",
					  "buySellType": "short", "openCloseType": "int", "instrumentType": "int", "speculator": "int",
					  "insertPrice": "float", "profitLossPrice": "float", "accountID": "string", "cancelAmount": "long",
					  "orderAmount": "long", "insertType": "int", "orderType": "int", "extSpdOrderID": "long",
					  "reservedType2": "int", "customCategory": "string", "orderProperty": "char",
					  "minMatchAmount": "long", "clientID": "string", "statusMsg": "string"}
structDict['DFITCOrderRtnField'] = DFITCOrderRtnField



#成交回报
DFITCMatchRtnField = {"localOrderID": "long", "OrderSysID": "string", "matchID": "string", "instrumentID": "string",
					  "buySellType": "short", "openCloseType": "int", "matchedPrice": "float", "orderAmount": "long",
					  "matchedAmount": "long", "matchedTime": "string", "insertPrice": "float", "spdOrderID": "long",
					  "matchType": "long", "speculator": "int", "exchangeID": "string", "fee": "float",
					  "sessionID": "long", "instrumentType": "int", "accountID": "string", "orderStatus": "short",
					  "margin": "float", "frozenCapita": "float", "adjustmentInfo": "string",
					  "customCategory": "string", "turnover": "float", "orderType": "int", "insertType": "int",
					  "clientID": "string"}
structDict['DFITCMatchRtnField'] = DFITCMatchRtnField



#撤单回报
DFITCOrderCanceledRtnField = {"localOrderID": "long", "OrderSysID": "string", "instrumentID": "string",
							  "insertPrice": "float", "buySellType": "short", "openCloseType": "int",
							  "cancelAmount": "long", "spdOrderID": "long", "speculator": "int", "exchangeID": "string",
							  "canceledTime": "string", "sessionID": "long", "orderStatus": "short",
							  "instrumentType": "int", "accountID": "string", "orderAmount": "long", "margin": "float",
							  "fee": "float", "customCategory": "string", "profitLossPrice": "float",
							  "minMatchAmount": "long", "insertType": "int", "clientID": "string",
							  "statusMsg": "string", "orderProperty": "char"}
structDict['DFITCOrderCanceledRtnField'] = DFITCOrderCanceledRtnField



#错误信息
DFITCErrorRtnField = {"requestID": "long", "sessionID": "long", "accountID": "string", "nErrorID": "int",
					  "spdOrderID": "long", "localOrderID": "long", "errorMsg": "string", "instrumentID": "string"}
structDict['DFITCErrorRtnField'] = DFITCErrorRtnField



#返回资金信息
DFITCCapitalInfoRtnField = {"requestID": "long", "accountID": "string", "preEquity": "float", "todayEquity": "float",
							"closeProfitLoss": "float", "positionProfitLoss": "float", "frozenMargin": "float",
							"margin": "float", "fee": "float", "available": "float", "withdraw": "float",
							"riskDegree": "float", "todayPremiumIncome": "float", "todayPremiumPay": "float",
							"yesterdayPremium": "float", "optMarketValue": "float", "floatProfitLoss": "float",
							"totFundOut": "float", "totFundIn": "float"}
structDict['DFITCCapitalInfoRtnField'] = DFITCCapitalInfoRtnField



#返回持仓信息
DFITCPositionInfoRtnField = {"lRequestID": "long", "accountID": "string", "exchangeID": "string",
							 "instrumentID": "string", "buySellType": "short", "openAvgPrice": "float",
							 "positionAvgPrice": "float", "positionAmount": "long", "totalAvaiAmount": "long",
							 "todayAvaiAmount": "long", "lastAvaiAmount": "long", "todayAmount": "long",
							 "lastAmount": "long", "tradingAmount": "long", "datePositionProfitLoss": "float",
							 "dateCloseProfitLoss": "float", "dPremium": "float", "floatProfitLoss": "float",
							 "dMargin": "float", "speculator": "int", "clientID": "string",
							 "preSettlementPrice": "float", "instrumentType": "int", "yesterdayTradingAmount": "long"}
structDict['DFITCPositionInfoRtnField'] = DFITCPositionInfoRtnField



#用户登录返回信息
DFITCUserLoginInfoRtnField = {"lRequestID": "long", "accountID": "string", "loginResult": "int",
							  "initLocalOrderID": "long", "sessionID": "long", "nErrorID": "int", "errorMsg": "string",
							  "DCEtime": "string", "SHFETime": "string", "CFFEXTime": "string", "CZCETime": "string",
							  "INETime": "string"}
structDict['DFITCUserLoginInfoRtnField'] = DFITCUserLoginInfoRtnField



#用户退出返回信息
DFITCUserLogoutInfoRtnField = {"lRequestID": "long", "accountID": "string", "logoutResult": "int", "nErrorID": "int",
							   "errorMsg": "string"}
structDict['DFITCUserLogoutInfoRtnField'] = DFITCUserLogoutInfoRtnField



#套利合约查询
DFITCAbiInstrumentField = {"lRequestID": "long", "accountID": "string", "exchangeID": "string"}
structDict['DFITCAbiInstrumentField'] = DFITCAbiInstrumentField



#套利合约返回信息
DFITCAbiInstrumentRtnField = {"lRequestID": "long", "exchangeID": "string", "InstrumentID": "string",
							  "instrumentName": "string"}
structDict['DFITCAbiInstrumentRtnField'] = DFITCAbiInstrumentRtnField



#指定的合约
DFITCSpecificInstrumentField = {"lRequestID": "long", "accountID": "string", "InstrumentID": "string",
								"exchangeID": "string", "instrumentType": "int"}
structDict['DFITCSpecificInstrumentField'] = DFITCSpecificInstrumentField




#指定的合约信息
DFITCSpecificInstrumentFieldEX = {"lRequestID": "long", "accountID": "string", "FunctionID": "string",
								  "InstrumentID": "string", "exchangeID": "string", "instrumentType": "int"}
structDict['DFITCSpecificInstrumentFieldEX'] = DFITCSpecificInstrumentFieldEX



#行情订阅返回信息
DFITCActiveContractField = {"lRequestID": "long", "activeContract": "string"}
structDict['DFITCActiveContractField'] = DFITCActiveContractField



#交易所合约返回信息
DFITCExchangeInstrumentRtnField = {"lRequestID": "long", "exchangeID": "string", "instrumentID": "string",
								   "VarietyName": "string", "instrumentType": "int", "orderTopLimit": "long",
								   "mktOrderTopLimit": "long", "contractMultiplier": "float",
								   "minPriceFluctuation": "float", "instrumentMaturity": "string",
								   "upperLimitPrice": "float", "lowerLimitPrice": "float", "preClosePrice": "float",
								   "preSettlementPrice": "float", "settlementPrice": "float", "preOpenInterest": "long",
								   "instrumentPrefix": "string", "instrumentExpiration": "string",
								   "underlying": "string", "optionType": "int", "strikePrice": "float",
								   "exchangeRiskDegree": "float", "minMargin": "float", "tradeSize": "long"}
structDict['DFITCExchangeInstrumentRtnField'] = DFITCExchangeInstrumentRtnField



#委托查询数据结构
DFITCOrderField = {"lRequestID": "long", "accountID": "string", "instrumentType": "int", "customCategory": "string",
				   "orderStatus": "short", "orderType": "int", "spdOrderID": "long", "localOrderID": "long",
				   "instrumentID": "string"}
structDict['DFITCOrderField'] = DFITCOrderField



#成交查询数据结构
DFITCMatchField = {"lRequestID": "long", "accountID": "string", "instrumentType": "int", "customCategory": "string",
				   "orderType": "int", "spdOrderID": "long", "instrumentID": "string"}
structDict['DFITCMatchField'] = DFITCMatchField



#委托查询响应数据结构
DFITCOrderCommRtnField = {"lRequestID": "long", "spdOrderID": "long", "orderStatus": "short", "instrumentID": "string",
						  "buySellType": "short", "openClose": "int", "insertPrice": "float", "orderAmount": "long",
						  "matchedPrice": "float", "matchedAmount": "long", "cancelAmount": "long", "insertType": "int",
						  "speculator": "int", "commTime": "string", "submitTime": "string", "clientID": "string",
						  "exchangeID": "string", "operStation": "string", "accountID": "string",
						  "instrumentType": "int", "sessionId": "long", "reservedType2": "int", "OrderSysID": "string",
						  "customCategory": "string", "margin": "float", "fee": "float", "localOrderID": "long",
						  "profitLossPrice": "float", "orderType": "int", "orderProperty": "char"}
structDict['DFITCOrderCommRtnField'] = DFITCOrderCommRtnField



#成交查询数据响应
DFITCMatchedRtnField = {"lRequestID": "long", "spdOrderID": "long", "accountID": "string", "exchangeID": "string",
						"instrumentID": "string", "buySellType": "short", "openClose": "int", "matchedPrice": "float",
						"matchedAmount": "long", "matchedMort": "float", "speculator": "int", "matchedTime": "string",
						"matchedID": "string", "localOrderID": "long", "clientID": "string", "matchType": "long",
						"instrumentType": "int", "sessionId": "long", "reservedType2": "int",
						"customCategory": "string", "fee": "float", "orderType": "int", "OrderSysID": "string"}
structDict['DFITCMatchedRtnField'] = DFITCMatchedRtnField



#返回合约信息数据结构
DFITCInstrumentRtnField = {"lRequestID": "long", "instrumentID": "string", "longMarginRatio": "float",
						   "shortMarginRatio": "float", "longMarginRatioByVolume": "float",
						   "shortMarginRatioByVolume": "float", "openFeeVolRatio": "float", "closeFeeVolRatio": "float",
						   "closeTodayFeeVolRatio": "float", "openFeeAmtRatio": "float", "closeFeeAmtRatio": "float",
						   "closeTodayFeeAmtRatio": "float", "orderTopLimit": "long", "contractMultiplier": "float",
						   "minimumPriceChange": "float", "instrumentType": "int", "instrumentMaturity": "string",
						   "computeMode": "int", "atMoneyNorm": "float", "upperLimitPrice": "float",
						   "lowerLimitPrice": "float", "preClosePrice": "float", "preSettlementPrice": "float",
						   "settlementPrice": "float", "preOpenInterest": "long", "optExecRatio": "float",
						   "optExecRatioPerVol": "float"}
structDict['DFITCInstrumentRtnField'] = DFITCInstrumentRtnField



#深度行情
DFITCDepthMarketDataField = {"tradingDay": "string", "instrumentID": "string", "exchangeID": "string",
							 "exchangeInstID": "string", "lastPrice": "float", "preSettlementPrice": "float",
							 "preClosePrice": "float", "preOpenInterest": "long", "openPrice": "float",
							 "highestPrice": "float", "lowestPrice": "float", "Volume": "long", "turnover": "float",
							 "openInterest": "long", "closePrice": "float", "settlementPrice": "float",
							 "upperLimitPrice": "float", "lowerLimitPrice": "float", "preDelta": "float",
							 "currDelta": "float", "UpdateTime": "string", "UpdateMillisec": "int",
							 "BidPrice1": "float", "BidVolume1": "int", "AskPrice1": "float", "AskVolume1": "int",
							 "BidPrice2": "float", "BidVolume2": "int", "AskPrice2": "float", "AskVolume2": "int",
							 "BidPrice3": "float", "BidVolume3": "int", "AskPrice3": "float", "AskVolume3": "int",
							 "BidPrice4": "float", "BidVolume4": "int", "AskPrice4": "float", "AskVolume4": "int",
							 "BidPrice5": "float", "BidVolume5": "int", "AskPrice5": "float", "AskVolume5": "int",
							 "AveragePrice": "float", "XSpeedTime": "string"}
structDict['DFITCDepthMarketDataField'] = DFITCDepthMarketDataField


#********************************期权扩展行情************************************


DFITCMarketDataFieldEx = {"FunctionID": "string", "tradingDay": "string", "UpdateTime": "string",
						  "UpdateMillisec": "int", "instrumentID": "string", "ExtMarketData": "string"}
structDict['DFITCMarketDataFieldEx'] = DFITCMarketDataFieldEx

#********************************************************************************



DFITCCustomMarketDataField = {"instrumentID": "string", "exchangeID": "string", "bidVolume1": "int",
							  "bidPrice1": "float", "askVolume1": "int", "askPrice1": "float", "lastPrice": "float"}
structDict['DFITCCustomMarketDataField'] = DFITCCustomMarketDataField


#查询持仓明细
DFITCPositionDetailField = {"lRequestID": "long", "accountID": "string", "instrumentID": "string",
							"instrumentType": "int"}
structDict['DFITCPositionDetailField'] = DFITCPositionDetailField



#查询持仓明细响应
DFITCPositionDetailRtnField = {"lRequestID": "long", "accountID": "string", "exchangeID": "string",
							   "instrumentID": "string", "buySellType": "short", "openPrice": "float", "volume": "long",
							   "matchID": "string", "matchedDate": "string", "datePositionProfitLoss": "float",
							   "dateCloseProfitLoss": "float", "floatProfitLoss": "float", "dMargin": "float",
							   "speculator": "int", "clientID": "string", "preSettlementPrice": "float",
							   "instrumentType": "int", "spdOrderID": "long", "customCategory": "string",
							   "closeOrderVol": "long", "closeMatchVol": "long", "positionDateType": "int"}
structDict['DFITCPositionDetailRtnField'] = DFITCPositionDetailRtnField



#用户事件通知信息
DFITCTradingNoticeInfoField = {"accountID": "string", "SendTime": "string", "FieldContent": "string",
							   "noticeType": "short"}
structDict['DFITCTradingNoticeInfoField'] = DFITCTradingNoticeInfoField



#合约交易状态通知信息
DFITCInstrumentStatusField = {"ExchangeID": "string", "InstrumentID": "string", "InstrumentStatus": "int",
							  "TradingSegmentSN": "int", "EnterTime": "string", "EnterReason": "short"}
structDict['DFITCInstrumentStatusField'] = DFITCInstrumentStatusField



#用户密码修改
DFITCResetPwdField = {"lRequestID": "long", "accountID": "string", "oldpasswd": "string", "newpasswd": "string"}
structDict['DFITCResetPwdField'] = DFITCResetPwdField



#用户密码修改返回信息
DFITCResetPwdRspField = {"lRequestID": "long", "accountID": "string", "execState": "int"}
structDict['DFITCResetPwdRspField'] = DFITCResetPwdRspField



#账单确认
DFITCBillConfirmField = {"lRequestID": "long", "accountID": "string", "date": "string", "confirmFlag": "int"}
structDict['DFITCBillConfirmField'] = DFITCBillConfirmField



#账单确认响应
DFITCBillConfirmRspField = {"lRequestID": "long", "accountID": "string", "execState": "int"}
structDict['DFITCBillConfirmRspField'] = DFITCBillConfirmRspField



#交易编码查询
DFITCQryTradeCodeField = {"lRequestID": "long", "accountID": "string"}
structDict['DFITCQryTradeCodeField'] = DFITCQryTradeCodeField



#交易编码查询响应
DFITCQryTradeCodeRtnField = {"lRequestID": "long", "accountID": "string", "exchangeCode": "string",
							 "clientID": "string", "clientStatus": "int", "clientIDType": "int"}
structDict['DFITCQryTradeCodeRtnField'] = DFITCQryTradeCodeRtnField



#浮盈浮亏是否计算到权益中
DFITCEquityComputModeRtnField = {"capConMode": "long", "priceNote": "int"}
structDict['DFITCEquityComputModeRtnField'] = DFITCEquityComputModeRtnField



#查询账单
DFITCQryBillField = {"lRequestID": "long", "accountID": "string", "date": "string"}
structDict['DFITCQryBillField'] = DFITCQryBillField



#查询账单响应
DFITCQryBillRtnField = {"lRequestID": "long", "accountID": "string", "message": "string"}
structDict['DFITCQryBillRtnField'] = DFITCQryBillRtnField



#厂商ID确认请求
DFITCProductField = {"productID": "string", "vendorID": "string"}
structDict['DFITCProductField'] = DFITCProductField



#厂商ID确认响应
DFITCProductRtnField = {"productID": "string", "vendorID": "string", "productOnlineCount": "long",
						"brokerInfoName": "string", "frontID": "int"}
structDict['DFITCProductRtnField'] = DFITCProductRtnField


#查询交易日请求
DFITCTradingDayField = {"lRequestID": "long"}
structDict['DFITCTradingDayField'] = DFITCTradingDayField



#交易日请求响应
DFITCTradingDayRtnField = {"lRequestID": "long", "date": "string"}
structDict['DFITCTradingDayRtnField'] = DFITCTradingDayRtnField



#询价通知订阅请求
DFITCQuoteSubscribeField = {"lRequestID": "long", "accountID": "string", "exchangeID": "string"}
structDict['DFITCQuoteSubscribeField'] = DFITCQuoteSubscribeField


#询价通知订阅响应
DFITCQuoteSubscribeRspField = {"lRequestID": "long", "subscribeFlag": "int", "exchangeID": "string"}
structDict['DFITCQuoteSubscribeRspField'] = DFITCQuoteSubscribeRspField


#询价通知退订请求
DFITCQuoteUnSubscribeField = {"lRequestID": "long", "accountID": "string", "exchangeID": "string"}
structDict['DFITCQuoteUnSubscribeField'] = DFITCQuoteUnSubscribeField


#询价通知退订响应
DFITCQuoteUnSubscribeRspField = {"lRequestID": "long", "subscribeFlag": "int", "exchangeID": "string"}
structDict['DFITCQuoteUnSubscribeRspField'] = DFITCQuoteUnSubscribeRspField


#询价通知订阅回报
DFITCQuoteSubscribeRtnField = {"quoteID": "string", "exchangeID": "string", "instrumentID": "string", "source": "short",
							   "quoteTime": "string"}
structDict['DFITCQuoteSubscribeRtnField'] = DFITCQuoteSubscribeRtnField


#询价通知查询请求
DFITCQryQuoteNoticeField = {"accountID": "string", "lRequestID": "long", "exchangeID": "string",
							"instrumentID": "string"}
structDict['DFITCQryQuoteNoticeField'] = DFITCQryQuoteNoticeField


#询价通知查询响应
DFITCQryQuoteNoticeRtnField = {"lRequestID": "long", "quoteID": "string", "exchangeID": "string",
							   "instrumentID": "string", "source": "short", "quoteTime": "string"}
structDict['DFITCQryQuoteNoticeRtnField'] = DFITCQryQuoteNoticeRtnField


#做市商报单请求
DFITCQuoteInsertField = {"accountID": "string", "lRequestID": "long", "localOrderID": "long", "insertType": "int",
						 "instrumentID": "string", "quoteID": "string", "instrumentType": "int", "bOrderAmount": "long",
						 "sOrderAmount": "long", "bInsertPrice": "float", "sInsertPrice": "float",
						 "bOpenCloseType": "int", "sOpenCloseType": "int", "bSpeculator": "int", "sSpeculator": "int",
						 "stayTime": "int", "customCategory": "string"}
structDict['DFITCQuoteInsertField'] = DFITCQuoteInsertField




#做市商报单响应
DFITCQuoteRspField = {"localOrderID": "long", "spdOrderID": "long", "lRequestID": "long", "fee": "float",
					  "margin": "float", "orderTime": "string", "orderStatus": "short", "customCategory": "string",
					  "instrumentID": "string", "accountID": "string", "quoteID": "string", "sessionID": "long",
					  "clientID": "string"}
structDict['DFITCQuoteRspField'] = DFITCQuoteRspField



#做市商报单回报
DFITCQuoteRtnField = {"exchangeID": "string", "clientID": "string", "orderSysID": "string", "instrumentID": "string",
					  "localOrderID": "long", "seatCode": "string", "bOpenCloseType": "int", "sOpenCloseType": "int",
					  "speculator": "int", "bOrderAmount": "long", "sOrderAmount": "long", "bInsertPrice": "float",
					  "sInsertPrice": "float", "spdOrderID": "long", "accountID": "string", "instrumentType": "int",
					  "suspendTime": "string", "entrusTeller": "string", "orderStatus": "short", "sessionID": "long",
					  "quoteID": "string", "errorMsg": "string", "customCategory": "string"}
structDict['DFITCQuoteRtnField'] = DFITCQuoteRtnField




#做市商撤单回报
DFITCQuoteCanceledRtnField = {"exchangeID": "string", "clientID": "string", "orderSysID": "string",
							  "instrumentID": "string", "localOrderID": "long", "seatCode": "string",
							  "bOpenCloseType": "int", "sOpenCloseType": "int", "speculator": "int",
							  "spdOrderID": "long", "accountID": "string", "entrusTeller": "string",
							  "orderStatus": "short", "cancelAmount": "long", "fee": "float", "margin": "float",
							  "sessionID": "long", "buySellType": "short", "quoteID": "string",
							  "canceledTime": "string", "customCategory": "string"}
structDict['DFITCQuoteCanceledRtnField'] = DFITCQuoteCanceledRtnField




#做市商成交回报
DFITCQuoteMatchRtnField = {"exchangeID": "string", "clientID": "string", "instrumentID": "string", "seatCode": "string",
						   "localOrderID": "long", "openCloseType": "int", "speculator": "int", "spdOrderID": "long",
						   "OrderSysID": "string", "matchID": "string", "matchedAmount": "long",
						   "matchedPrice": "float", "accountID": "string", "turnover": "float",
						   "entrusTeller": "string", "matchedTime": "string", "fee": "float", "insertPrice": "float",
						   "orderAmount": "long", "orderStatus": "short", "margin": "float", "buySellType": "short",
						   "closeTodayAmount": "long", "closePrice": "float", "closeTodayPrice": "float",
						   "adjustmentInfo": "string", "frozenCapita": "float", "dateCloseProfitLoss": "float",
						   "instrumentType": "int", "sessionID": "long", "largeMarginDirect": "string",
						   "quoteID": "string", "customCategory": "string"}
structDict['DFITCQuoteMatchRtnField'] = DFITCQuoteMatchRtnField



#批量撤单请求
DFITCCancelAllOrderField = {"lRequestID": "long", "accountID": "string", "exchangeID": "string"}
structDict['DFITCCancelAllOrderField'] = DFITCCancelAllOrderField


#批量撤单响应
DFITCCancelAllOrderRspField = {"lRequestID": "long", "accountID": "string", "orderStatus": "short"}
structDict['DFITCCancelAllOrderRspField'] = DFITCCancelAllOrderRspField


#询价请求
DFITCForQuoteField = {"lRequestID": "long", "accountID": "string", "instrumentID": "string"}
structDict['DFITCForQuoteField'] = DFITCForQuoteField


#询价请求响应
DFITCForQuoteRspField = {"lRequestID": "long", "spdOrderID": "long", "commTime": "string"}
structDict['DFITCForQuoteRspField'] = DFITCForQuoteRspField


#询价回报
DFITCForQuoteRtnField = {"spdOrderID": "long", "sessionID": "long", "instrumentID": "string", "exchangeID": "string",
						 "accountID": "string", "orderStatus": "short"}
structDict['DFITCForQuoteRtnField'] = DFITCForQuoteRtnField


#做市商报价委托查询
DFITCQuoteOrderField = {"lRequestID": "long", "exchangeID": "string", "accountID": "string", "instrumentID": "string",
						"localOrderID": "long", "spdOrderID": "long", "orderStatus": "short"}
structDict['DFITCQuoteOrderField'] = DFITCQuoteOrderField


#做市商报价查询响应
DFITCQuoteOrderRtnField = {"lRequestID": "long", "spdOrderID": "long", "orderStatus": "short", "instrumentID": "string",
						   "margin": "float", "fee": "float", "localOrderID": "long", "accountID": "string",
						   "commTime": "string", "submitTime": "string", "exchangeID": "string", "bOrderAmount": "long",
						   "bMatchedAmount": "long", "bCancelAmount": "long", "bInsertPrice": "float",
						   "bMatchedPrice": "float", "bOpenCloseType": "int", "sOrderAmount": "long",
						   "sMatchedAmount": "long", "sCancelAmount": "long", "sInsertPrice": "float",
						   "sMatchedPrice": "float", "sOpenCloseType": "int", "operStation": "string",
						   "sessionID": "long", "quoteID": "string", "customCategory": "string"}
structDict['DFITCQuoteOrderRtnField'] = DFITCQuoteOrderRtnField


#查询转账银行
DFITCQryTransferBankField = {"accountID": "string", "bankID": "string", "lRequestID": "long"}
structDict['DFITCQryTransferBankField'] = DFITCQryTransferBankField


#转帐银行响应
DFITCTransferBankRspField = {"accountID": "string", "bankID": "string", "bankAccount": "string", "currency": "string",
							 "registDate": "string", "lRequestID": "long"}
structDict['DFITCTransferBankRspField'] = DFITCTransferBankRspField


#查询转账流水
DFITCQryTransferSerialField = {"accountID": "string", "bankID": "string", "bankAccount": "string", "lRequestID": "long"}
structDict['DFITCQryTransferSerialField'] = DFITCQryTransferSerialField


#转账流水响应
DFITCTransferSerialRspField = {"accountID": "string", "bankID": "string", "bankAccount": "string", "currency": "string",
							   "applyNum": "int", "type": "int", "tradeAmount": "float", "curFutAccountFund": "float",
							   "bankSerialNum": "int", "reqTransferTime": "string", "dealTransferTime": "string",
							   "procResult": "int", "lRequestID": "long"}
structDict['DFITCTransferSerialRspField'] = DFITCTransferSerialRspField


#资金转账请求信息
DFITCReqTransferField = {"bankID": "string", "bankAccount": "string", "bankPassword": "string", "accountID": "string",
						 "password": "string", "currency": "string", "tradeAmount": "float", "lRequestID": "long"}
structDict['DFITCReqTransferField'] = DFITCReqTransferField


#资金转账响应信息
DFITCTransferRspField = {"bankID": "string", "bankAccount": "string", "accountID": "string", "tradeAmount": "float",
						 "applyNumber": "int", "lRequestID": "long"}
structDict['DFITCTransferRspField'] = DFITCTransferRspField


#资金转账通知信息
DFITCTransferRtnField = {"accountID": "string", "bankID": "string", "bankAccount": "string", "type": "int",
						 "tradeAmount": "float", "bankSerialNum": "int", "applyNumber": "int", "sessionID": "long"}
structDict['DFITCTransferRtnField'] = DFITCTransferRtnField


#银行或主席发起出金冲正通知
DFITCRepealRtnField = {"accountID": "string", "bankID": "string", "bankAccount": "string", "type": "int",
					   "tradeAmount": "float", "bankSerialNum": "int", "repealSerial": "int"}
structDict['DFITCRepealRtnField'] = DFITCRepealRtnField


#交易状态查询请求
DFITCQryExchangeStatusField = {"lRequestID": "long", "exchangeID": "string"}
structDict['DFITCQryExchangeStatusField'] = DFITCQryExchangeStatusField


#交易所状态查询响应
DFITCExchangeStatusRspField = {"lRequestID": "long", "exchangeStatus": "int", "exchangeID": "string"}
structDict['DFITCExchangeStatusRspField'] = DFITCExchangeStatusRspField


#交易所状态通知
DFITCExchangeStatusRtnField = {"exchangeID": "string", "instrumentID": "string", "exchangeStatus": "int"}
structDict['DFITCExchangeStatusRtnField'] = DFITCExchangeStatusRtnField


#行情查询请求
DFITCQryDepthMarketDataField = {"lRequestID": "long", "instrumentID": "string", "exchangeID": "string"}
structDict['DFITCQryDepthMarketDataField'] = DFITCQryDepthMarketDataField


#查询询价请求
DFITCQryForQuoteField = {"lRequestID": "long", "accountID": "string", "instrumentID": "string", "exchangeID": "string"}
structDict['DFITCQryForQuoteField'] = DFITCQryForQuoteField


#查询询价响应
DFITCQryForQuoteRtnField = {"lRequestID": "long", "accountID": "string", "spdOrderID": "long", "instrumentID": "string",
							"exchangeID": "string", "SuspendTime": "string", "orderStatus": "short"}
structDict['DFITCQryForQuoteRtnField'] = DFITCQryForQuoteRtnField



