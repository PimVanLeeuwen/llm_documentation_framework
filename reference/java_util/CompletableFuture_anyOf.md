#### anyOf

```
public static CompletableFuture<Object> anyOf(CompletableFuture<?>... cfs)
```
Returns a new CompletableFuture that is completed when any of
the given CompletableFutures complete, with the same result.
Otherwise, if it completed exceptionally, the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. If no CompletableFutures
are provided, returns an incomplete CompletableFuture.
Parameters:
`cfs` - the CompletableFutures
Returns:
a new CompletableFuture that is completed with the
result or exception of any of the given CompletableFutures when
one completes
Throws:
`NullPointerException` - if the array or any of its elements are
`null`

