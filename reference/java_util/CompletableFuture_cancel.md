#### cancel

```
public boolean cancel(boolean mayInterruptIfRunning)
```
If not already completed, completes this CompletableFuture with
a `CancellationException`. Dependent CompletableFutures
that have not already completed will also complete
exceptionally, with a `CompletionException` caused by
this `CancellationException`.
Specified by:
`cancel` in interface `Future<T>`
Parameters:
`mayInterruptIfRunning` - this value has no effect in this
implementation because interrupts are not used to control
processing.
Returns:
`true` if this task is now cancelled

