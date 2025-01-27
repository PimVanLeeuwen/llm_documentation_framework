#### getByteArray

```
public byte[] getByteArray(String key,
                           byte[] def)
```
Implements the getByteArray method as per the specification in
`Preferences.getByteArray(String,byte[])`.
Specified by:
`getByteArray` in class `Preferences`
Parameters:
`key` - key whose associated value is to be returned as a byte array.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as a byte array.
Returns:
the byte array value represented by the string associated with
key in this preference node, or def if the
associated value does not exist or cannot be interpreted as
a byte array.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null. (A
null value for def is permitted.)
See Also:
`Preferences.get(String,String)`,
`Preferences.putByteArray(String,byte[])`

