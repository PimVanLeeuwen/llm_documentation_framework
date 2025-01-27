#### invokeAll

```
public <T> List<Future<T>> invokeAll(Collection<? extends Callable<T>> tasks,
                                     long timeout,
                                     TimeUnit unit)
                              throws InterruptedException
```
Description copied from interface: `ExecutorService`
Executes the given tasks, returning a list of Futures holding
their status and results
when all complete or the timeout expires, whichever happens first.
`Future.isDone()` is `true` for each
element of the returned list.
Upon return, tasks that have not completed are cancelled.
Note that a completed task could have
terminated either normally or by throwing an exception.
The results of this method are undefined if the given
collection is modified while this operation is in progress.
Specified by:
`invokeAll` in interface `ExecutorService`
Type Parameters:
`T` - the type of the values returned from the tasks
Parameters:
`tasks` - the collection of tasks
`timeout` - the maximum time to wait
`unit` - the time unit of the timeout argument
Returns:
a list of Futures representing the tasks, in the same
sequential order as produced by the iterator for the
given task list. If the operation did not time out,
each task will have completed. If it did time out, some
of these tasks will not have completed.
Throws:
`InterruptedException` - if interrupted while waiting, in
which case unfinished tasks are cancelled




