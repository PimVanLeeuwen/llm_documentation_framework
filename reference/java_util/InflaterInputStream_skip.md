#### skip

```
public long skip(long n)
          throws IOException
```
Skips specified number of bytes of uncompressed data.
Overrides:
`skip` in class `FilterInputStream`
Parameters:
`n` - the number of bytes to skip
Returns:
the actual number of bytes skipped.
Throws:
`IOException` - if an I/O error has occurred
`IllegalArgumentException` - if `n < 0`

