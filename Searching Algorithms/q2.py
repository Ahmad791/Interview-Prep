def bsearch(x,num,start,end):
    if end-start<=1:   
        if x[start]==num:
            return start  
        else: 
            return end if x[end]==num else -1
    else:
        if x[((end-start)//2)+start]==num:
            return (end-start)//2 
        else:
            return bsearch(x,num,start,((end-start)//2)+start) if x[((end-start)//2)+start]>num else bsearch(x,num,((end-start)//2)+start+1,end)


if __name__ == '__main__':
    x=[a for a in input("Enter sorted list seperated by spaces\n").split()]
    num=input("Enter number to search for\n")
    res=bsearch(x,num,0,len(x))
    print("found it on index ", res) if res !=-1 else print("didn't find it")