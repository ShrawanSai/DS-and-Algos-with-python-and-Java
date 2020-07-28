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

     def swap_pairwise(self):

          d = d1 = Node(-1)

          d.next = self.head
          new_head = d.next.next

          while d.next and d.next.next:

               p = d.next
               q = d.next.next

               d.next,p.next,q.next = q, q.next, p
               d = p
          self.head = new_head
              
                    

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
LL1.swap_pairwise()
print("printing")
LL1.printll()
