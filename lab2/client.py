#python .\CRC\client.py
import socket 
s = socket.socket()
port = 12345            
s.connect(('127.0.0.1', port))
f_in_error=0

def BinaryToDecimal(binary):      
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def binarytocharacter(b):
    # print(b,end="-------")
    decimal_data=BinaryToDecimal(int(b))
    return chr(decimal_data)

def convertbinarytotext(filename):
    f=open(filename,'r')
    contents=f.read()
    # print(len(contents))
    l=int(len(contents)/7)
    for i in range(l):
        x=(i+1)*7
        y=i*7
        b=contents[y:x]
        # print(b)
        ch = binarytocharacter((b))
        f1=open('outputfile.txt','a')
        f1.write(ch)
        f1.close()
    # print(l)
    f.close()

def xor(a,c,n): 
    result=""
    a=remove_starting_zero(a,n)
    a_len=len(a)
    if a_len<n:
        return a
    for i in range(n):
        if(a[i]==c[i]):
            res='0'
        else:
            res='1'
        result+=res
    here=n-1
    j=0
    count_zero=0
    for j in range(n):
        if(result[j]=='0'):
            count_zero+=1
            continue
        else:
            here=j
            break
    if(count_zero==n):
        result=''
    else:
        result=result[here:n]
    return result

def remove_starting_zero(a,n):
    here_1=0
    for j in range(n):
        if(a[j]=='0'):
            continue
        else:
            here_1=j
            break
    a=a[here_1:n]
    return a

def modulo_2_div(t,c):
    result=''
    check=len(c)
    lent=len(t)
    t=remove_starting_zero(t,lent)
    len_t=len(t)
    i=0
    while len_t>=check :
        if i==0:
            dividend=t[i:i+check]
        else:
            to_add=t[i+res:i+res+x]
            dividend=result+to_add
        result=xor(dividend,c,check)
        res=len(result)
        x=check-res
        len_t-=x
        i+=x
    r=result
    return r


def correct_or_not(p,c):
    remainder=modulo_2_div(p,c)
    if(remainder==''):
        return 0 #OK Acknowledgement 0
    else:
        return 1 #NAK acknowledgement 1

def message_retrieval(pt,c): #client side message from pt
    chop=len(c)
    where=len(pt)
    upto=where-chop+1
    m=pt[0:upto]
    return m


sz=int(s.recv(1024).decode())

i=0

while i+128<sz:
    c='100000111'
    # c='11'
    
    pt=s.recv(1024).decode()
    
    if(correct_or_not(pt,c)==1): #error
            s.send('NAK'.encode())
            # print('NAK SENT')
            f_in_error+=1
    else:
        print(i)
        s.send('ACK'.encode())
        # print('ACK sesnt')
        m=message_retrieval(pt,c)
        string=list(m)
        with open('output.txt', 'a') as f:
            f.write(''.join(string))
            # print(m)
        i+=128

if(i<sz):
    pt=s.recv(1024).decode()
    if(correct_or_not(pt,c)==1): #error
            s.send('NAK'.encode())
            # print('NAK SENT')
            f_in_error+=1
    else:
        print(i)
        s.send('ACK'.encode())
        # print('ACK sesnt')
        m=message_retrieval(pt,c)
        string=list(m)
        with open('output.txt', 'a') as f:
            f.write(''.join(string))
            # print(m)
        

file='output.txt'
convertbinarytotext(file)
# close the connection
print('No. of frames in error: '+str(f_in_error))
s.close()    
    
   
