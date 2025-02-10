#### getDiscoveryInfoForMuid()


 std::optional< Message::Discovery > midi\_ci::Device::getDiscoveryInfoForMuid ( MUID m ) const 
 

Returns basic attributes about another device that was discovered.If there's no record of the provided device, this will return nullopt.