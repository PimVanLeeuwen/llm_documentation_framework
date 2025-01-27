#### setUseParentHandlers

```
public void setUseParentHandlers(boolean useParentHandlers)
```
Specify whether or not this logger should send its output
to its parent Logger. This means that any LogRecords will
also be written to the parent's Handlers, and potentially
to its parent, recursively up the namespace.
Parameters:
`useParentHandlers` - true if output is to be sent to the
logger's parent.
Throws:
`SecurityException` - if a security manager exists,
this logger is not anonymous, and the caller
does not have LoggingPermission("control").

