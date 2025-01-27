#### ofNullable

```
public static <T> Optional<T> ofNullable(T value)
```
Returns an `Optional` describing the specified value, if non-null,
otherwise returns an empty `Optional`.
Type Parameters:
`T` - the class of the value
Parameters:
`value` - the possibly-null value to describe
Returns:
an `Optional` with a present value if the specified value
is non-null, otherwise an empty `Optional`

