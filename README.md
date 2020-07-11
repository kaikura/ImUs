# ImUs
*ImUs* is an application that develops through the interaction with others. It investigates the sense of collectivity that technology can enhance and evolve. We believe collectivity to be something more than the sum of individuals.
*ImUs* is rooted in the key ideas of New Media Art:

- **Materiality:** the audience is engaged through the physical world
- **Embodiment:** mind and body have the same weight, they're not treated separately
- **The Cyborg:** the application have a certain degree of autonomy
- **Hybridity:** hybridity of disciplines involved is self evident; real world and virtual world merge through sound modulation and through visualization
- **Narrative:** the experience have starting point and a climax that can be reached by the audience
- **Interactivity:** the piece works through people

We developed the experience being inspired by those concepts, trying to convey our message.

See it here: (for presentation purpouses the visualization is on a computer screen)

# Tools
- *Exploration Space* - The portion of space dedicated to the users
- *First Camera* - Takes user photos
- *Second Camera* - Track users in the exploration space
- *Loudspeakers* - To listen to the exploration results
- *Projecting Screen* - To see the exploration results

# Scripts
comandantecheguevara.py links

# Step by Step

# Face Capture 
The users take pictures of their faces. The visualized ellipse defines the correct position and centering. Once the photos have been taken the *exploration space* is ready to be used.

# People Tracking
As people enter in the *exploration space* they are tracked by the camera. They are free to move and interact with others. They'll find themself immersed in a soundscape.

# The Network
Area indivi are sent via OSC messages through a LAN working on a hotspot or any other router. The python works as a server for MaxMSP sound processing and for Processing video processing.

# Environmental Sound Modulation

![](ImUs/resources/MAx_pat.png)

What the user will hear is that their physical presence have an effect on the sound landscape they're immersed in. 
The sound is generated and processed by MaxMSP. At the beginning, a first layer of two synth created with Hybrid 3 by AIR Music Technology is played in loop. It is filtered with a low pass which cutting frequency is controlled by th

# Face Merging
The faces obtained initially are merged by morpher.py via Delaunay triangulation, finding an average for each possible couple of faces and a global average of all faces. 
videoer.py returns an .avi file with the transactions between the averages. 
The video is saved as themorph.avi in the selected directory.

# Visualization
What the user will see is that their physical presence have an effect on the visualization.
videoOSC.pde reads the video and decompose it in cells resembling single pixels. 
Those cells are exploded by the code in the 3 dimensions. 
The z coordinate is controlled via OSC messages by the area of the figure individuated by the IDs of people_counter.py. The bigger it is (the bigger the distance between people is), the bigger z will be. In this way, as the closeness increases the planar visualization increases (and so the clearness of the video visualization).
The video is put in loop and then played at random points every 22 frames for aestetichs purpouses.

