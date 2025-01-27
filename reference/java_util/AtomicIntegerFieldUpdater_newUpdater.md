#### newUpdater

```
public static <U> AtomicIntegerFieldUpdater<U> newUpdater(Class<U> tclass,
                                                          String fieldName)
```
Creates and returns an updater for objects with the given field.
The Class argument is needed to check that reflective types and
generic types match.
Type Parameters:
`U` - the type of instances of tclass
Parameters:
`tclass` - the class of the objects holding the field
`fieldName` - the name of the field to be updated
Returns:
the updater
Throws:
`IllegalArgumentException` - if the field is not a
volatile integer type
`RuntimeException` - with a nested reflection-based
exception if the class does not hold field or is the wrong type,
or the field is inaccessible to the caller according to Java language
access control

