#### sendPropertyGetInquiry()


 std::optional< RequestKey > midi\_ci::Device::sendPropertyGetInquiry ( MUID m, 
 
 const PropertyRequestHeader & header, 
 std::function< void(const PropertyExchangeResult &)> onResult ) 

Initiates an inquiry to fetch a property from a particular device.Parameters

 m the MUID of the device to query 
 
 header specifies the resource to query, along with format/encoding options 
 onResult called when the transaction completes; not called if the transaction fails to start 



Returnsa key uniquely identifying this request, if the transaction begins successfully, or nullopt otherwise