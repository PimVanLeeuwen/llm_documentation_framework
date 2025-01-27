#### getMessage

```
public String getMessage()
```
Get the "raw" log message, before localization or formatting.May be null, which is equivalent to the empty string "".This message may be either the final text or a localization key.During formatting, if the source logger has a localization
ResourceBundle and if that ResourceBundle has an entry for
this message string, then the message string is replaced
with the localized value.
Returns:
the raw message string

