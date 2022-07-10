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


    

n = st.number_input("Enter a number between 2 and 10000", 2, 10000, 50, step = 5 )


list_of_primes = []
for num in range(n):
    if num >= 2:
        for x in range (2, num):
            if num % x == 0:
                break
        else:
            list_of_primes.append(num)

st.write (
    f" **List of primes less than {n+1} are:** \n {list_of_primes}")
