#### read

```
public int read(byte[] b,
                int off,
                int len)
         throws IOException
```
Reads from the current JAR file entry into an array of bytes.
If `len` is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and `0` is returned.
If verification has been enabled, any invalid signature
on the current entry will be reported at some point before the
end of the entry is reached.
Overrides:
`read` in class `ZipInputStream`
Parameters:
`b` - the buffer into which the data is read
`off` - the start offset in the destination array `b`
`len` - the maximum number of bytes to read
Returns:
the actual number of bytes read, or -1 if the end of the
entry is reached
Throws:
`NullPointerException` - If `b` is `null`.
`IndexOutOfBoundsException` - If `off` is negative,
`len` is negative, or `len` is greater than
`b.length - off`
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
`SecurityException` - if any of the jar file entries
are incorrectly signed.
See Also:
`FilterInputStream.in`

