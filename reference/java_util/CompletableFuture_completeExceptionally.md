#### completeExceptionally

```
public boolean completeExceptionally(Throwable ex)
```
If not already completed, causes invocations of `get()`
and related methods to throw the given exception.
Parameters:
`ex` - the exception
Returns:
`true` if this invocation caused this CompletableFuture
to transition to a completed state, else `false`

