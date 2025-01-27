#### formatMessage

```
public String formatMessage(LogRecord record)
```
Localize and format the message string from a log record. This
method is provided as a convenience for Formatter subclasses to
use when they are performing formatting.The message string is first localized to a format string using
the record's ResourceBundle. (If there is no ResourceBundle,
or if the message key is not found, then the key is used as the
format string.) The format String uses java.text style
formatting.If there are no parameters, no formatter is used.Otherwise, if the string contains "{0" then
java.text.MessageFormat is used to format the string.Otherwise no formatting is performed.
Parameters:
`record` - the log record containing the raw message
Returns:
a localized and formatted message




