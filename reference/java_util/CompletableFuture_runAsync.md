#### runAsync

```
public static CompletableFuture<Void> runAsync(Runnable runnable,
                                               Executor executor)
```
Returns a new CompletableFuture that is asynchronously completed
by a task running in the given executor after it runs the given
action.
Parameters:
`runnable` - the action to run before completing the
returned CompletableFuture
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletableFuture

