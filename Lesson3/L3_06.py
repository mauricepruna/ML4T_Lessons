"""Creating NumPy arrays"""
import numpy as np

def test_run():
    #List to 1D array
    # print np.array([(2,3,4),(5,6,7)])

    #Empty array
    # print np.empty(5)
    # print np.empty((5,4))

    #Arrays of 1s
    # print np.ones((5,4), dtype="int8")

    #Random
    a = np.random.random((5,4))
    print a
    print a.shape
    print a.shape[0]#rows 5
    print a.shape[1]#columns 4
    print len(a.shape)#dimensions 2
    print a.size#number of values (20)
    print a.dtype#type (float64)


    # print np.random.rand(5,4)

    #Normal distribution. Default (mean=0, s.d.=1)
    # print np.random.normal(50,10, size=(2,3))

    #Random integers
    # print "Single int"
    # print np.random.randint(10) # Single int
    # print "Single int with low,high"
    # print np.random.randint(0,10)  # Single int with low,high
    # print "5 random ints"
    # print np.random.randint(0,10, size=5)  # 5 random ints
    # print "2x3 array of random integers"
    # print np.random.randint(10, size=(2,3))  # 2x3 array of random integers

if __name__=="__main__":
    test_run()