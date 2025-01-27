#### newUpdater

```
public static <U,W> AtomicReferenceFieldUpdater<U,W> newUpdater(Class<U> tclass,
                                                                Class<W> vclass,
                                                                String fieldName)
```
Creates and returns an updater for objects with the given field.
The Class arguments are needed to check that reflective types and
generic types match.
Type Parameters:
`U` - the type of instances of tclass
`W` - the type of instances of vclass
Parameters:
`tclass` - the class of the objects holding the field
`vclass` - the class of the field
`fieldName` - the name of the field to be updated
Returns:
the updater
Throws:
`ClassCastException` - if the field is of the wrong type
`IllegalArgumentException` - if the field is not volatile
`RuntimeException` - with a nested reflection-based
exception if the class does not hold field or is the wrong type,
or the field is inaccessible to the caller according to Java language
access control

