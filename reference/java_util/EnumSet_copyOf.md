#### copyOf

```
public static <E extends Enum<E>> EnumSet<E> copyOf(Collection<E> c)
```
Creates an enum set initialized from the specified collection. If
the specified collection is an EnumSet instance, this static
factory method behaves identically to `copyOf(EnumSet)`.
Otherwise, the specified collection must contain at least one element
(in order to determine the new enum set's element type).
Type Parameters:
`E` - The class of the elements in the collection
Parameters:
`c` - the collection from which to initialize this enum set
Returns:
An enum set initialized from the given collection.
Throws:
`IllegalArgumentException` - if c is not an
EnumSet instance and contains no elements
`NullPointerException` - if c is null

