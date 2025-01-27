#### tryReleaseShared

```
protected boolean tryReleaseShared(long arg)
```
Attempts to set the state to reflect a release in shared mode.This method is always invoked by the thread performing release.The default implementation throws
`UnsupportedOperationException`.
Parameters:
`arg` - the release argument. This value is always the one
passed to a release method, or the current state value upon
entry to a condition wait. The value is otherwise
uninterpreted and can represent anything you like.
Returns:
`true` if this release of shared mode may permit a
waiting acquire (shared or exclusive) to succeed; and
`false` otherwise
Throws:
`IllegalMonitorStateException` - if releasing would place this
synchronizer in an illegal state. This exception must be
thrown in a consistent fashion for synchronization to work
correctly.
`UnsupportedOperationException` - if shared mode is not supported

