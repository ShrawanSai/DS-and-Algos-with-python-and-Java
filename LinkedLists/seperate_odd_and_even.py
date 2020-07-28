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


     def seperate_odd_and_even(self):

          ES, EE, OS, OE = None, None, None, None

          cur = self.head

          while cur is not None:
               if cur.data %2 == 0:
                    if ES is None:
                         ES = cur
                         EE = ES
                    else:
                         EE.next = cur
                         EE = EE.next
               else:
                    if OS is None:
                         OS = cur
                         OE = OS
                    else:
                         OE.next = cur
                         OE = OE.next
               cur = cur.next
          if OS is None or ES is None:
               return
          else:
               EE.next = OS
               self.head = ES
               OE.next = None
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
LL1.seperate_odd_and_even()
print("printing")
LL1.printll()
