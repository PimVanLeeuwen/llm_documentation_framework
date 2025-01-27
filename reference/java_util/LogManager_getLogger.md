#### getLogger

```
public Logger getLogger(String name)
```
Method to find a named logger.Note that since untrusted code may create loggers with
arbitrary names this method should not be relied on to
find Loggers for security sensitive logging.
It is also important to note that the Logger associated with the
String `name` may be garbage collected at any time if there
is no strong reference to the Logger. The caller of this method
must check the return value for null in order to properly handle
the case where the Logger has been garbage collected.
Parameters:
`name` - name of the logger
Returns:
matching logger or null if none is found

