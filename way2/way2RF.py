from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
trainSet = pd.read_csv('./way2Data/train.csv')
testSet = pd.read_csv('./way2Data/testSet.csv')
rf = RandomForestClassifier()
rf.fit(trainSet.ix[:, 2:6], trainSet.ix[:, -1])
trainRF_y = rf.predict(trainSet.ix[:, 2:6])
print(rf.score(trainSet.ix[:, 2:6], trainSet.ix[:, -1]))#0.998442832058
print(trainRF_y.sum())
print(trainRF_y)

#计算精准率和召回率
from sklearn.model_selection import train_test_split, cross_val_score
#计算测试f1得分
# testLRW_y = gbdt.predict(test_x.ix[:, 2:6])
precision_test = cross_val_score(rf, testSet.ix[:, 2:6], testSet.ix[:, -1], cv=5, scoring='precision')
print('precision_test:',precision_test)
recall_test = cross_val_score(rf, testSet.ix[:, 2:6], testSet.ix[:, -1], cv=5, scoring='recall')
print('recall_test:', recall_test)
f1_test = cross_val_score(rf, testSet.ix[:, 2:6], testSet.ix[:, -1], cv=5, scoring='f1')
print('f1得分：', np.mean(f1_test))   #f1得分： 0.0205669083718
