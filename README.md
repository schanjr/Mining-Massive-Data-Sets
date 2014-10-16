page_rank
=========

This is an ongoing improvement page_rank algorithm that will eventually be scalable


Matrix Parameter
For example there are only 2 web pages. Web page A, and B. Let's say 

A--->B

So the PR(B)=PR(A)/2   According to the formula PR(B)=SUM of (1/(N of links pointing elsewhere)
                      -Really you should know a little bit about the algorithm before coming here
                      
So the Matrix Parameter should be entered like this:
[0, 0, 0, 1]

Which really came from this:

   A  B
A  0  0
B  0  1  

Of course your matrix is not supposed to be like this because matrixes in page rank have to be stochastic, have eigenvectors and eigenvalues. 


Nodes Parameter
Using the example above, if you have web pages A and B, then you have 2 nodes. 

Beta Parameter
Default value is 0.85 if not entered.

Epsilon Parameter
This is the differnce of previous and the current iteration. If you want to have more accurancy of page rank computation, make this a small number. (For example 0.0000000000000001)

Period
This is the number of iterations you want the function to go through. 


Either Epsilon or Period needs to be entered. Otherwise the script will not start. 
