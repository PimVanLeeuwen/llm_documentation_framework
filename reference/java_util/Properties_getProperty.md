#### getProperty

```
public String getProperty(String key,
                          String defaultValue)
```
Searches for the property with the specified key in this property list.
If the key is not found in this property list, the default property list,
and its defaults, recursively, are then checked. The method returns the
default value argument if the property is not found.
Parameters:
`key` - the hashtable key.
`defaultValue` - a default value.
Returns:
the value in this property list with the specified key value.
See Also:
`setProperty(java.lang.String, java.lang.String)`,
`defaults`

