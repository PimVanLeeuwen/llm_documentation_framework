```
public static class ThreadPoolExecutor.DiscardOldestPolicy
extends Object
implements RejectedExecutionHandler
```
A handler for rejected tasks that discards the oldest unhandled
request and then retries `execute`, unless the executor
is shut down, in which case the task is discarded.
