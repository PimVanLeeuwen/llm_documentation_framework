#### toArray

```
<A> A[] toArray(IntFunction<A[]> generator)
```
Returns an array containing the elements of this stream, using the
provided `generator` function to allocate the returned array, as
well as any additional arrays that might be required for a partitioned
execution or for resizing.This is a terminal
operation.
API Note:
The generator function takes an integer, which is the size of the
desired array, and produces an array of the desired size. This can be
concisely expressed with an array constructor reference:
```

     Person[] men = people.stream()
                          .filter(p -> p.getGender() == MALE)
                          .toArray(Person[]::new);
 
```

Type Parameters:
`A` - the element type of the resulting array
Parameters:
`generator` - a function which produces a new array of the desired
type and the provided length
Returns:
an array containing the elements in this stream
Throws:
`ArrayStoreException` - if the runtime type of the array returned
from the array generator is not a supertype of the runtime type of every
element in this stream

