#### rejectedExecution

```
public void rejectedExecution(Runnable r,
                              ThreadPoolExecutor e)
```
Obtains and ignores the next task that the executor
would otherwise execute, if one is immediately available,
and then retries execution of task r, unless the executor
is shut down, in which case task r is instead discarded.
Specified by:
`rejectedExecution` in interface `RejectedExecutionHandler`
Parameters:
`r` - the runnable task requested to be executed
`e` - the executor attempting to execute this task




