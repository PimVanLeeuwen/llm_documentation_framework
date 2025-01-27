#### setLevel

```
public void setLevel(int level)
```
Sets the compression level to the specified value.If the compression level is changed, the next invocation
of `deflate` will compress the input available so far
with the old level (and may be flushed); the new level will
take effect only after that invocation.
Parameters:
`level` - the new compression level (0-9)
Throws:
`IllegalArgumentException` - if the compression level is invalid

