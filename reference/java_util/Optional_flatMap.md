#### flatMap

```
public <U> Optional<U> flatMap(Function<? super T,Optional<U>> mapper)
```
If a value is present, apply the provided `Optional`-bearing
mapping function to it, return that result, otherwise return an empty
`Optional`. This method is similar to `map(Function)`,
but the provided mapper is one whose result is already an `Optional`,
and if invoked, `flatMap` does not wrap it with an additional
`Optional`.
Type Parameters:
`U` - The type parameter to the `Optional` returned by
Parameters:
`mapper` - a mapping function to apply to the value, if present
the mapping function
Returns:
the result of applying an `Optional`-bearing mapping
function to the value of this `Optional`, if a value is present,
otherwise an empty `Optional`
Throws:
`NullPointerException` - if the mapping function is null or returns
a null result

