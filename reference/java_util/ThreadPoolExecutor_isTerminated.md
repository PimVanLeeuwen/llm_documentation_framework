#### isTerminated

```
public boolean isTerminated()
```
Description copied from interface: `ExecutorService`
Returns `true` if all tasks have completed following shut down.
Note that `isTerminated` is never `true` unless
either `shutdown` or `shutdownNow` was called first.
Returns:
`true` if all tasks have completed following shut down

