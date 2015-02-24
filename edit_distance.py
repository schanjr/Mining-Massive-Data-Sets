import texttable as tt
'''texttable does not come as standard library. A stand alone install for this module may be required. 
Open CMD and type in 'pip install texttable' should do the trick'''


def edit_distance(word1, word2):
    len_1=len(word1)
    len_2=len(word2)
    x =[[0]*(len_2+1) for _ in range(len_1+1)]#the matrix whose last element ->edit distance
    for i in range(0,len_1+1): #initialization of base case values
        x[i][0]=i
    for j in range(0,len_2+1):
        x[0][j]=j
    for i in range (1,len_1+1):
        for j in range(1,len_2+1):
            if word1[i-1]==word2[j-1]:
                x[i][j] = x[i-1][j-1] 
            else :
                x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1
    return x[i][j]

def ed_wrapper(word1,word2):
    if isinstance(word2, basestring):
        splits=word2.split()
    elif isinstance(word2, list):
        splits=word2
    elif isinstance(word2, tuple):
        splits=word2
    else:
        return "Please convert input parameters to either strings, lists, or tuples"
    tab = tt.Texttable()    
    x = [[]] # The empty row will have the header
    
    for i in range(len(splits)):
        x.append([word1,splits[i],edit_distance(word1, splits[i])])
    
    tab.add_rows(x)
    tab.set_cols_align(['r','r','r'])
    tab.header(['Word_1', 'Word_2', 'Edit Distance'])
    print tab.draw()
    
#Sample usage
'''
word1="Hi" <----The string that is used as a base for comparison
word2="what the heck is going on here?"  <----- The list of words or a large string to compare with word1
print ed_wrapper(word1, word2)
'''
"he,she,his,hers"
word1="his"
word2="hers"

print ed_wrapper(word1, word2)




