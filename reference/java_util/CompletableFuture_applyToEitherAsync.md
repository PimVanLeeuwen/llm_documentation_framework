#### applyToEitherAsync

```
public <U> CompletableFuture<U> applyToEitherAsync(CompletionStage<? extends T> other,
                                                   Function<? super T,U> fn,
                                                   Executor executor)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied function.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`applyToEitherAsync` in interface `CompletionStage<T>`
Type Parameters:
`U` - the function's return type
Parameters:
`other` - the other CompletionStage
`fn` - the function to use to compute the value of
the returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

