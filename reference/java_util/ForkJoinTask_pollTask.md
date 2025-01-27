#### pollTask

```
protected static ForkJoinTask<?> pollTask()
```
If the current thread is operating in a ForkJoinPool,
unschedules and returns, without executing, the next task
queued by the current thread but not yet executed, if one is
available, or if not available, a task that was forked by some
other thread, if available. Availability may be transient, so a
`null` result does not necessarily imply quiescence of
the pool this task is operating in. This method is designed
primarily to support extensions, and is unlikely to be useful
otherwise.
Returns:
a task, or `null` if none are available

