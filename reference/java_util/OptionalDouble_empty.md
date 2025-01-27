#### empty

```
public static OptionalDouble empty()
```
Returns an empty `OptionalDouble` instance. No value is present for this
OptionalDouble.
API Note:
Though it may be tempting to do so, avoid testing if an object
is empty by comparing with `==` against instances returned by
`Option.empty()`. There is no guarantee that it is a singleton.
Instead, use `isPresent()`.
Returns:
an empty `OptionalDouble`.

