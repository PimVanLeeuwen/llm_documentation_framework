#### release

```
public final boolean release(long arg)
```
Releases in exclusive mode. Implemented by unblocking one or
more threads if `tryRelease(long)` returns true.
This method can be used to implement method `Lock.unlock()`.
Parameters:
`arg` - the release argument. This value is conveyed to
`tryRelease(long)` but is otherwise uninterpreted and
can represent anything you like.
Returns:
the value returned from `tryRelease(long)`

