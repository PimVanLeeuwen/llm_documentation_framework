#### nextSetBit

```
public int nextSetBit(int fromIndex)
```
Returns the index of the first bit that is set to `true`
that occurs on or after the specified starting index. If no such
bit exists then `-1` is returned.To iterate over the `true` bits in a `BitSet`,
use the following loop:
```
 
 for (int i = bs.nextSetBit(0); i >= 0; i = bs.nextSetBit(i+1)) {
     // operate on index i here
     if (i == Integer.MAX_VALUE) {
         break; // or (i+1) would overflow
     }
 }
```

Parameters:
`fromIndex` - the index to start checking from (inclusive)
Returns:
the index of the next set bit, or `-1` if there
is no such bit
Throws:
`IndexOutOfBoundsException` - if the specified index is negative
Since:
1.4

