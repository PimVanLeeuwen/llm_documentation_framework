#### sort

```
public static <T> void sort(T[] a,
                            int fromIndex,
                            int toIndex,
                            Comparator<? super T> c)
```
Sorts the specified range of the specified array of objects according
to the order induced by the specified comparator. The range to be
sorted extends from index `fromIndex`, inclusive, to index
`toIndex`, exclusive. (If `fromIndex==toIndex`, the
range to be sorted is empty.) All elements in the range must be
mutually comparable by the specified comparator (that is,
`c.compare(e1, e2)` must not throw a `ClassCastException`
for any elements `e1` and `e2` in the range).This sort is guaranteed to be stable: equal elements will
not be reordered as a result of the sort.Implementation note: This implementation is a stable, adaptive,
iterative mergesort that requires far fewer than n lg(n) comparisons
when the input array is partially sorted, while offering the
performance of a traditional mergesort when the input array is
randomly ordered. If the input array is nearly sorted, the
implementation requires approximately n comparisons. Temporary
storage requirements vary from a small constant for nearly sorted
input arrays to n/2 object references for randomly ordered input
arrays.The implementation takes equal advantage of ascending and
descending order in its input array, and can take advantage of
ascending and descending order in different parts of the the same
input array. It is well-suited to merging two or more sorted arrays:
simply concatenate the arrays and sort the resulting array.The implementation was adapted from Tim Peters's list sort for Python
(
TimSort). It uses techniques from Peter McIlroy's "Optimistic
Sorting and Information Theoretic Complexity", in Proceedings of the
Fourth Annual ACM-SIAM Symposium on Discrete Algorithms, pp 467-474,
January 1993.
Type Parameters:
`T` - the class of the objects to be sorted
Parameters:
`a` - the array to be sorted
`fromIndex` - the index of the first element (inclusive) to be
sorted
`toIndex` - the index of the last element (exclusive) to be sorted
`c` - the comparator to determine the order of the array. A
`null` value indicates that the elements'
natural ordering should be used.
Throws:
`ClassCastException` - if the array contains elements that are not
mutually comparable using the specified comparator.
`IllegalArgumentException` - if `fromIndex > toIndex` or
(optional) if the comparator is found to violate the
`Comparator` contract
`ArrayIndexOutOfBoundsException` - if `fromIndex < 0` or
`toIndex > a.length`

