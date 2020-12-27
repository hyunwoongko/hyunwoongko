#!/usr/bin/env python
# coding: utf-8

# # 이진 연산

# ### 덧셈
# - 덧셈에서는 자리 올림이 발생할 수 있다.
# - 이 자리올림을 '캐리(Carry)'라고 한다.
# 
# ![img](https://user-images.githubusercontent.com/38183241/103154349-47eba400-47da-11eb-8ece-0adc01221be2.png)

# ### 뺄셈
# - 뺄셈에서는 상위 자리에서 빌려와야할 수 있다.
# - 이 자리 빌림을 '바로우(Borrow)'라고 한다.
# 
# ![img](https://user-images.githubusercontent.com/38183241/103154350-47eba400-47da-11eb-881a-847154411146.png)
# 

# ### 구현

# In[4]:


import re

def preprocessing(a:str):
    """
    숫자를 4의 배수길이로 맞춰주는 함수
    """
    
    # 빈칸 지우기
    a = re.sub(' ', '', a)
    
    # 길이가 0인경우 엑셉션 발생    
    if len(a) == 0:
        raise Exception() 
    
    # 자리수가 4의 배수가 될때까지 앞에 0을 insert함    
    while len(a) % 4 != 0:
        a = '0' + a[0:]
        
    return a


print('01 => {}'.format(preprocessing('01')))
print('11101 => {}'.format(preprocessing('11101')))
print('0001 => {}'.format(preprocessing('00001')))


# In[5]:


def split_binary(a:str) -> list:
    """
    00000000처럼 긴 형식을
    0000 0000형식으로 4자리씩 자르는 함수
    """
    
    arr, cache = [], ''
    
    for i, val in enumerate(list(a)):
        cache += val    
        if (i+1) % 4 == 0 and i != 0:
            arr.append(cache)
            cache = ''
    
    return arr


a, b = '01011001', '10111011'
print("a : {0} => {1}".format(a, ' '.join(split_binary(a))))
print("b : {0} => {1}".format(b, ' '.join(split_binary(b))))


# In[6]:


def binary_addition(a:str, b:str)->list:
    """
    두개의 2진수를 더해서 결과를 리턴하는 함수
    덧셈만 구현... 뺄셈까지 구현하기엔 귀찮음 (보수 씁시다 ^^)
    """
    
    a = split_binary(preprocessing(a))
    b = split_binary(preprocessing(b))
    total, carry = [], 0
    
    # 두 수의 자리수가 안맞으면 맞춰줌
    while len(a) != len(b):
        if len(a) > len(b): b.insert(0, '0000')
        else : a.insert(0, '0000')
    
    a.reverse() # 뒤부터 연산해야하기 때문에 뒤집음
    b.reverse() # 뒤부터 연산해야하기 때문에 뒤집음
    
    for n in zip(a, b):
        a_i = ''.join(reversed(n[0]))
        b_i = ''.join(reversed(n[1]))
        unit = []
        
        for j, m in enumerate(zip(a_i, b_i)):
            a_ij, b_ij = int(m[0]), int(m[1])
            result = a_ij + b_ij + carry
            
            if result >= 2: result -= 2 ; carry = 1
            else: carry = 0
            unit.append(result)
            
            if j == 3:
                unit.reverse()

        total += unit
        
    if carry == 1:
        for i in [0, 0, 0, 1]:
            total.append(i)
        
    total = [str(i) for i in total]
    total = split_binary(''.join(total))
    total.reverse()
    return total


a, b = '01011001', '10111011'
# 0101 1001 + 1011 1011 = 0001 0001 0100

print("{0} + {1}".format(a, b))
print('===> {}'.format(' '.join(binary_addition(a, b))))


# ### Reference
# > https://youtu.be/zUL4Np5QhXw
# 
