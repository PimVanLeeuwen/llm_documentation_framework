#### read

```
public int read(byte[] buf,
                int off,
                int len)
         throws IOException
```
Reads uncompressed data into an array of bytes. If `len` is not
zero, the method will block until some input can be decompressed; otherwise,
no bytes are read and `0` is returned.
Overrides:
`read` in class `InflaterInputStream`
Parameters:
`buf` - the buffer into which the data is read
`off` - the start offset in the destination array `b`
`len` - the maximum number of bytes read
Returns:
the actual number of bytes read, or -1 if the end of the
compressed input stream is reached
Throws:
`NullPointerException` - If `buf` is `null`.
`IndexOutOfBoundsException` - If `off` is negative,
`len` is negative, or `len` is greater than
`buf.length - off`
`ZipException` - if the compressed input data is corrupt.
`IOException` - if an I/O error has occurred.
See Also:
`FilterInputStream.in`

