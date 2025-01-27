#### valueOf

```
public static BitSet valueOf(ByteBuffer bb)
```
Returns a new bit set containing all the bits in the given byte
buffer between its position and limit.More precisely,
`BitSet.valueOf(bb).get(n) == ((bb.get(bb.position()+n/8) & (1<<(n%8))) != 0)`
for all `n < 8 * bb.remaining()`.The byte buffer is not modified by this method, and no
reference to the buffer is retained by the bit set.
Parameters:
`bb` - a byte buffer containing a little-endian representation
of a sequence of bits between its position and limit, to be
used as the initial bits of the new bit set
Returns:
a `BitSet` containing all the bits in the buffer in the
specified range
Since:
1.7

