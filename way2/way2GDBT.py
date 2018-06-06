import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
trainSet = pd.read_csv('./way2Data/train.csv')
testSet = pd.read_csv('./way2Data/testSet.csv')
gbdt = GradientBoostingClassifier(random_state=10)
gbdt.fit(trainSet.ix[:, 2:6], trainSet.ix[:, -1])
trainGBDT_y = gbdt.predict(trainSet.ix[:, 2:6])
print(trainGBDT_y.sum())
print(gbdt.score(trainSet.ix[:, 2:6], trainSet.ix[:, -1]))#0.996753139184

#计算精准率和召回率
from sklearn.model_selection import train_test_split, cross_val_score
#精准率
precision = cross_val_score(gbdt, trainSet.ix[:, 2:6], trainSet.ix[:, -1], cv=5, scoring='precision')
print('精确度：', np.mean(precision))
#召回率
recalls = cross_val_score(gbdt, trainSet.ix[:, 2:6], trainSet.ix[:, -1], cv=5, scoring='recall')
print('召回率：', np.mean(recalls))
#计算综合指标f1
f1 = cross_val_score(gbdt, trainSet.ix[:, 2:6], trainSet.ix[:, -1], cv=5, scoring='f1')
print('得分：', np.mean(f1))

#计算测试f1得分
# testLRW_y = gbdt.predict(test_x.ix[:, 2:6])
precision_test = cross_val_score(gbdt, testSet.ix[:, 2:6], testSet.ix[:, -1], cv=5, scoring='precision')
recall_test = cross_val_score(gbdt, testSet.ix[:, 2:6], testSet.ix[:, -1], cv=5, scoring='recall')
f1_test = cross_val_score(gbdt, testSet.ix[:, 2:6], testSet.ix[:, -1], cv=5, scoring='f1')
print('f1得分：', np.mean(f1_test))  #f1得分： 0.0125