#### toArray

```
public <T> T[] toArray(T[] a)
```
Returns an array containing all of the elements in this queue, in
proper sequence; the runtime type of the returned array is that of
the specified array. If the queue fits in the specified array, it
is returned therein. Otherwise, a new array is allocated with the
runtime type of the specified array and the size of this queue.If this queue fits in the specified array with room to spare
(i.e., the array has more elements than this queue), the element in
the array immediately following the end of the queue is set to
`null`.Like the `toArray()` method, this method acts as bridge between
array-based and collection-based APIs. Further, this method allows
precise control over the runtime type of the output array, and may,
under certain circumstances, be used to save allocation costs.Suppose `x` is a queue known to contain only strings.
The following code can be used to dump the queue into a newly
allocated array of `String`:
```
  String[] y = x.toArray(new String[0]);
```
Note that `toArray(new Object[0])` is identical in function to
`toArray()`.
Specified by:
`toArray` in interface `Collection<E>`
Overrides:
`toArray` in class `AbstractCollection<E>`
Type Parameters:
`T` - the runtime type of the array to contain the collection
Parameters:
`a` - the array into which the elements of the queue are to
be stored, if it is big enough; otherwise, a new array of the
same runtime type is allocated for this purpose
Returns:
an array containing all of the elements in this queue
Throws:
`ArrayStoreException` - if the runtime type of the specified array
is not a supertype of the runtime type of every element in
this queue
`NullPointerException` - if the specified array is null

