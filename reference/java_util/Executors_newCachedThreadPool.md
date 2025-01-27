#### newCachedThreadPool

```
public static ExecutorService newCachedThreadPool(ThreadFactory threadFactory)
```
Creates a thread pool that creates new threads as needed, but
will reuse previously constructed threads when they are
available, and uses the provided
ThreadFactory to create new threads when needed.
Parameters:
`threadFactory` - the factory to use when creating new threads
Returns:
the newly created thread pool
Throws:
`NullPointerException` - if threadFactory is null

