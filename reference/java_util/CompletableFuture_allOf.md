#### allOf

```
public static CompletableFuture<Void> allOf(CompletableFuture<?>... cfs)
```
Returns a new CompletableFuture that is completed when all of
the given CompletableFutures complete. If any of the given
CompletableFutures complete exceptionally, then the returned
CompletableFuture also does so, with a CompletionException
holding this exception as its cause. Otherwise, the results,
if any, of the given CompletableFutures are not reflected in
the returned CompletableFuture, but may be obtained by
inspecting them individually. If no CompletableFutures are
provided, returns a CompletableFuture completed with the value
`null`.Among the applications of this method is to await completion
of a set of independent CompletableFutures before continuing a
program, as in: `CompletableFuture.allOf(c1, c2,
c3).join();`.
Parameters:
`cfs` - the CompletableFutures
Returns:
a new CompletableFuture that is completed when all of the
given CompletableFutures complete
Throws:
`NullPointerException` - if the array or any of its elements are
`null`

