#### rejectedExecution

```
public void rejectedExecution(Runnable r,
                              ThreadPoolExecutor e)
```
Always throws RejectedExecutionException.
Specified by:
`rejectedExecution` in interface `RejectedExecutionHandler`
Parameters:
`r` - the runnable task requested to be executed
`e` - the executor attempting to execute this task
Throws:
`RejectedExecutionException` - always




