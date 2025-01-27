#### put

```
public void put(String key,
                String value)
```
Implements the put method as per the specification in
`Preferences.put(String,String)`.This implementation checks that the key and value are legal,
obtains this preference node's lock, checks that the node
has not been removed, invokes `putSpi(String,String)`, and if
there are any preference change listeners, enqueues a notification
event for processing by the event dispatch thread.
Specified by:
`put` in class `Preferences`
Parameters:
`key` - key with which the specified value is to be associated.
`value` - value to be associated with the specified key.
Throws:
`NullPointerException` - if key or value is null.
`IllegalArgumentException` - if key.length() exceeds
MAX\_KEY\_LENGTH or if value.length exceeds
MAX\_VALUE\_LENGTH.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.

