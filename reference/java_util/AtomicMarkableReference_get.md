#### get

```
public V get(boolean[] markHolder)
```
Returns the current values of both the reference and the mark.
Typical usage is `boolean[1] holder; ref = v.get(holder);` .
Parameters:
`markHolder` - an array of size of at least one. On return,
`markholder[0]` will hold the value of the mark.
Returns:
the current value of the reference

