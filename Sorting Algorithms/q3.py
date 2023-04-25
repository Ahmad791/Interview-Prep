def qsort(x):
    if len(x)==1 or len(x)==0:
        return x
    elif len(x)==2:
        return x if x[0]<x[1] else x[::-1]
    else:
        pivot,pivotindex,pivotsize,end,i=x[0],0,1,len(x)-1,1#end is where to put the bigger number (reduced by1 when when used)
        while i-1!=end:#note we choose the pivot x[0]
            if x[i]<pivot:
                x[i],x[pivotindex]=x[pivotindex],x[i]
                i,pivotindex=i+1,pivotindex+1
            elif x[i]>pivot:# in the original algorithm it doesn't increase the size of pivot but this makes the algorithm run faster since there will be less extreme cases
                x[i],x[end]=x[end],x[i]
                end-=1
            else:
                pivotsize+=1
                i+=1
        return qsort(x[:pivotindex])+[pivot]*pivotsize+qsort(x[pivotindex+pivotsize:])


if __name__ == '__main__':
    x=[int(a) for a in input("Enter list seperated by spaces\n").split()]
    x=qsort(x)
    print(x)