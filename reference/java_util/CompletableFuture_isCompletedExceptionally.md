#### isCompletedExceptionally

```
public boolean isCompletedExceptionally()
```
Returns `true` if this CompletableFuture completed
exceptionally, in any way. Possible causes include
cancellation, explicit invocation of `completeExceptionally`, and abrupt termination of a
CompletionStage action.
Returns:
`true` if this CompletableFuture completed
exceptionally

