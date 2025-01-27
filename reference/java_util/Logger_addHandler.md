#### addHandler

```
public void addHandler(Handler handler)
                throws SecurityException
```
Add a log Handler to receive logging messages.By default, Loggers also send their output to their parent logger.
Typically the root Logger is configured with a set of Handlers
that essentially act as default handlers for all loggers.
Parameters:
`handler` - a logging Handler
Throws:
`SecurityException` - if a security manager exists,
this logger is not anonymous, and the caller
does not have LoggingPermission("control").

