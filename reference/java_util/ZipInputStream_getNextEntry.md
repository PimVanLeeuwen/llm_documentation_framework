#### getNextEntry

```
public ZipEntry getNextEntry()
                      throws IOException
```
Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.
Returns:
the next ZIP file entry, or null if there are no more entries
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred

