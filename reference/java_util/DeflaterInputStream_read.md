#### read

```
public int read(byte[] b,
                int off,
                int len)
         throws IOException
```
Reads compressed data into a byte array.
This method will block until some input can be read and compressed.
Overrides:
`read` in class `FilterInputStream`
Parameters:
`b` - buffer into which the data is read
`off` - starting offset of the data within `b`
`len` - maximum number of compressed bytes to read into `b`
Returns:
the actual number of bytes read, or -1 if the end of the
uncompressed input stream is reached
Throws:
`IndexOutOfBoundsException` - if `len > b.length - off`
`IOException` - if an I/O error occurs or if this input stream is
already closed
See Also:
`FilterInputStream.in`

