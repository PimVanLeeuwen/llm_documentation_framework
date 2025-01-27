#### drainTo

```
int drainTo(Collection<? super E> c,
            int maxElements)
```
Removes at most the given number of available elements from
this queue and adds them to the given collection. A failure
encountered while attempting to add elements to
collection `c` may result in elements being in neither,
either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in
`IllegalArgumentException`. Further, the behavior of
this operation is undefined if the specified collection is
modified while the operation is in progress.
Parameters:
`c` - the collection to transfer elements into
`maxElements` - the maximum number of elements to transfer
Returns:
the number of elements transferred
Throws:
`UnsupportedOperationException` - if addition of elements
is not supported by the specified collection
`ClassCastException` - if the class of an element of this queue
prevents it from being added to the specified collection
`NullPointerException` - if the specified collection is null
`IllegalArgumentException` - if the specified collection is this
queue, or some property of an element of this queue prevents
it from being added to the specified collection




