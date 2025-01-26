

DeflaterInputStream (Java Platform SE 8 )














<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="DeflaterInputStream (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],8:["t4","Concrete Methods"]};
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
java.util.zipClass DeflaterInputStream
java.lang.Objectjava.io.InputStreamjava.io.FilterInputStreamjava.util.zip.DeflaterInputStream
All Implemented Interfaces:
Closeable, AutoCloseable


```
public class DeflaterInputStream
extends FilterInputStream
```
Implements an input stream filter for compressing data in the "deflate"
compression format.
Since:
1.6
See Also:
`DeflaterOutputStream`,
`InflaterOutputStream`,
`InflaterInputStream`

### Field Summary

Fields Modifier and TypeField and Description`protected byte[]``buf`
Input buffer for reading compressed data.`protected Deflater``def`
Compressor for this stream.

### Fields inherited from class java.io.FilterInputStream

`in`

### Constructor Summary

Constructors Constructor and Description`DeflaterInputStream(InputStream in)`
Creates a new input stream with a default compressor and buffer
size.`DeflaterInputStream(InputStream in,
Deflater defl)`
Creates a new input stream with the specified compressor and a
default buffer size.`DeflaterInputStream(InputStream in,
Deflater defl,
int bufLen)`
Creates a new input stream with the specified compressor and buffer
size.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`int``available()`
Returns 0 after EOF has been reached, otherwise always return 1.`void``close()`
Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.`void``mark(int limit)`
This operation is not supported.`boolean``markSupported()`
Always returns `false` because this input stream does not support
the `mark()` and `reset()` methods.`int``read()`
Reads a single byte of compressed data from the input stream.`int``read(byte[] b,
int off,
int len)`
Reads compressed data into a byte array.`void``reset()`
This operation is not supported.`long``skip(long n)`
Skips over and discards data from the input stream.

### Methods inherited from class java.io.FilterInputStream

`read`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Field Detail

#### def

```
protected final Deflater def
```
Compressor for this stream.

#### buf

```
protected final byte[] buf
```
Input buffer for reading compressed data.

### Constructor Detail

#### DeflaterInputStream

```
public DeflaterInputStream(InputStream in)
```
Creates a new input stream with a default compressor and buffer
size.
Parameters:
`in` - input stream to read the uncompressed data to
Throws:
`NullPointerException` - if `in` is null

#### DeflaterInputStream

```
public DeflaterInputStream(InputStream in,
                           Deflater defl)
```
Creates a new input stream with the specified compressor and a
default buffer size.
Parameters:
`in` - input stream to read the uncompressed data to
`defl` - compressor ("deflater") for this stream
Throws:
`NullPointerException` - if `in` or `defl` is null

#### DeflaterInputStream

```
public DeflaterInputStream(InputStream in,
                           Deflater defl,
                           int bufLen)
```
Creates a new input stream with the specified compressor and buffer
size.
Parameters:
`in` - input stream to read the uncompressed data to
`defl` - compressor ("deflater") for this stream
`bufLen` - compression buffer size
Throws:
`IllegalArgumentException` - if `bufLen <= 0`
`NullPointerException` - if `in` or `defl` is null

### Method Detail

#### close

```
public void close()
           throws IOException
```
Closes this input stream and its underlying input stream, discarding
any pending uncompressed data.
Specified by:
`close` in interface `Closeable`
Specified by:
`close` in interface `AutoCloseable`
Overrides:
`close` in class `FilterInputStream`
Throws:
`IOException` - if an I/O error occurs
See Also:
`FilterInputStream.in`

#### read

```
public int read()
         throws IOException
```
Reads a single byte of compressed data from the input stream.
This method will block until some input can be read and compressed.
Overrides:
`read` in class `FilterInputStream`
Returns:
a single byte of compressed data, or -1 if the end of the
uncompressed input stream is reached
Throws:
`IOException` - if an I/O error occurs or if this stream is
already closed
See Also:
`FilterInputStream.in`

#### read

```
public int read(byte[] b,
                int off,
                int len)
         throws IOException
```
Reads compressed data into a byte array.
This method will block until some input can be read and compressed.
Overrides:
`read` in class `FilterInputStream`
Parameters:
`b` - buffer into which the data is read
`off` - starting offset of the data within `b`
`len` - maximum number of compressed bytes to read into `b`
Returns:
the actual number of bytes read, or -1 if the end of the
uncompressed input stream is reached
Throws:
`IndexOutOfBoundsException` - if `len > b.length - off`
`IOException` - if an I/O error occurs or if this input stream is
already closed
See Also:
`FilterInputStream.in`

#### skip

```
public long skip(long n)
          throws IOException
```
Skips over and discards data from the input stream.
This method may block until the specified number of bytes are read and
skipped. Note: While `n` is given as a `long`,
the maximum number of bytes which can be skipped is
`Integer.MAX_VALUE`.
Overrides:
`skip` in class `FilterInputStream`
Parameters:
`n` - number of bytes to be skipped
Returns:
the actual number of bytes skipped
Throws:
`IOException` - if an I/O error occurs or if this stream is
already closed

#### available

```
public int available()
              throws IOException
```
Returns 0 after EOF has been reached, otherwise always return 1.Programs should not count on this method to return the actual number
of bytes that could be read without blocking
Overrides:
`available` in class `FilterInputStream`
Returns:
zero after the end of the underlying input stream has been
reached, otherwise always returns 1
Throws:
`IOException` - if an I/O error occurs or if this stream is
already closed

#### markSupported

```
public boolean markSupported()
```
Always returns `false` because this input stream does not support
the `mark()` and `reset()` methods.
Overrides:
`markSupported` in class `FilterInputStream`
Returns:
false, always
See Also:
`FilterInputStream.in`,
`InputStream.mark(int)`,
`InputStream.reset()`

#### mark

```
public void mark(int limit)
```
This operation is not supported.
Overrides:
`mark` in class `FilterInputStream`
Parameters:
`limit` - maximum bytes that can be read before invalidating the position marker
See Also:
`FilterInputStream.in`,
`FilterInputStream.reset()`

#### reset

```
public void reset()
           throws IOException
```
This operation is not supported.
Overrides:
`reset` in class `FilterInputStream`
Throws:
`IOException` - always thrown
See Also:
`FilterInputStream.in`,
`FilterInputStream.mark(int)`




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

