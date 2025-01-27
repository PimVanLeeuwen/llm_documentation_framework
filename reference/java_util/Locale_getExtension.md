#### getExtension

```
public String getExtension(char key)
```
Returns the extension (or private use) value associated with
the specified key, or null if there is no extension
associated with the key. To be well-formed, the key must be one
of `[0-9A-Za-z]`. Keys are case-insensitive, so
for example 'z' and 'Z' represent the same extension.
Parameters:
`key` - the extension key
Returns:
The extension, or null if this locale defines no
extension for the specified key.
Throws:
`IllegalArgumentException` - if key is not well-formed
Since:
1.7
See Also:
`PRIVATE_USE_EXTENSION`,
`UNICODE_LOCALE_EXTENSION`

