#### getCurrentPressure()


 float MouseInputSource::getCurrentPressure ( ) const noexcept 
 

Returns the device's current touch or pen pressure.The range is 0 (soft) to 1 (hard). If the input device doesn't provide any pressure data, it may return a negative value here, or 0.0 or 1.0, depending on the platform.