#### setPushLevel

```
public void setPushLevel(Level newLevel)
                  throws SecurityException
```
Set the pushLevel. After a LogRecord is copied
into our internal buffer, if its level is greater than or equal to
the pushLevel, then push will be called.
Parameters:
`newLevel` - the new value of the pushLevel
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

