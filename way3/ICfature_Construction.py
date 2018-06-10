import pandas as pd
#读取预处理数据
userAll = pd.read_csv('./way3Data/user_item_datetime_type.csv', encoding='utf-8')
# print(userAll.info())
userAll.drop_duplicates(inplace=True)
# print(userAll.info())
#构建IC类别特征
#①ic_u_rank_in_c(商品在所属类别中的用户人数排序	反映了item_id在item_category中的热度排名（用户覆盖性）)
#相同用户多次购买同一类产品,多次计数
userSub = userAll[['item_category', 'item_id']]
# print(userSub.info())
# print(userSub.head())
userSub.insert(2, 'user_count', value=1)
# userSub.loc[:, 'user_count'] = 1
userSub = userSub.groupby(['item_category', 'item_id'], as_index=False).sum()
userSub = userSub.sort_values(by=['item_category', 'item_id'])
# print(userSub.info())
# print(userSub.head())
# print(userSub.user_count.max())
userSub.loc[:, 'ic_u_rank_in_c'] = userSub['user_count'].groupby(userSub['item_category']).rank(ascending=0, method='dense')
userSub.drop('user_count', axis=1, inplace=True)
# print(userSub.info())
# print(userSub.head(30))
userSub.to_csv('./way3Data/ic_u_rank_in_c.csv', index=False, encoding='utf-8')

#②ic_b_rank_in_c(商品在所属类别中的行为总数排序	反映了item_id在item_category中的热度排名（用户停留性）)
userSub = userAll[['item_category', 'item_id', 'type_1', 'type_2', 'type_3', 'type_4']]
# print(userSub.info())
# print(userSub.head())
userSub.insert(6, 'b_count', value=userSub['type_1']+userSub['type_2']+userSub['type_3']+userSub['type_4'])
# print(userSub.info())
# print(userSub.head())
userSub = userSub.drop(['type_1', 'type_2', 'type_3', 'type_4'], axis=1)
# print(userSub.head())
userSub = userSub.groupby(['item_category', 'item_id'], as_index=False).sum()
# print(userSub.head(50))
# print(userSub.b_count.max())
userSub['ic_b_rank_in_c'] = userSub['b_count'].groupby(userSub['item_category']).rank(ascending=0, method='dense')
# print(userSub.head(30))
userSub.drop(['b_count'], axis = 1, inplace=True)
userSub.to_csv('./way3Data/ic_b_rank_in_c.csv', index=False, encoding='utf-8')

#③ic_b4_rank_in_c(商品在所属类别中的销量排序	反映了item_id在item_category中的热度排名（销量）)
userSub = userAll[['item_category', 'item_id', 'type_4']]
userSub = userSub.groupby(['item_category', 'item_id'], as_index=False).sum()
userSub['ic_b4_rank_in_c'] = userSub['type_4'].groupby(userSub['item_category']).rank(ascending=0, method='dense')
# print(userSub.info())
# print(userSub.head())
# print(userSub.type_4.max())
userSub.drop('type_4', axis=1, inplace=True)
userSub.to_csv('./way3Data/ic_b4_rank_in_c.csv', index=False, encoding='utf-8')