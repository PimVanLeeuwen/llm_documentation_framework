#### flatMap

```
<R> Stream<R> flatMap(Function<? super T,? extends Stream<? extends R>> mapper)
```
Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element. Each mapped stream is
`closed` after its contents
have been placed into this stream. (If a mapped stream is `null`
an empty stream is used, instead.)This is an intermediate
operation.
API Note:
The `flatMap()` operation has the effect of applying a one-to-many
transformation to the elements of the stream, and then flattening the
resulting elements into a new stream.Examples.If `orders` is a stream of purchase orders, and each purchase
order contains a collection of line items, then the following produces a
stream containing all the line items in all the orders:
```

     orders.flatMap(order -> order.getLineItems().stream())...
 
```
If `path` is the path to a file, then the following produces a
stream of the `words` contained in that file:
```

     Stream<String> lines = Files.lines(path, StandardCharsets.UTF_8);
     Stream<String> words = lines.flatMap(line -> Stream.of(line.split(" +")));
 
```
The `mapper` function passed to `flatMap` splits a line,
using a simple regular expression, into an array of words, and then
creates a stream of words from that array.
Type Parameters:
`R` - The element type of the new stream
Parameters:
`mapper` - a non-interfering,
stateless
function to apply to each element which produces a stream
of new values
Returns:
the new stream

