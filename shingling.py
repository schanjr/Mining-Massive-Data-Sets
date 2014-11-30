def shingling(string_1, string_2, shingle_k=2):
    #Lets say shingles is 2
    '''Outputs 2 numbers which is the intersection and the union. Taking these two numbers (intersection/union) would equate
    to Jaccard Similarity'''
    trunc_1=string_1.replace(" ","").upper()
    trunc_2=string_2.replace(" ","").upper()
    list_1=[]
    list_2=[]
    s_start=0
    s_end=shingle_k
    intersection=0
    leftovers=0
    for i in range(len(trunc_1)):
        if len(trunc_1) - shingle_k != s_start -1:
            list_1.append(trunc_1[s_start:s_end])
            s_start+=1
            s_end+=1
    list_set_1=list(set(list_1))
    s_start=0
    s_end=shingle_k
    for i in range(len(trunc_2)):
        if len(trunc_2) - shingle_k != s_start -1:
            list_2.append(trunc_2[s_start:s_end])
            s_start+=1
            s_end+=1
    list_set_2=list(set(list_2))
    for i in list_set_1:
        if i in list_set_2:
            intersection+=1
        else:
            leftovers+=1
    for i in list_set_2:
        if i not in list_set_1:
            leftovers+=1
    union=leftovers+intersection
    return intersection, union
'''
#Sample usage
string_1='ABRACADABRA'
string_2='BRICABRAC'
print shingling(string_1, string_2, 2)
'''
