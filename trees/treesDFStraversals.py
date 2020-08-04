class Node:

     def __init__(self, data):

          self.value = data
          self.left = None
          self.right = None

class BinaryTree:

     def __init__(self,root):
          self.root = Node(root)

     def print_tree(self, order):

          string = ''''''
          
          if order == 'inorder':
               print(self.inorder(self.root, string))
               
          elif order == 'preorder':
               print(self.preorder(self.root, string))
               
          elif order == 'postorder':
               print(self.postorder(self.root, string))

          elif order == 'level_order':
               print(self.level_order(self.root, string))

          elif order == 'level_order_newline':
               print(self.level_order_newline(self.root, string))

               
     def inorder(self, start, string):
          #string = ''''''
          if start:
               string = self.inorder(start.left,string)
               string += str(start.value)
               string = self.inorder(start.right, string)
          return string

     def preorder(self, start, string):
          #string = ''''''
          if start:
               string += str(start.value)
               string = self.inorder(start.left,string)
               string = self.inorder(start.right, string)
          return string
     
     def postorder(self, start, string):
          #string = ''''''
          if start:
               
               string = self.inorder(start.left,string)
               string = self.inorder(start.right, string)
               string += str(start.value)
          return string

     def level_order(self, start, string):

          queue = list()
          queue.append(start)

          while len(queue)>0:
               x = queue[0]

               if x.left:
                    queue.append(x.left)

               if x.right:
                    queue.append(x.right)

               string += str(queue.pop(0).value)
               
          return string

     def level_order_newline(self, start, string):

          queue = list()
          queue.append(start)
          queue.append(None)

          while len(queue)>1:
               x = queue[0]
               if x is None:
                    queue.append(None)
                    string += '\n'
                    queue.pop(0)
                    continue

               if x.left:
                    queue.append(x.left)

               if x.right:
                    queue.append(x.right)

               string += str(queue.pop(0).value)
               
          return string

     def size_of_tree(self,start):

          if start is None:
               print(0)

          queue = list()
          queue.append(start)
          count = 0

          while len(queue)>0:
               x = queue[0]

               if x.left:
                    queue.append(x.left)

               if x.right:
                    queue.append(x.right)

               queue.pop(0)
               count += 1
               
          print(count)
          return

def size(node):

     if node is None:
          return 0
     else:
          return (size(node.left)+ 1 + size(node.right))

def max_of_tree(node):

     if node is None:
          return 0
     else:
          return max(node.value , max(max_of_tree(node.left) , max_of_tree(node.right)))


def height(node):

     if node is None:
          return 0
     else:
          return max(height(node.left) , height(node.right)) + 1

def nodes_at_distance_k(node, k):

     if node is None:
          return
     if k == 0:
          print(node.value , end = ',')
     else:
          nodes_at_distance_k(node.left , k-1)
          nodes_at_distance_k(node.right ,k-1)

def leftview(root):

     queue = list()

     queue.append(root)

     while len(queue) > 0:
          m = len(queue)
          for i in range(m):
               g = queue.pop(0)
               if i == 0:
                    print(g.value)
               if g.left:
                    queue.append(g.left)

               if g.right:
                    queue.append(g.right)


def childrensumproperty(node):

     if node is None:
          return True
     if node.left is None and node.right is None:
          return True
     sum = 0
     if node.left:
          sum += node.left.value
     if node.right:
          sum += node.right.value
     if sum == node.value and childrensumproperty(node.left) and childrensumproperty(node.right):
          return True
     return False
               



          
     
          
               
               

print(' DEFINING TREE \n\n')
bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)
bt.root.left.left.left = Node(9)
print('\n\n Traversals \n\n ')
print('\n\n Inorder Traversal \n ')
bt.print_tree('inorder')
print('\n\n Preorder Traversal \n ')
bt.print_tree('preorder')
print(' \n\n Postorder Traversal \n ')
bt.print_tree('postorder')
print('\n\n Level Order Traversal \n ')
bt.print_tree('level_order')
print('\n\n Level Order Traversal in new line \n ')
bt.print_tree('level_order_newline')
print(" \n\n\n TREE SIZE \n")
bt.size_of_tree(bt.root)
print(" \n\n\n TREE SIZE calculated recursively \n")
print(size(bt.root))
print(" \n\n\n MAX TREE VALUE \n")
print(max_of_tree(bt.root))
print(" \n\n\n TREE HEIGHT \n")
print(height(bt.root))
print(" \n\n\n NODES AT K DISTANCE FROM ROOT \n")
nodes_at_distance_k(bt.root, 2)
print()
print(" \n\n\n LEFT VIEW OF TREE \n")
leftview(bt.root)
print()
print(" \n\n\n CHECK IF TREE FOLLOWS CHILDREN SUM PROPERTY \n")
print(childrensumproperty(bt.root))
print()
