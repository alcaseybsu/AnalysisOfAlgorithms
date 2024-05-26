#!/usr/bin/python3

import unittest

class Node:
    """
    A simplistic Node definition.

    :ivar key: the value stored on the node (a primitive value, or a node reference)
    :vartype key: int or str or Node
    :ivar next: pointer to the next node
    :vartype next: Node
    """

    def __init__(self, k, nxt=None):
        """ Initialize a new node.

        :param k: the key value
        :type k: int or str or Node
        """
        self.key = k
        self.next = nxt

    def __str__(self):
         return '|{}|'.format(self.key)


def evaluate_list(lst):
    """
    Evaluate an arithmetical expression represented as a linked list.
    (See algorithm above.)

    :param lst: the list (or element of a list)
    :type lst: Node
    :return: the numerical value of the arithmetical expression represented by the linked list
    :rtype: int or float
    """
    if isinstance(lst, Node):
        if isinstance(lst.key, str):  # operator
            op = lst.key
            left = evaluate_list(lst.next.key)
            right = evaluate_list(lst.next.next.key)
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
        else:  # operand
            return lst.key
    return lst  # base case for non-nested calls


class TestListEval(unittest.TestCase):

    @classmethod
    def prefix_to_list(cls, seq):
        """
        Transform a parenthesized expression into a linked list.

        :return: a reference to the first node of the list.
        :rtype: Node
        """
        if type(seq) is not tuple:  # base case: atom (operator or operand)
            return seq
        return Node(seq[0], Node(cls.prefix_to_list(seq[1]), Node(cls.prefix_to_list(seq[2]))))

    def test_addition(self):
        expr = self.prefix_to_list(('+', 14, 2))
        self.assertEqual(evaluate_list(expr), 16)

    def test_multiplication(self):
        expr = self.prefix_to_list(('*', 14, 2))
        self.assertEqual(evaluate_list(expr), 28)

    def test_subtraction(self):
        expr = self.prefix_to_list(('-', 14, 2))
        self.assertEqual(evaluate_list(expr), 12)

    def test_division(self):
        expr = self.prefix_to_list(('/', 14, 2))
        self.assertEqual(evaluate_list(expr), 7)

    def test_expression_1(self):
        expr = self.prefix_to_list(('/', ('*', 3, 56), ('+', 14, 2)))
        self.assertEqual(evaluate_list(expr), 10.5)

    def test_expression_2(self):
        expr = self.prefix_to_list(('-', ('/', ('*', 3, 56), ('+', 14, 2)), 5))
        self.assertEqual(evaluate_list(expr), 5.5)

    def test_expression_3(self):
        expr = self.prefix_to_list(('*', ('/', ('+', 1, 2), ('-', 5, 2)), 4))
        self.assertEqual(evaluate_list(expr), 4)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
