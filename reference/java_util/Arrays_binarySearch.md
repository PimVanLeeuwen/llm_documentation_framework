#### binarySearch

```
public static <T> int binarySearch(T[] a,
                                   int fromIndex,
                                   int toIndex,
                                   T key,
                                   Comparator<? super T> c)
```
Searches a range of
the specified array for the specified object using the binary
search algorithm.
The range must be sorted into ascending order
according to the specified comparator (as by the
`sort(T[], int, int, Comparator)`
method) prior to making this call.
If it is not sorted, the results are undefined.
If the range contains multiple elements equal to the specified object,
there is no guarantee which one will be found.
Type Parameters:
`T` - the class of the objects in the array
Parameters:
`a` - the array to be searched
`fromIndex` - the index of the first element (inclusive) to be
searched
`toIndex` - the index of the last element (exclusive) to be searched
`key` - the value to be searched for
`c` - the comparator by which the array is ordered. A
null value indicates that the elements'
natural ordering should be used.
Returns:
index of the search key, if it is contained in the array
within the specified range;
otherwise, (-(insertion point) - 1). The
insertion point is defined as the point at which the
key would be inserted into the array: the index of the first
element in the range greater than the key,
or toIndex if all
elements in the range are less than the specified key. Note
that this guarantees that the return value will be >= 0 if
and only if the key is found.
Throws:
`ClassCastException` - if the range contains elements that are not
mutually comparable using the specified comparator,
or the search key is not comparable to the
elements in the range using this comparator.
`IllegalArgumentException` - if `fromIndex > toIndex`
`ArrayIndexOutOfBoundsException` - if `fromIndex < 0 or toIndex > a.length`
Since:
1.6

