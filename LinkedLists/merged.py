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

     def merged(self, a, b):

          if a.data > b.data:
               head = b
               tail = b
               b = b.next
          else:
               head = a
               tail = a
               a = a.next
          while a and b:
               if b.data >= a.data:
                    tail.next = a
                    tail = a
                    a = a.next
               else:
                    tail.next = b
                    tail = b
                    b = b.next
          while a:
               tail.next = a
               tail = a
               a = a.next
          while b:
               tail.next = b
               tail = b
               b = b.next
          return head

LL1 = LinkedList()
LL2 = LinkedList()

LL1.append(1)
LL1.append(3)
LL1.append(5)
LL1.append(7)
LL1.append(9)
LL2.append(2)
LL2.append(4)
LL2.append(6)
LL2.append(8)
LL2.append(10)
LL1.printll()
LL2.printll()

a = LL1.head
b = LL2.head
LL1.merged(a,b)
print("printing")
LL1.printll()


               

