#### thenRun

```
CompletionStage<Void> thenRun(Runnable action)
```
Returns a new CompletionStage that, when this stage completes
normally, executes the given action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Parameters:
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

