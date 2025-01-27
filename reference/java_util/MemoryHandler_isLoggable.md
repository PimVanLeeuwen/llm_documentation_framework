#### isLoggable

```
public boolean isLoggable(LogRecord record)
```
Check if this Handler would actually log a given
LogRecord into its internal buffer.This method checks if the LogRecord has an appropriate level and
whether it satisfies any Filter. However it does not
check whether the LogRecord would result in a "push" of the
buffer contents. It will return false if the LogRecord is null.
Overrides:
`isLoggable` in class `Handler`
Parameters:
`record` - a LogRecord
Returns:
true if the LogRecord would be logged.




