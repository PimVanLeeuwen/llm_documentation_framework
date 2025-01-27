#### checkAccess

```
public void checkAccess()
                 throws SecurityException
```
Check that the current context is trusted to modify the logging
configuration. This requires LoggingPermission("control").If the check fails we throw a SecurityException, otherwise
we return normally.
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

