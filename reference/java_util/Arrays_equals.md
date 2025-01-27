#### equals

```
public static boolean equals(Object[] a,
                             Object[] a2)
```
Returns true if the two specified arrays of Objects are
equal to one another. The two arrays are considered equal if
both arrays contain the same number of elements, and all corresponding
pairs of elements in the two arrays are equal. Two objects e1
and e2 are considered equal if (e1==null ? e2==null
: e1.equals(e2)). In other words, the two arrays are equal if
they contain the same elements in the same order. Also, two array
references are considered equal if both are null.
Parameters:
`a` - one array to be tested for equality
`a2` - the other array to be tested for equality
Returns:
true if the two arrays are equal

