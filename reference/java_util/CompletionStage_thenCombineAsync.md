#### thenCombineAsync

```
<U,V> CompletionStage<V> thenCombineAsync(CompletionStage<? extends U> other,
                                          BiFunction<? super T,? super U,? extends V> fn,
                                          Executor executor)
```
Returns a new CompletionStage that, when this and the other
given stage complete normally, is executed using the supplied
executor, with the two results as arguments to the supplied
function.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Type Parameters:
`U` - the type of the other CompletionStage's result
`V` - the function's return type
Parameters:
`other` - the other CompletionStage
`fn` - the function to use to compute the value of
the returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

