#### setParent

```
public void setParent(Logger parent)
```
Set the parent for this Logger. This method is used by
the LogManager to update a Logger when the namespace changes.It should not be called from application code.
Parameters:
`parent` - the new parent logger
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").




