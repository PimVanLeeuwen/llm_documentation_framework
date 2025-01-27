#### skip

```
public long skip(long n)
          throws IOException
```
Skips over and discards data from the input stream.
This method may block until the specified number of bytes are read and
skipped. Note: While `n` is given as a `long`,
the maximum number of bytes which can be skipped is
`Integer.MAX_VALUE`.
Overrides:
`skip` in class `FilterInputStream`
Parameters:
`n` - number of bytes to be skipped
Returns:
the actual number of bytes skipped
Throws:
`IOException` - if an I/O error occurs or if this stream is
already closed

