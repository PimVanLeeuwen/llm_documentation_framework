#### isQuiescent

```
public boolean isQuiescent()
```
Returns `true` if all worker threads are currently idle.
An idle worker is one that cannot obtain a task to execute
because none are available to steal from other threads, and
there are no pending submissions to the pool. This method is
conservative; it might not return `true` immediately upon
idleness of all threads, but will eventually become true if
threads remain inactive.
Returns:
`true` if all threads are currently idle

