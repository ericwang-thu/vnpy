# encoding: UTF-8

structDict = {}














#用户登录请求
CThostFtdcReqUserLoginField = {"accountID": "string", "loginType": "int", "memberID": "string", "password": "string",
							   "tradeDate": "string"}
structDict['CThostFtdcReqUserLoginField'] = CThostFtdcReqUserLoginField


#用户登录应答
CThostFtdcRspUserLoginField = {"tradeDate": "string", "localOrderNo": "string", "loginbatch": "int",
							   "tradeCode": "string", "clientID": "string", "SeatNo": "string", "clientName": "string",
							   "lastLoginIp": "string", "lastLoginDate": "string", "lastLoginTime": "string"}
structDict['CThostFtdcRspUserLoginField'] = CThostFtdcRspUserLoginField

#用户登出请求
CThostFtdcUserLogoutField = {"traderID": "string"}
structDict['CThostFtdcUserLogoutField'] = CThostFtdcUserLogoutField





#合约
CThostFtdcInstrumentField = {"exchangeID": "string", "instID": "string", "lowerLimit": "float", "marketID": "string",
							 "maxHand": "int", "minHand": "int", "name": "string", "openFlag": "string",
							 "tick": "float", "tradeState": "string", "unit": "int", "upperLimit": "float",
							 "varietyID": "string", "varietyType": "string", "marketType": "string"}
structDict['CThostFtdcInstrumentField'] = CThostFtdcInstrumentField



CThostFtdcQryTradingAccountField = {"remian": "string"}
structDict['CThostFtdcQryTradingAccountField'] = CThostFtdcQryTradingAccountField


#资金账户
CThostFtdcTradingAccountField = {"availCap": "float", "available": "float", "posiMargin": "float",
								 "buyPosiMargin": "float", "sellPosiMargin": "float", "storageMargin": "float",
								 "totalFee": "float", "totalFrozen": "float", "orderFrozen": "float",
								 "spotSellFrozen": "float", "todayIn": "float", "todayOut": "float",
								 "lastFrozen": "float", "totalFrozenFee": "float", "pickUpMargin": "float",
								 "middleMargin": "float"}
structDict['CThostFtdcTradingAccountField'] = CThostFtdcTradingAccountField


#投资者持仓
CThostFtdcInvestorPositionField = {"instID": "string", "longPosi": "int", "longPosiAvgPrice": "float",
								   "shortPosi": "int", "shortPosiAvgPrice": "float", "longOpenAvgPrice": "float",
								   "shortOpenAvgPrice": "float", "longPosiFrozen": "int", "shortPosiFrozen": "int",
								   "longPosiVol": "int", "shortPosiVol": "int", "todayLong": "int", "todayShort": "int",
								   "todayOffsetShort": "int", "todayOffsetLong": "int", "lastLong": "int",
								   "lastShort": "int"}
structDict['CThostFtdcInvestorPositionField'] = CThostFtdcInvestorPositionField




#响应信息
CThostFtdcRspInfoField = {"ErrorID": "int", "ErrorMsg": "string"}
#错误代码
#错误信息
structDict['CThostFtdcRspInfoField'] = CThostFtdcRspInfoField

#深度行情
CThostFtdcDepthMarketDataField = {"InstID": "string", "Name": "string", "MarketName": "string", "PreSettle": "float",
								  "PreClose": "float", "Open": "float", "High": "float", "Low": "float",
								  "Last": "float", "Close": "float", "Bid1": "float", "BidLot1": "int", "Ask1": "float",
								  "AskLot1": "int", "Bid2": "float", "BidLot2": "int", "Ask2": "float",
								  "AskLot2": "int", "Bid3": "float", "BidLot3": "int", "Ask3": "float",
								  "AskLot3": "int", "Bid4": "float", "BidLot4": "int", "Ask4": "float",
								  "AskLot4": "int", "Bid5": "float", "BidLot5": "int", "Ask5": "float",
								  "AskLot5": "int", "Volume": "int", "OpenInt": "int", "UpDown": "float",
								  "Turnover": "float", "Settle": "float", "Average": "float", "QuoteDate": "string",
								  "QuoteTime": "string", "weight": "float", "highLimit": "float", "lowLimit": "float",
								  "UpDownRate": "float"}
structDict['CThostFtdcDepthMarketDataField'] = CThostFtdcDepthMarketDataField



