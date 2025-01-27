#### setFormatter

```
public void setFormatter(Formatter newFormatter)
                  throws SecurityException
```
Set a Formatter. This Formatter will be used
to format LogRecords for this Handler.Some Handlers may not use Formatters, in
which case the Formatter will be remembered, but not used.
Parameters:
`newFormatter` - the Formatter to use (may not be null)
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

