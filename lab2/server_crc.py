import socket
import random            
s = socket.socket() 
host='127.0.0.1'
port = 12345               
s.bind((host, port))
s.listen(5)            
client, addr = s.accept()    
print ('Got connection from', addr )
no_of_retries=0

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

def send_to_client(pt):
    no_error=pt
    pt=error(pt)
    # print(pt)
    while True:
        client.send(f'{pt}'.encode())
        client_ack=client.recv(1024).decode()
        if client_ack=='NAK':
            global no_of_retries
            no_of_retries+=1
            send_to_client(no_error)
            return 
        elif client_ack=='ACK':
            # print('received')
            return 
        break

def error(data):
    n=len(str(data))
    if n==0:
        return ""
    data=list(data)
    r1=random.randint(0,100)
    r2=random.randint(0,127)
    if r1%2==1:
        if(data[r2]=='1'):
            data[r2]='0'
        else:
            data[r2]='1'
           
    return "".join(data)

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


def create_t_from_m(m,c):
    k=len(c)-1
    app=""
    for i in range(k):
        app+='0'
    t=m+app
    return t

def create_p_from_t(t,r):
    t_len=len(t)
    r_len=len(r)
    apnd=count_zeros(t,t_len)
    p=str(int(r)+int(t))
    for i in range(apnd):
        p='0'+p
    return p

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

def count_zeros(a,n):
    i=0
    for j in range(n):
        if(a[j]=='0'):
            i+=1
        else:
            break
    return i


def modulo_2_div(t,c):
    check=len(c)
    lent=len(t)
    t=remove_starting_zero(t,lent)
    len_t=len(t)
    i=0
    result=''
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



c='100000111'
file='dandelion.txt'
convertTextToBinary(file)
f = open('binaryfile.txt', 'r')
file=f.read()
no_of_char=len(file)
client.send(f'{no_of_char}'.encode())
print(no_of_char)
i=0
frame='0'
while i<(no_of_char):
    # print(i)
    frame=str(int(frame)^1)
    m=file[i:i+128]
    # print(m)
    tx=create_t_from_m(m,c)
    # print(f"T(x)={tx}")

    remainder=modulo_2_div(tx,c)
    # print(f"Remainder={remainder}")

    pt=create_p_from_t(tx,remainder) 
    # print(f"P(x)={pt}")
    send_to_client(pt)
    i+=128
    
m=file[i:no_of_char]
if len(m)>0:
    # print(i)
    # print(m)
    frame=str(int(frame)^1)
    tx=create_t_from_m(m,c)
    # print(f"T(x)={tx}")

    remainder=modulo_2_div(tx,c)
    # print(f"Remainder={remainder}")

    pt=create_p_from_t(tx,remainder)
    # print(f"P(x)={pt}")
    send_to_client(pt)

print('No. of retries: ' + str(no_of_retries))



