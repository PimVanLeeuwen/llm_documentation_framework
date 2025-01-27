#### operator()()


template<typename ValueType > 

 ValueType StaticAnimationLimits< ValueType >::operator() ( float value ) const 
 

Evaluation operator.Returns a value that is a linear interpolation of the beginning and end state. It's a shorthand for the lerp() function.