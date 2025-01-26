

Attributes.Name (Java Platform SE 8 )

























<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Attributes.Name (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10};
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
java.util.jarClass Attributes.Name
java.lang.Objectjava.util.jar.Attributes.Name
Enclosing class:
Attributes


```
public static class Attributes.Name
extends Object
```
The Attributes.Name class represents an attribute name stored in
this Map. Valid attribute names are case-insensitive, are restricted
to the ASCII characters in the set [0-9a-zA-Z\_-], and cannot exceed
70 characters in length. Attribute values can contain any characters
and will be UTF8-encoded when written to the output stream. See the
JAR File Specification
for more information about valid attribute names and values.

### Field Summary

Fields Modifier and TypeField and Description`static Attributes.Name``CLASS_PATH`
`Name` object for `Class-Path`
manifest attribute.`static Attributes.Name``CONTENT_TYPE`
`Name` object for `Content-Type`
manifest attribute.`static Attributes.Name``EXTENSION_INSTALLATION`
Deprecated. 
Extension mechanism will be removed in a future release.
Use class path instead.
`static Attributes.Name``EXTENSION_LIST`
`Name` object for `Extension-List` manifest attribute
used for declaring dependencies on installed extensions.`static Attributes.Name``EXTENSION_NAME`
`Name` object for `Extension-Name` manifest attribute
used for declaring dependencies on installed extensions.`static Attributes.Name``IMPLEMENTATION_TITLE`
`Name` object for `Implementation-Title`
manifest attribute used for package versioning.`static Attributes.Name``IMPLEMENTATION_URL`
Deprecated. 
Extension mechanism will be removed in a future release.
Use class path instead.
`static Attributes.Name``IMPLEMENTATION_VENDOR`
`Name` object for `Implementation-Vendor`
manifest attribute used for package versioning.`static Attributes.Name``IMPLEMENTATION_VENDOR_ID`
Deprecated. 
Extension mechanism will be removed in a future release.
Use class path instead.
`static Attributes.Name``IMPLEMENTATION_VERSION`
`Name` object for `Implementation-Version`
manifest attribute used for package versioning.`static Attributes.Name``MAIN_CLASS`
`Name` object for `Main-Class` manifest
attribute used for launching applications packaged in JAR files.`static Attributes.Name``MANIFEST_VERSION`
`Name` object for `Manifest-Version`
manifest attribute.`static Attributes.Name``SEALED`
`Name` object for `Sealed` manifest attribute
used for sealing.`static Attributes.Name``SIGNATURE_VERSION`
`Name` object for `Signature-Version`
manifest attribute used when signing JAR files.`static Attributes.Name``SPECIFICATION_TITLE`
`Name` object for `Specification-Title`
manifest attribute used for package versioning.`static Attributes.Name``SPECIFICATION_VENDOR`
`Name` object for `Specification-Vendor`
manifest attribute used for package versioning.`static Attributes.Name``SPECIFICATION_VERSION`
`Name` object for `Specification-Version`
manifest attribute used for package versioning.

### Constructor Summary

Constructors Constructor and Description`Name(String name)`
Constructs a new attribute name using the given string name.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`boolean``equals(Object o)`
Compares this attribute name to another for equality.`int``hashCode()`
Computes the hash value for this attribute name.`String``toString()`
Returns the attribute name as a String.

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

### Field Detail

#### MANIFEST\_VERSION

```
public static final Attributes.Name MANIFEST_VERSION
```
`Name` object for `Manifest-Version`
manifest attribute. This attribute indicates the version number
of the manifest standard to which a JAR file's manifest conforms.
See Also:
Manifest and Signature Specification

#### SIGNATURE\_VERSION

```
public static final Attributes.Name SIGNATURE_VERSION
```
`Name` object for `Signature-Version`
manifest attribute used when signing JAR files.
See Also:
Manifest and Signature Specification

#### CONTENT\_TYPE

```
public static final Attributes.Name CONTENT_TYPE
```
`Name` object for `Content-Type`
manifest attribute.

#### CLASS\_PATH

```
public static final Attributes.Name CLASS_PATH
```
`Name` object for `Class-Path`
manifest attribute. Bundled extensions can use this attribute
to find other JAR files containing needed classes.
See Also:
JAR file specification

#### MAIN\_CLASS

