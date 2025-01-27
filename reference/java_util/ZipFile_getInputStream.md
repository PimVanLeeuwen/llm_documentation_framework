#### getInputStream

```
public InputStream getInputStream(ZipEntry entry)
                           throws IOException
```
Returns an input stream for reading the contents of the specified
zip file entry.Closing this ZIP file will, in turn, close all input
streams that have been returned by invocations of this method.
Parameters:
`entry` - the zip file entry
Returns:
the input stream for reading the contents of the specified
zip file entry.
Throws:
`ZipException` - if a ZIP format error has occurred
`IOException` - if an I/O error has occurred
`IllegalStateException` - if the zip file has been closed

