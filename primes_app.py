# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 11:06:24 2022

@author: Ibiene
"""


import streamlit as st
import numpy as np


st.write("""
# Prime Numbers App
### **This simple app finds all prime numbers less than the input**
""")


    

n = st.number_input("Enter a number between 2 and 100000", 2, 100000, 50, step = 5 )

# number range to be checked
number_range = set(range(2, n+1))

# empty list to append discovered primes to
primes_list = []

# iterate until list is empty
while number_range:
    prime = number_range.pop()
    primes_list.append(prime)
    multiples = set(range(prime*2, n+1, prime))
    number_range.difference_update(multiples)

prime_count = len(primes_list)
largest_prime = max(primes_list)
st.write (f"There are {prime_count} prime numbers between 1 and {n}, the largest of which is {largest_prime} \n")
st.write (f"List of primes are: {primes_list}")

