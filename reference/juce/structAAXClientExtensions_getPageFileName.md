#### getPageFileName()


 virtual String AAXClientExtensions::getPageFileName ( ) const virtual 
 

Returns an optional filename (including extension) for a page file to be used.A page file allows an AAX plugin to specify how its parameters are displayed on various control surfaces. For more information read the Page Table Guide in the AAX SDK documentation.By default this file will be searched for in `*.aaxplugin/Contents/Resources`.See alsogetPageFileSearchPath