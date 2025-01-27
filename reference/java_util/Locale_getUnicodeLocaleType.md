#### getUnicodeLocaleType

```
public String getUnicodeLocaleType(String key)
```
Returns the Unicode locale type associated with the specified Unicode locale key
for this locale. Returns the empty string for keys that are defined with no type.
Returns null if the key is not defined. Keys are case-insensitive. The key must
be two alphanumeric characters ([0-9a-zA-Z]), or an IllegalArgumentException is
thrown.
Parameters:
`key` - the Unicode locale key
Returns:
The Unicode locale type associated with the key, or null if the
locale does not define the key.
Throws:
`IllegalArgumentException` - if the key is not well-formed
`NullPointerException` - if `key` is null
Since:
1.7

