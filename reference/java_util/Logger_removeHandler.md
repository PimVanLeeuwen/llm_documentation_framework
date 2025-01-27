#### removeHandler

```
public void removeHandler(Handler handler)
                   throws SecurityException
```
Remove a log Handler.Returns silently if the given Handler is not found or is null
Parameters:
`handler` - a logging Handler
Throws:
`SecurityException` - if a security manager exists,
this logger is not anonymous, and the caller
does not have LoggingPermission("control").

