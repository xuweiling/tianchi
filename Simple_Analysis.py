import pandas as pd
user_behavior_file = './fresh_comp_offline/tianchi_fresh_comp_train_user.csv'    # 用户行为数据
result_file = './fresh_comp_offline/result/tianchi_mobile_recommendation_predict.csv'   #商品数据

###
#① 前一天加入购物车的东西很有可能第二天就被购买，所以筛选出
#用户行为表中 time匹配‘2014-12-08%’并且behavior=3的记录
###

user_behavior_data = pd.read_csv(user_behavior_file, encoding='utf-8')      #读取数据
str1 = '3'
str2 = '2014-12-08%'

# for column in user_behavior_data:
#     print(column)
#列名：user_id、item_id、behavior_type、user_geohash、item_category、time

result_data = user_behavior_data
index1 = user_behavior_data['time'].between('2014-12-08 00', '2014-12-08 24')    #筛选日期
index2 = user_behavior_data['behavior_type'].between(2, 4, False)     #筛选行为类型
result_data = user_behavior_data[index1 & index2]

result_data = result_data.iloc[:, [0, 1]]    #选取符合要求的user_id 和 item_id两列数据
# print(result_data.count)     #1207行2列
result_data = result_data.drop_duplicates()  #去重
# print(result_data.count)    #1133行2列


result_data.to_csv(result_file, index=False, encoding='utf-8')     #按照要求保存
