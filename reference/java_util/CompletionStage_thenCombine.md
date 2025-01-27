#### thenCombine

```
<U,V> CompletionStage<V> thenCombine(CompletionStage<? extends U> other,
                                     BiFunction<? super T,? super U,? extends V> fn)
```
Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied function.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Type Parameters:
`U` - the type of the other CompletionStage's result
`V` - the function's return type
Parameters:
`other` - the other CompletionStage
`fn` - the function to use to compute the value of
the returned CompletionStage
Returns:
the new CompletionStage

