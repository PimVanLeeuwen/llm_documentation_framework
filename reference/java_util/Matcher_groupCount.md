#### groupCount

```
public int groupCount()
```
Returns the number of capturing groups in this matcher's pattern.Group zero denotes the entire pattern by convention. It is not
included in this count.Any non-negative integer smaller than or equal to the value
returned by this method is guaranteed to be a valid group index for
this matcher.
Specified by:
`groupCount` in interface `MatchResult`
Returns:
The number of capturing groups in this matcher's pattern

