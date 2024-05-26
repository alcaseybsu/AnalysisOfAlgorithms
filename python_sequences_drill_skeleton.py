#!/usr/bin/python3

import unittest
import re

def filter( tpl ):   
    """
    Given a tuple (immutable list) of strings, return another list where:

    * words that have at least 10 letters are kept unchanged
    * words that have at least 5 letters (but less than 10) are replaced with the string "medium"
    * words that have less than 5 letters are replaced with the word length (character count)

    Ex. 

    .. code-block:: python

        >>> filter( ("lion", "hippopotamus", "kangaroo", "tyrannosaurus", "parrott") )
        [4, 'hippopotamus', 'medium', 'tyrannosaurus', 'medium'] 

    Topics: `if-elif-else`, length of sequences and strings

    :param tpl: a tuple of strings
    :type tpl: tuple
    :return: a list of strings
    :rtype: list
    """    
    A = []
    for i in tpl:
        if len(i) >= 10:
            A.append(i)
        elif len(i) >= 5:
            A.append('medium')
        else:
            A.append(len(i))
    return A
filter(("lion", "hippopotamus", "kangaroo", "tyrannosaurus", "parrott")) 
    



def reverse_minus_last( tpl ):
    """
    Given a list of values, return a second list that meets the given criteria:

    * it contains all elements of the first list, except the last one
    * the order is reversed

    Ex.

    .. code-block:: python

        >>> reverse_minus_last( (1, 2, 3, 4, 5) )
        [4, 3, 2, 1]

    Topics: ranges, sequence subscripts.

    :param tpl: tuple of integers.
    :type tpl: tuple
    :return: a list of integers.
    :rtype: list
    """
    arr = []
    for i in range(len(tpl) -2, -1, -1):
        arr.append(tpl[i])
    return arr
reverse_minus_last((1, 2, 3, 4, 5))    


def even_odd( tpl ):
    """ Given a tuple of integers, return another list where even integers are replaced with a 0, and odd integers,  with a 1.

    .. code-block:: python
        
        >>> even_odd((9, 7, 4, 3))
        [1, 1, 0, 1]

    :param tpl: tuple of integers.
    :type tpl: tuple
    :return: a list of 0s and 1s.
    :rtype: list
    """
    return [i%2 for i in tpl]
even_odd((9, 7, 4, 3))    



def differences( tpl ):               
    """ Given a tuple of integers of size :math:`n`, return a list where each of the :math:`n-1`  elements is the diffence between two consecutive elements of the first list.
    Ex. 
    .. code-block:: python    
    >>> differences((9, 7, 4, 3))
    [2, 3, 1]        
    :param tpl: tuple of integers.
    :type tpl: tuple
    :return: a list of integers
    :rtype: list
    """
    list_to_return = []
    #for idx in range(len(tpl)- 1): 
        #list_to_return.append(tpl[idx] - tpl[idx + 1])
    #return list_to_return  
    return [ tpl[idx] - tpl[idx + 1]for idx in range(len(tpl) -1) ] 
differences((9, 7, 4, 3))    


def swap( lst ):
    """ Swap two variables.

        Given a list, swap the first and last element of the list. The function modifies the given list, but does not return anything.

        :param lst: a list of values
        :type lst: list
    """
    lst[0], lst[-1] = lst[-1], lst[0]
lst = [5, 2, 3, 4, 1]
swap(lst)
print(lst)


def concatenate_different_types( integers, animals ):
    """
    Given a tuple of integers and a list of animal names, construct and return a string that combines one integer and one animal string. (Hint: use the `format()` function, as shown in the QuickSort example,  in project P3's tutorial). Each combination matches the following template: `I ran into <number> <animal>.`  A space separates each combination from the other.

    Ex.

    .. code-block:: python
        
        >>> concatenate_different_types( ((5,7,3,9), ("kangaroos", "lions", "sharks", "cats"))
        I ran into 5 kangaroos. I ran into 7 lions. I ran into 3 sharks. I ran into 9 cats.

    
    :param integers: a list of integers
    :type integers: tuple
    :param animals: a list of animal names 
    :type animals: tuple
    :return: a string of the form `I ran into <m> <animal>. I ran into <n> <animal>. ...` 
    :rtype: str
    """
    arrlist = []
    for i in range(len(integers)):
        arrlist.append("I ran into {} {}.".format(integers[i], animals[i]))
    return ' '.join(arrlist)
concatenate_different_types((5, 7, 3, 9), ('kangaroos', 'lions', 'sharks', 'cats'))    


def copy_tuple(tpl):
    """
    Return a copy of a tuple. Careful: it should be a *copy* of the object passed as a parameter, with the same values, not the same object! 
    
    * Assigning the variable to another will not do it;
    * returning a range of subscripts, such as `tpl[0:]` will not either (quite surprisingly); 
    * creating a new tuple from the original one with `tuple(tpl)` just returns a reference to the same object! 

    Instead, I suggest initializing a new `list` object from the tuple, and use this in turn as a parameter for a new, distinct `tuple` object.


    :param tpl: a tuple of values
    :type tpl: tuple
    :return: return a copy of the tuple passed as a parameter
    :rtype: tuple
    """    
    tpl = (1, 2, 3)
    newTpl = tuple(list(tpl))    
    return newTpl
copy_tuple((1, 2, 3))
    


class TestClass( unittest.TestCase ):


    def  test_differences(self):
        self.assertEqual( differences( (9, 7, 4, 3)), [2, 3, 1] )

 
    def test_swap(self):
        array = [1, 2, 3, 4]
        swap(array)
        self.assertEqual( array[0], 4)
        self.assertEqual( array[1], 2)
        self.assertEqual( array[2], 3)
        self.assertEqual( array[3], 1)

    def test_even_odd( self ):
        self.assertEqual( even_odd((5, 8, 9, 2, 13, 25, 14)), [1, 0, 1, 0, 1, 1, 0])


    def test_filter(self):
        self.assertEqual( filter( ("lion", "hippopotamus", "kangaroo", "tyrannosaurus", "parrott") ),
                            [4, 'hippopotamus', 'medium', 'tyrannosaurus', 'medium'])
        

    def test_reverse_minus_last(self):
        self.assertEqual( reverse_minus_last((5,4,3,2,1,0)), [1, 2, 3, 4, 5])


    def test_concatenate_different_types(self):
        rgxp = re.compile(' *I +ran +into +5 +lemurs(\.)? *I +ran +into +7 +kingfishers(\.)? *I +ran +into +3 +turtles(\.)? *I +ran +into +9 +hummingbirds(\.)? *')
        return_string = concatenate_different_types( (5,7,3,9), ("lemurs", "kingfishers", "turtles", "hummingbirds"))
        self.assertTrue( re.match(rgxp, return_string))

    def test_copy_tuple(self):
        """
        Test whether the tuple copy 
        + is a copy, not the original object
        + stores the the same values
        """
        original = (1,2,3)
        copy = copy_tuple( original )
        self.assertEqual( copy, original) 
        self.assertFalse( copy is original )

def main():
    unittest.main()

if __name__ == '__main__':
    main()