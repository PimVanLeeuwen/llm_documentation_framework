#### runAfterBoth

```
public CompletableFuture<Void> runAfterBoth(CompletionStage<?> other,
                                            Runnable action)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`runAfterBoth` in interface `CompletionStage<T>`
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

