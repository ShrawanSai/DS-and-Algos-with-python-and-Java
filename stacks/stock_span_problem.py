from collections import deque

def stock_span_problem(arr):
     stack = deque()

     stack.append(0)
     print(1)
     for i in range(1,len(arr)):
          #print(stack)
          while len(stack)>0 and arr[stack[-1]]<=arr[i]:
               stack.pop()

          if len(stack) == 0:
               print(i+1)
          else:
               print(i - stack[-1])
          stack.append(i)
          
               

print(stock_span_problem([15,13,12,14,16,8,6,4,10,30]))
