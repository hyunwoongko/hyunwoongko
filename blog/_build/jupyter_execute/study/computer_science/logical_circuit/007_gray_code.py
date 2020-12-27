#!/usr/bin/env python
# coding: utf-8

# # 그레이 코드

# ### 그레이 코드의 특징과 목적
# 그레이 코드는 각 비트패턴이 Unit Distance이면서 Reflective한 코드시스템이다. 시스템에서 2개 이상의 비트가 변할때 정밀하게 측정하면 정확히 동시에 변하지 않고 약간 시간 차이가 발생하는데 이 것을 실시간으로 측정하면 에러가 상당히 커지게 된다. 그레이코드는 한번에 한비트만 변하기 때문에 이로인해 발생할 수 있는 에러가 최소화된다.
# 
# #### Unit Distance 코드
# Unit Distance는 한번에 1비트만 변하는 구조를 의미한다. 그레이코드는 Unit Distance 코드이기 때문에 동시에 두 비트가 변하는 경우가 없고 때문에 에러가 적다.
# 
# #### Reflective 코드
# Unit Distance만큼이나 중요한 그레이코드의 특징이다. 만약 어떤 코드가 Reflective하면 첫번째 비트패턴과 마지막 비트패턴역시 Unit Distance로 연결될 수 있기 때문에 전체 패턴이 Unit Distance일 수 있다.

# ### 그레이코드 생성하기
# 
# #### 1 Bit 그레이코드
# - $0\;|\; 1$
# 
# #### 2 Bit 그레이코드
# 1. 이전비트 복사하기 (왼쪽) : $0\; 1\;|\; ?\; ?$
# 2. 리플렉팅 (순서 거꾸로) : $0\; 1\;|\; 1\; 0$
# 3. 앞자리에 비트추가 (왼쪽0, 오른쪽1) : $00\; 01\;|\; 11\; 10$
# 
# #### 3 Bit 그레이코드
# 1. 이전비트 복사하기 (왼쪽) : $00\; 01\; 11\; 10\;|\; ?\; ?\; ?\; ?$
# 2. 리플렉팅 (순서 거꾸로) : $00\; 01\; 11\; 10\;|\; 10\; 11\; 01\; 00$
# 3. 앞자리에 비트추가 (왼쪽0, 오른쪽1) : $000\; 001\; 011\; 010\;|\; 110\; 111\; 101\; 100$
# 
# #### 구현

# In[1]:


import copy

def gray_code(n_bit):
    """
    n 비트의 그레이코드를 만드는 함수
    """
    
    bit_set = ['0', '1']
    
    for i in range(n_bit-1):
        reflected = copy.deepcopy(bit_set)
        reflected.reverse()
        
        bit_set = ['0' + j[:] for j in bit_set]
        reflected = ['1' + j[:] for j in reflected]
        bit_set += reflected
    
    return bit_set

print('1bit =>', gray_code(1))
print('2bit =>', gray_code(2))
print('3bit =>', gray_code(3))


# ### 그레이코드와 이진코드 변환
# 
# #### 규칙
# - 이진 → 그레이 : 가장 앞비트는 그대로, 이전 원소와 다음 원소를 XOR한다.
# - 그레이 → 이진 : 가장 앞비트는 그대로, 이전 반환값과 다음 원소를 XOR한다.
# 
# ![img](https://user-images.githubusercontent.com/38183241/103154351-48843a80-47da-11eb-8c5c-be1bd1ed3c67.jpg)
# 
# #### 구현

# In[2]:


import re

def xor(a, b):
    if a == b: return '0'
    else: return '1'


def binary_to_gray(binary_code):
    """
    이진코드 => 그레이코드 변환함수
    """
    gray_code = []
    binary_code = re.sub(" ", "", binary_code)
    prev = binary_code[0]
    gray_code.append(prev) 
    # 첫 비트는 그대로 살림
    
    for after in binary_code[1:]:
        gray = xor(prev, after)
        gray_code.append(gray)
        # 이전 원소와 다음원소를 xor
        
        prev = after
        # 현재원소가 이전원소가 됨
    
    return ''.join(gray_code)


def gray_to_binary(gray_code):
    """
    그레이코드 => 이진코드 변환함수
    """
    binary_code = []
    gray_code = re.sub(" ", "", gray_code)
    prev = gray_code[0]
    binary_code.append(prev)
    
    for after in gray_code[1:]:
        xor_result = xor(after, prev)
        binary_code.append(xor_result)
        # 이전 xor결과값과 다음 원소를 xor
        
        prev = xor_result
        # xor의 결과값이 이전원소가 됨.
    
    return ''.join(binary_code)

    
print('binary 0111 => gray {}'.format(binary_to_gray('0111')))
print('gray 0100 => binary {}'.format(gray_to_binary('0100')))


# ### Reference
# > https://youtu.be/N6fhO0En4rk
# 
