import wave
import sys
import struct

rate = 44100

def convertTextToBinary(filename):
    f = open(filename,'r')
    s=f.read()
    l=[]
    for i in s:
        l.append(ord(i))
    f.close()
    f1=open('binaryfile.txt','a')
    for i in l:
        f1.write(bin(i)[2:])
    f1.close()
        

def convertAudioToBinary(filename):
    w = wave.open(filename,'rb')
    binary_data =w.readframes(w.getnframes())
    with open('binaryfile.txt','a') as f:
        f.write(str(binary_data))
    w.close()
    f.close()
    # print(binary_data)

# def output_wave(path, frames):
#     output = wave.open(path,'w')
#     output.setparams((2,2,rate,0,'NONE','not compressed'))
#     output.writeframes(frames)
#     output.close()

# def convertBinaryToAudio(filename):
#     with open(filename,'r') as f:
#         binary_data=f.read()
#     packedData = map(lambda v:struct.pack('h',v), binary_data)
#     frames = b''.join(packedData)
#     output_wave('example.wav', frames)

def convertVideoToBinary(filename):
    pass


def convert_to_binary(filename,num):
    if(num==1):
        convertAudioToBinary(filename)
    elif(num==2):
        convertVideoToBinary(filename)
    elif(num==3):
        convertTextToBinary(filename)
    else:
        print('Please Enter valid Input!!!')
        convert_to_binary(filename)


sys.modules[__name__] = convert_to_binary

# num=int(input('Choose which type of file you want to send:\n1)Audio file\n2)Video file\n3)Text file\n'))
# filename=input('Enter the filename : ')

num=3
filename='temp.txt'

convert_to_binary(filename,num)

# convertAudioToBinary('audio.wav')

# convertBinaryToAudio('binaryfile.txt')