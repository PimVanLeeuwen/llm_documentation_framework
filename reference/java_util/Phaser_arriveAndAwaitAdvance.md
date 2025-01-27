#### arriveAndAwaitAdvance

```
public int arriveAndAwaitAdvance()
```
Arrives at this phaser and awaits others. Equivalent in effect
to `awaitAdvance(arrive())`. If you need to await with
interruption or timeout, you can arrange this with an analogous
construction using one of the other forms of the `awaitAdvance` method. If instead you need to deregister upon
arrival, use `awaitAdvance(arriveAndDeregister())`.It is a usage error for an unregistered party to invoke this
method. However, this error may result in an `IllegalStateException` only upon some subsequent operation on
this phaser, if ever.
Returns:
the arrival phase number, or the (negative)
current phase if terminated
Throws:
`IllegalStateException` - if not terminated and the number
of unarrived parties would become negative

