# -*- coding: utf-8 -*-
import timeit

# ----------------------------------------------------
def recursive(n):
    if n==0 or n==1:
        return n
    else:
        return recursive(n-2)+recursive(n-1)


# ----------------------------------------------------
def dynamic(n):
    dp = [0 for i in range(1000)]
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n-1]


# ----------------------------------------------------
import matplotlib.pyplot as plt

time1, time2 = [], []

for i in range(50):
    temp = timeit.timeit('recursive(i)', setup='from __main__ import recursive, i', number=1)
    time1.append(temp)
    
x1 = list(range(50))
plt.plot(x1, time1, color='orange', lw='1', ls='-.', marker='.', label='Recursive')


for i in range(100):
    temp = timeit.timeit('dynamic(i)', setup='from __main__ import dynamic, i', number=1)
    time2.append(temp)
    
x2 = list(range(100))
plt.plot(x2, time2, color='royalblue', lw='1', ls='-.', marker='.', label='Dynamic')


plt.legend()
plt.grid(color='black', lw='0.5', ls=':', alpha=0.9)
plt.title("Recursive v.s Dynamic Programming", fontsize=15)
plt.xlabel('Input Quantity (n)', fontsize=10)
plt.ylabel('Execution Time (sec)')


# 執行時間 : 一個小時二十二分鐘
