#!/usr/bin/python3

import unittest

def partition(A, p, r):
    """
    Given an array A, partition the subarray A[p..r], using A[r] as the pivot value.

    :param A: the subarray to be partitioned
    :param p: the left boundary
    :param r: the right boundary
    :type A: list
    :type p: int
    :type r: int
    """
        
    pivot = A[r] 
    i = p-1
    for j in range(p, r): 
        if A[j] <= pivot:
            i += 1
            A[i], A[j], = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]        
    return i + 1 



def QuickSort(A, p, r):
    """
    Sort the subarray A[p..r] in place, recursively.

    :param A: the input array 
    :param p: left boundary of the subarray to be sorted
    :param r: right boundary of the subarray to be sorted
    :type A: list
    :type p: int
    :type r: int
    """
    if p < r:
        """partition the subarray around the pivot, which ends up in A[q]"""
        q = partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
        
    


class TestQuickSort( unittest.TestCase):
    """ A testing class - run automatically every time this
    script is called
     """

    # Partition
    def test_partition_1(self):

        A = [ 2, 8, 7, 1, 3, 5, 6, 4 ]
        q = partition(A, 0, 7)
        self.assertEqual( A, [2, 1, 3, 4, 7, 5, 6, 8] ) 
        self.assertEqual( q, 3) 

    def test_partition_2(self):

        A = [ 5, 2, 4, 7, 1, 3, 2, 6 ]
        q = partition(A, 0, 7)
        self.assertEqual(A, [5, 2, 4, 1, 3, 2, 6, 7])
        self.assertEqual(q, 6)


    def test_partition_2_single_elements_halves(self):
        """ Special case: 2-element array"""
        A = [ 4, 7 ]
        q = partition(A, 0, 1)
        self.assertEqual( A, [4, 7])
        self.assertEqual( q, 1)

    def test_partition_3(self):
        """ Emtpy L-partition """
        
        A = [7, 12, 6, 15, 32, 39, 35, 31, 41, 38, 47, 1 ]
        partition(A, 0, 11)
        self.assertEqual( A, [1,12,6,15,32,39, 35, 31, 41, 38, 47,7])

    def test_partition_4(self):
        """ Emtpy R-partition """
        
        A = [7, 12, 6, 15, 32, 39, 35, 31, 41, 38, 47, 50 ]
        partition(A, 0, 11)
        self.assertEqual( A, [7,12,6,15,32,39, 35, 31, 41, 38, 47,50])

    def test_quicksort_1(self):
        """ Non repeated numbers"""
        
        A = [1, 12, 6, 15, 32, 39, 35, 31, 41, 38, 47, 7 ]
        QuickSort(A, 0, 11)
        self.assertEqual( A, [1,6,7,12,15,31,32,35,38,39,41,47])

    def test_quicksort_2(self):
        """ Repeated numbers """
        
        A = [ 5, 2, 4, 7, 1, 3, 2, 6 ]
        QuickSort(A, 0, 7)
        self.assertEqual( A, [ 1, 2, 2, 3, 4, 5, 6, 7 ])

    def test_quicksort_uneven_length(self):
        """ Array of uneven length """
        
        A = [ 5, 4, 7, 1, 3, 2, 6 ]
        QuickSort(A, 0, 6)
        self.assertEqual( A, [ 1, 2, 3, 4, 5, 6, 7 ])
    
    def test_quicksort_2_element_array(self):
        """special case: 2-element array """
        
        A = [ 5, 4 ]
        QuickSort(A, 0, 1)
        self.assertEqual( A, [4, 5])
    
    def test_quicksort_1_element_array(self):
        """ special case: 1-element array"""
        
        A = [ 5 ]
        QuickSort(A, 0, 0)
        self.assertEqual( A, [5])


def main():
    unittest.main()

if __name__ == '__main__':
    main()
