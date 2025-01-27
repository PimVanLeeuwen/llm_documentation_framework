#### newTaskFor

```
protected <T> RunnableFuture<T> newTaskFor(Callable<T> callable)
```
Description copied from class: `AbstractExecutorService`
Returns a `RunnableFuture` for the given callable task.
Overrides:
`newTaskFor` in class `AbstractExecutorService`
Type Parameters:
`T` - the type of the callable's result
Parameters:
`callable` - the callable task being wrapped
Returns:
a `RunnableFuture` which, when run, will call the
underlying callable and which, as a `Future`, will yield
the callable's result as its result and provide for
cancellation of the underlying task




