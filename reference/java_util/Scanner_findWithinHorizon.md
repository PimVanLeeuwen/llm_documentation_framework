#### findWithinHorizon

```
public String findWithinHorizon(Pattern pattern,
                                int horizon)
```
Attempts to find the next occurrence of the specified pattern.This method searches through the input up to the specified
search horizon, ignoring delimiters. If the pattern is found the
scanner advances past the input that matched and returns the string
that matched the pattern. If no such pattern is detected then the
null is returned and the scanner's position remains unchanged. This
method may block waiting for input that matches the pattern.A scanner will never search more than `horizon` code
points beyond its current position. Note that a match may be clipped
by the horizon; that is, an arbitrary match result may have been
different if the horizon had been larger. The scanner treats the
horizon as a transparent, non-anchoring bound (see `Matcher.useTransparentBounds(boolean)` and `Matcher.useAnchoringBounds(boolean)`).If horizon is `0`, then the horizon is ignored and
this method continues to search through the input looking for the
specified pattern without bound. In this case it may buffer all of
the input searching for the pattern.If horizon is negative, then an IllegalArgumentException is
thrown.
Parameters:
`pattern` - the pattern to scan for
`horizon` - the search horizon
Returns:
the text that matched the specified pattern
Throws:
`IllegalStateException` - if this scanner is closed
`IllegalArgumentException` - if horizon is negative

