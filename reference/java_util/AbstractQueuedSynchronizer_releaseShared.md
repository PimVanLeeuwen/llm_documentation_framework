#### releaseShared

```
public final boolean releaseShared(int arg)
```
Releases in shared mode. Implemented by unblocking one or more
threads if `tryReleaseShared(int)` returns true.
Parameters:
`arg` - the release argument. This value is conveyed to
`tryReleaseShared(int)` but is otherwise uninterpreted
and can represent anything you like.
Returns:
the value returned from `tryReleaseShared(int)`

