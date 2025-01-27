#### getDSTSavings

```
public int getDSTSavings()
```
Returns the amount of time in milliseconds that the clock is
advanced during daylight saving time.
Overrides:
`getDSTSavings` in class `TimeZone`
Returns:
the number of milliseconds the time is advanced with
respect to standard time when the daylight saving rules are in
effect, or 0 (zero) if this time zone doesn't observe daylight
saving time.
Since:
1.2
See Also:
`setDSTSavings(int)`

