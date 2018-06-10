import pandas as pd
#读取预处理数据
userAll = pd.read_csv('./way3Data/user_item_datetime_type.csv', encoding='utf-8')
userAll.drop_duplicates(inplace=True)

#构建UI类别特征
#①ui_b_count_in_n（用户-商品对在考察日前n天的行为总数计数	反映了user_id - item_id的活跃度）
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub[['user_id', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
# print(userSub.info())
userSub.insert(6, 'ui_b_count_in_1', value=userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4'])
userSub = userSub[['user_id', 'item_id', 'ui_b_count_in_1']]
userSub = userSub.groupby(['user_id', 'item_id'], as_index=False).sum()
ui_b_count_in_1 = userSub.copy()
# print(userSub.info())
# print(userSub.head(50))

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
# print(userSub.info())
userSub.insert(6, 'ui_b_count_in_3', value=userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4'])
userSub = userSub[['user_id', 'item_id', 'ui_b_count_in_3']]
userSub = userSub.groupby(['user_id', 'item_id'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head(50))
ui_b_count_in_3 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
# print(userSub.info())
userSub.insert(6, 'ui_b_count_in_6', value=userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4'])
userSub = userSub[['user_id', 'item_id', 'ui_b_count_in_6']]
userSub = userSub.groupby(['user_id', 'item_id'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head(50))
ui_b_count_in_6 = userSub.copy()

ui_b_count_in_n  = pd.merge(ui_b_count_in_6, ui_b_count_in_3, on=['user_id', 'item_id'], how='left').fillna(0)
ui_b_count_in_n  = pd.merge(ui_b_count_in_n, ui_b_count_in_1, on=['user_id', 'item_id'], how='left').fillna(0)
# print(ui_b_count_in_n.info())
# print(ui_b_count_in_n.head())
userSub.to_csv('./way3Data/ui_b_count_in_n.csv', index=False, encoding='utf-8')

#②ui_bi_count_in_n(用户-商品对在考察日前n天的各项行为计数
# 反映了user_id - item_id的活跃度，反映了user_id - item_id的各项操作的活跃度，对应着user_id - item_id的购买习惯)
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub[['user_id', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub.rename(columns={'type_1':'ui_b1_count_in_1', 'type_2':'ui_b2_count_in_1', 'type_3':'ui_b3_count_in_1', 'type_4':'ui_b4_count_in_1'}, inplace=True)
userSub = userSub.groupby(['user_id', 'item_id'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head(20))
# print(userSub.ui_b1_count_in_1.max())
# print(userSub.ui_b2_count_in_1.max())
# print(userSub.ui_b3_count_in_1.max())
# print(userSub.ui_b4_count_in_1.max())
ui_bi_count_in_1 = userSub.copy()


userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub.rename(columns={'type_1':'ui_b1_count_in_3', 'type_2':'ui_b2_count_in_3', 'type_3':'ui_b3_count_in_3', 'type_4':'ui_b4_count_in_3'}, inplace=True)
userSub = userSub.groupby(['user_id', 'item_id'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head(20))
# print(userSub.ui_b1_count_in_3.max())
# print(userSub.ui_b2_count_in_3.max())
# print(userSub.ui_b3_count_in_3.max())
# print(userSub.ui_b4_count_in_3.max())
ui_bi_count_in_3 = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub.rename(columns={'type_1':'ui_b1_count_in_6', 'type_2':'ui_b2_count_in_6', 'type_3':'ui_b3_count_in_6', 'type_4':'ui_b4_count_in_6'}, inplace=True)
userSub = userSub.groupby(['user_id', 'item_id'], as_index=False).sum()
# print(userSub.info())
# print(userSub.head(20))
# print(userSub.ui_b1_count_in_6.max())
# print(userSub.ui_b2_count_in_6.max())
# print(userSub.ui_b3_count_in_6.max())
# print(userSub.ui_b4_count_in_6.max())
ui_bi_count_in_6 = userSub.copy()

ui_bi_count_in_n = pd.merge(ui_bi_count_in_6, ui_bi_count_in_3, on=['user_id', 'item_id'], how='left').fillna(0)
ui_bi_count_in_n = pd.merge(ui_bi_count_in_n, ui_bi_count_in_1, on=['user_id', 'item_id'], how='left').fillna(0)
# print(ui_bi_count_in_n.info())
# print(ui_bi_count_in_n.head())
ui_bi_count_in_n.to_csv('./way3Data/ui_bi_count_in_n.csv', index=False, encoding='utf-8')

#③ui_bi_last_hours(用户-商品对各项行为上一次发生距考察日(2014-12-17)的时差	反映了user_id - item_id的活跃时间特征)
import datetime
def to_time(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%Y-%m-%d")
def to_hour(string):
    string = str(string)
    return datetime.datetime.strptime(string, "%H:%M:%S")


userSub = userAll.copy()
userSub = userSub[userSub['time_day']<'2014-12-17']
# print(userSub[userSub['time_day'] == '2014-12-17'])
userSub1 = userSub[['user_id', 'item_id', 'type_1', 'time_day', 'time_hour']]
userSub2 = userSub[['user_id', 'item_id', 'type_2', 'time_day', 'time_hour']]
userSub3 = userSub[['user_id', 'item_id', 'type_3', 'time_day', 'time_hour']]
userSub4 = userSub[['user_id', 'item_id', 'type_4', 'time_day', 'time_hour']]

userSub1 = userSub1.sort_values(['user_id', 'item_id', 'time_day', 'time_hour'])
# print(userSub1.head(20))
userSub1 = userSub1.drop_duplicates(['user_id', 'item_id'], keep='last')
# print(userSub1.head(20))
userSub1.insert(5, 'ui_b1_last_hours', (to_time('2014-12-17') - userSub1['time_day'].map(lambda x:to_time(x))).map(lambda x:((x.days)*24)).map(lambda x:int(x))
                + userSub1['time_hour'].map(lambda x:str(x)).map(lambda x:x[0:2]).map(lambda x:int(x)))   #计算浏览行为上一次发生距考察日(2014-12-17)的小时（hour）差
# print(userSub1.info())
# print(userSub1.head(20))
# print(userSub1.ui_b1_last_hours.max())
userSub1 = userSub1[['user_id', 'item_id', 'ui_b1_last_hours']]


userSub2 = userSub2.sort_values(['user_id', 'item_id', 'time_day', 'time_hour'])
userSub2 = userSub2.drop_duplicates(['user_id', 'item_id'], keep='last')
# print(userSub1.head(20))
userSub2.insert(5, 'ui_b2_last_hours', (to_time('2014-12-17') - userSub2['time_day'].map(lambda x:to_time(x))).map(lambda x:((x.days)*24)).map(lambda x:int(x))
                + userSub2['time_hour'].map(lambda x:str(x)).map(lambda x:x[0:2]).map(lambda x:int(x)))   #计算浏览行为上一次发生距考察日(2014-12-17)的小时（hour）差
userSub2 = userSub2[['user_id', 'item_id', 'ui_b2_last_hours']]
# print(userSub2.info())
# print(userSub2.head())
# print(userSub2.ui_b2_last_hours.max())


userSub3 = userSub3.sort_values(['user_id', 'item_id', 'time_day', 'time_hour'])
userSub3 = userSub3.drop_duplicates(['user_id', 'item_id'], keep='last')
# print(userSub1.head(20))
userSub3.insert(5, 'ui_b3_last_hours', (to_time('2014-12-17') - userSub3['time_day'].map(lambda x:to_time(x))).map(lambda x:((x.days)*24)).map(lambda x:int(x))
                + userSub3['time_hour'].map(lambda x:str(x)).map(lambda x:x[0:2]).map(lambda x:int(x)))   #计算浏览行为上一次发生距考察日(2014-12-17)的小时（hour）差
userSub3 = userSub3[['user_id', 'item_id', 'ui_b3_last_hours']]
# print(userSub3.info())
# print(userSub3.head())
# print(userSub3.ui_b3_last_hours.max())


userSub4 = userSub4.sort_values(['user_id', 'item_id', 'time_day', 'time_hour'])
userSub4 = userSub4.drop_duplicates(['user_id', 'item_id'], keep='last')
# print(userSub1.head(20))
userSub4.insert(5, 'ui_b4_last_hours', (to_time('2014-12-17') - userSub4['time_day'].map(lambda x:to_time(x))).map(lambda x:((x.days)*24)).map(lambda x:int(x))
                + userSub4['time_hour'].map(lambda x:str(x)).map(lambda x:x[0:2]).map(lambda x:int(x)))   #计算浏览行为上一次发生距考察日(2014-12-17)的小时（hour）差

# print(userSub4[userSub4['ui_b4_last_hours'] == -24])

userSub4 = userSub4[['user_id', 'item_id', 'ui_b4_last_hours']]
# print(userSub4.info())
# print(userSub4.head())
# print(userSub4.ui_b4_last_hours.max())

ui_bi_last_hours = pd.merge(userSub1, userSub2, how='left')
ui_bi_last_hours = pd.merge(ui_bi_last_hours, userSub3, how='left')
ui_bi_last_hours = pd.merge(ui_bi_last_hours, userSub4, how='left')
# print(ui_bi_last_hours.info())
# print(ui_bi_last_hours.head())
# print(ui_bi_last_hours.ui_b4_last_hours.min())    #24
ui_bi_last_hours.to_csv('./way3Data/ui_bi_last_hours.csv', index=False, encoding='utf-8')

#④ui_b_count_rank_in_n_in_u(用户商品对的行为在用户所有商品中的排序	反映了user_id对item_id的行为偏好)
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub[['user_id', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id'], as_index=False).sum()
userSub['b_count'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
# print(userSub.info())
# print(userSub.head())
# print(userSub.b_count.max())
userSub['ui_b_count_rank_in_1_in_u'] = userSub['b_count'].groupby(userSub['user_id']).rank(ascending=0, method='dense')
# print(userSub.ui_b_count_rank_in_1_in_u.max())
userSub.drop('b_count', axis=1, inplace=True)
ui_b_count_rank_in_1_in_u = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id'], as_index=False).sum()
userSub['b_count'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
userSub['ui_b_count_rank_in_3_in_u'] = userSub['b_count'].groupby(userSub['user_id']).rank(ascending=0, method='dense')
userSub.drop('b_count', axis=1, inplace=True)
# print(userSub.info())
# print(userSub.head())
# print(userSub.ui_b_count_rank_in_3_in_u.max())
ui_b_count_rank_in_3_in_u = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_id'], as_index=False).sum()
userSub['b_count'] = userSub['type_1'] + userSub['type_2'] + userSub['type_3'] + userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
userSub['ui_b_count_rank_in_6_in_u'] = userSub['b_count'].groupby(userSub['user_id']).rank(ascending=0, method='dense')
userSub.drop('b_count', axis=1, inplace=True)
# print(userSub.info())
# print(userSub.head())
# print(userSub.ui_b_count_rank_in_6_in_u.max())
ui_b_count_rank_in_6_in_u = userSub.copy()

ui_b_count_rank_in_n_in_u = pd.merge(ui_b_count_rank_in_6_in_u, ui_b_count_rank_in_3_in_u, how='left', on=['user_id', 'item_id']).fillna(1000)   #没有的置为1000(没有竞争力的一个靠后排名)
ui_b_count_rank_in_n_in_u = pd.merge(ui_b_count_rank_in_n_in_u, ui_b_count_rank_in_1_in_u, how='left', on=['user_id', 'item_id']).fillna(1000)
# print(ui_b_count_rank_in_n_in_u.info())
# print(ui_b_count_rank_in_n_in_u.head())
ui_b_count_rank_in_n_in_u.to_csv('./way3Data/ui_b_count_rank_in_n_in_u.csv', index=False, encoding='utf-8')


#⑤ui_b_count_rank_in_n_in_uc(用户-商品对的行为在用户-类别对中的排序  反映了user_id对item_category中的各个item_id的行为偏好)
userSub = userAll[userAll['time_day'] == '2014-12-16']
userSub = userSub[['user_id', 'item_category', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_category', 'item_id'], as_index=False).sum()
userSub['b_count'] = userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
userSub = userSub.sort_values(by=['user_id', 'item_category'])
# print(userSub.info())
# print(userSub.head())
# print(userSub.b_count.max())
userSub['ui_b_count_rank_in_1_in_uc'] = userSub['b_count'].groupby(userSub['user_id'] & userSub['item_category']).rank(ascending=0, method='dense')
userSub.drop('b_count', axis=1, inplace=True)
# print(userSub.info())
# print(userSub.head(20))
ui_b_count_rank_in_1_in_uc = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-13') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_category', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_category', 'item_id'], as_index=False).sum()
userSub['b_count'] = userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
userSub = userSub.sort_values(by=['user_id', 'item_category'])
userSub['ui_b_count_rank_in_3_in_uc'] = userSub['b_count'].groupby(userSub['user_id'] & userSub['item_category']).rank(ascending=0, method='dense')
userSub.drop('b_count', axis=1, inplace=True)
# print(userSub.info())
# print(userSub.head(20))
ui_b_count_rank_in_3_in_uc = userSub.copy()

userSub = userAll[(userAll['time_day'] > '2014-12-10') & (userAll['time_day'] < '2014-12-17')]
userSub = userSub[['user_id', 'item_category', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
userSub = userSub.groupby(['user_id', 'item_category', 'item_id'], as_index=False).sum()
userSub['b_count'] = userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4']
userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1, inplace=True)
userSub = userSub.sort_values(by=['user_id', 'item_category'])
userSub['ui_b_count_rank_in_6_in_uc'] = userSub['b_count'].groupby(userSub['user_id'] & userSub['item_category']).rank(ascending=0, method='dense')
userSub.drop('b_count', axis=1, inplace=True)
# print(userSub.info())
# print(userSub.head(20))
ui_b_count_rank_in_6_in_uc = userSub.copy()

ui_b_count_rank_in_n_in_uc = pd.merge(ui_b_count_rank_in_6_in_uc, ui_b_count_rank_in_3_in_uc, how='left').fillna(1000)
ui_b_count_rank_in_n_in_uc = pd.merge(ui_b_count_rank_in_n_in_uc, ui_b_count_rank_in_1_in_uc, how='left').fillna(1000)
# print(ui_b_count_rank_in_n_in_uc.info())
# print(ui_b_count_rank_in_n_in_uc.head(20))
ui_b_count_rank_in_n_in_uc.to_csv('./way3Data/ui_b_count_rank_in_n_in_uc.csv', index=False, encoding='utf-8')
