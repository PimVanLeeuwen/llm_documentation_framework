#### shutdownNow

```
public List<Runnable> shutdownNow()
```
Possibly attempts to cancel and/or stop all tasks, and reject
all subsequently submitted tasks. Invocation has no effect on
execution state if this is the `commonPool()`, and no
additional effect if already shut down. Otherwise, tasks that
are in the process of being submitted or executed concurrently
during the course of this method may or may not be
rejected. This method cancels both existing and unexecuted
tasks, in order to permit termination in the presence of task
dependencies. So the method always returns an empty list
(unlike the case for some other Executors).
Returns:
an empty list
Throws:
`SecurityException` - if a security manager exists and
the caller is not permitted to modify threads
because it does not hold `RuntimePermission``("modifyThread")`

