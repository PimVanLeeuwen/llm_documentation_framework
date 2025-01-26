

Base64 (Java Platform SE 8 )











<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Base64 (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":9,"i1":9,"i2":9,"i3":9,"i4":9,"i5":9,"i6":9};
var tabs = {65535:["t0","All Methods"],1:["t1","Static Methods"],8:["t4","Concrete Methods"]};
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
java.utilClass Base64
java.lang.Objectjava.util.Base64
```
public class Base64
extends Object
```
This class consists exclusively of static methods for obtaining
encoders and decoders for the Base64 encoding scheme. The
implementation of this class supports the following types of Base64
as specified in
RFC 4648 and
RFC 2045.BasicUses "The Base64 Alphabet" as specified in Table 1 of
RFC 4648 and RFC 2045 for encoding and decoding operation.
The encoder does not add any line feed (line separator)
character. The decoder rejects data that contains characters
outside the base64 alphabet.URL and Filename safeUses the "URL and Filename safe Base64 Alphabet" as specified
in Table 2 of RFC 4648 for encoding and decoding. The
encoder does not add any line feed (line separator) character.
The decoder rejects data that contains characters outside the
base64 alphabet.MIMEUses the "The Base64 Alphabet" as specified in Table 1 of
RFC 2045 for encoding and decoding operation. The encoded output
must be represented in lines of no more than 76 characters each
and uses a carriage return `'\r'` followed immediately by
a linefeed `'\n'` as the line separator. No line separator
is added to the end of the encoded output. All line separators
or other characters not found in the base64 alphabet table are
ignored in decoding operation.Unless otherwise noted, passing a `null` argument to a
method of this class will cause a `NullPointerException` to be thrown.
Since:
1.8

### Nested Class Summary

Nested Classes Modifier and TypeClass and Description`static class``Base64.Decoder`
This class implements a decoder for decoding byte data using the
Base64 encoding scheme as specified in RFC 4648 and RFC 2045.`static class``Base64.Encoder`
This class implements an encoder for encoding byte data using
the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

### Method Summary

All Methods Static Methods Concrete Methods Modifier and TypeMethod and Description`static Base64.Decoder``getDecoder()`
Returns a `Base64.Decoder` that decodes using the
Basic type base64 encoding scheme.`static Base64.Encoder``getEncoder()`
Returns a `Base64.Encoder` that encodes using the
Basic type base64 encoding scheme.`static Base64.Decoder``getMimeDecoder()`
Returns a `Base64.Decoder` that decodes using the
MIME type base64 decoding scheme.`static Base64.Encoder``getMimeEncoder()`
Returns a `Base64.Encoder` that encodes using the
MIME type base64 encoding scheme.`static Base64.Encoder``getMimeEncoder(int lineLength,
byte[] lineSeparator)`
Returns a `Base64.Encoder` that encodes using the
MIME type base64 encoding scheme
with specified line length and line separators.`static Base64.Decoder``getUrlDecoder()`
Returns a `Base64.Decoder` that decodes using the
URL and Filename safe type base64
encoding scheme.`static Base64.Encoder``getUrlEncoder()`
Returns a `Base64.Encoder` that encodes using the
URL and Filename safe type base64
encoding scheme.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Method Detail

#### getEncoder

```
public static Base64.Encoder getEncoder()
```
Returns a `Base64.Encoder` that encodes using the
Basic type base64 encoding scheme.
Returns:
A Base64 encoder.

#### getUrlEncoder

```
public static Base64.Encoder getUrlEncoder()
```
Returns a `Base64.Encoder` that encodes using the
URL and Filename safe type base64
encoding scheme.
Returns:
A Base64 encoder.

#### getMimeEncoder

```
public static Base64.Encoder getMimeEncoder()
```
Returns a `Base64.Encoder` that encodes using the
MIME type base64 encoding scheme.
Returns:
A Base64 encoder.

#### getMimeEncoder

```
public static Base64.Encoder getMimeEncoder(int lineLength,
                                            byte[] lineSeparator)
```
Returns a `Base64.Encoder` that encodes using the
MIME type base64 encoding scheme
with specified line length and line separators.
Parameters:
`lineLength` - the length of each output line (rounded down to nearest multiple
of 4). If `lineLength <= 0` the output will not be separated
in lines
`lineSeparator` - the line separator for each output line
Returns:
A Base64 encoder.
Throws:
`IllegalArgumentException` - if `lineSeparator` includes any
character of "The Base64 Alphabet" as specified in Table 1 of
RFC 2045.

#### getDecoder

```
public static Base64.Decoder getDecoder()
```
Returns a `Base64.Decoder` that decodes using the
Basic type base64 encoding scheme.
Returns:
A Base64 decoder.

#### getUrlDecoder

```
public static Base64.Decoder getUrlDecoder()
```
Returns a `Base64.Decoder` that decodes using the
URL and Filename safe type base64
encoding scheme.
Returns:
A Base64 decoder.

#### getMimeDecoder

```
public static Base64.Decoder getMimeDecoder()
```
Returns a `Base64.Decoder` that decodes using the
MIME type base64 decoding scheme.
Returns:
A Base64 decoder.




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

