#### toLongArray

```
public long[] toLongArray()
```
Returns a new long array containing all the bits in this bit set.More precisely, if
`long[] longs = s.toLongArray();`
then `longs.length == (s.length()+63)/64` and
`s.get(n) == ((longs[n/64] & (1L<<(n%64))) != 0)`
for all `n < 64 * longs.length`.
Returns:
a long array containing a little-endian representation
of all the bits in this bit set
Since:
1.7

