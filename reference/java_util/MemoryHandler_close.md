#### close

```
public void close()
           throws SecurityException
```
Close the Handler and free all associated resources.
This will also close the target Handler.
Specified by:
`close` in class `Handler`
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

