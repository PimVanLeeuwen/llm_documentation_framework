#### acceptEither

```
public CompletableFuture<Void> acceptEither(CompletionStage<? extends T> other,
                                            Consumer<? super T> action)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`acceptEither` in interface `CompletionStage<T>`
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

