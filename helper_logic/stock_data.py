# https://www.notion.so/financedata/FinanceData-KR-6da3ac1cb8864178a4a61d9bc319cb53

import FinanceDataReader as fdr


class VolatilityCalc:
    def __init__(self):
        pass


    def volatility_calc(stock_code, start_date):
        df = fdr.DataReader(stock_code, start_date)
        print(df)

