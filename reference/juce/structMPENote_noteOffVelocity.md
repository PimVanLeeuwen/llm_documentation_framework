#### noteOffVelocity


 MPEValue MPENote::noteOffVelocity { MPEValue::minValue() } 
 

The release velocity ("lift") of the note after a noteoff has been received.This dimension will only have a meaningful value after a noteoff has been received for the note (and keyState is set to MPENote::off or MPENote::sustained). Initially, the value is undefined.