#### getLong

```
public long getLong(String key,
                    long def)
```
Implements the getLong method as per the specification in
`Preferences.getLong(String,long)`.This implementation invokes `get(key,
null)`. If the return value is non-null, the implementation
attempts to translate it to a long with
`Long.parseLong(String)`. If the attempt succeeds, the return
value is returned by this method. Otherwise, def is returned.
Specified by:
`getLong` in class `Preferences`
Parameters:
`key` - key whose associated value is to be returned as a long.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as a long.
Returns:
the long value represented by the string associated with
key in this preference node, or def if the
associated value does not exist or cannot be interpreted as
a long.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null.
See Also:
`Preferences.putLong(String,long)`,
`Preferences.get(String,String)`

