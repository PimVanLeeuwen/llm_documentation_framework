#### remove

```
public boolean remove(Runnable task)
```
Removes this task from the executor's internal queue if it is
present, thus causing it not to be run if it has not already
started.This method may be useful as one part of a cancellation
scheme. It may fail to remove tasks that have been converted
into other forms before being placed on the internal queue. For
example, a task entered using `submit` might be
converted into a form that maintains `Future` status.
However, in such cases, method `purge()` may be used to
remove those Futures that have been cancelled.
Parameters:
`task` - the task to remove
Returns:
`true` if the task was removed

