#  File: ExpressionTree.py

#  Description: This script reads in expressions and turns the infix expression into a tree. It then evaluates the expression and prints the result. It
#  can also write the prefix and postfix versions of the same expression.

#  Student's Name: Rishabh Shah


import sys

class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

class Node(object):
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = Node(None)

    def create_tree(self, expr):
        treestack = Stack()
        current = self.root
        left = '('
        right = ')'
        operands = ['1','2','3','4','5','6','7','8','9','0']
        operators = ['+', '-', '*', '/', '//', '%', '**']

        for token in expr:
            if token == left:
                current.lchild = Node(None)
                treestack.push(current)
                current = current.lchild
            elif token in operators:
                current.data = token
                treestack.push(current)
                current.rchild = Node(None)
                current = current.rchild
            elif token.isdigit() or '.' in token:
                current.data = token
                current = treestack.pop()
            elif token == right:
                if treestack.isEmpty() == False:
                    current = treestack.pop()

    def evaluate(self, aNode):
        if aNode.data == '+':
            return self.evaluate(aNode.lchild) + self.evaluate(aNode.rchild)
        elif aNode.data == '-':
            return ( self.evaluate(aNode.lchild) - self.evaluate(aNode.rchild) )
        elif aNode.data == '*':
            return ( self.evaluate(aNode.lchild) * self.evaluate(aNode.rchild) )
        elif aNode.data == '/':
            return ( self.evaluate(aNode.lchild) / self.evaluate(aNode.rchild) )
        elif aNode.data == '//':
            return ( self.evaluate(aNode.lchild) // self.evaluate(aNode.rchild) )
        elif aNode.data == '%':
            return ( self.evaluate(aNode.lchild) % self.evaluate(aNode.rchild) )
        elif aNode.data == '**':
            return ( self.evaluate(aNode.lchild) ** self.evaluate(aNode.rchild) )
        elif aNode.data.isdigit() or '.' in aNode.data:
            return eval(aNode.data)

    def pre_order(self, aNode):
        if aNode != None:
            print(aNode.data, end= " ")
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    def post_order(self, aNode):
        if aNode != None:
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data, end=" ")

def main():
    # read infix expression
    #line = sys.stdin.readline()
    #expr = line.strip()
    expr = '( ( 8 + 3 ) * ( 7 - 2 ) )'
    # evaluate the expression and print the result
    newtree = Tree()
    newtree.create_tree(expr)
    print(expr,'=',newtree.evaluate(newtree.root))
    print()
    # get the prefix version of the expression and print
    print("Prefix Expression: ", end= "")
    newtree.pre_order(newtree.root)
    print()
    print()
    # get the postfix version of the expression and print
    print("Postfix Expression: ", end= "")
    newtree.post_order(newtree.root)

if __name__ == "__main__":
    main()
