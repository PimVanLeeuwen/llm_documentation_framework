#### range

```
public static <E extends Enum<E>> EnumSet<E> range(E from,
                                                   E to)
```
Creates an enum set initially containing all of the elements in the
range defined by the two specified endpoints. The returned set will
contain the endpoints themselves, which may be identical but must not
be out of order.
Type Parameters:
`E` - The class of the parameter elements and of the set
Parameters:
`from` - the first element in the range
`to` - the last element in the range
Returns:
an enum set initially containing all of the elements in the
range defined by the two specified endpoints
Throws:
`NullPointerException` - if `from` or `to` are null
`IllegalArgumentException` - if `from.compareTo(to) > 0`

