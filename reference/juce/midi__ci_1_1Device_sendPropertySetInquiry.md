#### sendPropertySetInquiry()


 std::optional< RequestKey > midi\_ci::Device::sendPropertySetInquiry ( MUID m, 
 
 const PropertyRequestHeader & header, 
 Span< const std::byte > body, 
 std::function< void(const PropertyExchangeResult &)> onResult ) 

Initiates an inquiry to set a property on a particular device.Parameters

 m the MUID of the device to query 
 
 header specifies the resource to query, along with format/encoding options 
 body the unencoded body content of the message 
 onResult called when the transaction completes; not called if the transaction fails to start 



Returnsa key uniquely identifying this request, if the transaction begins successfully, or nullopt otherwise