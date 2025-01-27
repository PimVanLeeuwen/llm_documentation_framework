#### getBundle

```
public static ResourceBundle getBundle(String baseName,
                                       Locale targetLocale,
                                       ClassLoader loader,
                                       ResourceBundle.Control control)
```
Returns a resource bundle using the specified base name, target
locale, class loader and control. Unlike the `getBundle`
factory methods with no `control` argument, the given
`control` specifies how to locate and instantiate resource
bundles. Conceptually, the bundle loading process with the given
`control` is performed in the following steps.This factory method looks up the resource bundle in the cache for
the specified `baseName`, `targetLocale` and
`loader`. If the requested resource bundle instance is
found in the cache and the time-to-live periods of the instance and
all of its parent instances have not expired, the instance is returned
to the caller. Otherwise, this factory method proceeds with the
loading process below.The `control.getFormats` method is called to get resource bundle formats
to produce bundle or resource names. The strings
`"java.class"` and `"java.properties"`
designate class-based and property-based resource bundles, respectively. Other strings
starting with `"java."` are reserved for future extensions
and must not be used for application-defined formats. Other strings
designate application-defined formats.The `control.getCandidateLocales` method is called with the target
locale to get a list of candidate `Locale`s for
which resource bundles are searched.The `control.newBundle` method is called to
instantiate a `ResourceBundle` for the base bundle name, a
candidate locale, and a format. (Refer to the note on the cache
lookup below.) This step is iterated over all combinations of the
candidate locales and formats until the `newBundle` method
returns a `ResourceBundle` instance or the iteration has
used up all the combinations. For example, if the candidate locales
are `Locale("de", "DE")`, `Locale("de")` and
`Locale("")` and the formats are `"java.class"`
and `"java.properties"`, then the following is the
sequence of locale-format combinations to be used to call
`control.newBundle`.

`Locale``format``Locale("de", "DE")``java.class``Locale("de", "DE")``java.properties``Locale("de")``java.class``Locale("de")``java.properties``Locale("")``java.class``Locale("")``java.properties`
If the previous step has found no resource bundle, proceed to
Step 6. If a bundle has been found that is a base bundle (a bundle
for `Locale("")`), and the candidate locale list only contained
`Locale("")`, return the bundle to the caller. If a bundle
has been found that is a base bundle, but the candidate locale list
contained locales other than Locale(""), put the bundle on hold and
proceed to Step 6. If a bundle has been found that is not a base
bundle, proceed to Step 7.The `control.getFallbackLocale` method is called to get a fallback
locale (alternative to the current target locale) to try further
finding a resource bundle. If the method returns a non-null locale,
it becomes the next target locale and the loading process starts over
from Step 3. Otherwise, if a base bundle was found and put on hold in
a previous Step 5, it is returned to the caller now. Otherwise, a
MissingResourceException is thrown.At this point, we have found a resource bundle that's not the
base bundle. If this bundle set its parent during its instantiation,
it is returned to the caller. Otherwise, its parent chain is
instantiated based on the list of candidate locales from which it was
found. Finally, the bundle is returned to the caller.During the resource bundle loading process above, this factory
method looks up the cache before calling the `control.newBundle` method. If the time-to-live period of the
resource bundle found in the cache has expired, the factory method
calls the `control.needsReload`
method to determine whether the resource bundle needs to be reloaded.
If reloading is required, the factory method calls
`control.newBundle` to reload the resource bundle. If
`control.newBundle` returns `null`, the factory
method puts a dummy resource bundle in the cache as a mark of
nonexistent resource bundles in order to avoid lookup overhead for
subsequent requests. Such dummy resource bundles are under the same
expiration control as specified by `control`.All resource bundles loaded are cached by default. Refer to
`control.getTimeToLive` for details.The following is an example of the bundle loading process with the
default `ResourceBundle.Control` implementation.Conditions:Base bundle name: `foo.bar.Messages`Requested `Locale`: `Locale.ITALY`Default `Locale`: `Locale.FRENCH`Available resource bundles:
`foo/bar/Messages_fr.properties` and
`foo/bar/Messages.properties`First, `getBundle` tries loading a resource bundle in
the following sequence.class `foo.bar.Messages_it_IT`file `foo/bar/Messages_it_IT.properties`class `foo.bar.Messages_it`file `foo/bar/Messages_it.properties`class `foo.bar.Messages`file `foo/bar/Messages.properties`At this point, `getBundle` finds
`foo/bar/Messages.properties`, which is put on hold
because it's the base bundle. `getBundle` calls `control.getFallbackLocale("foo.bar.Messages", Locale.ITALY)` which
returns `Locale.FRENCH`. Next, `getBundle`
tries loading a bundle in the following sequence.class `foo.bar.Messages_fr`file `foo/bar/Messages_fr.properties`class `foo.bar.Messages`file `foo/bar/Messages.properties``getBundle` finds
`foo/bar/Messages_fr.properties` and creates a
`ResourceBundle` instance. Then, `getBundle`
sets up its parent chain from the list of the candidate locales. Only
`foo/bar/Messages.properties` is found in the list and
`getBundle` creates a `ResourceBundle` instance
that becomes the parent of the instance for
`foo/bar/Messages_fr.properties`.
Parameters:
`baseName` - the base name of the resource bundle, a fully qualified
class name
`targetLocale` - the locale for which a resource bundle is desired
`loader` - the class loader from which to load the resource bundle
`control` - the control which gives information for the resource
bundle loading process
Returns:
a resource bundle for the given base name and locale
Throws:
`NullPointerException` - if `baseName`, `targetLocale`,
`loader`, or `control` is
`null`
`MissingResourceException` - if no resource bundle for the specified base name can be found
`IllegalArgumentException` - if the given `control` doesn't perform properly
(e.g., `control.getCandidateLocales` returns null.)
Note that validation of `control` is performed as
needed.
Since:
1.6

