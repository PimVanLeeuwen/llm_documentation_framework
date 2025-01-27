#### submit

```
public <T> Future<T> submit(Callable<T> task)
```
Description copied from interface: `ExecutorService`
Submits a value-returning task for execution and returns a
Future representing the pending results of the task. The
Future's `get` method will return the task's result upon
successful completion.If you would like to immediately block waiting
for a task, you can use constructions of the form
`result = exec.submit(aCallable).get();`Note: The `Executors` class includes a set of methods
that can convert some other common closure-like objects,
for example, `PrivilegedAction` to
`Callable` form so they can be submitted.
Specified by:
`submit` in interface `ExecutorService`
Type Parameters:
`T` - the type of the task's result
Parameters:
`task` - the task to submit
Returns:
a Future representing pending completion of the task
Throws:
`RejectedExecutionException` - if the task cannot be
scheduled for execution
`NullPointerException` - if the task is null

