#!/usr/bin/python3

import unittest

class OverflowException( Exception): pass
class UnderflowException( Exception): pass

class Stack:
    """
    A simplistic Stack class
    See CLRS3, 10.1

    :ivar array: the array storing the values.
    :vartype array: list
    :ivar top: the index of the element that is currently at the top of the stack. 
    :vartype top: int
    """

    def __init__(self, size=100):
        """ Initialize a new Stack object.

        :param size: stack capacity (optional, default: 100)
        :type size: int
        """
        self.array = [None]*size
        self.top = -1

    def is_empty(self):
        """ 
        Test whether the stack is empty.

        :return: True if the stack is empty; False otherwise
        :rtype: bool
        """
        return self.top < 0


    def push(self, key):
        """ Insert a key at the top.

        :param key: the key value
        :type key: int or str
        """

        if self.top == len(self.array)-1:
            raise OverflowException()
        
        self.top += 1
        self.array[ self.top ] = key


    def pop(self):
        """ Retrieve last element from the top

        :return: a key value
        :rtype: int or str
        """
        if self.is_empty():
            raise UnderflowException()
        self.top -= 1
        return self.array[ self.top+1 ]

    def __str__(self):
        """ Console-friendly representation of the stack.

        :return: the list of active elements
        :rtype: str
        """
        return str(self.array[:self.top+1])


################ YOUR JOB STARTS HERE ##############



def evaluate(expr):
    """ Evaluate an arithmetical expression.

    Numerical operands can be positive or negative. A negative operand counts as a single token in the expression. For example: :math:`(-5)\\times 3` gives, in prefix notation: :math:`\\times\sqcup -5\\sqcup 3` (with visible spaces added for clarity) where the minus sign is not an operand.
    
    .. note:: The stack object is already created. You have to code the rest!

    :param expr: a list of numerical operands and operators, in prefix notation.
    :type expr: tuple
    :return: the numerical value of the expression
    :rtype: float or int
    """
    stack = Stack()
    for i in reversed(expr):
        if type(i) == int:
            stack.push(i)
        else:    
            x = stack.pop()
            y = stack.pop()
            if i == '+':
                value = x + y
            elif i == '-':
                value = x - y
            elif i == '*':
                value = x * y
            elif i == '/':
                value = x / y
            stack.push(value)
        
    return stack.pop()        
            
    # continue...
    


############ DO NOT MODIFY THE TEST CLASS! ######################


class TestCalculator( unittest.TestCase ):

    def test_addition( self ):
        expr = ('+',14,2)
        self.assertEqual( evaluate(expr), 16)

    def test_multiplication( self ):
        expr = ('*',14,2)
        self.assertEqual( evaluate(expr), 28)

    def test_subtraction( self ):
        expr = ('-',14,2)
        self.assertEqual( evaluate(expr), 12)

    def test_division( self ):
        expr = ('/',14,2)
        self.assertEqual( evaluate(expr), 7)

    def test_expression_1( self ):
        expr = ('/','*',3,56, '+', 14, 2)
        self.assertEqual( evaluate(expr), 10.5)

    def test_expression_2(self):
        expr= ('-','/','*',3,56,'+',14,2,5)
        self.assertEqual( evaluate(expr), 5.5)




def main():
    unittest.main()

if __name__ == '__main__':
    main()