```
public static final Attributes.Name MAIN_CLASS
```
`Name` object for `Main-Class` manifest
attribute used for launching applications packaged in JAR files.
The `Main-Class` attribute is used in conjunction
with the `-jar` command-line option of the
java application launcher.

#### SEALED

```
public static final Attributes.Name SEALED
```
`Name` object for `Sealed` manifest attribute
used for sealing.
See Also:
Package Sealing

#### EXTENSION\_LIST

```
public static final Attributes.Name EXTENSION_LIST
```
`Name` object for `Extension-List` manifest attribute
used for declaring dependencies on installed extensions.
See Also:
Installed extension dependency

#### EXTENSION\_NAME

```
public static final Attributes.Name EXTENSION_NAME
```
`Name` object for `Extension-Name` manifest attribute
used for declaring dependencies on installed extensions.
See Also:
Installed extension dependency

#### EXTENSION\_INSTALLATION

```
@Deprecated
public static final Attributes.Name EXTENSION_INSTALLATION
```
Deprecated. Extension mechanism will be removed in a future release.
Use class path instead.
`Name` object for `Extension-Name` manifest attribute
used for declaring dependencies on installed extensions.
See Also:
Installed extension dependency

#### IMPLEMENTATION\_TITLE

```
public static final Attributes.Name IMPLEMENTATION_TITLE
```
`Name` object for `Implementation-Title`
manifest attribute used for package versioning.
See Also:
Java Product Versioning Specification

#### IMPLEMENTATION\_VERSION

```
public static final Attributes.Name IMPLEMENTATION_VERSION
```
`Name` object for `Implementation-Version`
manifest attribute used for package versioning.
See Also:
Java Product Versioning Specification

#### IMPLEMENTATION\_VENDOR

```
public static final Attributes.Name IMPLEMENTATION_VENDOR
```
`Name` object for `Implementation-Vendor`
manifest attribute used for package versioning.
See Also:
Java Product Versioning Specification

#### IMPLEMENTATION\_VENDOR\_ID

```
@Deprecated
public static final Attributes.Name IMPLEMENTATION_VENDOR_ID
```
Deprecated. Extension mechanism will be removed in a future release.
Use class path instead.
`Name` object for `Implementation-Vendor-Id`
manifest attribute used for package versioning.
See Also:
Optional Package Versioning

#### IMPLEMENTATION\_URL

```
@Deprecated
public static final Attributes.Name IMPLEMENTATION_URL
```
Deprecated. Extension mechanism will be removed in a future release.
Use class path instead.
`Name` object for `Implementation-URL`
manifest attribute used for package versioning.
See Also:
Optional Package Versioning

#### SPECIFICATION\_TITLE

```
public static final Attributes.Name SPECIFICATION_TITLE
```
`Name` object for `Specification-Title`
manifest attribute used for package versioning.
See Also:
Java Product Versioning Specification

#### SPECIFICATION\_VERSION

```
public static final Attributes.Name SPECIFICATION_VERSION
```
`Name` object for `Specification-Version`
manifest attribute used for package versioning.
See Also:
Java Product Versioning Specification

#### SPECIFICATION\_VENDOR

```
public static final Attributes.Name SPECIFICATION_VENDOR
```
`Name` object for `Specification-Vendor`
manifest attribute used for package versioning.
See Also:
Java Product Versioning Specification

### Constructor Detail

#### Name

```
public Name(String name)
```
Constructs a new attribute name using the given string name.
Parameters:
`name` - the attribute string name
Throws:
`IllegalArgumentException` - if the attribute name was
invalid
`NullPointerException` - if the attribute name was null

### Method Detail

#### equals

```
public boolean equals(Object o)
```
Compares this attribute name to another for equality.
Overrides:
`equals` in class `Object`
Parameters:
`o` - the object to compare
Returns:
true if this attribute name is equal to the
specified attribute object
See Also:
`Object.hashCode()`,
`HashMap`

#### hashCode

```
public int hashCode()
```
Computes the hash value for this attribute name.
Overrides:
`hashCode` in class `Object`
Returns:
a hash code value for this object.
See Also:
`Object.equals(java.lang.Object)`,
`System.identityHashCode(java.lang.Object)`

#### toString

```
public String toString()
```
Returns the attribute name as a String.
Overrides:
`toString` in class `Object`
Returns:
a string representation of the object.




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

