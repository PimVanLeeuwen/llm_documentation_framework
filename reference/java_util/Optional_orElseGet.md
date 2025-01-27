#### orElseGet

```
public T orElseGet(Supplier<? extends T> other)
```
Return the value if present, otherwise invoke `other` and return
the result of that invocation.
Parameters:
`other` - a `Supplier` whose result is returned if no value
is present
Returns:
the value if present otherwise the result of `other.get()`
Throws:
`NullPointerException` - if value is not present and `other` is
null

