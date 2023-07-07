# requests_low_memory_exmaple
A quick sample to show that the Requests library does not work with low memory on Pico W


Simple example that loads a bitmaps into a list until the memory is low. This will quickly crash, however it does show the exceptions below 40k are not indicative of what is the real issue. 

