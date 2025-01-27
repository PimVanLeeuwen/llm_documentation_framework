#### putByteArray

```
public void putByteArray(String key,
                         byte[] value)
```
Implements the putByteArray method as per the specification in
`Preferences.putByteArray(String,byte[])`.
Specified by:
`putByteArray` in class `Preferences`
Parameters:
`key` - key with which the string form of value is to be associated.
`value` - value whose string form is to be associated with key.
Throws:
`NullPointerException` - if key or value is null.
`IllegalArgumentException` - if key.length() exceeds MAX\_KEY\_LENGTH
or if value.length exceeds MAX\_VALUE\_LENGTH\*3/4.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`Preferences.getByteArray(String,byte[])`,
`Preferences.get(String,String)`

