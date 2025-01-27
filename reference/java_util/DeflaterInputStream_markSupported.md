#### markSupported

```
public boolean markSupported()
```
Always returns `false` because this input stream does not support
the `mark()` and `reset()` methods.
Overrides:
`markSupported` in class `FilterInputStream`
Returns:
false, always
See Also:
`FilterInputStream.in`,
`InputStream.mark(int)`,
`InputStream.reset()`

