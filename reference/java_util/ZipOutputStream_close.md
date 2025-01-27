#### close

```
public void close()
           throws IOException
```
Closes the ZIP output stream as well as the stream being filtered.
Specified by:
`close` in interface `Closeable`
Specified by:
`close` in interface `AutoCloseable`
Overrides:
`close` in class `DeflaterOutputStream`
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
See Also:
`FilterOutputStream.flush()`,
`FilterOutputStream.out`




