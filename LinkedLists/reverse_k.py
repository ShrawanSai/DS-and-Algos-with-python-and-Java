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

     def reverse_k(self,k):

          curr = self.head
          is_first_pass = True
          prev_First = None

          while curr is not None:

               first = curr
               prev = None
               count = 0

               while curr is not None and count < k:
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
                    count += 1

               if is_first_pass:
                    self.head = prev
                    is_first_pass = False
               else:
                    prev_First.next = prev
               prev_First = first
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
LL1.reverse_k(3)
LL1.printll()

                    
