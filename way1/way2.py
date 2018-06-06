import pandas as pd
import numpy as np
user_behavior_file = './fresh_comp_offline/tianchi_fresh_comp_train_user.csv'    # 用户行为数据
item_file = './fresh_comp_offline/tianchi_fresh_comp_train_item.csv'
result_file = './fresh_comp_offline/result/tianchi_mobile_recommendation_predict.csv'   #商品数据

#step1:查看、处理user表格
#读取user表格数据
userAll = pd.read_csv(user_behavior_file, usecols=['user_id','item_id','behavior_type','time'], encoding='utf-8')
print(userAll.head())#显示前5行数据
print(userAll.info())#查看数据表相关信息
print(userAll.duplicated().sum())#检查有无重复行

#step2:查看、处理item子集表格
#读取item表格数据
itemSub = pd.read_csv(item_file, usecols=['item_id'], encoding='utf-8')
print(itemSub.item_id.is_unique) #查看子集中商品item编号是否有重复
print(itemSub.item_id.value_counts().head())#查看每个item_id有多少重复
print(itemSub.info())#查看商品表相关信息

itemSet = itemSub[['item_id']].drop_duplicates()#去除重复的行
print(itemSet.info())

#step3:取user与item子集上的交集
#由于预测user_item(哪些用户买了哪些商品)是在item子集上进行，因此，
# 可以自考虑user在这些商品子集上的交互行为，来预测user_item。
# 当然还可以用全部的user表格通过分析user在不同种类商品的交互行为，来预测user_item

# 合并两列, 默认方法是how=inner, 只合并相同的部分, how的取值可以为['left', 'right', 'outer', 'inner']
userSub = pd.merge(userAll, itemSet, on='item_id', how='inner')
print(userSub.info())
print(userSub.head())
userSub.to_csv('./way2Data/userSub.csv', index=False)#将该数据保存到csv文件里

#step4处理时间数据
#读取userSub，（先保存userSub,再读取userSub，是更换index为time的一种间接方法，
#此外，userSub作为我们作预测的主要数据集，是需要保存的。 ）
userSub = pd.read_csv('./way2Data/userSub.csv', usecols=['user_id','item_id','behavior_type','time'],parse_dates = True)
print(userSub.info())
print(userSub.head())
# userSub = userSub.set_index('time')#重置index
userSub = userSub.sort_index().copy()
print(userSub.index)
print(userSub.head())

#step5：进行特征处理
#特征处理包括两部分：
# ①将user-item(用户商品对)的交互行为进行哑变量编码
# ②设置时间窗口，提取交互行为的一段时间内统计量
print(pd.get_dummies(userSub['behavior_type'], prefix='type').head())#get_dummies是将拥有不同值的变量转换为0/1数值。
typeDummies = pd.get_dummies(userSub['behavior_type'], prefix='type')#onehot哑变量编码
print(userSub.info())
userSubOneHot = pd.concat([userSub[['user_id', 'item_id', 'time']], typeDummies], axis= 1)#可以将数据根据不同的轴作简单的融合

usertem = pd.concat([userSub[['user_id', 'item_id']], typeDummies, userSub[['time']]], axis=1)#将哑变量特征加入表中
print(usertem.head())
print(usertem.groupby(['time', 'user_id', 'item_id'], as_index=False).sum().head())#已将关键字排序，统计用户商品对的交互行为

print(userSubOneHot.head())
print(userSubOneHot.info())
userSubOneHotGroup = userSubOneHot.groupby(['time', 'user_id', 'item_id'], as_index=False).sum()#另外一种方法是在sum()后使用.reset_index()方法
print(userSubOneHotGroup.info())
print(userSubOneHotGroup.head())

#拆分天和小时
# time_day_Series = userSubOneHotGroup.time.map(lambda x:x.split(' ')[0])
# time_hour_Series = userSubOneHotGroup.time.map(lambda x:x.split(' ')[1])
userSubOneHotGroup['time_day'] = pd.to_datetime(userSubOneHotGroup.time.values).date
userSubOneHotGroup['time_hour'] = pd.to_datetime(userSubOneHotGroup.time.values).time
print(userSubOneHotGroup.head())
dataHour = userSubOneHotGroup.ix[:, 0:7]
print(dataHour.info())

#保存
dataHour.to_csv('./way2Data/dataHour.csv', encoding='utf-8')
print(dataHour.duplicated().sum())#检查重复行为0

dataDay = userSubOneHotGroup.groupby(['time_day', 'user_id', 'item_id'], as_index=False).sum()
print(dataDay.info())
print(dataDay.head())
#保存
dataDay.to_csv('./way2Data/dataDay.csv', encoding='utf-8')
print(dataDay.duplicated().sum())#计算出的重复行为0
print(dataDay.type_4.max())

#step6:构造训练测试数据集
#使用的采样频率为天的数据表，对每个用户商品对进行是否发生购买行为进行分类，发生购买行为分类标签为1，反之为0
dataDay_load = pd.read_csv('./way2Data/dataDay.csv', usecols= ['time_day','user_id','item_id','type_1', 'type_2','type_3','type_4'], index_col = 'time_day',parse_dates = True)
print(dataDay_load.head())
print(dataDay_load.info())

train_x = dataDay_load.ix['2014-12-16', :]  #16号选取特征数据
print(train_x.info())
print(train_x.describe())
train_y = dataDay_load.ix['2014-12-17', ['user_id', 'item_id', 'type_4']]#17号购买行为作为分类标签
print(train_y.info())
print(train_y.describe())

dataSet = pd.merge(train_x, train_y, on=['user_id', 'item_id'], suffixes=('_x', '_y'), how='left').fillna(0.0)#特征数据和标签数据构成训练数据集   suffixes(后缀)
print(dataSet.info())
print(dataSet.describe())
print(np.sign(dataSet.type_4_y.values).sum())# np.sign()功能就是大于0的返回1.0,小于0的返回-1.0,等于0的返回0.0

dataSet['labels'] = dataSet.type_4_y.map(lambda x:1.0 if x>0.0 else 0.0)
print(dataSet.info())
print(dataSet.head())

print(np.sign(dataSet.type_3.values).sum())#发生加购物车交互行为的用户商品对
trainSet = dataSet.copy()#重命名并保存训练数据集
trainSet.to_csv('./way2Data/train.csv')

test_x = dataDay_load.ix['2014-12-17', :]#17号特征数据集，作为测试输入数据集
test_y = dataDay_load.ix['2014-12-18', ['user_id', 'item_id', 'type_4']]#18号购买行为作为测试标签数据集
testSet = pd.merge(test_x, test_y, on=['user_id', 'item_id'], suffixes=('_x', '_y'), how='left').fillna(0.0)#构成测试数据集
print(testSet.info())
print(testSet.describe())
testSet['labels'] = testSet.type_4_y.map(lambda x:1.0 if x>0.0 else 0.0)
print(testSet.describe())
print(testSet.info())
print(testSet['labels'].values.sum())  #购买样例总数
testSet.to_csv('./way2Data/testSet.csv')

#step7:训练模型
#逻辑回归模型
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(trainSet.ix[:,2:6], trainSet[:, -1])
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
              intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
              penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
              verbose=0, warm_start=False)
print(model.score(trainSet.ix[:,2:6],trainSet.ix[:,-1]))