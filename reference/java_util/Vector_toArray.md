#### toArray

```
public <T> T[] toArray(T[] a)
```
Returns an array containing all of the elements in this Vector in the
correct order; the runtime type of the returned array is that of the
specified array. If the Vector fits in the specified array, it is
returned therein. Otherwise, a new array is allocated with the runtime
type of the specified array and the size of this Vector.If the Vector fits in the specified array with room to spare
(i.e., the array has more elements than the Vector),
the element in the array immediately following the end of the
Vector is set to null. (This is useful in determining the length
of the Vector only if the caller knows that the Vector
does not contain any null elements.)
Specified by:
`toArray` in interface `Collection<E>`
Specified by:
`toArray` in interface `List<E>`
Overrides:
`toArray` in class `AbstractCollection<E>`
Type Parameters:
`T` - the runtime type of the array to contain the collection
Parameters:
`a` - the array into which the elements of the Vector are to
be stored, if it is big enough; otherwise, a new array of the
same runtime type is allocated for this purpose.
Returns:
an array containing the elements of the Vector
Throws:
`ArrayStoreException` - if the runtime type of a is not a supertype
of the runtime type of every element in this Vector
`NullPointerException` - if the given array is null
Since:
1.2

