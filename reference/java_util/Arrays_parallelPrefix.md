#### parallelPrefix

```
public static void parallelPrefix(int[] array,
                                  int fromIndex,
                                  int toIndex,
                                  IntBinaryOperator op)
```
Performs `parallelPrefix(int[], IntBinaryOperator)`
for the given subrange of the array.
Parameters:
`array` - the array
`fromIndex` - the index of the first element, inclusive
`toIndex` - the index of the last element, exclusive
`op` - a side-effect-free, associative function to perform the
cumulation
Throws:
`IllegalArgumentException` - if `fromIndex > toIndex`
`ArrayIndexOutOfBoundsException` - if `fromIndex < 0` or `toIndex > array.length`
`NullPointerException` - if the specified array or function is null
Since:
1.8

