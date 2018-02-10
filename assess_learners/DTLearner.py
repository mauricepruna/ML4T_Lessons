"""
A simple wrapper for linear regression.  (c) 2015 Tucker Balch
"""

import numpy as np


class DTLearner(object):
    def __init__(self, leaf_size, verbose):

        self.leaf_size = leaf_size
        self.verbose = verbose

    def author(self):
        return 'mpruna3'  # replace tb34 with your Georgia Tech username

    def addEvidence(self, dataX, dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
        if(self.verbose):
            print "dataX: {0}".format(dataX)
            print "dataY: {0}".format(dataY)
        # build and save the model
        self.model_coefs = self.build_tree(dataX, dataY)
        if (self.verbose):
            print "model_coefs: {0}".format(self.model_coefs)
        return self.model_coefs

    def build_tree(self, dataX, dataY):
        if (dataX.shape[0] == 1): return np.array([-1, dataY[0], np.nan, np.nan])
        elif ((dataY == dataY[0]).all()):
            return np.array([-1, dataY[0], np.nan, np.nan])
        else:
            best_factor = self.best_feature(dataX, dataY)
            split_val = np.median(dataX[:, best_factor])
            left_tree = self.build_tree(dataX[dataX[:, best_factor] <= split_val],
                                         dataY[dataX[:, best_factor] <= split_val])
            right_tree = self.build_tree(dataX[dataX[:, best_factor] > split_val],
                                          dataY[dataX[:, best_factor] > split_val])
            root = np.array([best_factor, split_val, 1, left_tree.shape[0] + 1])
            if (self.verbose):
                print "root.shape: {0}".format(root.shape)
                print "left.shape: {0}".format(left_tree.shape)
                print "right.shape: {0}".format(right_tree.shape)
            temp_arr = np.row_stack((root,left_tree))
            result_arr = np.row_stack((temp_arr,right_tree))
            return result_arr

    def best_feature(self,dataX,dataY):
        best_factor=np.array([0,0.0])
        idx = 0
        dataT = dataX.T
        for column in dataT:
            if((column == column[0]).all()): correlation = 0
            else:
                correlation = np.corrcoef(column, dataY)[1,0]
            abs_corr = np.absolute(correlation)
            if(abs_corr>best_factor[1]):
                best_factor[0]= idx
                best_factor[1] = abs_corr
            idx=idx+1
        return (int(best_factor[0]))

    def query(self, points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        # return (self.model_coefs[:-1] * points).sum(axis=1) + self.model_coefs[-1]
        i = 0
        if (self.verbose):
            print "points: {0}".format(points)
        sh = points.shape[0]
        result = np.empty([sh])  # create an empty array
        while i < sh:
            arrayIndex = 0
            while not np.isnan(self.model_coefs[arrayIndex, -1]):  # checks if the row in "decision tree" array is a leaf
                val = self.model_coefs[arrayIndex, 1]  # finds the split value
                if points[i, int(self.model_coefs[
                                     arrayIndex, 0])] <= val:  # compares the split value of the feature with the value of the same feature in test set
                    arrayIndex = arrayIndex + 1  # goes to the right ree
                else:
                    arrayIndex = arrayIndex + int(self.model_coefs[arrayIndex, -1])  # goes to the left tree
            value = self.model_coefs[arrayIndex, 1]
            result[i] = value
            i = i + 1
        return result


if __name__ == "__main__":
    print "the secret clue is 'zzyzx'"
