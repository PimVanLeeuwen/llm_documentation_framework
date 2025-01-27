#### rejectedExecution

```
void rejectedExecution(Runnable r,
                       ThreadPoolExecutor executor)
```
Method that may be invoked by a `ThreadPoolExecutor` when
`execute` cannot accept a
task. This may occur when no more threads or queue slots are
available because their bounds would be exceeded, or upon
shutdown of the Executor.In the absence of other alternatives, the method may throw
an unchecked `RejectedExecutionException`, which will be
propagated to the caller of `execute`.
Parameters:
`r` - the runnable task requested to be executed
`executor` - the executor attempting to execute this task
Throws:
`RejectedExecutionException` - if there is no remedy




