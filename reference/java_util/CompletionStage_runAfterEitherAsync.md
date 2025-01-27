#### runAfterEitherAsync

```
CompletionStage<Void> runAfterEitherAsync(CompletionStage<?> other,
                                          Runnable action,
                                          Executor executor)
```
Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using the supplied executor.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

