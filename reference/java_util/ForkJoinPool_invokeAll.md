#### invokeAll

```
public <T> List<Future<T>> invokeAll(Collection<? extends Callable<T>> tasks)
```
Description copied from interface: `ExecutorService`
Executes the given tasks, returning a list of Futures holding
their status and results when all complete.
`Future.isDone()` is `true` for each
element of the returned list.
Note that a completed task could have
terminated either normally or by throwing an exception.
The results of this method are undefined if the given
collection is modified while this operation is in progress.
Specified by:
`invokeAll` in interface `ExecutorService`
Overrides:
`invokeAll` in class `AbstractExecutorService`
Type Parameters:
`T` - the type of the values returned from the tasks
Parameters:
`tasks` - the collection of tasks
Returns:
a list of Futures representing the tasks, in the same
sequential order as produced by the iterator for the
given task list, each of which has completed
Throws:
`NullPointerException` - if tasks or any of its elements are `null`
`RejectedExecutionException` - if any task cannot be
scheduled for execution

