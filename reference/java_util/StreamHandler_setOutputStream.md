#### setOutputStream

```
protected void setOutputStream(OutputStream out)
                        throws SecurityException
```
Change the output stream.If there is a current output stream then the Formatter's
tail string is written and the stream is flushed and closed.
Then the output stream is replaced with the new output stream.
Parameters:
`out` - New output stream. May not be null.
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

