#### decorateTask

```
protected <V> RunnableScheduledFuture<V> decorateTask(Callable<V> callable,
                                                      RunnableScheduledFuture<V> task)
```
Modifies or replaces the task used to execute a callable.
This method can be used to override the concrete
class used for managing internal tasks.
The default implementation simply returns the given task.
Type Parameters:
`V` - the type of the task's result
Parameters:
`callable` - the submitted Callable
`task` - the task created to execute the callable
Returns:
a task that can execute the callable
Since:
1.6

