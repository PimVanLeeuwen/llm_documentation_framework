#### reset

```
public void reset()
           throws SecurityException
```
Reset the logging configuration.For all named loggers, the reset operation removes and closes
all Handlers and (except for the root logger) sets the level
to null. The root logger's level is set to Level.INFO.
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

