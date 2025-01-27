#### allowCoreThreadTimeOut

```
public void allowCoreThreadTimeOut(boolean value)
```
Sets the policy governing whether core threads may time out and
terminate if no tasks arrive within the keep-alive time, being
replaced if needed when new tasks arrive. When false, core
threads are never terminated due to lack of incoming
tasks. When true, the same keep-alive policy applying to
non-core threads applies also to core threads. To avoid
continual thread replacement, the keep-alive time must be
greater than zero when setting `true`. This method
should in general be called before the pool is actively used.
Parameters:
`value` - `true` if should time out, else `false`
Throws:
`IllegalArgumentException` - if value is `true`
and the current keep-alive time is not greater than zero
Since:
1.6

