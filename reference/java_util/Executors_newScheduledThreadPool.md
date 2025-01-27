#### newScheduledThreadPool

```
public static ScheduledExecutorService newScheduledThreadPool(int corePoolSize,
                                                              ThreadFactory threadFactory)
```
Creates a thread pool that can schedule commands to run after a
given delay, or to execute periodically.
Parameters:
`corePoolSize` - the number of threads to keep in the pool,
even if they are idle
`threadFactory` - the factory to use when the executor
creates a new thread
Returns:
a newly created scheduled thread pool
Throws:
`IllegalArgumentException` - if `corePoolSize < 0`
`NullPointerException` - if threadFactory is null

