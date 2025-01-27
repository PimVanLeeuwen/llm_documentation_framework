#### copyDocumentToParentDocument()


 AndroidDocument AndroidDocument::copyDocumentToParentDocument ( const AndroidDocument & target ) const 
 

Experimental: Attempts to copy this document to a new parent, and returns an AndroidDocument representing the copy.On failure, the returned AndroidDocument may be invalid, and will return false from hasValue().This function may fail if the document doesn't allow copying, and when using URIbased documents on devices with API level 23 or lower. On failure, the returned AndroidDocument will return false from hasValue(). In testing, copying was not supported on the Android emulator for API 24, 30, or 31, so there's a good chance this function won't work on real devices.See alsoAndroidDocumentInfo::canCopy