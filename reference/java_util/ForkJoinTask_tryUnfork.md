#### tryUnfork

```
public boolean tryUnfork()
```
Tries to unschedule this task for execution. This method will
typically (but is not guaranteed to) succeed if this task is
the most recently forked task by the current thread, and has
not commenced executing in another thread. This method may be
useful when arranging alternative local processing of tasks
that could have been, but were not, stolen.
Returns:
`true` if unforked

