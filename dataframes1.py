# BY SULAIMAN SHAMS
from operator import index
import pandas as pd

data1=[25,27,28]
df=pd.DataFrame(data1,columns=['data'])
print(df)
#---------------------------------------------------------

data2=[['Sulaiman Shams', 25, 'Karachi'], ['Haris Ali', 26, 'Peshwar']]
df1=pd.DataFrame(data2, columns=['name', 'age', 'location'])
print(df1)

#---------------------------------------------------------

print(pd.DataFrame({'Names':['Sulaiman Shams', 'Haris Ali'], 'Age':[24, 26]}))

#-----------------------------------------------------------
#NULL DATA 
columns=['Name','city','Address']
dfz=pd.DataFrame(index=['a','b'],columns=columns)
print(dfz)