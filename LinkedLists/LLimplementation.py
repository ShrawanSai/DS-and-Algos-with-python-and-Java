class Node:

     def __init__(self, data):
          self.data = data
          self.next = None

class LinkedList:
     def __init__(self):
          self.head = None
          self.count = 0

     def prepend(self,data):

          new_node = Node(data)
          
          if self.head is None:
               self.head = new_node
               self.count += 1
               return
          else:
               new_node.next = self.head
               self.head = new_node
               self.count += 1

     def append(self,data):


          new_node = Node(data)

          cur_node = self.head

          while cur_node.next is not None:
               cur_node = cur_node.next

          cur_node.next = new_node
          self.count += 1


     def insert_at_index(self, req_index, data):

          new_node = Node(data)

          if self.count == 0:
               if req_index == 0:
                    self.head = new_node
               else:
                    print(data)
                    print("noob")
          
                    
               

          index = -1

          cur_node = self.head
          #self.count += 1
          if req_index == 0:
               self.prepend(data)
               return

          while cur_node.next is not None:
               index += 1
               if index+1 == req_index:
                    break
               cur_node = cur_node.next
          else:
               print("invalid index")
          new_node.next = cur_node.next
          cur_node.next = new_node
          self.count += 1


     def reverse_ll(self):

          curr = self.head
          prev = None

          while curr is not None:
               #print(curr.data)

               nextN = curr.next
               curr.next = prev
               prev = curr
               curr = nextN
          self.head = prev
          

     

          
     def printll(self):

          if self.head is None:
               print('Empty Linked List')

          cur_node = self.head
          print(cur_node.data, end = ' -->  ')          
          while cur_node.next is not None:

               print(cur_node.next.data, end = ' -->  ')
               cur_node = cur_node.next
          print()
          print(self.head.data)

LL1 = LinkedList()

LL1.prepend(7)
LL1.prepend(6)
LL1.prepend(5)
LL1.prepend(4)
LL1.insert_at_index(2,"Yeet")
LL1.printll()
LL1.append(9)
LL1.append(10)
LL1.printll()
LL1.prepend(3)
LL1.prepend(2)
LL1.append(11)
LL1.insert_at_index(0,"IDK yo")
LL1.printll()
LL1.reverse_ll()
#LL1.prepend("Head")
LL1.printll()
               
