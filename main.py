# -*- coding: utf-8 -*-

#   AUTHOR: fluxoid, ifi@yandex.ru
#   VERSION: 0.1.1
#   LATEST REVISION: 10.09.2018
#   DESCRIPTION: Калькулятор выражений на питоне
#   PURPOSES: Educational

# общая архитектура
# - перевод полученной строки в обратную польскую нотацию
# - вычисление выражения в обратной польской нотации

import math, sys

app_version="0.1.1"

def isdelimiter(c):
    if c=='=' or c==' ':
        return True
    return False

def isoperator(c):
    if c=='+' or c=='-' or c=='*' or c=='/' or c=='^' or c=='^' or c=='(' or c==')':
        return True
    return False

def getpriority(s):
    if s=='(':
        return 0
    elif s==')':
        return 1
    elif s=='+':
        return 2
    elif s=='-':
        return 3
    elif s=='*':
        return 4
    elif s=='/':
        return 4
    elif s=='^':
        return 5
    return 6

def translate(text):
    output=''
    stack=list()
    i=0
    num=''
    # задолбало выходить за границы строки
    # поэтому добавил индикатор конца строки
    text+='N'
    while i<len(text):
        if isdelimiter(text[i]):
            i+=1
            continue
        if text[i].isdigit():
            while not isdelimiter(text[i]) and not isoperator(text[i]) and text[i]!='N':
                output+=text[i]
                i+=1
            output+=' '
            i-=1       
        if isoperator(text[i]):
            if text[i]=='(':
                stack.append(text[i])
            elif text[i]==')':
                while stack[len(stack)-1]!='(' and len(stack)>0:
                    output+=stack.pop()+' '
                if len(stack)>0:
                    stack.pop()
            else:
                if len(stack)>0:
                    while getpriority(text[i])<=getpriority(stack[len(stack)-1]):
                        output+=stack.pop()+' '
                        if len(stack)==0:
                            break
                stack.append(text[i])                    
        i+=1
    while len(stack)>0:
        output+=stack.pop()+' '
    return output

# вычисляем
def compute(expr):
    res=0
    expr+='N'
    tmp=list()
    i=0
    while i<len(expr):
        if expr[i].isdigit():
            a=''
            while not isdelimiter(expr[i]) and not isoperator(expr[i]) and expr[i]!='N':
                a+=expr[i]
                i+=1
            tmp.append(float(a))
            i-=1
        elif isoperator(expr[i]):
            a=float(tmp.pop())
            b=float(tmp.pop())
            if expr[i]=='+':
                res=b+a
            elif expr[i]=='-':
                res=b-a
            elif expr[i]=='*':
                res=b*a
            elif expr[i]=='*':
                res=b*a
            elif expr[i]=='/':
                res=b/a
            elif expr[i]=='^':
                res=math.pow(b,a)
            tmp.append(res)
        i+=1
    return tmp[len(tmp)-1]

def show_help():
    print('EasyCalc by fluxoid')
    print('Verion '+app_version)
    print('Version Date: 10.02.2018')
    print('Supported operators: + - * / ^')
    print('To exit type \'q\' and press Enter')
    print('Math functions and variable support soon to be added')

def main():
    text=''
    expr=''
    result=0
    show_help()

    while 1:
        text=input('ec>')
        if text=='q':
            break
        if text=='help':
            show_help()
            continue
        expr=translate(text)
        result=compute(expr)
        print('{0}'.format(result))

if __name__=="__main__":
    main()
