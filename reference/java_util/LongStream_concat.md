#### concat

```
static LongStream concat(LongStream a,
                         LongStream b)
```
Creates a lazily concatenated stream whose elements are all the
elements of the first stream followed by all the elements of the
second stream. The resulting stream is ordered if both
of the input streams are ordered, and parallel if either of the input
streams is parallel. When the resulting stream is closed, the close
handlers for both input streams are invoked.
Implementation Note:
Use caution when constructing streams from repeated concatenation.
Accessing an element of a deeply concatenated stream can result in deep
call chains, or even `StackOverflowException`.
Parameters:
`a` - the first stream
`b` - the second stream
Returns:
the concatenation of the two input streams




