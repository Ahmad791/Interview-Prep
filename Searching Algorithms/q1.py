def main(x,num):
    for i in x:
        if i==num:
            print("found it")
            return i
        
    print("doesn't exist")
    return -1 


if __name__ == '__main__':
    x=[a for a in input("Enter list seperated by spaces\n").split()]
    num=input("Enter number to search for\n")
    main(x,num)