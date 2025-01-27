#### previousClearBit

```
public int previousClearBit(int fromIndex)
```
Returns the index of the nearest bit that is set to `false`
that occurs on or before the specified starting index.
If no such bit exists, or if `-1` is given as the
starting index, then `-1` is returned.
Parameters:
`fromIndex` - the index to start checking from (inclusive)
Returns:
the index of the previous clear bit, or `-1` if there
is no such bit
Throws:
`IndexOutOfBoundsException` - if the specified index is less
than `-1`
Since:
1.7

