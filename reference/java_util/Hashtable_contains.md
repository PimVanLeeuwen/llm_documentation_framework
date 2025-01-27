#### contains

```
public boolean contains(Object value)
```
Tests if some key maps into the specified value in this hashtable.
This operation is more expensive than the `containsKey` method.Note that this method is identical in functionality to
`containsValue`, (which is part of the
`Map` interface in the collections framework).
Parameters:
`value` - a value to search for
Returns:
`true` if and only if some key maps to the
`value` argument in this hashtable as
determined by the equals method;
`false` otherwise.
Throws:
`NullPointerException` - if the value is `null`

