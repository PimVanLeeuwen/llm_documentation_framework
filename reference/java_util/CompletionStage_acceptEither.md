#### acceptEither

```
CompletionStage<Void> acceptEither(CompletionStage<? extends T> other,
                                   Consumer<? super T> action)
```
Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

