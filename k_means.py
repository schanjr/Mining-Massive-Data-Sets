import sklearn.cluster as skc
import numpy as np


pts = np.array([[25.,125.], [44.,105.], [29.,97.], [35.,63.], [55.,63.], [42.,57.], [23.,40.], [64.,37.], [33.,22.], [55.,20.], [28.,145.], [65.,140.], [50.,130.], [38.,115.], [55.,118.], [50.,90.], [63.,88.], [43.,83.], [50.,60.], [50.,30.]])
inits = np.array([[25.,125.], [44.,105.], [29.,97.], [35.,63.], [55.,63.], [42.,57.], [23.,40.], [64.,37.], [33.,22.], [55.,20.]])

#inits = np.array([[5.,10.],[20.,5.]])
#pts1 = np.array([[6.,7.],[11.,4.],[11.,5.],[17.,2.]])
#pts2 = np.array([[7.,8.],[12.,5.],[15.,14.],[20.,10.]])
#pts3 = np.array([[6.,15.],[13.,7.],[16.,16.],[18.,5.]])
#pts4 = np.array([[6.,7.],[11.,4.],[14.,10.],[23.,6.]])


a = skc.k_means(pts, 10, init=inits, precompute_distances=True, n_init=10, max_iter=300, verbose=True, tol=True, copy_x=False)
'''This algorithm works pretty well already, I don't need to write my own! :)'''


print a 


