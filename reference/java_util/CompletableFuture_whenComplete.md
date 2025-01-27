#### whenComplete

```
public CompletableFuture<T> whenComplete(BiConsumer<? super T,? super Throwable> action)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action when this stage completes.When this stage is complete, the given action is invoked with the
result (or `null` if none) and the exception (or `null`
if none) of this stage as arguments. The returned stage is completed
when the action returns. If the supplied action itself encounters an
exception, then the returned stage exceptionally completes with this
exception unless this stage also completed exceptionally.
Specified by:
`whenComplete` in interface `CompletionStage<T>`
Parameters:
`action` - the action to perform
Returns:
the new CompletionStage

