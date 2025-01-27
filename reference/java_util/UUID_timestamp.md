#### timestamp

```
public long timestamp()
```
The timestamp value associated with this UUID.The 60 bit timestamp value is constructed from the time\_low,
time\_mid, and time\_hi fields of this `UUID`. The resulting
timestamp is measured in 100-nanosecond units since midnight,
October 15, 1582 UTC.The timestamp value is only meaningful in a time-based UUID, which
has version type 1. If this `UUID` is not a time-based UUID then
this method throws UnsupportedOperationException.
Returns:
The timestamp of this `UUID`.
Throws:
`UnsupportedOperationException` - If this UUID is not a version 1 UUID

