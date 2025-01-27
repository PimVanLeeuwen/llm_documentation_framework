#### setSize

```
public void setSize(long size)
```
Sets the uncompressed size of the entry data.
Parameters:
`size` - the uncompressed size in bytes
Throws:
`IllegalArgumentException` - if the specified size is less
than 0, is greater than 0xFFFFFFFF when
ZIP64 format is not supported,
or is less than 0 when ZIP64 is supported
See Also:
`getSize()`

