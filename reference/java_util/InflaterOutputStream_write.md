#### write

```
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```
Writes an array of bytes to the uncompressed output stream.
Overrides:
`write` in class `FilterOutputStream`
Parameters:
`b` - buffer containing compressed data to decompress and write to
the output stream
`off` - starting offset of the compressed data within `b`
`len` - number of bytes to decompress from `b`
Throws:
`IndexOutOfBoundsException` - if `off < 0`, or if
`len < 0`, or if `len > b.length - off`
`IOException` - if an I/O error occurs or this stream is already
closed
`NullPointerException` - if `b` is null
`ZipException` - if a compression (ZIP) format error occurs
See Also:
`FilterOutputStream.write(int)`




