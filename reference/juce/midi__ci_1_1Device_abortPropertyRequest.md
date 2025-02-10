#### abortPropertyRequest()


 void midi\_ci::Device::abortPropertyRequest ( RequestKey ) 
 

Cancels a request started with sendPropertyGetInquiry() or sendPropertySetInquiry().This sends a property notify message indicating that the responder no longer needs to process the initial request.