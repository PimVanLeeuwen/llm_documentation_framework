#### format

```
public String format(LogRecord record)
```
Format the given message to XML.This method can be overridden in a subclass.
It is recommended to use the `Formatter.formatMessage(java.util.logging.LogRecord)`
convenience method to localize and format the message field.
Specified by:
`format` in class `Formatter`
Parameters:
`record` - the log record to be formatted.
Returns:
a formatted log record

