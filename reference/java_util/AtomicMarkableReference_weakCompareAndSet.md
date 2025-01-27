#### weakCompareAndSet

```
public boolean weakCompareAndSet(V expectedReference,
                                 V newReference,
                                 boolean expectedMark,
                                 boolean newMark)
```
Atomically sets the value of both the reference and mark
to the given update values if the
current reference is `==` to the expected reference
and the current mark is equal to the expected mark.May fail
spuriously and does not provide ordering guarantees, so is
only rarely an appropriate alternative to `compareAndSet`.
Parameters:
`expectedReference` - the expected value of the reference
`newReference` - the new value for the reference
`expectedMark` - the expected value of the mark
`newMark` - the new value for the mark
Returns:
`true` if successful

