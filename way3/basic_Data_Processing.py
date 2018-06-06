import pandas as pd
import numpy as np

user_behavior_file = '../fresh_comp_offline/tianchi_fresh_comp_train_user.csv'
item_file = '../fresh_comp_offline/tianchi_fresh_comp_train_item.csv'

#step1:查看、处理user表格
userAll = pd.read_csv(user_behavior_file, usecols=['user_id','item_id','behavior_type','time'], encoding='utf-8')
# print(userAll.head())
# print(userAll.info())
# print(userAll.duplicated().sum())   #11505107

#step2:查看、处理item子集表格
itemSub = pd.read_csv(item_file, usecols=['item_id', 'item_category'], encoding='utf-8')
# print(itemSub.item_id.is_unique)  #False
# print(itemSub.item_id.value_counts().head())
# print(itemSub.info())
itemSet = itemSub[['item_id', 'item_category']].drop_duplicates()
# print(itemSet.info())

#step3:取user与item子集的交集
userSub = pd.merge(userAll, itemSet, how='inner') #on 用于连接的列名，必须同时存在于左右两个DataFrame对象中，如果未指定，则以left和right列名的交集作为连接键
userSub.to_csv('./way3Data/user_item_category.csv', index=False, encoding='utf-8')
# print(userSub.info()) #Int64Index: 2084859 entries, 0 to 2084858  memory usage: 95.4+ MB
# print(userSub.head())

#step4:处理时间数据
userSub = pd.read_csv('./way3Data/user_item_category.csv', usecols=['user_id','item_id', 'item_category', 'behavior_type', 'time'], encoding='utf-8', parse_dates=True)
# print(userSub.info())
# print(userSub.head())
userSub['time_day'] = pd.to_datetime(userSub.time.values).date
userSub['time_hour'] = pd.to_datetime(userSub.time.values).time
# print(userSub.info())
userSub.drop('time', axis=1, inplace=True)
# print(userSub.info())
# print(userSub.head())
userSub.to_csv('./way3Data/user_item_category_datetime.csv', index=False, encoding='utf-8')#将datetime列拆开并保存

#step5:将交互行为进行哑变量编码
typeDummies = pd.get_dummies(userSub['behavior_type'], prefix='type')  #onehot哑变量编码
userSub = pd.concat([userSub, typeDummies], axis=1)#将哑变量特征加入到表中
# print(userSub.info())
# print(userSub.head())
userSub.drop('behavior_type', axis=1, inplace=True)
userSub = userSub[['user_id', 'item_id', 'item_category', 'type_1', 'type_2', 'type_3', 'type_4', 'time_day', 'time_hour']]#调整dataframe列顺序
# print(userSub.info())
# print(userSub.head())
userSub.to_csv('./way3Data/user_item_datetime_type.csv', index=False, encoding='utf-8')#将behavior列进行哑变量编码处理并保存

