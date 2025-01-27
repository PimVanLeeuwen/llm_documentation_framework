#### setLoggerLevel

```
void setLoggerLevel(String loggerName,
                    String levelName)
```
Sets the specified logger to the specified new level.
If the levelName is not null, the level
of the specified logger is set to the parsed Level
matching the levelName.
If the levelName is null, the level
of the specified logger is set to null and
the effective level of the logger is inherited from
its nearest ancestor with a specific (non-null) level value.
Parameters:
`loggerName` - The name of the Logger to be set.
Must be non-null.
`levelName` - The name of the level to set on the specified logger,
or null if setting the level to inherit
from its nearest ancestor.
Throws:
`IllegalArgumentException` - if the specified logger
does not exist, or levelName is not a valid level name.
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").
See Also:
`Logger.setLevel(java.util.logging.Level)`

