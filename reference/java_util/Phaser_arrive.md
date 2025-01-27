#### arrive

```
public int arrive()
```
Arrives at this phaser, without waiting for others to arrive.It is a usage error for an unregistered party to invoke this
method. However, this error may result in an `IllegalStateException` only upon some subsequent operation on
this phaser, if ever.
Returns:
the arrival phase number, or a negative value if terminated
Throws:
`IllegalStateException` - if not terminated and the number
of unarrived parties would become negative

