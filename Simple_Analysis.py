import pandas as pd
user_behavior_file = './fresh_comp_offline/tianchi_fresh_comp_train_user.csv'    # 用户行为数据
result_file = './fresh_comp_offline/tianchi_mobile_recommendation_predict.csv'   #商品数据

user_behavior_data = pd.read_csv(user_behavior_file, encoding='utf-8')      #读取数据
index1 = user_behavior_data['behavior_type'].equals(u'3')
index2 = user_behavior_data['time'].equals(u'2014-12-08%')

result_data = user_behavior_data[index1 and index2]