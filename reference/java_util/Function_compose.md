#### compose

```
default <V> Function<V,R> compose(Function<? super V,? extends T> before)
```
Returns a composed function that first applies the `before`
function to its input, and then applies this function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.
Type Parameters:
`V` - the type of input to the `before` function, and to the
composed function
Parameters:
`before` - the function to apply before this function is applied
Returns:
a composed function that first applies the `before`
function and then applies this function
Throws:
`NullPointerException` - if before is null
See Also:
`andThen(Function)`

