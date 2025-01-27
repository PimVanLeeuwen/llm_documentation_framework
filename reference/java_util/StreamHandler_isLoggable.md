#### isLoggable

```
public boolean isLoggable(LogRecord record)
```
Check if this Handler would actually log a given LogRecord.This method checks if the LogRecord has an appropriate level and
whether it satisfies any Filter. It will also return false if
no output stream has been assigned yet or the LogRecord is null.
Overrides:
`isLoggable` in class `Handler`
Parameters:
`record` - a LogRecord
Returns:
true if the LogRecord would be logged.

