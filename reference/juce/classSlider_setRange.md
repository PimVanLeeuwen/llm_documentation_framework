#### setRange() [2/2]


 void Slider::setRange ( Range< double > newRange, 
 
 double newInterval ) 

Sets the limits that the slider's value can take.Parameters

 newRange the range to allow 
 
 newInterval the steps in which the value is allowed to increase if this is not zero, the value will always be (newMinimum + (newInterval \* an integer)).