def liss(inp):
    n=len(inp)
    longest=[1]*n
    for i in range(n-1,-1,-1):
        m=1#max len subseq,
        for j in range(i,n):
            if(inp[i]<inp[j] and longest[j]>=m):
                m=longest[j]+1
        longest[i]=m
    print(max(longest))
            
                    
liss([10,9,2,5,3,7,101,18])