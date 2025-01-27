#### runAfterEither

```
CompletionStage<Void> runAfterEither(CompletionStage<?> other,
                                     Runnable action)
```
Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

