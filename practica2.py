#例外処理
# class MyException(Exception):
#     pass
#
# def div (a,b):
#     try:
#         if( b<0):
#             raise MyException('not minue')
#         print(a/b)
#     except ZeroDivisionError:
#         print('noto by zero')
#     except MyException as e:
#         print(e)
#     else:
#         print('no except')
#     finally:
#         print('end')
#
# div(10,-3)
# div(10,0)

#リスト型
# scores = [10,20,30]
# # print(scores[2])
# # print(len(scores))
# scores.append(100)
# # print(scores)
#
# # for score in scores: #左から順にすべて表示
# #     print(score)
# for i  , score in enumerate(scores):
    #指定した番号だけを表示
    # print('{0}:{1}'.format(i,score))
#タプルの使い方tuple
# items = (20, 'apple' ,13)
# print(items[1])

#スライス
# scores = [20,30,40,50,60,]
# print(scores[0:4])#20,30,40
# print(scores[:5])#20,30,40,50
# print(scores[3:])#50,60
#
# s = 'hello'
# print(s[1:3])#el

#辞書型
# sales = {'kenta':200, 'gis':500,'suzuki':200,'kouichi':400}
# print(sales['kenta'])
# sales['kenta']=300
# sales['cris']=500
# # print(sales)
# del sales['kenta']
# print(sales)
#
# for key,value in sales.items():
#     print('{0}:{1}'.format(key,value))
#
# #イテレータ
# scores = [50,60,70,80,90]
# it = iter(scores)
# print(next(it))
# print(next(it))
# print('hello')
# print(next(it))
#
# for score in scores:
#     print(score)

#map(関数,イテレーター)
# def triple(n):
#     return n*3
#
# print(list(map(triple,[1,2,3])))
# lambda 引数：処理
# print(list(map(lambda n : n*3 , [1,2,3])))

#内包表記
# print([i *2for i in range(10)])
#偶数だけ取り出し
# print([i *3for i in range(10) if  i  % 2 ==0])

# print(i * 3 for i in range(10)  if  i  % 2 ==0)
# print({i *3for i in range(10) if  i  % 2 ==0})

# def largo(a,b,c,d):
#     return a*1000*b/c/d
# result=largo(100,0.8,64,8.9)
# print(result)

# mojisu=len(input('mojisuu :  '))
# # print(mojisu)
# def nijou():
#     n = input('numero :')
#     n = int(n)
#     return n**2
# result = nijou()
# print(result)

# def  nyuryoku():
a = input('peso :  ')
a=float(a)
b= input('espesor :  ')
b=float(b)
c = input('ancho :  ')
c=float(c)
d= input('densidad :  ')
d=float(d)

result=a*1000/b/c/d
hrs = result/

print(result)
