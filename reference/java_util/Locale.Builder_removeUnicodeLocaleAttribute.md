#### removeUnicodeLocaleAttribute

```
public Locale.Builder removeUnicodeLocaleAttribute(String attribute)
```
Removes a unicode locale attribute, if present, otherwise has no
effect. The attribute must not be null and must be well-formed or an exception
is thrown.Attribute comparision for removal is case-insensitive.
Parameters:
`attribute` - the attribute
Returns:
This builder.
Throws:
`NullPointerException` - if `attribute` is null
`IllformedLocaleException` - if `attribute` is ill-formed
See Also:
`setExtension(char, String)`

