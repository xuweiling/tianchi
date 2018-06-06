import pandas as pd
#读取预处理数据
userAll = pd.read_csv('./way3Data/user_item_datetime_type.csv', encoding='utf-8')
userAll.drop_duplicates(inplace=True)

#构建IC类别特征
#①ic_u_rank_in_c(商品在所属类别中的用户人数排序	反映了item_id在item_category中的热度排名（用户覆盖性）)
#相同用户多次购买同一类产品,多次计数
userSub = userAll[['item_category', 'item_id']]
# print(userSub.info())
# print(userSub.head())
userSub.loc[:, 'user_count'] = 1
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

#