#### commonPool

```
public static ForkJoinPool commonPool()
```
Returns the common pool instance. This pool is statically
constructed; its run state is unaffected by attempts to `shutdown()` or `shutdownNow()`. However this pool and any
ongoing processing are automatically terminated upon program
`System.exit(int)`. Any program that relies on asynchronous
task processing to complete before program termination should
invoke `commonPool().``awaitQuiescence`,
before exit.
Returns:
the common pool instance
Since:
1.8

