#### getEmptyProperties()


 static constexpr auto ARAHostModel::MusicalContext::getEmptyProperties ( ) staticconstexpr 
 

Returns an ARA versioned struct with the `structSize` correctly set for the currently used SDK version.You should leave `structSize` unchanged, and fill out the rest of the fields appropriately for the host implementation of the ARA model object.References makeARASizedStruct().