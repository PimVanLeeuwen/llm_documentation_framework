#### markSupported

```
public boolean markSupported()
```
Tests if this input stream supports the `mark` and
`reset` methods. The `markSupported`
method of `InflaterInputStream` returns
`false`.
Overrides:
`markSupported` in class `FilterInputStream`
Returns:
a `boolean` indicating if this stream type supports
the `mark` and `reset` methods.
See Also:
`InputStream.mark(int)`,
`InputStream.reset()`

