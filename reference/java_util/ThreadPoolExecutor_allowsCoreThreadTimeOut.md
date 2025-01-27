#### allowsCoreThreadTimeOut

```
public boolean allowsCoreThreadTimeOut()
```
Returns true if this pool allows core threads to time out and
terminate if no tasks arrive within the keepAlive time, being
replaced if needed when new tasks arrive. When true, the same
keep-alive policy applying to non-core threads applies also to
core threads. When false (the default), core threads are never
terminated due to lack of incoming tasks.
Returns:
`true` if core threads are allowed to time out,
else `false`
Since:
1.6

