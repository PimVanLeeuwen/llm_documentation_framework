#### reset

```
public void reset()
           throws IOException
```
Repositions this stream to the position at the time the
`mark` method was last called on this input stream.The method `reset` for class
`InflaterInputStream` does nothing except throw an
`IOException`.
Overrides:
`reset` in class `FilterInputStream`
Throws:
`IOException` - if this method is invoked.
See Also:
`InputStream.mark(int)`,
`IOException`




