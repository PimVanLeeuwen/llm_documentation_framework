#### setCrc

```
public void setCrc(long crc)
```
Sets the CRC-32 checksum of the uncompressed entry data.
Parameters:
`crc` - the CRC-32 value
Throws:
`IllegalArgumentException` - if the specified CRC-32 value is
less than 0 or greater than 0xFFFFFFFF
See Also:
`getCrc()`

