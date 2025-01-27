#### node

```
public long node()
```
The node value associated with this UUID.The 48 bit node value is constructed from the node field of this
UUID. This field is intended to hold the IEEE 802 address of the machine
that generated this UUID to guarantee spatial uniqueness.The node value is only meaningful in a time-based UUID, which has
version type 1. If this UUID is not a time-based UUID then this method
throws UnsupportedOperationException.
Returns:
The node value of this `UUID`
Throws:
`UnsupportedOperationException` - If this UUID is not a version 1 UUID

