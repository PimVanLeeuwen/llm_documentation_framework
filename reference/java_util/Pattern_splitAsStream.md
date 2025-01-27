#### splitAsStream

```
public Stream<String> splitAsStream(CharSequence input)
```
Creates a stream from the given input sequence around matches of this
pattern.The stream returned by this method contains each substring of the
input sequence that is terminated by another subsequence that matches
this pattern or is terminated by the end of the input sequence. The
substrings in the stream are in the order in which they occur in the
input. Trailing empty strings will be discarded and not encountered in
the stream.If this pattern does not match any subsequence of the input then
the resulting stream has just one element, namely the input sequence in
string form.When there is a positive-width match at the beginning of the input
sequence then an empty leading substring is included at the beginning
of the stream. A zero-width match at the beginning however never produces
such empty leading substring.If the input sequence is mutable, it must remain constant during the
execution of the terminal stream operation. Otherwise, the result of the
terminal stream operation is undefined.
Parameters:
`input` - The character sequence to be split
Returns:
The stream of strings computed by splitting the input
around matches of this pattern
Since:
1.8
See Also:
`split(CharSequence)`




