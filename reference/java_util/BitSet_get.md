#### get

```
public BitSet get(int fromIndex,
                  int toIndex)
```
Returns a new `BitSet` composed of bits from this `BitSet`
from `fromIndex` (inclusive) to `toIndex` (exclusive).
Parameters:
`fromIndex` - index of the first bit to include
`toIndex` - index after the last bit to include
Returns:
a new `BitSet` from a range of this `BitSet`
Throws:
`IndexOutOfBoundsException` - if `fromIndex` is negative,
or `toIndex` is negative, or `fromIndex` is
larger than `toIndex`
Since:
1.4

