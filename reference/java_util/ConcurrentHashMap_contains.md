#### contains

```
public boolean contains(Object value)
```
Legacy method testing if some key maps into the specified value
in this table. This method is identical in functionality to
`containsValue(Object)`, and exists solely to ensure
full compatibility with class `Hashtable`,
which supported this method prior to introduction of the
Java Collections framework.
Parameters:
`value` - a value to search for
Returns:
`true` if and only if some key maps to the
`value` argument in this table as
determined by the `equals` method;
`false` otherwise
Throws:
`NullPointerException` - if the specified value is null

