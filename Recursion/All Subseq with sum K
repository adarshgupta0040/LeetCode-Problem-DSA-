def f(ind,n,arr,l,summ,k):
    if ind>=n:
        if summ==k:
            print(l)
        return 
    l.append(arr[ind])
    summ+=arr[ind]
    f(ind+1,n,arr,l,summ,k)
    l.remove(arr[ind])
    summ-=arr[ind]
    f(ind+1,n,arr,l,summ,k)

arr=[1,2,1]
n=len(arr)
k=2
f(0,n,arr,[],0,k)
