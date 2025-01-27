#### toArray

```
public <T> T[] toArray(T[] a)
```
Returns an array containing all of the elements in this list in proper
sequence (from first to last element); the runtime type of the returned
array is that of the specified array. If the list fits in the
specified array, it is returned therein. Otherwise, a new array is
allocated with the runtime type of the specified array and the size of
this list.If the list fits in the specified array with room to spare
(i.e., the array has more elements than the list), the element in
the array immediately following the end of the collection is set to
null. (This is useful in determining the length of the
list only if the caller knows that the list does not contain
any null elements.)
Specified by:
`toArray` in interface `Collection<E>`
Specified by:
`toArray` in interface `List<E>`
Overrides:
`toArray` in class `AbstractCollection<E>`
Type Parameters:
`T` - the runtime type of the array to contain the collection
Parameters:
`a` - the array into which the elements of the list are to
be stored, if it is big enough; otherwise, a new array of the
same runtime type is allocated for this purpose.
Returns:
an array containing the elements of the list
Throws:
`ArrayStoreException` - if the runtime type of the specified array
is not a supertype of the runtime type of every element in
this list
`NullPointerException` - if the specified array is null

