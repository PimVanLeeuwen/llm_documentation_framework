#### newSingleThreadExecutor

```
public static ExecutorService newSingleThreadExecutor(ThreadFactory threadFactory)
```
Creates an Executor that uses a single worker thread operating
off an unbounded queue, and uses the provided ThreadFactory to
create a new thread when needed. Unlike the otherwise
equivalent `newFixedThreadPool(1, threadFactory)` the
returned executor is guaranteed not to be reconfigurable to use
additional threads.
Parameters:
`threadFactory` - the factory to use when creating new
threads
Returns:
the newly created single-threaded Executor
Throws:
`NullPointerException` - if threadFactory is null

