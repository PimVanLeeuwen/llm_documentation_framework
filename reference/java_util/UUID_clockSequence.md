#### clockSequence

```
public int clockSequence()
```
The clock sequence value associated with this UUID.The 14 bit clock sequence value is constructed from the clock
sequence field of this UUID. The clock sequence field is used to
guarantee temporal uniqueness in a time-based UUID.The `clockSequence` value is only meaningful in a time-based
UUID, which has version type 1. If this UUID is not a time-based UUID
then this method throws UnsupportedOperationException.
Returns:
The clock sequence of this `UUID`
Throws:
`UnsupportedOperationException` - If this UUID is not a version 1 UUID

