#### get

```
public V get(int[] stampHolder)
```
Returns the current values of both the reference and the stamp.
Typical usage is `int[1] holder; ref = v.get(holder);` .
Parameters:
`stampHolder` - an array of size of at least one. On return,
`stampholder[0]` will hold the value of the stamp.
Returns:
the current value of the reference

