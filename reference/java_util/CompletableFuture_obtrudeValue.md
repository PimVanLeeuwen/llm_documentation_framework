#### obtrudeValue

```
public void obtrudeValue(T value)
```
Forcibly sets or resets the value subsequently returned by
method `get()` and related methods, whether or not
already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.
Parameters:
`value` - the completion value

