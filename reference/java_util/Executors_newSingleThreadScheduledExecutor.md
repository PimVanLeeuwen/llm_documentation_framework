#### newSingleThreadScheduledExecutor

```
public static ScheduledExecutorService newSingleThreadScheduledExecutor(ThreadFactory threadFactory)
```
Creates a single-threaded executor that can schedule commands
to run after a given delay, or to execute periodically. (Note
however that if this single thread terminates due to a failure
during execution prior to shutdown, a new one will take its
place if needed to execute subsequent tasks.) Tasks are
guaranteed to execute sequentially, and no more than one task
will be active at any given time. Unlike the otherwise
equivalent `newScheduledThreadPool(1, threadFactory)`
the returned executor is guaranteed not to be reconfigurable to
use additional threads.
Parameters:
`threadFactory` - the factory to use when creating new
threads
Returns:
a newly created scheduled executor
Throws:
`NullPointerException` - if threadFactory is null

