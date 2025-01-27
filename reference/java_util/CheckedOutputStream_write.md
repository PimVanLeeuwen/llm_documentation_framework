#### write

```
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```
Writes an array of bytes. Will block until the bytes are
actually written.
Overrides:
`write` in class `FilterOutputStream`
Parameters:
`b` - the data to be written
`off` - the start offset of the data
`len` - the number of bytes to be written
Throws:
`IOException` - if an I/O error has occurred
See Also:
`FilterOutputStream.write(int)`

