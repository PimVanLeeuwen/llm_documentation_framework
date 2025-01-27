#### acceptEitherAsync

```
public CompletableFuture<Void> acceptEitherAsync(CompletionStage<? extends T> other,
                                                 Consumer<? super T> action,
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
`acceptEitherAsync` in interface `CompletionStage<T>`
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

