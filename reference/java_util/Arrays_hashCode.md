#### hashCode

```
public static int hashCode(Object[] a)
```
Returns a hash code based on the contents of the specified array. If
the array contains other arrays as elements, the hash code is based on
their identities rather than their contents. It is therefore
acceptable to invoke this method on an array that contains itself as an
element, either directly or indirectly through one or more levels of
arrays.For any two arrays a and b such that
Arrays.equals(a, b), it is also the case that
Arrays.hashCode(a) == Arrays.hashCode(b).The value returned by this method is equal to the value that would
be returned by Arrays.asList(a).hashCode(), unless a
is null, in which case 0 is returned.
Parameters:
`a` - the array whose content-based hash code to compute
Returns:
a content-based hash code for a
Since:
1.5
See Also:
`deepHashCode(Object[])`

