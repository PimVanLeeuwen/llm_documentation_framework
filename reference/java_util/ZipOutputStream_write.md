#### write

```
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```
Writes an array of bytes to the current ZIP entry data. This method
will block until all the bytes are written.
Overrides:
`write` in class `DeflaterOutputStream`
Parameters:
`b` - the data to be written
`off` - the start offset in the data
`len` - the number of bytes that are written
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
See Also:
`FilterOutputStream.write(int)`

