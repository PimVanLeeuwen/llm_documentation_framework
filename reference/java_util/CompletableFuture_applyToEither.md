#### applyToEither

```
public <U> CompletableFuture<U> applyToEither(CompletionStage<? extends T> other,
                                              Function<? super T,U> fn)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied function.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`applyToEither` in interface `CompletionStage<T>`
Type Parameters:
`U` - the function's return type
Parameters:
`other` - the other CompletionStage
`fn` - the function to use to compute the value of
the returned CompletionStage
Returns:
the new CompletionStage

