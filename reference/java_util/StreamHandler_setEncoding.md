#### setEncoding

```
public void setEncoding(String encoding)
                 throws SecurityException,
                        UnsupportedEncodingException
```
Set (or change) the character encoding used by this Handler.The encoding should be set before any LogRecords are written
to the Handler.
Overrides:
`setEncoding` in class `Handler`
Parameters:
`encoding` - The name of a supported character encoding.
May be null, to indicate the default platform encoding.
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").
`UnsupportedEncodingException` - if the named encoding is
not supported.

