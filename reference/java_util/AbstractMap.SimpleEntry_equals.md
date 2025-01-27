#### equals

```
public boolean equals(Object o)
```
Compares the specified object with this entry for equality.
Returns `true` if the given object is also a map entry and
the two entries represent the same mapping. More formally, two
entries `e1` and `e2` represent the same mapping
if
```

   (e1.getKey()==null ?
    e2.getKey()==null :
    e1.getKey().equals(e2.getKey()))
   &&
   (e1.getValue()==null ?
    e2.getValue()==null :
    e1.getValue().equals(e2.getValue()))
```
This ensures that the `equals` method works properly across
different implementations of the `Map.Entry` interface.
Specified by:
`equals` in interface `Map.Entry<K,V>`
Overrides:
`equals` in class `Object`
Parameters:
`o` - object to be compared for equality with this map entry
Returns:
`true` if the specified object is equal to this map
entry
See Also:
`hashCode()`

