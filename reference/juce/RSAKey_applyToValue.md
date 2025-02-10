#### applyToValue()


 bool RSAKey::applyToValue ( BigInteger & value ) const 
 

Encodes or decodes a value.Call this on the public key object to encode some data, then use the matching private key object to decode it.Returns false if the operation couldn't be completed, e.g. if this key hasn't been initialised correctly.NOTE: This method dumbly applies this key to this data. If you encode some data and then try to decode it with a key that doesn't match, this method will still happily do its job and return true, but the result won't be what you were expecting. It's your responsibility to check that the result is what you wanted.