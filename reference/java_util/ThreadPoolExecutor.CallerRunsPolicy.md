```
public static class ThreadPoolExecutor.CallerRunsPolicy
extends Object
implements RejectedExecutionHandler
```
A handler for rejected tasks that runs the rejected task
directly in the calling thread of the `execute` method,
unless the executor has been shut down, in which case the task
is discarded.
