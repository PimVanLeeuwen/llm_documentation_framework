#### deepHashCode

```
public static int deepHashCode(Object[] a)
```
Returns a hash code based on the "deep contents" of the specified
array. If the array contains other arrays as elements, the
hash code is based on their contents and so on, ad infinitum.
It is therefore unacceptable to invoke this method on an array that
contains itself as an element, either directly or indirectly through
one or more levels of arrays. The behavior of such an invocation is
undefined.For any two arrays a and b such that
Arrays.deepEquals(a, b), it is also the case that
Arrays.deepHashCode(a) == Arrays.deepHashCode(b).The computation of the value returned by this method is similar to
that of the value returned by `List.hashCode()` on a list
containing the same elements as a in the same order, with one
difference: If an element e of a is itself an array,
its hash code is computed not by calling e.hashCode(), but as
by calling the appropriate overloading of Arrays.hashCode(e)
if e is an array of a primitive type, or as by calling
Arrays.deepHashCode(e) recursively if e is an array
of a reference type. If a is null, this method
returns 0.
Parameters:
`a` - the array whose deep-content-based hash code to compute
Returns:
a deep-content-based hash code for a
Since:
1.5
See Also:
`hashCode(Object[])`

