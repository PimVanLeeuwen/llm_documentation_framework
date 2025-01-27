```
public interface ScheduledFuture<V>
extends Delayed, Future<V>
```
A delayed result-bearing action that can be cancelled.
Usually a scheduled future is the result of scheduling
a task with a `ScheduledExecutorService`.
Since:
1.5
