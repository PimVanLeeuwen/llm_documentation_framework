#### getPoolSize

```
public int getPoolSize()
```
Returns the number of worker threads that have started but not
yet terminated. The result returned by this method may differ
from `getParallelism()` when threads are created to
maintain parallelism when others are cooperatively blocked.
Returns:
the number of worker threads

