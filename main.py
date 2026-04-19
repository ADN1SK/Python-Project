# # function that counts the number of words in a string
# def count_words(string):
#     words = string.split()
#     return len(words)
# print(count_words("Hello world! This is a test and my name is Adam."))


# xfile= open('Life Expectancy Data.csv')
# count=0
# for line in xfile:
#     count= count +1
#     print('line count: ',count)

# xfile= open('Life Expectancy Data.csv')
# inp= xfile.read()
# print(len(inp))
# print(inp[:20])
        
# xfile=open('MONGODB adammoha0987 db.txt')
# for line in xfile:
#     line=line.lstrip()
#     if not line.startswith("adam"):
#         continue
#     print(line)


# fname= input("enter the file name:")
# fhand=open(fname)
# count=0
# for line in fhand:
#     if line.startswith("m"):
#         count= count + 1
# print("there were", count, "m line in", fname)

# fname= input('enter file:')
# if len(fname) < 1:fname='test.txt'
# hand= open(fname)
# for line in hand:
#     line= line.rstrip()
#     #print(line)
#     wds=line.split()
#     print(wds)
#     for w in wds:
#         print(w)
# import socket 
# mysock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True:
#     data= mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
# mysock.close()
# print(ord('H'))
# print(ord('e'))
# print(ord('\n'))
name= input('enter file:')
handle= open(name)
text= handle.read()
words= text.split()
counts= dict()
for word in words:
    counts[word]= counts.get(word,0) 

# ord() function returns the Unicode code point for a given character. In this case, it returns the code points for 'H', 'e', and the newline character '\n'.
