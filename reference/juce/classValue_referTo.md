#### referTo()


 void Value::referTo ( const Value & valueToReferTo ) 
 

Makes this object refer to the same underlying ValueSource as another one.Once this object has been connected to another one, changing either one will update the other.Existing listeners will still be registered after you call this method, and they'll continue to receive messages when the new value changes.Referenced by ValueTreePropertyWithDefault::ValueTreePropertyWithDefault(), ValueTreePropertyWithDefault::ValueTreePropertyWithDefault(), and ValueTreePropertyWithDefault::ValueTreePropertyWithDefault().