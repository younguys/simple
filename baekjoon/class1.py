#1번문제
#a,b,c,d,e=map(int,input().split())
#total=(a*a+b*b+c*c+d*d+e*e)%10
#print(int(total))
#2번문제ord,hex
#a=input()
#print(ord(a))
#3번문제 개행문자앞까지 읽음 sys.stdin.readline().
#int(input())
#a=list(map(int,input().split()))
#print(min(a),max(a))
#4번문제
#str=list(input().split())
#print(len(str))
#5번문제
#a=[]
#for i in range(9):
#    a.append(int(input()))
#print(max(a))
#print(a.index(max(a))+1)
#6번문제
#from itertools import count
#a=[]
#for i in range(3):
#    a.append(int(input()))
#x=str(a[0]*a[1]*a[2])
#list=map(int,str(x))
#for i in range(10):
#    print(x.count(str(i)))
#7번문제 문자열도 list처럼 반복문이자로 사용가능
#t=int(input())
#for i in range(t):
# a,b=input().split()
# for j in b:
#  print(int(a)*j, end='')
# print()
#8문제 문자열자체를 비교 보다는 아스키코로 바로 비교하는게 좋을듯 ord아스키 문자chr
#a=input().upper()
#temp=[]
#str=[]
#for i in range(len(a)):
#   flag=False
#    for j in range(len(temp)):
#        if a[i]==str[j]:
#            flag=True
#            break
#    if flag==False:
#        str.append(a[i])
#        temp.append(a.count(a[i]))
#if temp.count(max(temp))==1:
#    print(str[temp.index(max(temp))])
#else:
#    print('?')
#9번문제
#a=int(input())
#b=input()
#total=0
#for i in range(a):
#    total=total+int(b[i])
#print(total)
#10번문제 리스트 관련해서 찾아 볼필요가 있을듯
#a,b=input().split()
#print(max([int(a[::-1]),int(b[::-1])]))
#for i in range (2,-1,-1):
#    if int(a[0][i]) >int(a[1][i]):
#        print(a[0][2]+a[0][1]+a[0][0])
#        break
#    elif int(a[0][i]) <int(a[1][i]):
#        print(a[1][2]+a[1][1]+a[1][0])
#        break  
#    else:
#        continue
#문제11번
#tempstr=input()
#if'12345678'==tempstr[::2]:
#    print('ascending')
#elif"87654321"==tempstr[::2]:
#    print('descending')
#else:
#    print('mixed')
#12번문제
#a=int(input())
#tempstr=[]
#for i in range(a):
#   tempstr.append(input())
#for i in range(a):
#    count=0
#    totalsum=0
#    for j in range(len(tempstr[i])):
#        if tempstr[i][j]=='O':
#            count=count+1
#            totalsum=totalsum+count
#        else:
#            count=0
#            continue
#    print(totalsum)
#13 set()함수이용하여 중복제거 가능
#a=[]
#for i in range(10):
#    num=int(int(input())%42)
#    flag=False
#    for j in a:
#        if num == j:
#            flag=True
#            break
#        else:
#            flag=False
#            continue
#    if flag == False:
#        a.append(num)
#print(len(a))
#a=[]
#for i in range(10):
#    a.append(int(input())%42)
#print(len(set(a)))
#14문제 for문 한줄로 적을 수있음 join문으로 리스트내용출력
#a=list(input())
#b=[]
#temp=[]
#for i in range(len(a)):
#    b.append(ord(a[i]))
#b.sort()
#b=set(b)
#for i in range(ord('a'),ord('z')+1):
#    flag=False
#    for j in b:
#        if j==i:
#            flag=True
#            temp.append(a.index(chr(i)))
#            break
#        else:
#            flag=False
#            continue
#    if flag==False:
#        temp.append(-1)
#print(" ".join(str(s)for s in temp))
