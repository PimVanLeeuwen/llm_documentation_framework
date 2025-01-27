#### andThen

```
default <V> BiFunction<T,U,V> andThen(Function<? super R,? extends V> after)
```
Returns a composed function that first applies this function to
its input, and then applies the `after` function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.
Type Parameters:
`V` - the type of output of the `after` function, and of the
composed function
Parameters:
`after` - the function to apply after this function is applied
Returns:
a composed function that first applies this function and then
applies the `after` function
Throws:
`NullPointerException` - if after is null




