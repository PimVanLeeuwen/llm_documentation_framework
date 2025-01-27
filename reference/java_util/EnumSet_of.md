#### of

```
@SafeVarargs
public static <E extends Enum<E>> EnumSet<E> of(E first,
                                                             E... rest)
```
Creates an enum set initially containing the specified elements.
This factory, whose parameter list uses the varargs feature, may
be used to create an enum set initially containing an arbitrary
number of elements, but it is likely to run slower than the overloadings
that do not use varargs.
Type Parameters:
`E` - The class of the parameter elements and of the set
Parameters:
`first` - an element that the set is to contain initially
`rest` - the remaining elements the set is to contain initially
Returns:
an enum set initially containing the specified elements
Throws:
`NullPointerException` - if any of the specified elements are null,
or if rest is null

