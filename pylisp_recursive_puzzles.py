#!/usr/bin/python3
#
# pylisp.py
# nprenet@bsu.edu, 11/2022

# WHAT? Recursion on lists: a quick implementation of Lisp/Scheme primitive functions 
# (car, cdr, cons), and some applications. 

import unittest

class WrongTypeArgumentException(Exception):
    pass

def car(lst):
    """ The first of the 3 primitive functions: return the first element of a sequence. 

    .. note:: The Law of Car: The `car` function is only defined for non-empty lists.

    :param lst: a non-empty sequence; passing an empty sequence raises an exception.
    :type lst: tuple
    :returns: an object
    :rtype: object
    """
    if not lst:
        raise WrongTypeArgumentException("car is not defined for empty sequences")
    return lst[0]

def cdr(lst):
    """ The second of the 3 primitive functions: return a sequence, minus the first element.

    .. note:: The Law of Cdr: The `cdr` function is only defined for non-empty lists; the `cdr` of any non-empty list is always another list.

    :param lst: a non-empty sequence; passing an empty sequence raises an exception.
    :type lst: tuple
    :returns: a tuple; if the sequence has only one element, return an empty sequence.
    :rtype: tuple
    """
    if not lst:
        raise WrongTypeArgumentException("cdr is not defined for empty sequences")
    return lst[1:]

def cons(a, lst):
    """ The third of the 3 primitive functions: return the sequence created by adding element `a` to the sequence `lst`.

    .. note:: The Law of Cons: the primitive `cons` takes two arguments; the second argument to `cons` must be a list; the result is a list.
    
    :param a: an object
    :param lst: a tuple
    :type a: object
    :type lst: tuple
    :returns: the tuple resulting from adding parameter `a` in front of sequence `lst`.
    :rtype: tuple
    """
    if not isinstance(lst, tuple):
        raise WrongTypeArgumentException("cons expects the second argument to be a tuple")
    return (a,) + lst

def copy_sequence(seq):
    """ Return the copy of a sequence, recursively (implementation provided as an example).

    :param seq: the sequence to be copied
    :type seq: tuple
    :returns: a tuple, identical to the sequence that has been passed in
    :rtype: tuple
    """ 
    if seq == ():
        return ()
    return cons(car(seq), copy_sequence(cdr(seq)))

def reverse_sequence(seq):
    """ Return a sequence, in the reverse order, recursively.

    :param seq: the sequence to be reversed.
    :type seq: tuple
    :returns: a tuple, with the same elements, in the reverse order.
    :rtype: tuple
    """ 
    if seq == ():
        return ()
    return concatenate_sequences(reverse_sequence(cdr(seq)), (car(seq),))

def count_sequence(seq):
    """ Count the elements in a sequence, recursively. 

    :param seq: the sequence whose elements are to be counted
    :type seq: tuple
    :returns: the numbers of elements in the sequence
    :rtype: int
    """ 
    if seq == ():
        return 0
    return 1 + count_sequence(cdr(seq))

def search_sequence(seq, item):
    """ Search a sequence for the given item.

    :param seq: the sequence to be searched.
    :param item: the item to be searched
    :type seq: tuple
    :type item: str
    :returns: True if the item is contained in the sequence, False otherwise.
    :rtype: bool
    """ 
    if seq == ():
        return False
    if car(seq) == item:
        return True
    return search_sequence(cdr(seq), item)

def filter_sequence(seq, item):
    """ Return sequence, minus the matching item. 

    Ex. 

        .. code-block:: python
           
            >>> filter_sequence(("I", "blah", "did", "not", "do", "it", "!", "blah"), "blah") 
            ("I", "did", "not", "do", "it", "!")
    
    :param seq: the sequence to be searched.
    :param item: the item to be filtered
    :type seq: tuple
    :type item: str
    :returns: the same sequence, with the item removed
    :rtype: tuple
    """ 
    if seq == ():
        return ()
    if car(seq) == item:
        return filter_sequence(cdr(seq), item)
    return cons(car(seq), filter_sequence(cdr(seq), item))

def concatenate_sequences(seq1, seq2):
    """ Return a sequence that is made of the concatenation of the provided sequences.

    Ex.

        .. code-block:: python
           
            >>> concatenate_sequences(("I", "did" "not"), ("do", "it", "!"))
            ("I", "did", "not", "do", "it", "!")

    :param seq1: the leading sequence.
    :param seq2: the trailing sequence.
    :type seq1: tuple
    :type seq2: tuple
    :returns: a single sequence, with the elements of the first sequence followed by the elements of the second sequence.
    :rtype: tuple
    """ 
    if seq1 == ():
        return seq2
    return cons(car(seq1), concatenate_sequences(cdr(seq1), seq2))

