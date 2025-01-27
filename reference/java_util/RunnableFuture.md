```
public interface RunnableFuture<V>
extends Runnable, Future<V>
```
A `Future` that is `Runnable`. Successful execution of
the `run` method causes completion of the `Future`
and allows access to its results.
Since:
1.6
See Also:
`FutureTask`,
`Executor`
