#### set

```
public void set(int fromIndex,
                int toIndex,
                boolean value)
```
Sets the bits from the specified `fromIndex` (inclusive) to the
specified `toIndex` (exclusive) to the specified value.
Parameters:
`fromIndex` - index of the first bit to be set
`toIndex` - index after the last bit to be set
`value` - value to set the selected bits to
Throws:
`IndexOutOfBoundsException` - if `fromIndex` is negative,
or `toIndex` is negative, or `fromIndex` is
larger than `toIndex`
Since:
1.4

