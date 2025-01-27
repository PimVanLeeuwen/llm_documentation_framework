#### getExactSizeIfKnown

```
default long getExactSizeIfKnown()
```
Convenience method that returns `estimateSize()` if this
Spliterator is `SIZED`, else `-1`.
Implementation Requirements:
The default implementation returns the result of `estimateSize()`
if the Spliterator reports a characteristic of `SIZED`, and
`-1` otherwise.
Returns:
the exact size, if known, else `-1`.

