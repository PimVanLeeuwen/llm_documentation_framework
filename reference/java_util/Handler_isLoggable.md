#### isLoggable

```
public boolean isLoggable(LogRecord record)
```
Check if this Handler would actually log a given LogRecord.This method checks if the LogRecord has an appropriate
Level and whether it satisfies any Filter. It also
may make other Handler specific checks that might prevent a
handler from logging the LogRecord. It will return false if
the LogRecord is null.
Parameters:
`record` - a LogRecord
Returns:
true if the LogRecord would be logged.




