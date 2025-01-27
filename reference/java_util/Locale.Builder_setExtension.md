#### setExtension

```
public Locale.Builder setExtension(char key,
                                   String value)
```
Sets the extension for the given key. If the value is null or the
empty string, the extension is removed. Otherwise, the extension
must be well-formed or an exception
is thrown.Note: The key `UNICODE_LOCALE_EXTENSION` ('u') is used for the Unicode locale extension.
Setting a value for this key replaces any existing Unicode locale key/type
pairs with those defined in the extension.Note: The key `PRIVATE_USE_EXTENSION` ('x') is used for the private use code. To be
well-formed, the value for this key needs only to have subtags of one to
eight alphanumeric characters, not two to eight as in the general case.
Parameters:
`key` - the extension key
`value` - the extension value
Returns:
This builder.
Throws:
`IllformedLocaleException` - if `key` is illegal
or `value` is ill-formed
See Also:
`setUnicodeLocaleKeyword(String, String)`

