#### write

```
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```
Writes an array of bytes to the compressed output stream. This
method will block until all the bytes are written.
Overrides:
`write` in class `FilterOutputStream`
Parameters:
`b` - the data to be written
`off` - the start offset of the data
`len` - the length of the data
Throws:
`IOException` - if an I/O error has occurred
See Also:
`FilterOutputStream.write(int)`

