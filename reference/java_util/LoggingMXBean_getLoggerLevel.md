#### getLoggerLevel

```
String getLoggerLevel(String loggerName)
```
Gets the name of the log level associated with the specified logger.
If the specified logger does not exist, null
is returned.
This method first finds the logger of the given name and
then returns the name of the log level by calling:`Logger.getLevel()`.`getName()`;If the Level of the specified logger is null,
which means that this logger's effective level is inherited
from its parent, an empty string will be returned.
Parameters:
`loggerName` - The name of the Logger to be retrieved.
Returns:
The name of the log level of the specified logger; or
an empty string if the log level of the specified logger
is null. If the specified logger does not
exist, null is returned.
See Also:
`Logger.getLevel()`

