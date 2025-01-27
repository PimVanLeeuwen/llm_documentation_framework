#### putNextEntry

```
public void putNextEntry(ZipEntry e)
                  throws IOException
```
Begins writing a new ZIP file entry and positions the stream to the
start of the entry data. Closes the current entry if still active.
The default compression method will be used if no compression method
was specified for the entry, and the current time will be used if
the entry has no set modification time.
Parameters:
`e` - the ZIP entry to be written
Throws:
`ZipException` - if a ZIP format error has occurred
`IOException` - if an I/O error has occurred

