#### toByteArray

```
public byte[] toByteArray()
```
Returns a new byte array containing all the bits in this bit set.More precisely, if
`byte[] bytes = s.toByteArray();`
then `bytes.length == (s.length()+7)/8` and
`s.get(n) == ((bytes[n/8] & (1<<(n%8))) != 0)`
for all `n < 8 * bytes.length`.
Returns:
a byte array containing a little-endian representation
of all the bits in this bit set
Since:
1.7

