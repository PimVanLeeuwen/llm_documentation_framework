#### fromDocument()


 static AndroidDocument AndroidDocument::fromDocument ( const URL & documentUrl ) static 
 

Create an AndroidDocument representing a single document.The argument should be a URL representing a document. Such URLs are returned by the system filepicker when it is not in folderselection mode. If you pass a tree URL, this function will fail.This function may fail on Android devices with API level 18 or lower, and on nonAndroid platforms. If this function fails, hasValue() will return false on the returned document. If calling this function fails, you may want to retry creating an AndroidDocument with fromFile(), passing the result of URL::getLocalFile().