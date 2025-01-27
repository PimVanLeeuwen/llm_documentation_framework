#### thenRun

```
public CompletableFuture<Void> thenRun(Runnable action)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when this stage completes
normally, executes the given action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`thenRun` in interface `CompletionStage<T>`
Parameters:
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

