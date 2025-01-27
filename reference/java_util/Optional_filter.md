#### filter

```
public Optional<T> filter(Predicate<? super T> predicate)
```
If a value is present, and the value matches the given predicate,
return an `Optional` describing the value, otherwise return an
empty `Optional`.
Parameters:
`predicate` - a predicate to apply to the value, if present
Returns:
an `Optional` describing the value of this `Optional`
if a value is present and the value matches the given predicate,
otherwise an empty `Optional`
Throws:
`NullPointerException` - if the predicate is null

