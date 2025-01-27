#### thenAcceptBoth

```
public <U> CompletableFuture<Void> thenAcceptBoth(CompletionStage<? extends U> other,
                                                  BiConsumer<? super T,? super U> action)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied action.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`thenAcceptBoth` in interface `CompletionStage<T>`
Type Parameters:
`U` - the type of the other CompletionStage's result
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
Returns:
the new CompletionStage

