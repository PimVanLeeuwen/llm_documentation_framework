#### orElseGet

```
public double orElseGet(DoubleSupplier other)
```
Return the value if present, otherwise invoke `other` and return
the result of that invocation.
Parameters:
`other` - a `DoubleSupplier` whose result is returned if no value
is present
Returns:
the value if present otherwise the result of `other.getAsDouble()`
Throws:
`NullPointerException` - if value is not present and `other` is
null

