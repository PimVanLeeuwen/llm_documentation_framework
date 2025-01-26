

RandomAccess (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="RandomAccess (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

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
java.utilInterface RandomAccess
All Known Implementing Classes:
ArrayList, AttributeList, CopyOnWriteArrayList, RoleList, RoleUnresolvedList, Stack, Vector


```
public interface RandomAccess
```
Marker interface used by List implementations to indicate that
they support fast (generally constant time) random access. The primary
purpose of this interface is to allow generic algorithms to alter their
behavior to provide good performance when applied to either random or
sequential access lists.The best algorithms for manipulating random access lists (such as
ArrayList) can produce quadratic behavior when applied to
sequential access lists (such as LinkedList). Generic list
algorithms are encouraged to check whether the given list is an
instanceof this interface before applying an algorithm that would
provide poor performance if it were applied to a sequential access list,
and to alter their behavior if necessary to guarantee acceptable
performance.It is recognized that the distinction between random and sequential
access is often fuzzy. For example, some List implementations
provide asymptotically linear access times if they get huge, but constant
access times in practice. Such a List implementation
should generally implement this interface. As a rule of thumb, a
List implementation should implement this interface if,
for typical instances of the class, this loop:
```

     for (int i=0, n=list.size(); i < n; i++)
         list.get(i);
 
```
runs faster than this loop:
```

     for (Iterator i=list.iterator(); i.hasNext(); )
         i.next();
 
```
This interface is a member of the
Java Collections Framework.
Since:
1.4




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

