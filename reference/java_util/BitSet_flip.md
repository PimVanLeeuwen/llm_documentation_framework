#### flip

```
public void flip(int fromIndex,
                 int toIndex)
```
Sets each bit from the specified `fromIndex` (inclusive) to the
specified `toIndex` (exclusive) to the complement of its current
value.
Parameters:
`fromIndex` - index of the first bit to flip
`toIndex` - index after the last bit to flip
Throws:
`IndexOutOfBoundsException` - if `fromIndex` is negative,
or `toIndex` is negative, or `fromIndex` is
larger than `toIndex`
Since:
1.4

