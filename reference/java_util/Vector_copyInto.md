#### copyInto

```
public void copyInto(Object[] anArray)
```
Copies the components of this vector into the specified array.
The item at index `k` in this vector is copied into
component `k` of `anArray`.
Parameters:
`anArray` - the array into which the components get copied
Throws:
`NullPointerException` - if the given array is null
`IndexOutOfBoundsException` - if the specified array is not
large enough to hold all the components of this vector
`ArrayStoreException` - if a component of this vector is not of
a runtime type that can be stored in the specified array
See Also:
`toArray(Object[])`

