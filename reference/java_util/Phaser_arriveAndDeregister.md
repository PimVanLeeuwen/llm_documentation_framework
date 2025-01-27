#### arriveAndDeregister

```
public int arriveAndDeregister()
```
Arrives at this phaser and deregisters from it without waiting
for others to arrive. Deregistration reduces the number of
parties required to advance in future phases. If this phaser
has a parent, and deregistration causes this phaser to have
zero parties, this phaser is also deregistered from its parent.It is a usage error for an unregistered party to invoke this
method. However, this error may result in an `IllegalStateException` only upon some subsequent operation on
this phaser, if ever.
Returns:
the arrival phase number, or a negative value if terminated
Throws:
`IllegalStateException` - if not terminated and the number
of registered or unarrived parties would become negative

