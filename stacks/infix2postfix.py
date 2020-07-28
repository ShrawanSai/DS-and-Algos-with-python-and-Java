def InfixtoPostfix(exp):
    #code here
    stack = []
    string = ''''''
    
    preced = {'(': 5,'^':0, '/':1, '*': 1, '-':2, '+':2}
    
    for i in exp:
        
        if i == '(':
            stack.append(i)
        elif i == ')':

             while len(stack)>0:
                  s = stack.pop()
                  
                  if s == '(':
                       #print('yes')
                       break
                  else:
                       string += s
                    
                  
             
        elif i in preced.keys():
            try:
                while len(stack)>0 and preced[stack[-1]] <= preced[i]:
                    string += stack.pop()
                stack.append(i)
            except:
                stack.append(i)
                
        else:
            string += i

    while len(stack) > 0:
         string += stack.pop()
    return string
print(InfixtoPostfix('a+b*(c^d-e)^(f+g*h)-i'))
#if (: push
#if ) pop untill you get (. print what youre popping
#if alphabet: print
#if operator:
#    check priority:
#         if operator p > stack top p:
#                push to stack
#         else:
#                pop untill you can push

# stack +*-
# o/p abcd^e-fgh*+^*+i-
