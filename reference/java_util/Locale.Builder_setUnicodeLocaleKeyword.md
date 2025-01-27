#### setUnicodeLocaleKeyword

```
public Locale.Builder setUnicodeLocaleKeyword(String key,
                                              String type)
```
Sets the Unicode locale keyword type for the given key. If the type
is null, the Unicode keyword is removed. Otherwise, the key must be
non-null and both key and type must be well-formed or an exception
is thrown.Keys and types are converted to lower case.Note:Setting the 'u' extension via `setExtension(char, java.lang.String)`
replaces all Unicode locale keywords with those defined in the
extension.
Parameters:
`key` - the Unicode locale key
`type` - the Unicode locale type
Returns:
This builder.
Throws:
`IllformedLocaleException` - if `key` or `type`
is ill-formed
`NullPointerException` - if `key` is null
See Also:
`setExtension(char, String)`

