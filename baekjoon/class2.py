#마지막문제
#a=int(input())
#b=list(map(int,input().split()))
#total=0
#for i in b:
#    total=total+i/max(b)*100
#print(total/a)
#class2 1번문제
# x,y,w,h=map(int,input().split())
# data=[x,y,w-x,h-y]
# print(min(data))
#문제2번
# while True:
#     a,b,c=map(int,input().split())
#     if a==0 and b==0 and c==0:
#         break
#     else:
#         print('right'if a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b else'wrong')
#문제3번
#a=int(input())
# for i in range(a):
#     x,y,z=map(int,input().split())
#     if z%x==0:
#         print(str(x)+'0'+str(int(z/x))if len(str(int(z/x)))==1 else str(x)+str(int(z/x)))
#     else:
#         print(str(z%x)+'0'+str(int(z/x+1))if len(str(int(z/x+1)))==1 else str(z%x)+str(int(z/x+1)))
#문제4번
# a=input()
# for i in range(1,int(a)+1):
#     total=sum(map(int,str(i)))
#     total=total+i
#     if total ==int(a):
#         print(i)
#         break
# else:
#     print(0)
#문제5번 문제를 잘 읽자
# a=int(input())
# count=1
# endnum=1
# if a==1:
#     print(1)
# else:    
#     while True:
#         endnum=count*6+endnum
#         if endnum>=a:
#             print(count+1)
#             break
#         elif 1000000000<a:
#             break
#         else:
#             count=count+1
#문제6번
# num,m=map(int,input().split())
# temp=list(map(int,input().split()))
# total=[]
# for i in range(num):
#     for j in range(num):
#         for k in range(num):
#             if temp[i]!=temp[j] and temp[j]!=temp[k] and temp[i]!=temp[k] and m>=temp[i]+temp[j]+temp[k]:
#                 total.append(temp[i]+temp[j]+temp[k])
#             else:
#                 continue
#             print(temp[i]+temp[j]+temp[k])
# print(max(total))
#문제7번
# a=input()
# s=input()
# total=0
# for i in range(len(s)):
#     total=total + (ord(s[i])-96)*pow(31,i)
# print(total%1234567891)
#문제8번
# while True:
#     s=input()
#     if s=='0':
#         break
#     else:
#         print('yes'if s[::]==s[::-1] else 'no')
#문제9번
# c=int(input())
# for i in range(c):
#     a=int(input())
#     b=int(input())
#     temp=[]
#     temp1=[]
#     for i in range(b):
#         temp.append(i+1)
#         temp1.append(i+1)
#     for k in range(a):
#         for i in range(1,b+1):
#             total=0
#             for j in range(i):
#                 total=total+temp[j]
#             temp1[i-1]=total
#         temp=temp1.copy()
#     print(max(temp))18
#문제10번
# a=int(input())
# if a%5==0:
#     print(a//5)
# else:
#     count=0
#     while True:
#         a=a-3
#         count += 1
#         if a%5==0:
#             print(a//5+count)
#             break
#         elif a==0:
#             print(count)
#             break
#         elif a==1 or 1==2:
#             print(-1)
#             break
#         else:
#             continue
#문제11번
# a,b,c=map(int,input().split())
# if c-a ==0:
#     print(1)
# else:
#     if (c-a)%(a-b)!=0:
#         print((c-a)//(a-b)+2)
#     else:
#         print((c-a)//(a-b)+1)
# a,b=map(int,input().split())
# B=1
# T=1
# for i in range(1,a-b+1):
#     B=B*i
# for i in range(1,b+1):
#     B=B*i
# for i in range(1,a+1):
#     T=T*i
# print(T//B)
#문제12번
# a=list(map(int,input().split()))
# temp=[]
# num=[]
# for i in range(1,max(a)+1):
#     if a[0]%i==0 and a[1]%i==0:
#         temp.append(i)
#     if max(a)*i%min(a)==0:
#         num.append(max(a)*i)
# print(max(temp))
# print(min(num))
#문제13번
