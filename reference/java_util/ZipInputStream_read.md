#### read

```
public int read(byte[] b,
                int off,
                int len)
         throws IOException
```
Reads from the current ZIP entry into an array of bytes.
If `len` is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and `0` is returned.
Overrides:
`read` in class `InflaterInputStream`
Parameters:
`b` - the buffer into which the data is read
`off` - the start offset in the destination array `b`
`len` - the maximum number of bytes read
Returns:
the actual number of bytes read, or -1 if the end of the
entry is reached
Throws:
`NullPointerException` - if `b` is `null`.
`IndexOutOfBoundsException` - if `off` is negative,
`len` is negative, or `len` is greater than
`b.length - off`
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
See Also:
`FilterInputStream.in`

