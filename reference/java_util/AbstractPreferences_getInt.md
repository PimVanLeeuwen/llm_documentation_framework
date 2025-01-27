#### getInt

```
public int getInt(String key,
                  int def)
```
Implements the getInt method as per the specification in
`Preferences.getInt(String,int)`.This implementation invokes `get(key,
null)`. If the return value is non-null, the implementation
attempts to translate it to an int with
`Integer.parseInt(String)`. If the attempt succeeds, the return
value is returned by this method. Otherwise, def is returned.
Specified by:
`getInt` in class `Preferences`
Parameters:
`key` - key whose associated value is to be returned as an int.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as an int.
Returns:
the int value represented by the string associated with
key in this preference node, or def if the
associated value does not exist or cannot be interpreted as
an int.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null.
See Also:
`Preferences.putInt(String,int)`,
`Preferences.get(String,String)`

