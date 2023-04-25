def merge(x,y):
    ix,iy=0,0
    z=[]
    while(ix<len(x) and iy<len(y)):
        if x[ix]<y[iy]:
            z.append(x[ix])
            ix+=1
        else:
            z.append(y[iy])
            iy+=1
    return z+y[iy:]+x[ix:]


    

def recSort(x):
    if len(x)>1:
        return merge(recSort(x[:len(x)//2]),recSort(x[len(x)//2:]))
    else:
        return x
if __name__ == '__main__':
    x=[int(a) for a in input("Enter list seperated by spaces\n").split()]
    x=recSort(x)
    print(x)