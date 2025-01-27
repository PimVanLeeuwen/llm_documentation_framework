#### withHttpRequestCmd()


 InputStreamOptions URL::InputStreamOptions::withHttpRequestCmd ( const String & httpRequestCmd ) const nodiscard 
 

Specifies which HTTP request command to use.If this is not set, then the command will be POST if parameterHandling is set to ParameterHandling::inPostData or if any POST data has been specified via withPOSTData(), withFileToUpload(), or withDataToUpload(). Otherwise it will be GET.