#### runAfterBoth

```
CompletionStage<Void> runAfterBoth(CompletionStage<?> other,
                                   Runnable action)
```
Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

