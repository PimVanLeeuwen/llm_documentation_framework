#### inflate

```
public int inflate(byte[] b)
            throws DataFormatException
```
Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.
Parameters:
`b` - the buffer for the uncompressed data
Returns:
the actual number of uncompressed bytes
Throws:
`DataFormatException` - if the compressed data format is invalid
See Also:
`needsInput()`,
`needsDictionary()`

