#### fill

```
public static void fill(Object[] a,
                        int fromIndex,
                        int toIndex,
                        Object val)
```
Assigns the specified Object reference to each element of the specified
range of the specified array of Objects. The range to be filled
extends from index fromIndex, inclusive, to index
toIndex, exclusive. (If fromIndex==toIndex, the
range to be filled is empty.)
Parameters:
`a` - the array to be filled
`fromIndex` - the index of the first element (inclusive) to be
filled with the specified value
`toIndex` - the index of the last element (exclusive) to be
filled with the specified value
`val` - the value to be stored in all elements of the array
Throws:
`IllegalArgumentException` - if fromIndex > toIndex
`ArrayIndexOutOfBoundsException` - if fromIndex < 0 or
toIndex > a.length
`ArrayStoreException` - if the specified value is not of a
runtime type that can be stored in the specified array

