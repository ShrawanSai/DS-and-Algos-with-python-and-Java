from collections import deque

def prev_greatest(arr):
     stack = deque()

     stack.append(0)
     print(-1)
     for i in range(1,len(arr)):

          while len(stack) != 0 and arr[stack[-1]] <= arr[i]:
               stack.pop()

          if len(stack) == 0:
               print(-1)
          else:
               print(arr[stack[-1]])
          stack.append(i)

print(prev_greatest([15,10,18,12,4,6,2,8]))
