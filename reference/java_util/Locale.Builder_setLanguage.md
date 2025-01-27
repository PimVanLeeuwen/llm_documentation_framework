#### setLanguage

```
public Locale.Builder setLanguage(String language)
```
Sets the language. If `language` is the empty string or
null, the language in this `Builder` is removed. Otherwise,
the language must be well-formed
or an exception is thrown.The typical language value is a two or three-letter language
code as defined in ISO639.
Parameters:
`language` - the language
Returns:
This builder.
Throws:
`IllformedLocaleException` - if `language` is ill-formed

