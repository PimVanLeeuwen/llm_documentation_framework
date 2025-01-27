#### mark

```
public void mark(int readlimit)
```
Marks the current position in this input stream.The `mark` method of `InflaterInputStream`
does nothing.
Overrides:
`mark` in class `FilterInputStream`
Parameters:
`readlimit` - the maximum limit of bytes that can be read before
the mark position becomes invalid.
See Also:
`InputStream.reset()`

