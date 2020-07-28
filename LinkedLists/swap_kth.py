class Node:

     def __init__(self, data):
          self.data = data
          self.next = None

class LinkedList:
     def __init__(self):
          self.head = None
          self.count = 0

     def append(self,data):
          new_node = Node(data)

          if self.head is None:
               self.head = new_node
               return

          cur_node = self.head

          while cur_node.next is not None:
               cur_node = cur_node.next

          cur_node.next = new_node
          self.count += 1

     def printll(self):

          if self.head is None:
               print('Empty Linked List')

          cur_node = self.head
          print(cur_node.data, end = ' -->  ')          
          while cur_node.next is not None:

               print(cur_node.next.data, end = ' -->  ')
               cur_node = cur_node.next
          print()

     def swap_kth(self,num,k):

         prevX = None
         pX = self.head
         c = 0
         while pX and c<k-1:
             prevX = pX
             pX = pX.next
             c += 1
         #print(prevX.data)
         prevY = None
         pY = self.head
         c = 0
         while pY and c<num - k:
             prevY = pY
             pY = pY.next
             c +=1
         #print(prevY.data)
    
         temp = pY.next
         #print(temp.data)
         pY.next = pX.next
         pX.next = temp
    
         if prevX is None:
             self.head = pY
             prevY.next = pX
         elif prevY is None:
             self.head = pX
             prevX.next = pY
         else:
             prevY.next = pX
             prevX.next = pY
         return 
LL1 = LinkedList()

LL1.append(4)
LL1.append(5)
LL1.append(6)
LL1.append(7)
LL1.append(8)
LL1.append(9)
LL1.append(10)
LL1.append(11)
LL1.printll()
LL1.swap_kth(8,8)
print("printing")
LL1.printll()

               


     
