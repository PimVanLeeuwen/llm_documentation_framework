#### runAfterBothAsync

```
public CompletableFuture<Void> runAfterBothAsync(CompletionStage<?> other,
                                                 Runnable action,
                                                 Executor executor)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when this and the other
given stage complete normally, executes the given action using
the supplied executor.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`runAfterBothAsync` in interface `CompletionStage<T>`
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

