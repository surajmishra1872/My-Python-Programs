def revs_list(l):
    rev=[]
    for i in l:
        
        rev.append(i[::-1])
    return rev
s=["abc","xyz","mnp"]
print(revs_list(s))
