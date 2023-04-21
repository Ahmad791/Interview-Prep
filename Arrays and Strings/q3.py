if __name__ == '__main__':
    x=[a for a in input("Enter sorted array\n").split()]
    ans=[]
    for i in range(len(x)-1):
        if x[i]!=x[i+1]:
            ans.append(x[i])
    ans.append(x[-1])
    print(ans)