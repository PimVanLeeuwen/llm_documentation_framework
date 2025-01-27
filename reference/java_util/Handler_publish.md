#### publish

```
public abstract void publish(LogRecord record)
```
Publish a LogRecord.The logging request was made initially to a Logger object,
which initialized the LogRecord and forwarded it here.The Handler is responsible for formatting the message, when and
if necessary. The formatting should include localization.
Parameters:
`record` - description of the log event. A null record is
silently ignored and is not published

