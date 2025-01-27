#### isLoggable

```
public boolean isLoggable(Level level)
```
Check if a message of the given level would actually be logged
by this logger. This check is based on the Loggers effective level,
which may be inherited from its parent.
Parameters:
`level` - a message logging level
Returns:
true if the given message level is currently being logged.

