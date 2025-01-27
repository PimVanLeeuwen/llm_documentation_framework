#### thenAcceptAsync

```
public CompletableFuture<Void> thenAcceptAsync(Consumer<? super T> action,
                                               Executor executor)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`thenAcceptAsync` in interface `CompletionStage<T>`
Parameters:
`action` - the action to perform before completing the
returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

