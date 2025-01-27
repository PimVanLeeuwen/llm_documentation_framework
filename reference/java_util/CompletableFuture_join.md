#### join

```
public T join()
```
Returns the result value when complete, or throws an
(unchecked) exception if completed exceptionally. To better
conform with the use of common functional forms, if a
computation involved in the completion of this
CompletableFuture threw an exception, this method throws an
(unchecked) `CompletionException` with the underlying
exception as its cause.
Returns:
the result value
Throws:
`CancellationException` - if the computation was cancelled
`CompletionException` - if this future completed
exceptionally or a completion computation threw an exception

