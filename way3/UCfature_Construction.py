import pandas as pd
#读取预处理数据
userAll = pd.read_csv('./way3Data/user_item_datetime_type.csv', encoding='utf-8')
userAll.drop_duplicates(inplace=True)

#构建UI类别特征
#①uc_b_count_in_n(用户-类别对在考察日前n天的行为总数计数	反映了user_id - item_category的活跃度)
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_category'], as_index=False).sum()
userSub['uc_b_count_in_1'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
uc_b_count_in_1 = userSub.copy()
# print(uc_b_count_in_1.info())
# print(uc_b_count_in_1.head())

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_category'], as_index=False).sum()
userSub['uc_b_count_in_3'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
uc_b_count_in_3 = userSub.copy()
# print(uc_b_count_in_3.info())
# print(uc_b_count_in_3.head())

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_category'], as_index=False).sum()
userSub['uc_b_count_in_6'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
uc_b_count_in_6 = userSub.copy()
# print(uc_b_count_in_6.info())
# print(uc_b_count_in_6.head())

uc_b_count_in_n = pd.merge(uc_b_count_in_6, uc_b_count_in_3, how='left').fillna(0)
uc_b_count_in_n = pd.merge(uc_b_count_in_n, uc_b_count_in_1, how='left').fillna(0)
# print(uc_b_count_in_n.info())
# print(uc_b_count_in_n.head())
uc_b_count_in_n.to_csv('./way3Data/uc_b_count_in_n.csv', index=False, encoding='utf-8')


#②uc_bi_count_in_n(用户-类别对在考察日前n天的各项行为计数	反映了user_id -item_category的活跃度，反映了user_id -item_category的各项操作的活跃度，对应着user_id -item_category的购买习惯)
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub.rename(columns={'type_1':'uc_b1_count_in_1', 'type_2':'uc_b2_count_in_1', 'type_3':'uc_b3_count_in_1', 'type_4':'uc_b4_count_in_1'}, inplace=True)
userSub = userSub.groupby(['user_id', 'item_category'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head())
uc_bi_count_in_1 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub.rename(columns={'type_1':'uc_b1_count_in_3', 'type_2':'uc_b2_count_in_3', 'type_3':'uc_b3_count_in_3', 'type_4':'uc_b4_count_in_3'}, inplace=True)
userSub = userSub.groupby(['user_id', 'item_category'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head())
uc_bi_count_in_3 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub.rename(columns={'type_1':'uc_b1_count_in_6', 'type_2':'uc_b2_count_in_6', 'type_3':'uc_b3_count_in_6', 'type_4':'uc_b4_count_in_6'}, inplace=True)
userSub = userSub.groupby(['user_id', 'item_category'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head())
uc_bi_count_in_6 = userSub.copy()

uc_bi_count_in_n = pd.merge(uc_bi_count_in_6, uc_bi_count_in_3, how='left').fillna(0)
uc_bi_count_in_n = pd.merge(uc_bi_count_in_n, uc_bi_count_in_1, how='left').fillna(0)
# print(uc_bi_count_in_n.info())
# print(uc_bi_count_in_n.head())
uc_bi_count_in_n.to_csv('./way3Data/uc_bi_count_in_n.csv', index=False, encoding='utf-8')

#③uc_bi_last_hours(用户-类别对各项行为上一次发生距考察日的时差	反映了user_id -item_category的活跃时间特征)
import datetime
def to_time(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%Y-%m-%d")
def to_hour(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%H:%M:%S")

userSub = userAll[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4', 'time_day', 'time_hour']]
userSub = userSub[userSub['time_day']<'2014-12-17']
userSub1 = userSub[['user_id', 'item_category', 'type_1', 'time_day', 'time_hour']]
userSub2 = userSub[['user_id', 'item_category', 'type_2', 'time_day', 'time_hour']]
userSub3 = userSub[['user_id', 'item_category', 'type_3', 'time_day', 'time_hour']]
userSub4 = userSub[['user_id', 'item_category', 'type_4', 'time_day', 'time_hour']]

userSub1 = userSub1.sort_values(['user_id', 'item_category', 'time_day', 'time_hour'])
userSub1 = userSub1.drop_duplicates(['user_id', 'item_category'], keep='last')
userSub1.insert(5, 'uc_b1_last_hours', (to_time('2014-12-17') - userSub1['time_day'].map(lambda x:to_time(x))).map(lambda x:((x.days)*24)).map(lambda x:int(x))
                + userSub1['time_hour'].map(lambda x:str(x)).map(lambda x:x[0:2]).map(lambda x:int(x)))   #计算浏览行为上一次发生距考察日(2014-12-17)的小时（hour）差
userSub1 = userSub1[['user_id', 'item_category', 'uc_b1_last_hours']]
# print(userSub1.info())
# print(userSub1.head())

userSub2 = userSub2.sort_values(['user_id', 'item_category', 'time_day', 'time_hour'])
userSub2 = userSub2.drop_duplicates(['user_id', 'item_category'], keep='last')
userSub2.insert(5, 'uc_b2_last_hours', (to_time('2014-12-17') - userSub2['time_day'].map(lambda x:to_time(x))).map(lambda x:((x.days)*24)).map(lambda x:int(x))
                + userSub2['time_hour'].map(lambda x:str(x)).map(lambda x:x[0:2]).map(lambda x:int(x)))   #计算浏览行为上一次发生距考察日(2014-12-17)的小时（hour）差
userSub2 = userSub2[['user_id', 'item_category', 'uc_b2_last_hours']]
# print(userSub2.info())
# print(userSub2.head())

userSub3 = userSub3.sort_values(['user_id', 'item_category', 'time_day', 'time_hour'])
userSub3 = userSub3.drop_duplicates(['user_id', 'item_category'], keep='last')
userSub3.insert(5, 'uc_b3_last_hours', (to_time('2014-12-17') - userSub3['time_day'].map(lambda x:to_time(x))).map(lambda x:((x.days)*24)).map(lambda x:int(x))
                + userSub3['time_hour'].map(lambda x:str(x)).map(lambda x:x[0:2]).map(lambda x:int(x)))   #计算浏览行为上一次发生距考察日(2014-12-17)的小时（hour）差
userSub3 = userSub3[['user_id', 'item_category', 'uc_b3_last_hours']]
# print(userSub3.info())
# print(userSub3.head())

userSub4 = userSub4.sort_values(['user_id', 'item_category', 'time_day', 'time_hour'])
userSub4 = userSub4.drop_duplicates(['user_id', 'item_category'], keep='last')
userSub4.insert(5, 'uc_b4_last_hours', (to_time('2014-12-17') - userSub4['time_day'].map(lambda x:to_time(x))).map(lambda x:((x.days)*24)).map(lambda x:int(x))
                + userSub4['time_hour'].map(lambda x:str(x)).map(lambda x:x[0:2]).map(lambda x:int(x)))   #计算浏览行为上一次发生距考察日(2014-12-17)的小时（hour）差
userSub4 = userSub4[['user_id', 'item_category', 'uc_b4_last_hours']]
# print(userSub4.info())
# print(userSub4.head())
uc_bi_last_hours = pd.merge(userSub4, userSub3, how='left')
uc_bi_last_hours = pd.merge(uc_bi_last_hours, userSub2, how='left')
uc_bi_last_hours = pd.merge(uc_bi_last_hours, userSub1, how='left')
# print(uc_bi_last_hours.info())
# print(uc_bi_last_hours.head())
uc_bi_last_hours.to_csv('./way3Data/uc_bi_last_hours.csv', index=False, encoding='utf-8')


#④uc_b_count_rank_in_n_in_u(用户-类别对的行为在用户所有商品中的排序  反映了user_id对item_category的行为偏好)
userSub = userAll[userAll['time_day'] == '2014-12-14']
userSub = userSub[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_category'], as_index=False).sum()
userSub['b_count'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
userSub['uc_b_count_rank_in_1_in_u'] = userSub['b_count'].groupby(userSub['user_id']).rank(ascending=0, method='dense')
userSub.drop('b_count', axis=1, inplace=True)
uc_b_count_rank_in_1_in_u = userSub.copy()
# print(uc_b_count_rank_in_1_in_u.info())
# print(uc_b_count_rank_in_1_in_u.head(20))

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_category'], as_index=False).sum()
userSub['b_count'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
userSub['uc_b_count_rank_in_3_in_u'] = userSub['b_count'].groupby(userSub['user_id']).rank(ascending=0, method='dense')
userSub.drop('b_count', axis=1, inplace=True)
uc_b_count_rank_in_3_in_u = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_category'], as_index=False).sum()
userSub['b_count'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
userSub['uc_b_count_rank_in_6_in_u'] = userSub['b_count'].groupby(userSub['user_id']).rank(ascending=0, method='dense')
userSub.drop('b_count', axis=1, inplace=True)
uc_b_count_rank_in_6_in_u = userSub.copy()

uc_b_count_rank_in_n_in_u = pd.merge(uc_b_count_rank_in_6_in_u, uc_b_count_rank_in_3_in_u, how='left', on=['user_id', 'item_category']).fillna(1000)   #没有的置为1000(没有竞争力的一个靠后排名)
uc_b_count_rank_in_n_in_u = pd.merge(uc_b_count_rank_in_n_in_u, uc_b_count_rank_in_1_in_u, how='left', on=['user_id', 'item_category']).fillna(1000)
uc_b_count_rank_in_n_in_u.to_csv('./way3Data/uc_b_count_rank_in_n_in_u.csv', index=False, encoding='utf-8')
# print(uc_b_count_rank_in_n_in_u.info())
# print(uc_b_count_rank_in_n_in_u.head())
