import functools
import math
import sys
import threading
from functools import cmp_to_key
from collections import defaultdict
from collections import deque
 
# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
"""
Recursion Template

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

"""
 
 
# def I(): return int(input())
 
# def II(): return map(int, input().split())
 
# def IL(): return list(map(int, input().split()))
 
# def SIL(): return sorted(map(int, input().split()),)

# def S() : return input()

# def SL() : return list(input().split())
 
# def solve():
#     pass
 
 
 
 
# T = 1
# for _ in range(T):
#     solve()



from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    pass
 
 
 
 
T = 1
for _ in range(T):
    solve()