#### useAnchoringBounds

```
public Matcher useAnchoringBounds(boolean b)
```
Sets the anchoring of region bounds for this matcher.Invoking this method with an argument of true will set this
matcher to use anchoring bounds. If the boolean
argument is false, then non-anchoring bounds will be
used.Using anchoring bounds, the boundaries of this
matcher's region match anchors such as ^ and $.Without anchoring bounds, the boundaries of this
matcher's region will not match anchors such as ^ and $.By default, a matcher uses anchoring region boundaries.
Parameters:
`b` - a boolean indicating whether or not to use anchoring bounds.
Returns:
this matcher
Since:
1.5
See Also:
`hasAnchoringBounds()`

