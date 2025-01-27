#### finisher

```
Function<A,R> finisher()
```
Perform the final transformation from the intermediate accumulation type
`A` to the final result type `R`.If the characteristic `IDENTITY_TRANSFORM` is
set, this function may be presumed to be an identity transform with an
unchecked cast from `A` to `R`.
Returns:
a function which transforms the intermediate result to the final
result

