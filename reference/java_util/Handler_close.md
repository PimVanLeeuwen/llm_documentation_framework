#### close

```
public abstract void close()
                    throws SecurityException
```
Close the Handler and free all associated resources.The close method will perform a flush and then close the
Handler. After close has been called this Handler
should no longer be used. Method calls may either be silently
ignored or may throw runtime exceptions.
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

