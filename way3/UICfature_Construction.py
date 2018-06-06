import pandas as pd

#基于user_id、item_id、category三大基本维度进行特征构建，
# 这里将所需构建的特征分为六大类：U、I、C、UI、UC、IC

#step1:读取要用到的数据
userAll = pd.read_csv('./way3Data/user_item_datetime_type.csv', encoding='utf-8')
# print(userAll.info())
# print(userAll.head())

#step2:构建U类特征
# ①u_b_count_in_n(n=1/3/6; 用户在考察日前n天的行为总量计数，考察日取2014-12-17)
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub[['user_id', 'item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id', 'item_category'], as_index=False).sum()
userSub['u_b_count_in_1'] = userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
# print(userSub.info())
# print("最大值：", userSub['behavior'].max())   #20
u_b_count_in_1 = userSub.copy()
# print(u_b_count_in_1.info())
# print(u_b_count_in_1.head())
# usertmp = userSub[['user_id', 'item_id', 'item_category']]
# print(usertmp.duplicated().sum())# 重复行为0

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id', 'item_category'], as_index=False).sum()
userSub['u_b_count_in_3'] = userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
u_b_count_in_3 = userSub.copy()
# print(u_b_count_in_3.info())
# print(u_b_count_in_3.head())

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id', 'item_category'], as_index=False).sum()
userSub['u_b_count_in_6'] = userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
u_b_count_in_6 = userSub.copy()
# print(u_b_count_in_6.info())
# print(u_b_count_in_6.head())

u_b_count_in_n = pd.merge(u_b_count_in_6, u_b_count_in_3, on=['user_id', 'item_id', 'item_category'], how='left').fillna(0.0)
u_b_count_in_n = pd.merge(u_b_count_in_n, u_b_count_in_1, on=['user_id', 'item_id', 'item_category'], how='left').fillna(0.0)
# print(u_b_count_in_n.info())
# print(u_b_count_in_n.head())
u_b_count_in_n.to_csv('./way3Data/u_b_count_in_n.csv', index=False, encoding='utf-8')

#②u_bi_count_in_n(n=1/3/6;i=1/2/3/4; 用户在考察日前n天的各类行为总量计数，考察日取2014-12-17)
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub[['user_id', 'item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id', 'item_category'], as_index=False).sum()
userSub['u_b1_count_in_1'] = userSub['type_1']   #用户在考察日前1天的浏览（1）行为总量计数
userSub['u_b2_count_in_1'] = userSub['type_2']   #用户在考察日前1天的收藏（2）行为总量计数
userSub['u_b3_count_in_1'] = userSub['type_3']   #用户在考察日前1天的加购物车（3）行为总量计数
userSub['u_b4_count_in_1'] = userSub['type_4']   #用户在考察日前1天的购买（4）行为总量计数
userSub.drop(['type_1'], axis=1, inplace=True)
userSub.drop(['type_2'], axis=1, inplace=True)
userSub.drop(['type_3'], axis=1, inplace=True)
userSub.drop(['type_4'], axis=1, inplace=True)
u_bi_count_in_1 = userSub.copy()
# print(u_bi_count_in_1.info())
# print(u_bi_count_in_1.u_b1_count_in_3.max())

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id', 'item_category'], as_index=False).sum()
userSub['u_b1_count_in_3'] = userSub['type_1']   #用户在考察日前3天的浏览（1）行为总量计数
userSub['u_b2_count_in_3'] = userSub['type_2']
userSub['u_b3_count_in_3'] = userSub['type_3']
userSub['u_b4_count_in_3'] = userSub['type_4']
userSub.drop(['type_1'], axis=1, inplace=True)
userSub.drop(['type_2'], axis=1, inplace=True)
userSub.drop(['type_3'], axis=1, inplace=True)
userSub.drop(['type_4'], axis=1, inplace=True)
u_bi_count_in_3 = userSub.copy()
# print(u_bi_count_in_3.info())
# print(u_bi_count_in_3.u_b3_count_in_3.max())

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id', 'item_category'], as_index=False).sum()
userSub['u_b1_count_in_6'] = userSub['type_1']   #用户在考察日前6天的浏览（1）行为总量计数
userSub['u_b2_count_in_6'] = userSub['type_2']
userSub['u_b3_count_in_6'] = userSub['type_3']
userSub['u_b4_count_in_6'] = userSub['type_4']
userSub.drop(['type_1'], axis=1, inplace=True)
userSub.drop(['type_2'], axis=1, inplace=True)
userSub.drop(['type_3'], axis=1, inplace=True)
userSub.drop(['type_4'], axis=1, inplace=True)
u_bi_count_in_6 = userSub.copy()
# print(u_bi_count_in_6.info())
# print(u_bi_count_in_6.u_b2_count_in_6.max())

