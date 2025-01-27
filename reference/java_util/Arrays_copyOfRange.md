#### copyOfRange

```
public static boolean[] copyOfRange(boolean[] original,
                                    int from,
                                    int to)
```
Copies the specified range of the specified array into a new array.
The initial index of the range (from) must lie between zero
and original.length, inclusive. The value at
original[from] is placed into the initial element of the copy
(unless from == original.length or from == to).
Values from subsequent elements in the original array are placed into
subsequent elements in the copy. The final index of the range
(to), which must be greater than or equal to from,
may be greater than original.length, in which case
false is placed in all elements of the copy whose index is
greater than or equal to original.length - from. The length
of the returned array will be to - from.
Parameters:
`original` - the array from which a range is to be copied
`from` - the initial index of the range to be copied, inclusive
`to` - the final index of the range to be copied, exclusive.
(This index may lie outside the array.)
Returns:
a new array containing the specified range from the original array,
truncated or padded with false elements to obtain the required length
Throws:
`ArrayIndexOutOfBoundsException` - if `from < 0`
or `from > original.length`
`IllegalArgumentException` - if from > to
`NullPointerException` - if original is null
Since:
1.6

