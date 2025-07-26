# gas_blending
Boot.Dev Hackathon project

This will be a simple tool to take a few inputs and provide a response for a trained gas blender to properly mix the gases. 

At this time, this tool only supports partial pressure blending. premixes WILL NOT work.

This tool assumes that the tank is empty before filling. if you had to empty the tank, please take the time to validate it is O2 clean, it costs nothing and prevents potential fires :)


This will also provide an option for you to initialize the value of the source containers so you can bill the customer accordingly for the materials for the gas blending

This will fill a niche that is sorely missing in the dive community. 

Please note, mixing any high pressure cylinders should be done with care and in a clean environment. please make sure this is also done by a certified gas blending technician. 

Any attempts to blend gas using the ratios here while not trained in gas blending techniques can lead to serious injury. 


How to run program:
clone the repository and call main.py
answer the prompts to get the answers

default answers to help the non-diving user:
80cuft tank
3000psi
32 or 36 %O2 is a standard for diving



future plans:
    - UI 
    - Trimix Compatibility
    - PPO2 input 
    - MOD input and gas blend suggestion output