u_bi_count_in_n = pd.merge(u_bi_count_in_6, u_bi_count_in_3, on=['user_id', 'item_id', 'item_category'], how='left').fillna(0.0)
u_bi_count_in_n = pd.merge(u_bi_count_in_n, u_bi_count_in_1, on=['user_id', 'item_id', 'item_category'], how='left').fillna(0.0)
# print(u_bi_count_in_n.info())
# print(u_bi_count_in_n.u_b4_count_in_6.max())
u_bi_count_in_n.to_csv('./way3Data/u_bi_count_in_n.csv', index=False, encoding='utf-8')

#③u_b4_rate(用户的点击购买转化率，反映了用户的购买决策操作习惯)（此处使用大转化，不是分层转化，分层转化主要为了找出用户流失环节进而改进）
userSub = userAll[['user_id', 'item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id', 'item_category'], as_index=False).sum()
# usertmp = userSub[['user_id', 'item_id', 'item_category']]
# print(usertmp.duplicated().sum())
userSub['u_b4_rate'] = userSub['type_4']/(userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4']).map(lambda x:x+1 if x == 0 else x)
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
u_b4_rate = userSub.copy()
# print(u_b4_rate.info())
# print(u_b4_rate.head())
# print(u_b4_rate.u_b4_rate.max())
u_b4_rate.to_csv('./way3Data/u_b4_rate.csv', index=False, encoding='utf-8')

#④u_b4_diff_hours（用户的点击购买平均时差，反映了用户的购买决策时间习惯）
userSub = userAll.copy()
# print(userSub.info())
userSub.drop_duplicates(inplace=True)
userSub = userSub[['user_id', 'item_id', 'item_category', 'type_1', 'type_4', 'time_day', 'time_hour']]
userSub = userSub.sort_values(by=['type_4'], axis=0, ascending=True)##用最早的购买时间和最晚的浏览时间计算购买时差
userSub = userSub.sort_values(by=['type_1'], axis=0, ascending=False)
userSub = userSub.drop_duplicates(['user_id', 'item_id','item_category', 'type_1', 'type_4'], keep='first', inplace=False)
# print(userSub.info())
# print(userSub.head())
usertmp1 = userSub[userSub['type_1'] == 1]
usertmp1 = usertmp1.drop(['type_4'], axis=1)
usertmp1.rename(columns={'time_day':'time_day_1', 'time_hour':'time_hour_1'}, inplace=True)
usertmp4 = userSub[userSub['type_4'] == 1]
usertmp4 = usertmp4.drop(['type_1'], axis=1)
usertmp4.rename(columns={'time_day':'time_day_4', 'time_hour':'time_hour_4'}, inplace=True)
# print(usertmp1.info())
# print(usertmp4.info())
usertmp = pd.merge(usertmp1, usertmp4, how='right')
usertmp.dropna(axis=0, how='any', inplace=True)
# print(usertmp.info())
# print(usertmp.head())
# print(usertmp[usertmp['type_1']!=1])
# print(usertmp[usertmp['type_4']!=1])

import datetime
def to_time(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%Y-%m-%d")
def to_hour(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%H:%M:%S")

usertmp['u_b4_diff_hours'] = (usertmp['time_day_4'].map(lambda x:to_time(x))-usertmp['time_day_1'].map(lambda x:to_time(x)))+(usertmp['time_hour_4'].map(lambda x:to_hour(x))-usertmp['time_hour_1'].map(lambda x:to_hour(x)))
usertmp = usertmp[['item_id', 'item_category', 'u_b4_diff_hours']]
# print(usertmp.info())
# print(usertmp.head())
usertmp.to_csv('./way3Data/u_b4_diff_hours.csv', index=False, encoding='utf-8')

# step3:构建I类特征
#①i_u_count_in_n (商品在考察日(2014-12-17)前n天的用户总数计数	反映了item_id的热度（用户覆盖性）)
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub[['user_id', 'item_id', 'item_category']]
# print(userSub.info())
userSub = userSub.drop_duplicates()
# print(userSub.info())
userSub = userSub.drop('user_id', axis=1, inplace=False)
# print(userSub.info())
userSub['i_u_count_in_1'] = 1
# print(userSub.info())
# print(userSub.head())
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
userSub = userSub.drop_duplicates()
# print(userSub.info())
# print(userSub.head())
i_u_count_in_1 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'item_category']]
userSub = userSub.drop_duplicates()
userSub = userSub.drop('user_id', axis=1, inplace=False)
# print(userSub.info())
# print(userSub.head())
userSub['i_u_count_in_3'] = 1
# print(userSub.info())
# print(userSub.head())
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
userSub = userSub.drop_duplicates()
# print(userSub.info())
# print(userSub.head())
i_u_count_in_3 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'item_category']]
userSub = userSub.drop_duplicates()
userSub = userSub.drop('user_id', axis=1, inplace=False)
# print(userSub.info())
# print(userSub.head())
userSub['i_u_count_in_6'] = 1.0
# print(userSub.info())
# print(userSub.head())
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
userSub = userSub.drop_duplicates()
# print(userSub.info())
# print(userSub.head())
i_u_count_in_6 = userSub.copy()
# print(i_u_count_in_6.info())
# print(i_u_count_in_6.head())

