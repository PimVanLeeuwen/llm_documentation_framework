#### close

```
public void close()
           throws SecurityException
```
Close the current output stream.The Formatter's "tail" string is written to the stream before it
is closed. In addition, if the Formatter's "head" string has not
yet been written to the stream, it will be written before the
"tail" string.
Specified by:
`close` in class `Handler`
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").




