#### deepToString

```
public static String deepToString(Object[] a)
```
Returns a string representation of the "deep contents" of the specified
array. If the array contains other arrays as elements, the string
representation contains their contents and so on. This method is
designed for converting multidimensional arrays to strings.The string representation consists of a list of the array's
elements, enclosed in square brackets ("[]"). Adjacent
elements are separated by the characters ", " (a comma
followed by a space). Elements are converted to strings as by
String.valueOf(Object), unless they are themselves
arrays.If an element e is an array of a primitive type, it is
converted to a string as by invoking the appropriate overloading of
Arrays.toString(e). If an element e is an array of a
reference type, it is converted to a string as by invoking
this method recursively.To avoid infinite recursion, if the specified array contains itself
as an element, or contains an indirect reference to itself through one
or more levels of arrays, the self-reference is converted to the string
"[...]". For example, an array containing only a reference
to itself would be rendered as "[[...]]".This method returns "null" if the specified array
is null.
Parameters:
`a` - the array whose string representation to return
Returns:
a string representation of a
Since:
1.5
See Also:
`toString(Object[])`

