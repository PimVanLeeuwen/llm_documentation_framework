#### propertyGetDataRequested()


 virtual PropertyReplyData midi\_ci::PropertyDelegate::propertyGetDataRequested ( MUID , const PropertyRequestHeader & ) pure virtual 
 

Returns a header/body containing the requested data.To report an error, you can return a failure status code in the header and leave the body empty.