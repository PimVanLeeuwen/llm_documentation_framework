#### bulkRegister

```
public int bulkRegister(int parties)
```
Adds the given number of new unarrived parties to this phaser.
If an ongoing invocation of `onAdvance(int, int)` is in progress,
this method may await its completion before returning. If this
phaser has a parent, and the given number of parties is greater
than zero, and this phaser previously had no registered
parties, this child phaser is also registered with its parent.
If this phaser is terminated, the attempt to register has no
effect, and a negative value is returned.
Parameters:
`parties` - the number of additional parties required to
advance to the next phase
Returns:
the arrival phase number to which this registration
applied. If this value is negative, then this phaser has
terminated, in which case registration has no effect.
Throws:
`IllegalStateException` - if attempting to register more
than the maximum supported number of parties
`IllegalArgumentException` - if `parties < 0`

