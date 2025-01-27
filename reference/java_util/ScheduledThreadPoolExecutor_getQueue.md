#### getQueue

```
public BlockingQueue<Runnable> getQueue()
```
Returns the task queue used by this executor. Each element of
this queue is a `ScheduledFuture`, including those
tasks submitted using `execute` which are for scheduling
purposes used as the basis of a zero-delay
`ScheduledFuture`. Iteration over this queue is
not guaranteed to traverse tasks in the order in
which they will execute.
Overrides:
`getQueue` in class `ThreadPoolExecutor`
Returns:
the task queue




