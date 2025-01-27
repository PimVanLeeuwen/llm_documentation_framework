#### exceptionally

```
public CompletableFuture<T> exceptionally(Function<Throwable,? extends T> fn)
```
Returns a new CompletableFuture that is completed when this
CompletableFuture completes, with the result of the given
function of the exception triggering this CompletableFuture's
completion when it completes exceptionally; otherwise, if this
CompletableFuture completes normally, then the returned
CompletableFuture also completes normally with the same value.
Note: More flexible versions of this functionality are
available using methods `whenComplete` and `handle`.
Specified by:
`exceptionally` in interface `CompletionStage<T>`
Parameters:
`fn` - the function to use to compute the value of the
returned CompletableFuture if this CompletableFuture completed
exceptionally
Returns:
the new CompletableFuture

