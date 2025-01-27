#### onCompletion

```
public void onCompletion(CountedCompleter<?> caller)
```
Performs an action when method `tryComplete()` is invoked
and the pending count is zero, or when the unconditional
method `complete(T)` is invoked. By default, this method
does nothing. You can distinguish cases by checking the
identity of the given caller argument. If not equal to `this`, then it is typically a subtask that may contain results
(and/or links to other results) to combine.
Parameters:
`caller` - the task invoking this method (which may
be this task itself)

