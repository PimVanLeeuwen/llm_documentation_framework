#### putNextEntry

```
public void putNextEntry(ZipEntry ze)
                  throws IOException
```
Begins writing a new JAR file entry and positions the stream
to the start of the entry data. This method will also close
any previous entry. The default compression method will be
used if no compression method was specified for the entry.
The current time will be used if the entry has no set modification
time.
Overrides:
`putNextEntry` in class `ZipOutputStream`
Parameters:
`ze` - the ZIP/JAR entry to be written
Throws:
`ZipException` - if a ZIP error has occurred
`IOException` - if an I/O error has occurred




