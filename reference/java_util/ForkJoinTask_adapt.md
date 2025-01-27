#### adapt

```
public static <T> ForkJoinTask<T> adapt(Callable<? extends T> callable)
```
Returns a new `ForkJoinTask` that performs the `call`
method of the given `Callable` as its action, and returns
its result upon `join()`, translating any checked exceptions
encountered into `RuntimeException`.
Type Parameters:
`T` - the type of the callable's result
Parameters:
`callable` - the callable action
Returns:
the task




