

BaseStream (Java Platform SE 8 )













<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="BaseStream (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":6,"i2":6,"i3":6,"i4":6,"i5":6,"i6":6,"i7":6};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"]};
var altColor = "altColor";
var rowColor = "rowColor";
var tableTab = "tableTab";
var activeTableTab = "activeTableTab";

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method




compact1, compact2, compact3
java.util.streamInterface BaseStream<T,S extends BaseStream<T,S>>
Type Parameters:
`T` - the type of the stream elements
`S` - the type of the stream implementing `BaseStream`

All Superinterfaces:
AutoCloseable

All Known Subinterfaces:
DoubleStream, IntStream, LongStream, Stream<T>


```
public interface BaseStream<T,S extends BaseStream<T,S>>
extends AutoCloseable
```
Base interface for streams, which are sequences of elements supporting
sequential and parallel aggregate operations. The following example
illustrates an aggregate operation using the stream types `Stream`
and `IntStream`, computing the sum of the weights of the red widgets:
```

     int sum = widgets.stream()
                      .filter(w -> w.getColor() == RED)
                      .mapToInt(w -> w.getWeight())
                      .sum();
 
```
See the class documentation for `Stream` and the package documentation
for java.util.stream for additional
specification of streams, stream operations, stream pipelines, and
parallelism, which governs the behavior of all stream types.
Since:
1.8
See Also:
`Stream`,
`IntStream`,
`LongStream`,
`DoubleStream`,
java.util.stream

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`void``close()`
Closes this stream, causing all close handlers for this stream pipeline
to be called.`boolean``isParallel()`
Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel.`Iterator<T>``iterator()`
Returns an iterator for the elements of this stream.`S``onClose(Runnable closeHandler)`
Returns an equivalent stream with an additional close handler.`S``parallel()`
Returns an equivalent stream that is parallel.`S``sequential()`
Returns an equivalent stream that is sequential.`Spliterator<T>``spliterator()`
Returns a spliterator for the elements of this stream.`S``unordered()`
Returns an equivalent stream that is
unordered.

### Method Detail

#### iterator

```
Iterator<T> iterator()
```
Returns an iterator for the elements of this stream.This is a terminal
operation.
Returns:
the element iterator for this stream

#### spliterator

```
Spliterator<T> spliterator()
```
Returns a spliterator for the elements of this stream.This is a terminal
operation.
Returns:
the element spliterator for this stream

#### isParallel

```
boolean isParallel()
```
Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel. Calling this method after invoking an
terminal stream operation method may yield unpredictable results.
Returns:
`true` if this stream would execute in parallel if executed

#### sequential

```
S sequential()
```
Returns an equivalent stream that is sequential. May return
itself, either because the stream was already sequential, or because
the underlying stream state was modified to be sequential.This is an intermediate
operation.
Returns:
a sequential stream

#### parallel

```
S parallel()
```
Returns an equivalent stream that is parallel. May return
itself, either because the stream was already parallel, or because
the underlying stream state was modified to be parallel.This is an intermediate
operation.
Returns:
a parallel stream

#### unordered

```
S unordered()
```
Returns an equivalent stream that is
unordered. May return
itself, either because the stream was already unordered, or because
the underlying stream state was modified to be unordered.This is an intermediate
operation.
Returns:
an unordered stream

#### onClose

```
S onClose(Runnable closeHandler)
```
Returns an equivalent stream with an additional close handler. Close
handlers are run when the `close()` method
is called on the stream, and are executed in the order they were
added. All close handlers are run, even if earlier close handlers throw
exceptions. If any close handler throws an exception, the first
exception thrown will be relayed to the caller of `close()`, with
any remaining exceptions added to that exception as suppressed exceptions
(unless one of the remaining exceptions is the same exception as the
first exception, since an exception cannot suppress itself.) May
return itself.This is an intermediate
operation.
Parameters:
`closeHandler` - A task to execute when the stream is closed
Returns:
a stream with a handler that is run if the stream is closed

#### close

```
void close()
```
Closes this stream, causing all close handlers for this stream pipeline
to be called.
Specified by:
`close` in interface `AutoCloseable`
See Also:
`AutoCloseable.close()`




Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method


 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

