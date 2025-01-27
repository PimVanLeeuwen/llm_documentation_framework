#### setLevel

```
public void setLevel(Level newLevel)
              throws SecurityException
```
Set the log level specifying which message levels will be
logged by this Handler. Message levels lower than this
value will be discarded.The intention is to allow developers to turn on voluminous
logging, but to limit the messages that are sent to certain
Handlers.
Parameters:
`newLevel` - the new value for the log level
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

