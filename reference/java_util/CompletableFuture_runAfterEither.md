#### runAfterEither

```
public CompletableFuture<Void> runAfterEither(CompletionStage<?> other,
                                              Runnable action)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`runAfterEither` in interface `CompletionStage<T>`
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

