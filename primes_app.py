# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 00:56:11 2022

@author: Ibiene
"""

import streamlit as st
import numpy as np


st.write("""
# Prime Numbers App
### **This simple app finds all prime numbers less than the input**
""")


    
num = st.number_input("Enter a number between 2 and 10000", 2, 10000, 20, step = 5 )

primes = [2]
numbers_list =np.arange(2, num).tolist()
for num in numbers_list:
    nums_LT_input = np.arange(2, num+1).tolist()
    for x in nums_LT_input:
        if num % x == 0:
            break
        else:
            primes.append(num)
            break
st.write (
    f" **List of primes less than {num+1} are:** \n {primes}")

