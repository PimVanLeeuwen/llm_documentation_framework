#### withNumRedirectsToFollow()


 WebInputStream & WebInputStream::withNumRedirectsToFollow ( int numRedirects ) 
 

Specify the number of redirects to be followed.Returns a reference to itself so that several methods can be chained.Parameters

 numRedirects specifies the number of redirects that will be followed before returning a response (ignored for Android which follows up to 5 redirects)