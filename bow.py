from sklearn.svm import LinearSVC
from sklearn.cross_validation import LeaveOneOut
from sklearn.metrics import classification_report, accuracy_score

import numpy as np

datafile = '/home/yzhu7/git/abstract/training.csv'
data = np.loadtxt(datafile, delimiter=',', skiprows=1)
X = data[:, 40:]
labels = data[:,:40].T.astype(np.int32)
y = labels[6]
loo = LeaveOneOut(y.shape[0])
clf = LinearSVC()
pp = np.array([(clf.fit(X[train], y[train]).predict(X[test])[0], y[test][0]) for train, test in loo]).T
print(classification_report(pp[1], pp[0]))
print accuracy_score(pp[1], pp[0])
