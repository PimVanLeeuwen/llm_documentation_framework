#### close

```
public void close()
           throws IOException
```
Closes the ZIP file.Closing this ZIP file will close all of the input streams
previously returned by invocations of the `getInputStream` method.
Specified by:
`close` in interface `Closeable`
Specified by:
`close` in interface `AutoCloseable`
Throws:
`IOException` - if an I/O error has occurred

