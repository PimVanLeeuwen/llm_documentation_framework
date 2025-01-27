#### putByteArray

```
public abstract void putByteArray(String key,
                                  byte[] value)
```
Associates a string representing the specified byte array with the
specified key in this preference node. The associated string is
the Base64 encoding of the byte array, as defined in RFC 2045, Section 6.8,
with one minor change: the string will consist solely of characters
from the Base64 Alphabet; it will not contain any newline
characters. Note that the maximum length of the byte array is limited
to three quarters of MAX\_VALUE\_LENGTH so that the length
of the Base64 encoded String does not exceed MAX\_VALUE\_LENGTH.
This method is intended for use in conjunction with
`getByteArray(java.lang.String, byte[])`.
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
`getByteArray(String,byte[])`,
`get(String,String)`

