#### toString

```
public static String toString(Object[] a)
```
Returns a string representation of the contents of the specified array.
If the array contains other arrays as elements, they are converted to
strings by the `Object.toString()` method inherited from
Object, which describes their identities rather than
their contents.The value returned by this method is equal to the value that would
be returned by Arrays.asList(a).toString(), unless a
is null, in which case "null" is returned.
Parameters:
`a` - the array whose string representation to return
Returns:
a string representation of a
Since:
1.5
See Also:
`deepToString(Object[])`

