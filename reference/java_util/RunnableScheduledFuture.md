```
public interface RunnableScheduledFuture<V>
extends RunnableFuture<V>, ScheduledFuture<V>
```
A `ScheduledFuture` that is `Runnable`. Successful
execution of the `run` method causes completion of the
`Future` and allows access to its results.
Since:
1.6
See Also:
`FutureTask`,
`Executor`
