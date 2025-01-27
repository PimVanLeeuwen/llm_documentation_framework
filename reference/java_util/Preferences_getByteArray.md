#### getByteArray

```
public abstract byte[] getByteArray(String key,
                                    byte[] def)
```
Returns the byte array value represented by the string associated with
the specified key in this preference node. Valid strings are
Base64 encoded binary data, as defined in RFC 2045, Section 6.8,
with one minor change: the string must consist solely of characters
from the Base64 Alphabet; no newline characters or
extraneous characters are permitted. This method is intended for use
in conjunction with `putByteArray(java.lang.String, byte[])`.Returns the specified default if there is no value
associated with the key, the backing store is inaccessible, or if the
associated value is not a valid Base64 encoded byte array
(as defined above).If the implementation supports stored defaults and such a
default exists and is accessible, it is used in preference to the
specified default, unless the stored default is not a valid Base64
encoded byte array (as defined above), in which case the
specified default is used.
Parameters:
`key` - key whose associated value is to be returned as a byte array.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as a byte array,
or the backing store is inaccessible.
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
`get(String,String)`,
`putByteArray(String,byte[])`

