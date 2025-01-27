#### toArray

```
<T> T[] toArray(T[] a)
```
Returns an array containing all of the elements in this set; the
runtime type of the returned array is that of the specified array.
If the set fits in the specified array, it is returned therein.
Otherwise, a new array is allocated with the runtime type of the
specified array and the size of this set.If this set fits in the specified array with room to spare
(i.e., the array has more elements than this set), the element in
the array immediately following the end of the set is set to
null. (This is useful in determining the length of this
set only if the caller knows that this set does not contain
any null elements.)If this set makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements
in the same order.Like the `toArray()` method, this method acts as bridge between
array-based and collection-based APIs. Further, this method allows
precise control over the runtime type of the output array, and may,
under certain circumstances, be used to save allocation costs.Suppose x is a set known to contain only strings.
The following code can be used to dump the set into a newly allocated
array of String:
```

     String[] y = x.toArray(new String[0]);
```
Note that toArray(new Object[0]) is identical in function to
toArray().
Specified by:
`toArray` in interface `Collection<E>`
Type Parameters:
`T` - the runtime type of the array to contain the collection
Parameters:
`a` - the array into which the elements of this set are to be
stored, if it is big enough; otherwise, a new array of the same
runtime type is allocated for this purpose.
Returns:
an array containing all the elements in this set
Throws:
`ArrayStoreException` - if the runtime type of the specified array
is not a supertype of the runtime type of every element in this
set
`NullPointerException` - if the specified array is null

