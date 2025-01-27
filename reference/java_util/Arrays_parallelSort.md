#### parallelSort

```
public static <T> void parallelSort(T[] a,
                                    int fromIndex,
                                    int toIndex,
                                    Comparator<? super T> cmp)
```
Sorts the specified range of the specified array of objects according
to the order induced by the specified comparator. The range to be
sorted extends from index `fromIndex`, inclusive, to index
`toIndex`, exclusive. (If `fromIndex==toIndex`, the
range to be sorted is empty.) All elements in the range must be
mutually comparable by the specified comparator (that is,
`c.compare(e1, e2)` must not throw a `ClassCastException`
for any elements `e1` and `e2` in the range).This sort is guaranteed to be stable: equal elements will
not be reordered as a result of the sort.
Implementation Note:
The sorting algorithm is a parallel sort-merge that breaks the
array into sub-arrays that are themselves sorted and then merged. When
the sub-array length reaches a minimum granularity, the sub-array is
sorted using the appropriate `Arrays.sort`
method. If the length of the specified array is less than the minimum
granularity, then it is sorted using the appropriate `Arrays.sort` method. The algorithm requires a working
space no greater than the size of the specified range of the original
array. The `ForkJoin common pool` is
used to execute any parallel tasks.
Type Parameters:
`T` - the class of the objects to be sorted
Parameters:
`a` - the array to be sorted
`fromIndex` - the index of the first element (inclusive) to be
sorted
`toIndex` - the index of the last element (exclusive) to be sorted
`cmp` - the comparator to determine the order of the array. A
`null` value indicates that the elements'
natural ordering should be used.
Throws:
`IllegalArgumentException` - if `fromIndex > toIndex` or
(optional) if the natural ordering of the array elements is
found to violate the `Comparable` contract
`ArrayIndexOutOfBoundsException` - if `fromIndex < 0` or
`toIndex > a.length`
`ClassCastException` - if the array contains elements that are
not mutually comparable (for example, strings and
integers).
Since:
1.8

