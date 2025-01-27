#### read

```
public int read(byte[] b,
                int off,
                int len)
         throws IOException
```
Reads uncompressed data into an array of bytes. If `len` is not
zero, the method will block until some input can be decompressed; otherwise,
no bytes are read and `0` is returned.
Overrides:
`read` in class `FilterInputStream`
Parameters:
`b` - the buffer into which the data is read
`off` - the start offset in the destination array `b`
`len` - the maximum number of bytes read
Returns:
the actual number of bytes read, or -1 if the end of the
compressed input is reached or a preset dictionary is needed
Throws:
`NullPointerException` - If `b` is `null`.
`IndexOutOfBoundsException` - If `off` is negative,
`len` is negative, or `len` is greater than
`b.length - off`
`ZipException` - if a ZIP format error has occurred
`IOException` - if an I/O error has occurred
See Also:
`FilterInputStream.in`

