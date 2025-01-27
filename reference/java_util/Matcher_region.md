#### region

```
public Matcher region(int start,
                      int end)
```
Sets the limits of this matcher's region. The region is the part of the
input sequence that will be searched to find a match. Invoking this
method resets the matcher, and then sets the region to start at the
index specified by the `start` parameter and end at the
index specified by the `end` parameter.Depending on the transparency and anchoring being used (see
`useTransparentBounds` and
`useAnchoringBounds`), certain constructs such
as anchors may behave differently at or around the boundaries of the
region.
Parameters:
`start` - The index to start searching at (inclusive)
`end` - The index to end searching at (exclusive)
Returns:
this matcher
Throws:
`IndexOutOfBoundsException` - If start or end is less than zero, if
start is greater than the length of the input sequence, if
end is greater than the length of the input sequence, or if
start is greater than end.
Since:
1.5

