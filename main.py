import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv(r'TATASTEEL.csv')
print(df)
report=ProfileReport(df)
report.to_file(output_file="stocks.html")