if __name__ == '__main__':
        x=[a for a in input("Enter list seperated by spaces\n").split()]
        q=input("search for max or min? (answer by max or min)\n")
        m=x[0]
        if q=="max":
            for i in x:
                m=m if m>i else i
        else:
            for i in x:
                m=m if m<i else i
        print(m)