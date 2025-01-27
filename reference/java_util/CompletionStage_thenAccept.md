#### thenAccept

```
CompletionStage<Void> thenAccept(Consumer<? super T> action)
```
Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Parameters:
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

