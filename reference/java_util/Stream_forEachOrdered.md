#### forEachOrdered

```
void forEachOrdered(Consumer<? super T> action)
```
Performs an action for each element of this stream, in the encounter
order of the stream if the stream has a defined encounter order.This is a terminal
operation.This operation processes the elements one at a time, in encounter
order if one exists. Performing the action for one element
happens-before
performing the action for subsequent elements, but for any given element,
the action may be performed in whatever thread the library chooses.
Parameters:
`action` - a 
non-interfering action to perform on the elements
See Also:
`forEach(Consumer)`

