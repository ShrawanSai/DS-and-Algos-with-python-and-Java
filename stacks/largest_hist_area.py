from collections import deque

def largest_hist_area(arr,n):
     stack = deque()
     m = 0
     for i in range(len(arr)):
          
          while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
               tp = stack.pop()
               if len(stack) == 0:
                    x = i
               else:
                    x = i - stack[-1] - 1
               m = max(m,arr[tp]*x)
          #print(123)
          stack.append(i)
          print(stack)

     while len(stack)>0:
          tp = stack.pop()
          if len(stack) == 0:
               x = n
          else:
               x = n - stack[-1] - 1
          m = max(m,arr[tp]*x)
          #print(stack)
     return m
print(largest_hist_area([6,2,5,4,1,5,6],7))
