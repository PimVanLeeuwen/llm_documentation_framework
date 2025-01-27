#### toCompletableFuture

```
CompletableFuture<T> toCompletableFuture()
```
Returns a `CompletableFuture` maintaining the same
completion properties as this stage. If this stage is already a
CompletableFuture, this method may return this stage itself.
Otherwise, invocation of this method may be equivalent in
effect to `thenApply(x -> x)`, but returning an instance
of type `CompletableFuture`. A CompletionStage
implementation that does not choose to interoperate with others
may throw `UnsupportedOperationException`.
Returns:
the CompletableFuture
Throws:
`UnsupportedOperationException` - if this implementation
does not interoperate with CompletableFuture




