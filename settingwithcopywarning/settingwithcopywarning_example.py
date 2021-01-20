# 1. Chained assigment that will raise warning of SettingWithCopyWarning
import pandas as pd

data = {
    'id': [1, 2, 3],
    'employee': ['Mark', 'Antoine', 'Clement'],
    'sales': [50, 60, 70],
    'pay_raise': [0, 0, 0]
}
df = pd.DataFrame(data)
print(df)
df.loc[df['sales'] > 50]['pay_raise'] = 1
print(df)


# 2. Compress chained assignment into single loc
import pandas as pd

data = {
    'id': [1, 2, 3],
    'employee': ['Mark', 'Antoine', 'Clement'],
    'sales': [50, 60, 70],
    'pay_raise': [0, 0, 0]
}
df = pd.DataFrame(data)
print(df)
df.loc[df['sales'] > 50, 'pay_raise'] = 1
print(df)


# 3.1 Hidden chained assigment can also lead to warning
import pandas as pd

data = {
    'id': [1, 2, 3],
    'employee': ['Mark', 'Antoine', 'Clement'],
    'sales': [50, 60, 70],
    'pay_raise': [0, 0, 0]
}
df = pd.DataFrame(data)

df1 = df.loc[df['sales'] > 50]
df1['pay_raise'] = 1

print('df1 \n:', df1)
print('df \n:', df)

# 3.2 No error if initiate df1 from scratch
data = {
    'id': [2, 3],
    'employee': ['Antoine', 'Clement'],
    'sales': [60, 70],
    'pay_raise': [0, 0]
}

df1 = pd.DataFrame(data)
df1['promotion'] = 1
print(df1)

#========================================
#======== How to deal with ==============
#========================================

# B.1 Ignore warnings
import warnings
warnings.filterwarnings("ignore")
df1['promotion'] = 1


# B.2