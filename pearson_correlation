import math
from collections import Counter
from sklearn.metrics import mean_squared_error
#import sys
#from compiler.ast import flatten

def buildVector(iterable1, iterable2):
    '''used for discovering text cosine similarity'''
    counter1 = Counter(iterable1)
    counter2= Counter(iterable2)
    all_items = set(counter1.keys()).union( set(counter2.keys()) )
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

def normalizer(matrix):
    counter=0
    normed_list=[]
    for i in matrix:
        for j in i:
            if j != 0:
                counter+=1
        average = float(sum(i))/counter if len(i) > 0 else float('nan')
        counter=0
        normed = [j - average if j != 0 else 0 for j in i]
        normed_list.append(normed)
    return normed_list


 
def cosim(v1, v2):
    dot_product = sum(n1 * n2 for n1,n2 in zip(v1, v2))
    magnitude1 = math.sqrt (sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt (sum(n ** 2 for n in v2))
    z = dot_product / (magnitude1 * magnitude2)
    return z


def cosim_finder(v_against, v_everything):
    cosim_storage = []
    counter = 0
    for i in v_everything:
        cosim_storage.append([counter, cosim(v_against, i)])
        counter += 1
    return cosim_storage
    
'''
m = (([4., 0, 0, 5., 1., 0, 0], 
      [5., 5., 4., 0, 0, 0, 0], 
      [0, 0, 0, 2., 4., 5., 0],
      [0, 3., 12, 0, 0, 0, 3.]))'''

m = (([1., 0, 3., 0, 0, 5., 0, 0, 5., 0, 4., 0],
      [0,0,5.,4.,0,0,4.,0,0,2.,1.,3],
      [2., 4., 0, 1., 2., 0, 3., 0, 4., 3., 5., 0],
      [0,2.,4.,0,5,0,0,4.,0,0,2.,0],
      [0, 0, 4., 3., 4., 2., 0, 0, 0, 0, 2., 5],
      [1., 0, 3., 0, 3., 0, 0, 2., 0, 0, 4., 0]
      ))


def rmse(actual, predicted):
    ''' This function is not used for collaborative filtering
        Sample usage
        predicted=[1,2,3,4]
        actual=[2,3,4,100]
        Output = 48                                             '''
    rmse = math.sqrt(mean_squared_error(actual, predicted))
    return rmse


def collab_filtering(x, y, m, sim_threshold=0.05):
    ''' 
    x and y are the positional points of the matrix of the interested value. For example in a 3 by 3 matrix, if you are interested
    in the first row and the second column, the x and y points of this matrix is (0,1)
    
    m is the actual matrix that needs to be inserted into this function
    
    the sim_threshold is the cosine similarity threshold. By default, the threshold is 5%
    
    sample usage is 
    print collab_filtering(3,3,m,0.001)
    '''
    num_list = []
    denom_list = []
    normed_m = normalizer(m)
    c = cosim_finder(normed_m[x], normed_m)
    for i in c:
        if i[1] >= sim_threshold and i[1] != 0 and i[0] != x:
            num_list.append((i[1])*(m[i[0]][y]))
            denom_list.append(i[1])
    result = (sum(num_list))/(sum(denom_list))
    return result




