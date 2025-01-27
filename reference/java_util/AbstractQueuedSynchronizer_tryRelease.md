#### tryRelease

```
protected boolean tryRelease(int arg)
```
Attempts to set the state to reflect a release in exclusive
mode.This method is always invoked by the thread performing release.The default implementation throws
`UnsupportedOperationException`.
Parameters:
`arg` - the release argument. This value is always the one
passed to a release method, or the current state value upon
entry to a condition wait. The value is otherwise
uninterpreted and can represent anything you like.
Returns:
`true` if this object is now in a fully released
state, so that any waiting threads may attempt to acquire;
and `false` otherwise.
Throws:
`IllegalMonitorStateException` - if releasing would place this
synchronizer in an illegal state. This exception must be
thrown in a consistent fashion for synchronization to work
correctly.
`UnsupportedOperationException` - if exclusive mode is not supported

