#### awaitAdvance

```
public int awaitAdvance(int phase)
```
Awaits the phase of this phaser to advance from the given phase
value, returning immediately if the current phase is not equal
to the given phase value or this phaser is terminated.
Parameters:
`phase` - an arrival phase number, or negative value if
terminated; this argument is normally the value returned by a
previous call to `arrive` or `arriveAndDeregister`.
Returns:
the next arrival phase number, or the argument if it is
negative, or the (negative) current phase
if terminated

