#### getCurrentTilt()


 float MouseInputSource::getCurrentTilt ( bool tiltX ) const noexcept 
 

Returns the angle of tilt of the pointer in a range of 1.0 to 1.0 either in the x or yaxis.The default is 0. If xaxis, a positive value indicates a tilt to the right and if yaxis, a positive value indicates a tilt toward the user. Only reported by a pen pointer.