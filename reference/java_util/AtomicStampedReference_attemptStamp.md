#### attemptStamp

```
public boolean attemptStamp(V expectedReference,
                            int newStamp)
```
Atomically sets the value of the stamp to the given update value
if the current reference is `==` to the expected
reference. Any given invocation of this operation may fail
(return `false`) spuriously, but repeated invocation
when the current value holds the expected value and no other
thread is also attempting to set the value will eventually
succeed.
Parameters:
`expectedReference` - the expected value of the reference
`newStamp` - the new value for the stamp
Returns:
`true` if successful




