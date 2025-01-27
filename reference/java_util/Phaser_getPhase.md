#### getPhase

```
public final int getPhase()
```
Returns the current phase number. The maximum phase number is
`Integer.MAX_VALUE`, after which it restarts at
zero. Upon termination, the phase number is negative,
in which case the prevailing phase prior to termination
may be obtained via `getPhase() + Integer.MIN_VALUE`.
Returns:
the phase number, or a negative value if terminated

