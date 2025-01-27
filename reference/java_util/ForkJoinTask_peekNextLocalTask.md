#### peekNextLocalTask

```
protected static ForkJoinTask<?> peekNextLocalTask()
```
Returns, but does not unschedule or execute, a task queued by
the current thread but not yet executed, if one is immediately
available. There is no guarantee that this task will actually
be polled or executed next. Conversely, this method may return
null even if a task exists but cannot be accessed without
contention with other threads. This method is designed
primarily to support extensions, and is unlikely to be useful
otherwise.
Returns:
the next task, or `null` if none are available

