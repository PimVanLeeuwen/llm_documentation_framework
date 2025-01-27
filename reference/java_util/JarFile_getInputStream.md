#### getInputStream

```
public InputStream getInputStream(ZipEntry ze)
                           throws IOException
```
Returns an input stream for reading the contents of the specified
zip file entry.
Overrides:
`getInputStream` in class `ZipFile`
Parameters:
`ze` - the zip file entry
Returns:
an input stream for reading the contents of the specified
zip file entry
Throws:
`ZipException` - if a zip file format error has occurred
`IOException` - if an I/O error has occurred
`SecurityException` - if any of the jar file entries
are incorrectly signed.
`IllegalStateException` - may be thrown if the jar file has been closed




