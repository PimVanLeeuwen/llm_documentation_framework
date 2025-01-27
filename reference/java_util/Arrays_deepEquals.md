#### deepEquals

```
public static boolean deepEquals(Object[] a1,
                                 Object[] a2)
```
Returns true if the two specified arrays are deeply
equal to one another. Unlike the `equals(Object[],Object[])`
method, this method is appropriate for use with nested arrays of
arbitrary depth.Two array references are considered deeply equal if both
are null, or if they refer to arrays that contain the same
number of elements and all corresponding pairs of elements in the two
arrays are deeply equal.Two possibly null elements e1 and e2 are
deeply equal if any of the following conditions hold:e1 and e2 are both arrays of object reference
types, and Arrays.deepEquals(e1, e2) would return truee1 and e2 are arrays of the same primitive
type, and the appropriate overloading of
Arrays.equals(e1, e2) would return true.e1 == e2e1.equals(e2) would return true.Note that this definition permits null elements at any depth.If either of the specified arrays contain themselves as elements
either directly or indirectly through one or more levels of arrays,
the behavior of this method is undefined.
Parameters:
`a1` - one array to be tested for equality
`a2` - the other array to be tested for equality
Returns:
true if the two arrays are equal
Since:
1.5
See Also:
`equals(Object[],Object[])`,
`Objects.deepEquals(Object, Object)`

