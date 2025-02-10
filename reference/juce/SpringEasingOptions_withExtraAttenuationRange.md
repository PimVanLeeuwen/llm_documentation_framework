#### withExtraAttenuationRange()


 auto SpringEasingOptions::withExtraAttenuationRange ( float newExtraAttenuationRange ) const nodiscard 
 

Specifies the input value at which an extra nonphysical attenuation begins to be applied.The value must be in the range [0.05f, 0.98f].This ensures that the easing always reaches an output value of 1.0f when the input value is 1.0f. If the attenuation is set sufficiently high this won't have a visible effect.See alsogetExtraAttenuationRange, withFrequency, withAttenuation References withMember().