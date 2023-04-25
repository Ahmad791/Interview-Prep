if __name__ == '__main__':
    x=[a for a in input("Enter list seperated by spaces\n").split()]
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    print(x)