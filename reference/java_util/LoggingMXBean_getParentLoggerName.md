#### getParentLoggerName

```
String getParentLoggerName(String loggerName)
```
Returns the name of the parent for the specified logger.
If the specified logger does not exist, null is returned.
If the specified logger is the root Logger in the namespace,
the result will be an empty string.
Parameters:
`loggerName` - The name of a Logger.
Returns:
the name of the nearest existing parent logger;
an empty string if the specified logger is the root logger.
If the specified logger does not exist, null
is returned.




