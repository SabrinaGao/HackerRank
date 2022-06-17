N=int(input())
X=[int(x) for x in input().split()]

def mean(N,X):
    mean=round(sum(X)/N,1)
    return mean

def median(N,X):
    X.sort()
    if N%2==0:
        idx=int(N/2)
        return round((X[idx]+X[idx-1])/2,1)     
    else: 
        idx=(N-1)/2
        return round(X[idx],1)
    

def mode(N,X):
    frequency={}
    modes=[]
    for i in X:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    for values in frequency.values():
        if values==max(frequency.values()):
            modes.append(values)
    if len(modes)==1:
        mode=modes[0]
    else:
        mode=min(modes)
    for keys in frequency.keys():
        if frequency[keys]==mode:
            return keys   

print(mean(N,X))
print(median(N,X))
print(mode(N,X))