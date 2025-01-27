#### write

```
public void write(byte[] buf,
                  int off,
                  int len)
           throws IOException
```
Writes array of bytes to the compressed output stream. This method
will block until all the bytes are written.
Overrides:
`write` in class `DeflaterOutputStream`
Parameters:
`buf` - the data to be written
`off` - the start offset of the data
`len` - the length of the data
Throws:
`IOException` - If an I/O error has occurred.
See Also:
`FilterOutputStream.write(int)`

