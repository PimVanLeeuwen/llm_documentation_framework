

java.util.zip (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="java.util.zip (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->




compact1Package java.util.zip
Provides classes for reading and writing the standard ZIP and GZIP
file formats.
See: Description

Interface Summary InterfaceDescriptionChecksumAn interface representing a data checksum.

Class Summary ClassDescriptionAdler32A class that can be used to compute the Adler-32 checksum of a data
stream.CheckedInputStreamAn input stream that also maintains a checksum of the data being read.CheckedOutputStreamAn output stream that also maintains a checksum of the data being
written.CRC32A class that can be used to compute the CRC-32 of a data stream.DeflaterThis class provides support for general purpose compression using the
popular ZLIB compression library.DeflaterInputStreamImplements an input stream filter for compressing data in the "deflate"
compression format.DeflaterOutputStreamThis class implements an output stream filter for compressing data in
the "deflate" compression format.GZIPInputStreamThis class implements a stream filter for reading compressed data in
the GZIP file format.GZIPOutputStreamThis class implements a stream filter for writing compressed data in
the GZIP file format.InflaterThis class provides support for general purpose decompression using the
popular ZLIB compression library.InflaterInputStreamThis class implements a stream filter for uncompressing data in the
"deflate" compression format.InflaterOutputStreamImplements an output stream filter for uncompressing data stored in the
"deflate" compression format.ZipEntryThis class is used to represent a ZIP file entry.ZipFileThis class is used to read entries from a zip file.ZipInputStreamThis class implements an input stream filter for reading files in the
ZIP file format.ZipOutputStreamThis class implements an output stream filter for writing files in the
ZIP file format.

Exception Summary ExceptionDescriptionDataFormatExceptionSignals that a data format error has occurred.ZipExceptionSignals that a Zip exception of some sort has occurred.

Error Summary ErrorDescriptionZipErrorSignals that an unrecoverable error has occurred.

Package java.util.zip DescriptionProvides classes for reading and writing the standard ZIP and GZIP
file formats. Also includes classes for compressing and decompressing
data using the DEFLATE compression algorithm, which is used by the
ZIP and GZIP file formats. Additionally, there are utility classes
for computing the CRC-32 and Adler-32 checksums of arbitrary
input streams.Package Specification
Info-ZIP Application Note 970311
 - a detailed description of the Info-ZIP format upon which
the `java.util.zip` classes are based.An implementation may optionally support the ZIP64(tm) format extensions
defined by the
PKWARE ZIP File Format Specification. The ZIP64(tm) format extensions
are used to overcome the size limitations of the original ZIP format.APPENDIX D of 
PKWARE ZIP File Format Specification - Language Encoding Flag (EFS) to
encode ZIP entry filename and comment fields using UTF-8.
ZLIB Compressed Data Format Specification version 3.3
 
(pdf)
(RFC 1950)
DEFLATE Compressed Data Format Specification version 1.3
 
(pdf)
(RFC 1951)
GZIP file format specification version 4.3
 
(pdf)
(RFC 1952)CRC-32 checksum is described in RFC 1952 (above)Adler-32 checksum is described in RFC 1950 (above)
Since:
JDK1.1



Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->



 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

