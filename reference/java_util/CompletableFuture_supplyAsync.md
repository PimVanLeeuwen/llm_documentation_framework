#### supplyAsync

```
public static <U> CompletableFuture<U> supplyAsync(Supplier<U> supplier,
                                                   Executor executor)
```
Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor with the value obtained
by calling the given Supplier.
Type Parameters:
`U` - the function's return type
Parameters:
`supplier` - a function returning the value to be used
to complete the returned CompletableFuture
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletableFuture

