#### complementOf

```
public static <E extends Enum<E>> EnumSet<E> complementOf(EnumSet<E> s)
```
Creates an enum set with the same element type as the specified enum
set, initially containing all the elements of this type that are
not contained in the specified set.
Type Parameters:
`E` - The class of the elements in the enum set
Parameters:
`s` - the enum set from whose complement to initialize this enum set
Returns:
The complement of the specified set in this set
Throws:
`NullPointerException` - if s is null

