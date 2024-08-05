# https://www.acmicpc.net/problem/1781

import sys
import heapq

input = sys.stdin.readline
     
num = int(input())
for _ in range(num):
    data, reward = map(int, input().split())