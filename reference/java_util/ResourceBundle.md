```
public abstract class ResourceBundle
extends Object
```
Resource bundles contain locale-specific objects. When your program needs a
locale-specific resource, a `String` for example, your program can
load it from the resource bundle that is appropriate for the current user's
locale. In this way, you can write program code that is largely independent
of the user's locale isolating most, if not all, of the locale-specific
information in resource bundles.This allows you to write programs that can:be easily localized, or translated, into different languageshandle multiple locales at oncebe easily modified later to support even more localesResource bundles belong to families whose members share a common base
name, but whose names also have additional components that identify
their locales. For example, the base name of a family of resource
bundles might be "MyResources". The family should have a default
resource bundle which simply has the same name as its family -
"MyResources" - and will be used as the bundle of last resort if a
specific locale is not supported. The family can then provide as
many locale-specific members as needed, for example a German one
named "MyResources\_de".Each resource bundle in a family contains the same items, but the items have
been translated for the locale represented by that resource bundle.
For example, both "MyResources" and "MyResources\_de" may have a
`String` that's used on a button for canceling operations.
In "MyResources" the `String` may contain "Cancel" and in
"MyResources\_de" it may contain "Abbrechen".If there are different resources for different countries, you
can make specializations: for example, "MyResources\_de\_CH" contains objects for
the German language (de) in Switzerland (CH). If you want to only
modify some of the resources
in the specialization, you can do so.When your program needs a locale-specific object, it loads
the `ResourceBundle` class using the
`getBundle`
method:
```

 ResourceBundle myResources =
      ResourceBundle.getBundle("MyResources", currentLocale);
 
```
Resource bundles contain key/value pairs. The keys uniquely
identify a locale-specific object in the bundle. Here's an
example of a `ListResourceBundle` that contains
two key/value pairs:
```

 public class MyResources extends ListResourceBundle {
     protected Object[][] getContents() {
         return new Object[][] {
             // LOCALIZE THE SECOND STRING OF EACH ARRAY (e.g., "OK")
             {"OkKey", "OK"},
             {"CancelKey", "Cancel"},
             // END OF MATERIAL TO LOCALIZE
        };
     }
 }
 
```
Keys are always `String`s.
In this example, the keys are "OkKey" and "CancelKey".
In the above example, the values
are also `String`s--"OK" and "Cancel"--but
they don't have to be. The values can be any type of object.You retrieve an object from resource bundle using the appropriate
getter method. Because "OkKey" and "CancelKey"
are both strings, you would use `getString` to retrieve them:
```

 button1 = new Button(myResources.getString("OkKey"));
 button2 = new Button(myResources.getString("CancelKey"));
 
```
The getter methods all require the key as an argument and return
the object if found. If the object is not found, the getter method
throws a `MissingResourceException`.Besides `getString`, `ResourceBundle` also provides
a method for getting string arrays, `getStringArray`,
as well as a generic `getObject` method for any other
type of object. When using `getObject`, you'll
have to cast the result to the appropriate type. For example:
```

 int[] myIntegers = (int[]) myResources.getObject("intList");
 
```
The Java Platform provides two subclasses of `ResourceBundle`,
`ListResourceBundle` and `PropertyResourceBundle`,
that provide a fairly simple way to create resources.
As you saw briefly in a previous example, `ListResourceBundle`
manages its resource as a list of key/value pairs.
`PropertyResourceBundle` uses a properties file to manage
its resources.If `ListResourceBundle` or `PropertyResourceBundle`
do not suit your needs, you can write your own `ResourceBundle`
subclass. Your subclasses must override two methods: `handleGetObject`
and `getKeys()`.The implementation of a `ResourceBundle` subclass must be thread-safe
if it's simultaneously used by multiple threads. The default implementations
of the non-abstract methods in this class, and the methods in the direct
known concrete subclasses `ListResourceBundle` and
`PropertyResourceBundle` are thread-safe.