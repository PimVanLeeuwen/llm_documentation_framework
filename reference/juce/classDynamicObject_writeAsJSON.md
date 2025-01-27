#### writeAsJSON()


 virtual void DynamicObject::writeAsJSON ( OutputStream & , const JSON::FormatOptions & ) virtual 
 

Writes this object to a text stream in JSON format.This method is used by JSON::toString and JSON::writeToStream, and you should never need to call it directly, but it's virtual so that custom object types can stringify themselves appropriately.