class PyLisp_unittest(unittest.TestCase):

    sandwich = ("jelly","butter", "mustard", "bread", "pickles", "jam", "cheese")

    # Unit tests for the car, cons, and cdr functions
    def test_car(self):
        self.assertEqual(car(('a', 'b', 'c')), 'a')
        self.assertRaises(WrongTypeArgumentException, car, ())

    def test_cdr(self):
        self.assertEqual(cdr(('a', 'b', 'c')), ('b', 'c'))
        self.assertEqual(cdr(('a',)), ())
        self.assertRaises(WrongTypeArgumentException, cdr, ())

    def test_cons(self):
        self.assertEqual(cons('a', ('b', 'c')), ('a', 'b', 'c'))
        self.assertRaises(WrongTypeArgumentException, cons, 'a', 'b')

    ###

    def test_copy_sequence_0(self):
        """ Read empty tuple """
        sandwich = ()
        self.assertEqual(copy_sequence(sandwich), ())

    def test_copy_sequence_1(self):
        """ Read single-element tuple"""
        sandwich = ('mustard',)
        self.assertEqual(copy_sequence(sandwich), ('mustard',))

    def test_copy_sequence_2(self):
        """ Read 7-element tuple"""
        sandwich = ("jelly","butter", "mustard", "bread", "pickles", "jam", "cheese")
        self.assertEqual(copy_sequence(sandwich), sandwich)

    def test_reverse_sequence_0(self):
        """ Reverse empty tuple """
        sandwich = ()
        self.assertEqual(reverse_sequence(sandwich), ())

    def test_reverse_sequence_1(self):
        """ Reverse single-element tuple"""
        sandwich = ('mustard',)
        self.assertEqual(reverse_sequence(sandwich), ('mustard',))

    def test_reverse_sequence_2(self):
        """ Reverse 7-element tuple"""
        sandwich = ("jelly","butter", "mustard", "bread", "pickles", "jam", "cheese")
        self.assertEqual(reverse_sequence(sandwich), sandwich[::-1])

    def test_count_sequence_0(self):
        """ Count empty tuple """
        sandwich = ()
        self.assertEqual(count_sequence(sandwich), 0)

    def test_count_sequence_1(self):
        """ Count single-element tuple"""
        sandwich = ('mustard',)
        self.assertEqual(count_sequence(sandwich), 1)

    def test_count_sequence_2(self):
        """ Count 7-element tuple"""
        sandwich = ("jelly","butter", "mustard", "bread", "pickles", "jam", "cheese")
        self.assertEqual(count_sequence(sandwich), 7)

    def test_search_sequence_0(self):
        """ Search empty tuple """
        sandwich = ()
        self.assertEqual(search_sequence(sandwich, 'ham'), False)

    def test_search_sequence_size_1_1(self):
        """ Search  single-element tuple: successful search"""
        sandwich = ('mustard',)
        self.assertEqual(search_sequence(sandwich, 'mustard'), True)

    def test_search_sequence_size_1_2(self):
        """ Search single-element tuple: unsuccessful search"""
        sandwich = ('mustard',)
        self.assertEqual(search_sequence(sandwich, 'ham'), False)

    def test_search_sequence_size_7_1(self):
        """ Search 7-element tuple: successful search"""
        sandwich = ("jelly","butter", "mustard", "bread", "pickles", "jam", "cheese")
        self.assertEqual(search_sequence(sandwich, 'pickles'), True)

    def test_search_sequence_size_7_2(self):
        """ Search 7-element tuple: unsuccessful search"""
        sandwich = ("jelly","butter", "mustard", "bread", "pickles", "jam", "cheese")
        self.assertEqual(search_sequence(sandwich, 'pear'), False)

    def test_filter_sequence_size_0(self):
        """ Filter empty tuple """
        sandwich = ()
        self.assertEqual(filter_sequence(sandwich, 'mustard'), ())

    def test_filter_sequence_size_1_2(self):
        """ Filter single-element tuple: successful filter"""
        sandwich = ('mustard',)
        self.assertEqual(filter_sequence(sandwich, 'mustard'), ())

    def test_filter_sequence_size_7_1(self):
        """ Filter 7-element tuple: successful filter"""
        sandwich = ("jelly","butter", "mustard", "bread", "pickles", "jam", "cheese")
        self.assertEqual(filter_sequence(sandwich, 'pickles'), ("jelly","butter", "mustard", "bread", "jam", "cheese"))

    def test_concatenate_sequences_0(self):
        """ Concatenate empty tuple with empty tuple """
        self.assertEqual(concatenate_sequences((), ()), ())

    def test_concatenate_sequences_1(self):
        """ Concatenate empty tuple with non-empty tuple """
        self.assertEqual(concatenate_sequences((), ('a', 'b')), ('a', 'b'))

    def test_concatenate_sequences_2(self):
        """ Concatenate non-empty tuple with empty tuple """
        self.assertEqual(concatenate_sequences(('a', 'b'), ()), ('a', 'b'))

    def test_concatenate_sequences_3(self):
        """ Concatenate two non-empty tuples """
        self.assertEqual(concatenate_sequences(('a', 'b'), ('c', 'd')), ('a', 'b', 'c', 'd'))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
