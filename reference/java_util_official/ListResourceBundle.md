

ListResourceBundle (Java Platform SE 8 )









<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ListResourceBundle (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":10,"i2":10,"i3":10};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"],8:["t4","Concrete Methods"]};
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
java.utilClass ListResourceBundle
java.lang.Objectjava.util.ResourceBundlejava.util.ListResourceBundle
Direct Known Subclasses:
AccessibleResourceBundle


```
public abstract class ListResourceBundle
extends ResourceBundle
```
`ListResourceBundle` is an abstract subclass of
`ResourceBundle` that manages resources for a locale
in a convenient and easy to use list. See `ResourceBundle` for
more information about resource bundles in general.Subclasses must override `getContents` and provide an array,
where each item in the array is a pair of objects.
The first element of each pair is the key, which must be a
`String`, and the second element is the value associated with
that key.The following example shows two members of a resource
bundle family with the base name "MyResources".
"MyResources" is the default member of the bundle family, and
"MyResources\_fr" is the French member.
These members are based on `ListResourceBundle`
(a related example shows
how you can add a bundle to this family that's based on a properties file).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.
```


 public class MyResources extends ListResourceBundle {
     protected Object[][] getContents() {
         return new Object[][] {
         // LOCALIZE THIS
             {"s1", "The disk \"{1}\" contains {0}."},  // MessageFormat pattern
             {"s2", "1"},                               // location of {0} in pattern
             {"s3", "My Disk"},                         // sample disk name
             {"s4", "no files"},                        // first ChoiceFormat choice
             {"s5", "one file"},                        // second ChoiceFormat choice
             {"s6", "{0,number} files"},                // third ChoiceFormat choice
             {"s7", "3 Mar 96"},                        // sample date
             {"s8", new Dimension(1,5)}                 // real object, not just string
         // END OF MATERIAL TO LOCALIZE
         };
     }
 }

 public class MyResources_fr extends ListResourceBundle {
     protected Object[][] getContents() {
         return new Object[][] {
         // LOCALIZE THIS
             {"s1", "Le disque \"{1}\" {0}."},          // MessageFormat pattern
             {"s2", "1"},                               // location of {0} in pattern
             {"s3", "Mon disque"},                      // sample disk name
             {"s4", "ne contient pas de fichiers"},     // first ChoiceFormat choice
             {"s5", "contient un fichier"},             // second ChoiceFormat choice
             {"s6", "contient {0,number} fichiers"},    // third ChoiceFormat choice
             {"s7", "3 mars 1996"},                     // sample date
             {"s8", new Dimension(1,3)}                 // real object, not just string
         // END OF MATERIAL TO LOCALIZE
         };
     }
 }
 
```
The implementation of a `ListResourceBundle` subclass must be thread-safe
if it's simultaneously used by multiple threads. The default implementations
of the methods in this class are thread-safe.
Since:
JDK1.1
See Also:
`ResourceBundle`,
`PropertyResourceBundle`

### Nested Class Summary

### Nested classes/interfaces inherited from class java.util.ResourceBundle

`ResourceBundle.Control`

### Field Summary

### Fields inherited from class java.util.ResourceBundle

`parent`

### Constructor Summary

Constructors Constructor and Description`ListResourceBundle()`
Sole constructor.

### Method Summary

All Methods Instance Methods Abstract Methods Concrete Methods Modifier and TypeMethod and Description`protected abstract Object[][]``getContents()`
Returns an array in which each item is a pair of objects in an
`Object` array.`Enumeration<String>``getKeys()`
Returns an `Enumeration` of the keys contained in
this `ResourceBundle` and its parent bundles.`Object``handleGetObject(String key)`
Gets an object for the given key from this resource bundle.`protected Set<String>``handleKeySet()`
Returns a `Set` of the keys contained
only in this `ResourceBundle`.

### Methods inherited from class java.util.ResourceBundle

`clearCache, clearCache, containsKey, getBaseBundleName, getBundle, getBundle, getBundle, getBundle, getBundle, getBundle, getLocale, getObject, getString, getStringArray, keySet, setParent`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### ListResourceBundle

```
public ListResourceBundle()
```
Sole constructor. (For invocation by subclass constructors, typically
implicit.)

### Method Detail

#### handleGetObject

```
public final Object handleGetObject(String key)
```
Description copied from class: `ResourceBundle`
Gets an object for the given key from this resource bundle.
Returns null if this resource bundle does not contain an
object for the given key.
Specified by:
`handleGetObject` in class `ResourceBundle`
Parameters:
`key` - the key for the desired object
Returns:
the object for the given key, or null

#### getKeys

```
public Enumeration<String> getKeys()
```
Returns an `Enumeration` of the keys contained in
this `ResourceBundle` and its parent bundles.
Specified by:
`getKeys` in class `ResourceBundle`
Returns:
an `Enumeration` of the keys contained in
this `ResourceBundle` and its parent bundles.
See Also:
`ResourceBundle.keySet()`

#### handleKeySet

```
protected Set<String> handleKeySet()
```
Returns a `Set` of the keys contained
only in this `ResourceBundle`.
Overrides:
`handleKeySet` in class `ResourceBundle`
Returns:
a `Set` of the keys contained only in this
`ResourceBundle`
Since:
1.6
See Also:
`ResourceBundle.keySet()`

#### getContents

```
protected abstract Object[][] getContents()
```
Returns an array in which each item is a pair of objects in an
`Object` array. The first element of each pair is
the key, which must be a `String`, and the second
element is the value associated with that key. See the class
description for details.
Returns:
an array of an `Object` array representing a
key-value pair.




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

