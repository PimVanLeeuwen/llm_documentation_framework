#### copyOf

```
public static boolean[] copyOf(boolean[] original,
                               int newLength)
```
Copies the specified array, truncating or padding with false (if necessary)
so the copy has the specified length. For all indices that are
valid in both the original array and the copy, the two arrays will
contain identical values. For any indices that are valid in the
copy but not the original, the copy will contain false.
Such indices will exist if and only if the specified length
is greater than that of the original array.
Parameters:
`original` - the array to be copied
`newLength` - the length of the copy to be returned
Returns:
a copy of the original array, truncated or padded with false elements
to obtain the specified length
Throws:
`NegativeArraySizeException` - if newLength is negative
`NullPointerException` - if original is null
Since:
1.6

