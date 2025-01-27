#### rejectedExecution

```
public void rejectedExecution(Runnable r,
                              ThreadPoolExecutor e)
```
Executes task r in the caller's thread, unless the executor
has been shut down, in which case the task is discarded.
Specified by:
`rejectedExecution` in interface `RejectedExecutionHandler`
Parameters:
`r` - the runnable task requested to be executed
`e` - the executor attempting to execute this task




