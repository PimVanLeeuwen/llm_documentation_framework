#### thenRunAsync

```
public CompletableFuture<Void> thenRunAsync(Runnable action,
                                            Executor executor)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`thenRunAsync` in interface `CompletionStage<T>`
Parameters:
`action` - the action to perform before completing the
returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

