#### previousSetBit

```
public int previousSetBit(int fromIndex)
```
Returns the index of the nearest bit that is set to `true`
that occurs on or before the specified starting index.
If no such bit exists, or if `-1` is given as the
starting index, then `-1` is returned.To iterate over the `true` bits in a `BitSet`,
use the following loop:
```
 
 for (int i = bs.length(); (i = bs.previousSetBit(i-1)) >= 0; ) {
     // operate on index i here
 }
```

Parameters:
`fromIndex` - the index to start checking from (inclusive)
Returns:
the index of the previous set bit, or `-1` if there
is no such bit
Throws:
`IndexOutOfBoundsException` - if the specified index is less
than `-1`
Since:
1.7

