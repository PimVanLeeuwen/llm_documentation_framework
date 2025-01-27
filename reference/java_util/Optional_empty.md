#### empty

```
public static <T> Optional<T> empty()
```
Returns an empty `Optional` instance. No value is present for this
Optional.
API Note:
Though it may be tempting to do so, avoid testing if an object
is empty by comparing with `==` against instances returned by
`Option.empty()`. There is no guarantee that it is a singleton.
Instead, use `isPresent()`.
Type Parameters:
`T` - Type of the non-existent value
Returns:
an empty `Optional`

