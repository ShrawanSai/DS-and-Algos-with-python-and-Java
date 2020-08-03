from collections import deque
def max_of_subarray_of_k(arr,n,k):

     dq = deque()

     for i in range(k):

          while len(dq) >0 and arr[dq[-1]] < arr[i]:

               dq.pop()
          dq.append(i)

     for j in range(k,n):

          print(arr[dq[0]])

          while len(dq) > 0 and dq[0] <= j-k:
               dq.popleft()

          while len(dq) > 0 and arr[dq[-1]] < arr[j]:
               dq.pop()
          dq.append(j)

     print(arr[dq[0]])

max_of_subarray_of_k([20,40,30,10,60],5,3)
