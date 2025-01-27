#### allOf

```
public static <E extends Enum<E>> EnumSet<E> allOf(Class<E> elementType)
```
Creates an enum set containing all of the elements in the specified
element type.
Type Parameters:
`E` - The class of the elements in the set
Parameters:
`elementType` - the class object of the element type for this enum
set
Returns:
An enum set containing all the elements in the specified type.
Throws:
`NullPointerException` - if elementType is null

