#### publish

```
public void publish(LogRecord record)
```
Publish a LogRecord.The logging request was made initially to a Logger object,
which initialized the LogRecord and forwarded it here.
Overrides:
`publish` in class `StreamHandler`
Parameters:
`record` - description of the log event. A null record is
silently ignored and is not published

