#### fork

```
public final ForkJoinTask<V> fork()
```
Arranges to asynchronously execute this task in the pool the
current task is running in, if applicable, or using the `ForkJoinPool.commonPool()` if not `inForkJoinPool()`. While
it is not necessarily enforced, it is a usage error to fork a
task more than once unless it has completed and been
reinitialized. Subsequent modifications to the state of this
task or any data it operates on are not necessarily
consistently observable by any thread other than the one
executing it unless preceded by a call to `join()` or
related methods, or a call to `isDone()` returning `true`.
Returns:
`this`, to simplify usage

