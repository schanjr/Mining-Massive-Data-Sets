import numpy
from compiler.ast import flatten
from collections import defaultdict

'''page_rank
This is an ongoing improvement page_rank algorithm that will eventually be scalable

Matrix Parameter For example there are only 2 web pages. Web page A, and B. Let's say

A--->B

So the PR(B)=PR(A)/2 According to the formula PR(B)=SUM of (1/(N of links pointing elsewhere)

Please refer to http://en.wikipedia.org/wiki/PageRank

So the Matrix Parameter should be entered like this: [0, 0, 0, 1]

Which really came from this

PR(A)=[0,0]

PR(B)=[0,1]

A six page example can be found here: http://people.revoledu.com/kardi/tutorial/PageRank/Images/Page-Rank-Numerical-Example_clip_image006.gif For every sum of the corresponding row is the page rank of the page.

Typically matrix is supposed to be stochastic. So hopefully your matrix does not have "Dead ends or Spider Traps" but this script has the teleport algorithm embedded as well.

Nodes Parameter

Using the example above, if you have web pages A and B, then you have 2 nodes.

Beta Parameter

This is the "Damper". I call it beta. Default value is 0.85 if not entered.

Epsilon Parameter

This is the differnce of previous and the current iteration. If you want to have more accurancy of page rank computation, make this a small number. (For example 0.0000000000000001)

Period

This is the number of iterations you want the function to go through.

Either Epsilon or Period needs to be entered. Otherwise the script will not start. '''


def page_rank(matrix, nodes, beta=0.85, epsilon=None, period=None):

    #input parameters-for testing
    #matrix=[1./2,1./2,0,1./2,0,0,0,1./2,1]
    #beta=0.8
    #nodes=3
    #epsilon=0.0001
    
    t=0
    #comprehensions
    
    teleport_matrix=[]
    teleport_matrix=[((1-beta)*1.0/nodes) for i in (range(nodes)*nodes)]
    flatten(matrix)
    matrix=[(float(i)*beta) for i in matrix]
    
    alpha=[(i+j) for i,j in zip(matrix,teleport_matrix)]
    alpha_array=numpy.matrix(alpha)
    alpha_array=alpha_array.reshape(nodes,nodes)
    
    ######################
    page_ranks=defaultdict(list)
    gen=[i for i in range(nodes)]
    
    for i in gen:
        page_ranks[i].append(0.)
        page_ranks[i].append(1./nodes)
        
    t=0
    
    
        
        
    def vectorize(page_ranks):
        vector=[]
        for i in page_ranks:
            vector.append(page_ranks[i][-1])
        c=numpy.matrix(vector).transpose()
        return c
    
    
    if epsilon is None and period is not None:
        while t<period:
            current_page_ranks=alpha_array*vectorize(page_ranks)
            for i, n in enumerate(current_page_ranks):
                page_ranks[i].append(float(n))           
            t+=1
    elif epsilon is not None and period is None:
        while float(abs(page_ranks[i][-1]-page_ranks[i][-2]))>epsilon:
            current_page_ranks=alpha_array*vectorize(page_ranks)
            for i, n in enumerate(current_page_ranks):
                page_ranks[i].append(float(n))           
            t+=1        
    else:
        print "Please enter either an Epsilon or Period parameter. Both cannot be empty and both cannot be given!"
    
    for i in page_ranks:
        print "The Page Ranks Are:",i,"   ",page_ranks[i][-1]
    print "It took %d iterations" % (t)



