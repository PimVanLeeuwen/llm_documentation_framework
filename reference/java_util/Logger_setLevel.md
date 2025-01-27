#### setLevel

```
public void setLevel(Level newLevel)
              throws SecurityException
```
Set the log level specifying which message levels will be
logged by this logger. Message levels lower than this
value will be discarded. The level value Level.OFF
can be used to turn off logging.If the new level is null, it means that this node should
inherit its level from its nearest ancestor with a specific
(non-null) level value.
Parameters:
`newLevel` - the new value for the log level (may be null)
Throws:
`SecurityException` - if a security manager exists,
this logger is not anonymous, and the caller
does not have LoggingPermission("control").

