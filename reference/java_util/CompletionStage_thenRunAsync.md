#### thenRunAsync

```
CompletionStage<Void> thenRunAsync(Runnable action,
                                   Executor executor)
```
Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Parameters:
`action` - the action to perform before completing the
returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

