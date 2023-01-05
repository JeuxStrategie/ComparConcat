import pandas as pd
dt1=pd.read_csv('EXEMPLE4_0/fichiers_detail/archives20180101_20190101_detailv1.csv',sep='|')
dt=pd.read_csv('EXEMPLE4_0/fichiers_detail/archives20180101_20190101_detail.csv',sep='|')
joint=pd.merge(dt1,dt,how='left',indicator=True)
print(joint[joint['_merge']!='both'])