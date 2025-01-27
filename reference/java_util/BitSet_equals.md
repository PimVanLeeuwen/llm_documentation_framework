#### equals

```
public boolean equals(Object obj)
```
Compares this object against the specified object.
The result is `true` if and only if the argument is
not `null` and is a `Bitset` object that has
exactly the same set of bits set to `true` as this bit
set. That is, for every nonnegative `int` index `k`,
```
((BitSet)obj).get(k) == this.get(k)
```
must be true. The current sizes of the two bit sets are not compared.
Overrides:
`equals` in class `Object`
Parameters:
`obj` - the object to compare with
Returns:
`true` if the objects are the same;
`false` otherwise
See Also:
`size()`

