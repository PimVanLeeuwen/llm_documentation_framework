#### compareAndSet

```
public boolean compareAndSet(V expectedReference,
                             V newReference,
                             int expectedStamp,
                             int newStamp)
```
Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is `==` to the expected reference
and the current stamp is equal to the expected stamp.
Parameters:
`expectedReference` - the expected value of the reference
`newReference` - the new value for the reference
`expectedStamp` - the expected value of the stamp
`newStamp` - the new value for the stamp
Returns:
`true` if successful

