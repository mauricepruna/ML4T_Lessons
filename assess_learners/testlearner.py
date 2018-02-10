"""
Test a learner.  (c) 2015 Tucker Balch
"""

import numpy as np
import math
import LinRegLearner as lrl
import DTLearner as dtl
import RTLearner as rtl
import BagLearner as bl
import sys

if __name__=="__main__":
    # if len(sys.argv) != 2:
    #     print "Usage: python testlearner.py <filename>"
    #     sys.exit(1)
    # inf = open(sys.argv[1])
    # data = np.array([map(float,s.strip().split(',')) for s in inf.readlines()])

    # data = np.array([[0.885,	0.330,	9.100,  4.000],
    #           [0.725,	0.390,	10.900, 5.000],
    #           [0.560,	0.500,	9.400,  6.000],
    #           [0.735,	0.570,	9.800,  5.000],
    #           [0.610,	0.630,	8.400,  3.000],
    #           [0.260,	0.630,	11.800, 8.000],
    #           [0.500,	0.680,	10.500, 7.000],
    #           [0.320,	0.780,	10.000, 6.000]
    #           ])

    data = np.array([
        [0.61, 0.63, 8.4, 3],
        [0.885, 0.33, 9.1, 4],
        [0.56, 0.5, 9.4, 6],
        [0.735, 0.57, 9.8, 5],
        [0.32, 0.78, 10, 6],
        [0.26, 0.63, 11.8, 8],
        [0.5, 0.68, 10.5, 7],
        [0.725, 0.39, 10.9, 5],
    ])
    # compute how much of the data is training and testing
    train_rows = int(0.6* data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    trainX = data[:train_rows,0:-1]
    trainY = data[:train_rows,-1]
    testX = data[train_rows:,0:-1]
    testY = data[train_rows:,-1]

    print testX.shape
    print testY.shape

    # create a learner and train it
    learner = lrl.LinRegLearner(verbose = True) # create a LinRegLearner
    # learner = dtl.DTLearner(leaf_size=1, verbose=True)
    # learner = rtl.RTLearner(leaf_size=1, verbose=True)
    # learner = bl.BagLearner(learner=dtl.DTLearner, kwars={"leaf_size":1}, bags=20, boost=False, verbose=False)
    learner.addEvidence(trainX, trainY) # train it
    print learner.author()

    # evaluate in sample
    predY = learner.query(trainX) # get the predictions
    rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
    print
    print "In sample results"
    print "RMSE: ", rmse
    c = np.corrcoef(predY, y=trainY)
    print "corr: ", c[0,1]

    # evaluate out of sample
    predY = learner.query(testX) # get the predictions
    rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
    print
    print "Out of sample results"
    print "RMSE: ", rmse
    c = np.corrcoef(predY, y=testY)
    print "corr: ", c[0,1]



