#### getBlocker

```
public static Object getBlocker(Thread t)
```
Returns the blocker object supplied to the most recent
invocation of a park method that has not yet unblocked, or null
if not blocked. The value returned is just a momentary
snapshot -- the thread may have since unblocked or blocked on a
different blocker object.
Parameters:
`t` - the thread
Returns:
the blocker
Throws:
`NullPointerException` - if argument is null
Since:
1.6