i_u_count_in_n = pd.merge(i_u_count_in_6, i_u_count_in_3, on=['item_id', 'item_category'], how='left').fillna(0)
i_u_count_in_n = pd.merge(i_u_count_in_n, i_u_count_in_1, on=['item_id', 'item_category'], how='left').fillna(0)
# print(i_u_count_in_n.info())
# print(i_u_count_in_n.head())
i_u_count_in_n.to_csv('./way3Data/i_u_count_in_n.csv', index=False, encoding='utf-8')

#②i_b_count_in_n（商品在考察日前n天的行为总数计数	反映了item_id的热度（用户停留性））
userSub = userAll[userAll['time_day'] == '2014-12-16']
# print(userSub.info())
# print(userSub.head())
userSub = userSub[['item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
# print(userSub.info())
# print(userSub.head())
userSub['i_b_count_in_1'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
# print(userSub.head())
userSub = userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=False)
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head())
i_b_count_in_1 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub['i_b_count_in_3'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub = userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=False)
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head())
i_b_count_in_3 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub['i_b_count_in_6'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub = userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=False)
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head())
i_b_count_in_6 = userSub.copy()

i_b_count_in_n = pd.merge(i_b_count_in_6, i_b_count_in_3, on=['item_id', 'item_category'], how='left').fillna(0)
i_b_count_in_n = pd.merge(i_b_count_in_n, i_b_count_in_1, on=['item_id', 'item_category'], how='left').fillna(0)
# print(i_b_count_in_n.info())
# print(i_b_count_in_n.head())
i_b_count_in_n.to_csv('./way3Data/i_b_count_in_n.csv', index=False, encoding='utf-8')

