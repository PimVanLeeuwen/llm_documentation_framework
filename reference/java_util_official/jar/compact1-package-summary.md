

java.util.jar (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="java.util.jar (Java Platform SE 8 )";
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




compact1Package java.util.jar
Provides classes for reading and writing the JAR (Java ARchive) file
format, which is based on the standard ZIP file format with an
optional manifest file.
See: Description

Interface Summary InterfaceDescriptionPack200.PackerThe packer engine applies various transformations to the input JAR file,
making the pack stream highly compressible by a compressor such as
gzip or zip.Pack200.UnpackerThe unpacker engine converts the packed stream to a JAR file.

Class Summary ClassDescriptionAttributesThe Attributes class maps Manifest attribute names to associated string
values.Attributes.NameThe Attributes.Name class represents an attribute name stored in
this Map.JarEntryThis class is used to represent a JAR file entry.JarFileThe `JarFile` class is used to read the contents of a jar file
from any file that can be opened with `java.io.RandomAccessFile`.JarInputStreamThe `JarInputStream` class is used to read the contents of
a JAR file from any input stream.JarOutputStreamThe `JarOutputStream` class is used to write the contents
of a JAR file to any output stream.ManifestThe Manifest class is used to maintain Manifest entry names and their
associated Attributes.Pack200Transforms a JAR file to or from a packed stream in Pack200 format.

Exception Summary ExceptionDescriptionJarExceptionSignals that an error of some sort has occurred while reading from
or writing to a JAR file.

Package java.util.jar DescriptionProvides classes for reading and writing the JAR (Java ARchive) file
format, which is based on the standard ZIP file format with an
optional manifest file. The manifest stores meta-information about the
JAR file contents and is also used for signing JAR files.Package SpecificationThe `java.util.jar` package is based on the following specifications:Info-ZIP file format - The JAR format is based on the Info-ZIP
file format. See
java.util.zip
package description.In JAR files, all file names must be encoded in the UTF-8 encoding.
Manifest and Signature Specification - The manifest format specification.
Since:
1.2



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

