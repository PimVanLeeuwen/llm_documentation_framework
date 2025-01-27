#### setFilter

```
public void setFilter(Filter newFilter)
               throws SecurityException
```
Set a Filter to control output on this Handler.For each call of publish the Handler will call
this Filter (if it is non-null) to check if the
LogRecord should be published or discarded.
Parameters:
`newFilter` - a Filter object (may be null)
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

