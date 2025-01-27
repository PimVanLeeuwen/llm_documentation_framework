#### addUnicodeLocaleAttribute

```
public Locale.Builder addUnicodeLocaleAttribute(String attribute)
```
Adds a unicode locale attribute, if not already present, otherwise
has no effect. The attribute must not be null and must be well-formed or an exception
is thrown.
Parameters:
`attribute` - the attribute
Returns:
This builder.
Throws:
`NullPointerException` - if `attribute` is null
`IllformedLocaleException` - if `attribute` is ill-formed
See Also:
`setExtension(char, String)`

