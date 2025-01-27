#### thenAcceptBothAsync

```
<U> CompletionStage<Void> thenAcceptBothAsync(CompletionStage<? extends U> other,
                                              BiConsumer<? super T,? super U> action,
                                              Executor executor)
```
Returns a new CompletionStage that, when this and the other
given stage complete normally, is executed using the supplied
executor, with the two results as arguments to the supplied
function.
Type Parameters:
`U` - the type of the other CompletionStage's result
Parameters:
`other` - the other CompletionStage
`action` - the action to perform before completing the
returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

