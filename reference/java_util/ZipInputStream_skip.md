#### skip

```
public long skip(long n)
          throws IOException
```
Skips specified number of bytes in the current ZIP entry.
Overrides:
`skip` in class `InflaterInputStream`
Parameters:
`n` - the number of bytes to skip
Returns:
the actual number of bytes skipped
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
`IllegalArgumentException` - if `n < 0`

