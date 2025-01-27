#### setScript

```
public Locale.Builder setScript(String script)
```
Sets the script. If `script` is null or the empty string,
the script in this `Builder` is removed.
Otherwise, the script must be well-formed or an
exception is thrown.The typical script value is a four-letter script code as defined by ISO 15924.
Parameters:
`script` - the script
Returns:
This builder.
Throws:
`IllformedLocaleException` - if `script` is ill-formed

