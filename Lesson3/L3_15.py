"""Locate maximum value."""

import numpy as np



def test_run():
    # a = np.random.rand(5,4)
    # print "Array:\n",a
    #
    # #Slicing
    # #Note: Slice n:m:t specifies a range that starts at n, and stops before m, in
    # print a[:2,0:3:2]


    #Look for indices
    # np.random.seed(5)
    # a = np.random.rand(5)
    # indices  = np.array((1,1,2,3))
    # print a
    # print a[indices]

    #Masking
    # a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    # print a
    # mean = a.mean()
    # print mean
    # #masking
    # a[a<mean] = mean
    # print a

    # Arithmetic operations
    a = np.array([(1,2,3,4,5), (10,20,30,40,50)])
    print a
    # Multiply by 2
    a = 2*a
    print a





if __name__ == "__main__":
    test_run()
