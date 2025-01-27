#### attemptMark

```
public boolean attemptMark(V expectedReference,
                           boolean newMark)
```
Atomically sets the value of the mark to the given update value
if the current reference is `==` to the expected
reference. Any given invocation of this operation may fail
(return `false`) spuriously, but repeated invocation
when the current value holds the expected value and no other
thread is also attempting to set the value will eventually
succeed.
Parameters:
`expectedReference` - the expected value of the reference
`newMark` - the new value for the mark
Returns:
`true` if successful




