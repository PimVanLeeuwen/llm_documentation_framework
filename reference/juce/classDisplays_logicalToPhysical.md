#### logicalToPhysical() [3/3]


template<typename ValueType > 

 Point< ValueType > Displays::logicalToPhysical ( Point< ValueType > logicalPoint, const Display \* useScaleFactorOfDisplay = nullptr ) const noexcept 
 

Converts a Point from logical to physical pixels.If useScaleFactorOfDisplay is not null then its scale factor will be used for the conversion regardless of the display that the Point to be converted is on.