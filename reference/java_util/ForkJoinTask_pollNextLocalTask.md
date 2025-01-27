#### pollNextLocalTask

```
protected static ForkJoinTask<?> pollNextLocalTask()
```
Unschedules and returns, without executing, the next task
queued by the current thread but not yet executed, if the
current thread is operating in a ForkJoinPool. This method is
designed primarily to support extensions, and is unlikely to be
useful otherwise.
Returns:
the next task, or `null` if none are available

