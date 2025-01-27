#### releaseShared

```
public final boolean releaseShared(long arg)
```
Releases in shared mode. Implemented by unblocking one or more
threads if `tryReleaseShared(long)` returns true.
Parameters:
`arg` - the release argument. This value is conveyed to
`tryReleaseShared(long)` but is otherwise uninterpreted
and can represent anything you like.
Returns:
the value returned from `tryReleaseShared(long)`

