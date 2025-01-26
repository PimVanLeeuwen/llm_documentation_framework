

InflaterOutputStream (Java Platform SE 8 )











<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="InflaterOutputStream (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10};
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
java.util.zipClass InflaterOutputStream
java.lang.Objectjava.io.OutputStreamjava.io.FilterOutputStreamjava.util.zip.InflaterOutputStream
All Implemented Interfaces:
Closeable, Flushable, AutoCloseable


```
public class InflaterOutputStream
extends FilterOutputStream
```
Implements an output stream filter for uncompressing data stored in the
"deflate" compression format.
Since:
1.6
See Also:
`InflaterInputStream`,
`DeflaterInputStream`,
`DeflaterOutputStream`

### Field Summary

Fields Modifier and TypeField and Description`protected byte[]``buf`
Output buffer for writing uncompressed data.`protected Inflater``inf`
Decompressor for this stream.

### Fields inherited from class java.io.FilterOutputStream

`out`

### Constructor Summary

Constructors Constructor and Description`InflaterOutputStream(OutputStream out)`
Creates a new output stream with a default decompressor and buffer
size.`InflaterOutputStream(OutputStream out,
Inflater infl)`
Creates a new output stream with the specified decompressor and a
default buffer size.`InflaterOutputStream(OutputStream out,
Inflater infl,
int bufLen)`
Creates a new output stream with the specified decompressor and
buffer size.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``close()`
Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.`void``finish()`
Finishes writing uncompressed data to the output stream without closing
the underlying stream.`void``flush()`
Flushes this output stream, forcing any pending buffered output bytes to be
written.`void``write(byte[] b,
int off,
int len)`
Writes an array of bytes to the uncompressed output stream.`void``write(int b)`
Writes a byte to the uncompressed output stream.

### Methods inherited from class java.io.FilterOutputStream

`write`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Field Detail

#### inf

```
protected final Inflater inf
```
Decompressor for this stream.

#### buf

```
protected final byte[] buf
```
Output buffer for writing uncompressed data.

### Constructor Detail

#### InflaterOutputStream

```
public InflaterOutputStream(OutputStream out)
```
Creates a new output stream with a default decompressor and buffer
size.
Parameters:
`out` - output stream to write the uncompressed data to
Throws:
`NullPointerException` - if `out` is null

#### InflaterOutputStream

```
public InflaterOutputStream(OutputStream out,
                            Inflater infl)
```
Creates a new output stream with the specified decompressor and a
default buffer size.
Parameters:
`out` - output stream to write the uncompressed data to
`infl` - decompressor ("inflater") for this stream
Throws:
`NullPointerException` - if `out` or `infl` is null

#### InflaterOutputStream

```
public InflaterOutputStream(OutputStream out,
                            Inflater infl,
                            int bufLen)
```
Creates a new output stream with the specified decompressor and
buffer size.
Parameters:
`out` - output stream to write the uncompressed data to
`infl` - decompressor ("inflater") for this stream
`bufLen` - decompression buffer size
Throws:
`IllegalArgumentException` - if `bufLen <= 0`
`NullPointerException` - if `out` or `infl` is null

### Method Detail

#### close

```
public void close()
           throws IOException
```
Writes any remaining uncompressed data to the output stream and closes
the underlying output stream.
Specified by:
`close` in interface `Closeable`
Specified by:
`close` in interface `AutoCloseable`
Overrides:
`close` in class `FilterOutputStream`
Throws:
`IOException` - if an I/O error occurs
See Also:
`FilterOutputStream.flush()`,
`FilterOutputStream.out`

#### flush

```
public void flush()
           throws IOException
```
Flushes this output stream, forcing any pending buffered output bytes to be
written.
Specified by:
`flush` in interface `Flushable`
Overrides:
`flush` in class `FilterOutputStream`
Throws:
`IOException` - if an I/O error occurs or this stream is already
closed
See Also:
`FilterOutputStream.out`

#### finish

```
public void finish()
            throws IOException
```
Finishes writing uncompressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters in
succession to the same output stream.
Throws:
`IOException` - if an I/O error occurs or this stream is already
closed

#### write

```
public void write(int b)
           throws IOException
```
Writes a byte to the uncompressed output stream.
Overrides:
`write` in class `FilterOutputStream`
Parameters:
`b` - a single byte of compressed data to decompress and write to
the output stream
Throws:
`IOException` - if an I/O error occurs or this stream is already
closed
`ZipException` - if a compression (ZIP) format error occurs

#### write

```
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```
Writes an array of bytes to the uncompressed output stream.
Overrides:
`write` in class `FilterOutputStream`
Parameters:
`b` - buffer containing compressed data to decompress and write to
the output stream
`off` - starting offset of the compressed data within `b`
`len` - number of bytes to decompress from `b`
Throws:
`IndexOutOfBoundsException` - if `off < 0`, or if
`len < 0`, or if `len > b.length - off`
`IOException` - if an I/O error occurs or this stream is already
closed
`NullPointerException` - if `b` is null
`ZipException` - if a compression (ZIP) format error occurs
See Also:
`FilterOutputStream.write(int)`




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

