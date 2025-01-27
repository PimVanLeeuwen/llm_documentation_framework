#### read

```
public int read(byte[] buf,
                int off,
                int len)
         throws IOException
```
Reads into an array of bytes. If `len` is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and `0` is returned.
Overrides:
`read` in class `FilterInputStream`
Parameters:
`buf` - the buffer into which the data is read
`off` - the start offset in the destination array `b`
`len` - the maximum number of bytes read
Returns:
the actual number of bytes read, or -1 if the end
of the stream is reached.
Throws:
`NullPointerException` - If `buf` is `null`.
`IndexOutOfBoundsException` - If `off` is negative,
`len` is negative, or `len` is greater than
`buf.length - off`
`IOException` - if an I/O error has occurred
See Also:
`FilterInputStream.in`