#输入报单
CThostFtdcInputOrderField = {"seatID": "string", "tradeCode": "string", "instID": "string", "buyOrSell": "string",
							 "offsetFlag": "string", "amount": "int", "middleFlag": "string", "priceFlag": "string",
							 "price": "float", "trigPrice": "float", "marketID": "string", "LocalOrderNo": "string",
							 "tradeWay": "string"}
structDict['CThostFtdcInputOrderField'] = CThostFtdcInputOrderField


#报单
CThostFtdcOrderField = {"orderNo": "string", "localOrderNo": "string", "marketID": "string", "instID": "string",
						"buyOrSell": "string", "offsetFlag": "string", "amount": "int", "weight": "float",
						"price": "float", "matchQty": "int", "matchWeight": "float", "status": "string",
						"entrustTime": "string", "forceoffset_flag": "string", "cancelQty": "int",
						"cancelTime": "string", "tradeWay": "string"}
structDict['CThostFtdcOrderField'] = CThostFtdcOrderField


#报单撤单回报
CThostFtdcOrderRtnField = {"orderNo": "string", "localOrderNo": "string", "status": "string", "cancelQty": "int"}
structDict['CThostFtdcOrderRtnField'] = CThostFtdcOrderRtnField



#输入报单操作(cancel order)
CThostFtdcInputOrderActionField = {"localOrderNo": "string", "marketID": "string", "status": "string"}
structDict['CThostFtdcInputOrderActionField'] = CThostFtdcInputOrderActionField


#报单操作
CThostFtdcOrderActionField = {"localOrderNo": "string", "orderFlag": "string", "marketID": "string",
							  "traderID": "string", "tradeWay": "string"}
structDict['CThostFtdcOrderActionField'] = CThostFtdcOrderActionField

#成交
CThostFtdcTradeField = {"orderNo": "string", "matchNo": "string", "instID": "string", "buyOrSell": "string",
						"offSetFlag": "string", "price": "float", "volume": "int", "amount": "float", "weight": "float",
						"order_flag": "string", "matchDate": "string", "matchTime": "string", "localOrderNo": "string",
						"marketID": "string", "trade_fee": "float", "forceoffset_flag": "string",
						"forcebatchnum": "int", "tradeWay": "string"}
structDict['CThostFtdcTradeField'] = CThostFtdcTradeField


#查询合约
CThostFtdcQryInstrumentField = {"ContractID": "string", "ProductID": "string"}
structDict['CThostFtdcQryInstrumentField'] = CThostFtdcQryInstrumentField



#查询成交
CThostFtdcQryTradeField = {"matchNo": "string", "instID": "string", "marketID": "string", "localOrderNo": "string"}
structDict['CThostFtdcQryTradeField'] = CThostFtdcQryTradeField



#查询报单
CThostFtdcQryOrderField = {"instID": "string", "marketID": "string", "localOrderNo": "string"}
structDict['CThostFtdcQryOrderField'] = CThostFtdcQryOrderField





#查询投资者持仓
CThostFtdcQryInvestorPositionField = {"marketID": "string", "instID": "string"}
structDict['CThostFtdcQryInvestorPositionField'] = CThostFtdcQryInvestorPositionField



#查询库存
CThostFtdcQryStorageField = {"varietyID": "string"}
structDict['CThostFtdcQryStorageField'] = CThostFtdcQryStorageField



CThostFtdcStorageField = {"varietyID": "string", "varietyName": "string", "totalStorage": "float",
						  "availableStorage": "float", "frozenStorage": "float", "pendStorage": "float",
						  "todayBuy": "float", "todaySell": "float", "todayDeposit": "float",
						  "todayRealDeposit": "float", "todayBorrow": "float", "todayLend": "float",
						  "impawnStorage": "float", "lawFrozen": "float", "bankFrozen": "float", "customType": "string",
						  "storageCost": "float", "impawnFrozen": "float"}
structDict['CThostFtdcStorageField'] = CThostFtdcStorageField



CThostFtdcMarketStatusField = {"MktStatus": "string", "marketID": "string"}
structDict['CThostFtdcMarketStatusField'] = CThostFtdcMarketStatusField

#指定的合约
CThostFtdcSpecificInstrumentField = {"InstrumentID": "string"}
#合约代码
structDict['CThostFtdcSpecificInstrumentField'] = CThostFtdcSpecificInstrumentField



