#### format

```
public abstract String format(LogRecord record)
```
Format the given log record and return the formatted string.The resulting formatted String will normally include a
localized and formatted version of the LogRecord's message field.
It is recommended to use the `formatMessage(java.util.logging.LogRecord)`
convenience method to localize and format the message field.
Parameters:
`record` - the log record to be formatted.
Returns:
the formatted log record

