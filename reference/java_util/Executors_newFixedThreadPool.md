#### newFixedThreadPool

```
public static ExecutorService newFixedThreadPool(int nThreads,
                                                 ThreadFactory threadFactory)
```
Creates a thread pool that reuses a fixed number of threads
operating off a shared unbounded queue, using the provided
ThreadFactory to create new threads when needed. At any point,
at most `nThreads` threads will be active processing
tasks. If additional tasks are submitted when all threads are
active, they will wait in the queue until a thread is
available. If any thread terminates due to a failure during
execution prior to shutdown, a new one will take its place if
needed to execute subsequent tasks. The threads in the pool will
exist until it is explicitly `shutdown`.
Parameters:
`nThreads` - the number of threads in the pool
`threadFactory` - the factory to use when creating new threads
Returns:
the newly created thread pool
Throws:
`NullPointerException` - if threadFactory is null
`IllegalArgumentException` - if `nThreads <= 0`

