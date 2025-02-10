#### getArray()


 Array< var > \* var::getArray ( ) const noexcept 
 

If this variant holds an array, this provides access to it.NOTE: Beware when you use this the array pointer is only valid for the lifetime of the variant that returned it, so be very careful not to call this method on temporary var objects that are the returnvalue of a function, and which may go out of scope before you use the array!Referenced by ValueTreePropertyWithDefault::setValue().