#③i_bi_count_in_n(商品在考察日前n天的各项行为计数	反映了item_id的热度（用户操作吸引），折射出item_id产生的购买习惯特点)
userSub = userAll[userAll['time_day'] == '2014-12-16']
# print(userSub.head())
userSub = userSub[['item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
# print(userSub.head())
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
# print(userSub.type_4.max())
userSub.rename(columns={'type_1':'i_b1_count_in_1', 'type_2':'i_b2_count_in_1','type_3':'i_b3_count_in_1', 'type_4':'i_b4_count_in_1'}, inplace=True)
# print(userSub.info())
# print(userSub.head())
# print(userSub.i_b4_count_in_1.max())
i_bi_count_in_1 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
userSub.rename(columns={'type_1':'i_b1_count_in_3', 'type_2':'i_b2_count_in_3','type_3':'i_b3_count_in_3', 'type_4':'i_b4_count_in_3'}, inplace=True)
# print(userSub.info())
# print(userSub.head())
# print(userSub.i_b4_count_in_3.max())
i_bi_count_in_3 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
userSub.rename(columns={'type_1':'i_b1_count_in_6', 'type_2':'i_b2_count_in_6','type_3':'i_b3_count_in_6', 'type_4':'i_b4_count_in_6'}, inplace=True)
# print(userSub.info())
# print(userSub.head())
# print(userSub.i_b4_count_in_6.max())
i_bi_count_in_6 = userSub.copy()

i_bi_count_in_n = pd.merge(i_bi_count_in_6, i_bi_count_in_3, on=['item_id', 'item_category'], how='left').fillna(0)
i_bi_count_in_n = pd.merge(i_bi_count_in_n, i_bi_count_in_1, on=['item_id', 'item_category'], how='left').fillna(0)
# print(i_bi_count_in_n.info())
# print(i_bi_count_in_n.head())
i_bi_count_in_n.to_csv('./way3Data/i_bi_count_in_n.csv', index=False, encoding='utf-8')

#④i_b4_rate(商品的点击购买转化率	反映了商品的购买决策操作特点)
userSub  =userAll.copy()
# print(userSub.duplicated().sum())
userSub = userSub.drop_duplicates()
# print(userSub.duplicated().sum())
userSub = userSub[['item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
# print(userSub.info())
userSub = userSub.groupby(['item_id', 'item_category'], as_index=False).sum()
userSub['i_b4_rate'] = (userSub['type_4'])/(userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4']).map(lambda x:x if x>0 else x+1)
# print(userSub.i_b4_rate.max())
userSub = userSub[['item_id', 'item_category', 'i_b4_rate']]
# print(userSub.info())
# usertmp = userSub[userSub['i_b4_rate'] > 0]
# print(usertmp.head(50))
i_b4_rate = userSub.copy()
i_b4_rate.to_csv('./way3Data/i_b4_rate.csv', index=False, encoding='utf-8')

#⑤i_b4_diff_hours(商品的点击购买平均时差	反映了商品的购买决策时间特点)
userSub = userAll.copy()
# print(userSub.info())
userSub = userSub[['item_id', 'item_category', 'type_1', 'type_4', 'time_day', 'time_hour']]
# print(userSub.info())
# print(userSub.head())
userSub = userSub.sort_values(by=['type_4'], axis=0, ascending=True)      #用最早的购买时间和最晚的浏览时间计算购买时差
userSub = userSub.sort_values(by=['type_1'], axis=0, ascending=False)

userSub = userSub.drop_duplicates(['item_id', 'item_category', 'type_1', 'type_4'], keep='first', inplace=False)
# print(userSub.head())
usertmp1 = userSub[userSub['type_1'] == 1]
usertmp1 = usertmp1.drop(['type_4'], axis=1)
usertmp1.rename(columns={'time_day':'time_day_1', 'time_hour':'time_hour_1'}, inplace=True)
usertmp4 = userSub[userSub['type_4'] == 1]
usertmp4 = usertmp4.drop(['type_1'], axis=1)
usertmp4.rename(columns={'time_day':'time_day_4', 'time_hour':'time_hour_4'}, inplace=True)
# print(usertmp1.info())
# print(usertmp4.info())
usertmp = pd.merge(usertmp1, usertmp4, on=['item_id', 'item_category'], how='right')
# usertmp = usertmp.drop(usertmp.loc[:, 'type_4'] == 0, axis=0)
# usertmp = usertmp.drop(usertmp.loc[:, 'type_1'] == 'NaN', axis=0)
usertmp.dropna(axis=0, how='any', inplace=True) #drop all rows that have any NaN values
# print(usertmp[usertmp['type_1'] != 1])
# print(usertmp[usertmp['type_4'] != 1])

import datetime
def to_time(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%Y-%m-%d")
def to_hour(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%H:%M:%S")

usertmp['i_b4_diff_hours'] = (usertmp['time_day_4'].map(lambda x:to_time(x))-usertmp['time_day_1'].map(lambda x:to_time(x)))+(usertmp['time_hour_4'].map(lambda x:to_hour(x))-usertmp['time_hour_1'].map(lambda x:to_hour(x)))
usertmp = usertmp[['item_id', 'item_category', 'i_b4_diff_hours']]
# print(usertmp.info())
# print(usertmp.head())
usertmp.to_csv('./way3Data/i_b4_diff_hours.csv', index=False, encoding='utf-8')

#step4:构建C(category)类特征
#①c_u_count_in_n(类别在考察日前n天的用户总数计数	反映了item_category的热度（用户覆盖性）)
userSub = userAll[userAll['time_day'] == '2014-12-16']
# print(userSub.info())
userSub = userSub.drop_duplicates()   #去除重复的用户
# print(userSub.info())
userSub = userSub[['item_category']]
userSub['c_u_count_in_1'] = 1
# print(userSub.head())
userSub = userSub.groupby(['item_category'], as_index=False).sum()
# print(userSub.info())
# print(userSub.c_u_count_in_1.max())
c_u_count_in_1 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub.drop_duplicates()
userSub = userSub[['item_category']]
userSub['c_u_count_in_3'] = 1
userSub = userSub.groupby(['item_category'], as_index=False).sum()
# print(userSub.info())
# print(userSub.c_u_count_in_3.max())
c_u_count_in_3 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub.drop_duplicates()
userSub = userSub[['item_category']]
userSub['c_u_count_in_6'] = 1
userSub = userSub.groupby(['item_category'], as_index=False).sum()
# print(userSub.info())
# print(userSub.c_u_count_in_6.max())
c_u_count_in_6 = userSub.copy()

c_u_count_in_n = pd.merge(c_u_count_in_6, c_u_count_in_3, on=['item_category'], how='left').fillna(0)
c_u_count_in_n = pd.merge(c_u_count_in_n, c_u_count_in_1, on=['item_category'], how='left').fillna(0)
# print(c_u_count_in_n.info())
# print(c_u_count_in_n.head())
c_u_count_in_n.to_csv('./way3Data/c_u_count_in_n.csv', index=False, encoding='utf-8')

#②c_bi_count_in_n(类别在考察日前n天的各项行为计数	反映了item_category的热度（用户操作吸引），包含着item_category产生的购买习惯特点)
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub.drop_duplicates()
userSub = userSub[['item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['item_category'], as_index=False).sum()
# print(userSub.head())
userSub.rename(columns={'type_1':'c_b1_count_in_1', 'type_2':'c_b2_count_in_1', 'type_3':'c_b3_count_in_1',
                          'type_4':'c_b4_count_in_1'}, inplace=True)
# print(userSub.info())
# print(userSub.head())
c_bi_count_in_1 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub.drop_duplicates()
userSub = userSub[['item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['item_category'], as_index=False).sum()
userSub.rename(columns={'type_1':'c_b1_count_in_3', 'type_2':'c_b2_count_in_3', 'type_3':'c_b3_count_in_3',
                          'type_4':'c_b4_count_in_3'}, inplace=True)
c_bi_count_in_3 = userSub.copy()
# print(c_bi_count_in_3.info())
# print(c_bi_count_in_3.head())

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub.drop_duplicates()
userSub = userSub[['item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['item_category'], as_index=False).sum()
userSub.rename(columns={'type_1':'c_b1_count_in_6', 'type_2':'c_b2_count_in_6', 'type_3':'c_b3_count_in_6',
                          'type_4':'c_b4_count_in_6'}, inplace=True)
c_bi_count_in_6 = userSub.copy()
# print(c_bi_count_in_6.info())
# print(c_bi_count_in_6.head())

c_bi_count_in_n = pd.merge(c_bi_count_in_6, c_bi_count_in_3, on=['item_category'], how='left').fillna(0)
c_bi_count_in_n = pd.merge(c_bi_count_in_n, c_bi_count_in_1, on=['item_category'], how='left').fillna(0)
# print(c_bi_count_in_n.info())
# print(c_bi_count_in_n.head())
c_bi_count_in_n.to_csv('./way3Data/c_b_count_in_n.csv', index=False, encoding='utf-8')

#③c_b_count_in_n(类别在考察日前n天的行为总数计数	反映了item_category的热度（用户停留性）)
userSub = c_bi_count_in_n.copy()
userSub['c_b_count_in_1'] = userSub['c_b1_count_in_1']+userSub['c_b2_count_in_1']+userSub['c_b3_count_in_1']+userSub['c_b4_count_in_1']
userSub['c_b_count_in_3'] = userSub['c_b1_count_in_3']+userSub['c_b2_count_in_3']+userSub['c_b3_count_in_3']+userSub['c_b4_count_in_3']
userSub['c_b_count_in_6'] = userSub['c_b1_count_in_6']+userSub['c_b2_count_in_6']+userSub['c_b3_count_in_6']+userSub['c_b4_count_in_6']
userSub = userSub[['item_category', 'c_b_count_in_1', 'c_b_count_in_3', 'c_b_count_in_6']]
# print(userSub.info())
# print(userSub.head())
c_b_count_in_n = userSub.copy()
c_b_count_in_n.to_csv('./way3Data/c_b_count_in_n.csv', index=False, encoding='utf-8')

#④c_b4_rate(类别的点击购买转化率	反映了item_category的购买决策操作特点)
userSub = userAll.copy()
userSub.drop_duplicates(inplace=True)
userSub = userSub[['item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['item_category'], as_index=False).sum()
userSub['c_b4_rate'] = userSub['type_4']/(userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4']).map(lambda x:x if x!=0 else x+1)
# print(userSub.head())
c_b4_rate = userSub[['item_category', 'c_b4_rate']]
# print(c_b4_rate.info())
# print(c_b4_rate.head())
c_b4_rate.to_csv('./way3Data/c_b4_rate.csv', index=False, encoding='utf-8')

#⑤c_b4_diff_hours(类别的点击购买平均时差	反映了item_category的购买决策时间特点)
userSub = userAll.copy()
userSub.drop_duplicates(inplace=True)
userSub = userSub[['item_category', 'type_1', 'type_4', 'time_day', 'time_hour']]
# print(userSub.info())
# print(userSub.head())
userSub = userSub.sort_values(by=['type_4'], axis=0, ascending=True)#用最早的购买时间和最晚的浏览时间计算购买时差
userSub = userSub.sort_values(by=['type_1'], axis=0, ascending=False)
userSub = userSub.drop_duplicates(['item_category', 'type_1', 'type_4'], keep='first', inplace=False)
# print(userSub.type_4.max())
usertmp1 = userSub[userSub['type_1'] == 1]
usertmp1 = usertmp1.drop(['type_4'], axis=1)
usertmp1.rename(columns={'time_day':'time_day_1', 'time_hour':'time_hour_1'}, inplace=True)
usertmp4 = userSub[userSub['type_4'] == 1]
usertmp4 = usertmp4.drop(['type_1'], axis=1)
usertmp4.rename(columns={'time_day':'time_day_4', 'time_hour':'time_hour_4'}, inplace=True)
# print(usertmp1.info())
# print(usertmp4.info())
usertmp = pd.merge(usertmp1, usertmp4, on=['item_category'], how='right')
usertmp.dropna(axis=0, how='any', inplace=True)
# print(usertmp[usertmp['type_1']!=1])
# print(usertmp[usertmp['type_4']!=1])
import datetime
def to_time(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%Y-%m-%d")
def to_hour(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%H:%M:%S")

usertmp['c_b4_diff_hours'] = (usertmp['time_day_4'].map(lambda x:to_time(x))-usertmp['time_day_1'].map(lambda x:to_time(x)))+(usertmp['time_hour_4'].map(lambda x:to_hour(x))-usertmp['time_hour_1'].map(lambda x:to_hour(x)))
usertmp = usertmp[['item_category', 'c_b4_diff_hours']]
# print(usertmp.info())     #结果有负值,需要优化
# print(usertmp.head())
usertmp.to_csv('./way3Data/c_b4_diff_hours.csv', index=False, encoding='utf-8')

