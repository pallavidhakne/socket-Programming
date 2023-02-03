def convertTextToBinary(filename):
    f = open(filename,'r')
    s=f.read()
    l=[]
    for i in s:
        l.append(ord(i))
        # print(i,end=" ")
    f.close()
    f1=open('binaryfile.txt','a')
    for i in l:
        b=bin(i)[2:]
        if len(b)<7:
            # prepend zeroes
            l=7-len(b)
            for i in range(l):
                b='0'+b
        f1.write(b)

    f1.close()
        

# convertTextToBinary('temp.txt')

# filename='dandelion.txt'

# convertTextToBinary(filename)


