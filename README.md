# gas_blending
<h1>Boot.Dev Hackathon project</h1>


<h2>Overview</h2>
This will be a simple tool to take a few inputs and provide a response for a trained gas blender to properly mix gases. 

At this time, this tool only supports partial pressure blending. premixes WILL NOT work.

This tool assumes that the tank is empty before filling. if you had to empty the tank, please take the time to validate it is O2 clean, it costs nothing and prevents potential fires :)

There will also be an option for you to initialize the value of the source containers so you can bill the customer accordingly for the materials for the gas blending, the default values are listed in defaults.md.

<h2>Rationale</h2>
This will fill a niche that is sorely missing in the dive community. 

I remember using an application that had this exact same functionality, it currently is not updated at all and unusable on the modern iOS. I wanted to create something that simingly anyone could use(accepting you have a python interpreter downloaded)

<h2>Important Saftey Notes</h2>
Please note, mixing any high pressure cylinders should be done with care and in a clean environment. please make sure this is also done by a certified gas blending technician. 

Any attempts to blend gas using the ratios here while not trained in gas blending techniques can lead to serious injury. 

Always validate any math that you yourself do not understand, make sure the MOD and the Contingency are within the customers dive plan. It is your responsibility as the gas blender to provide guidance and offer options to better suit the divers needs.


<h2>How To Run the Program</h2>

clone the repository and call main.py within the source folder
answer the prompts provided. if you do not have any background in diving, please refer below to standard tank size and oxygen blend.

<h3>default answers:</h3>
- 80cuft tank
- 3000psi
- 32 or 36 %O2 is a standard for diving



- future plans:
    * UI 
    * Trimix Compatibility
    * PPO2 input 
    * MOD input and gas blend suggestion output
