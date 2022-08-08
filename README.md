# Violin-Playing-Classification
Tensorflow lite model used to classify images in real time of violin playing using the openMV h7 plus camera/microcontroller

Example of images along with their outputs (as color frames) is in the example_video_320x280.mp4 video.
Some more examples are in the video_examples folder. 


To use:
Download 200x200 data. Consider adding your own 200x200 data of images of violin playing, using the python scrips from code -> frames_into_folder.py.

Then, Download image data onto google drive, as google colab is quite useful here. 

From the code folder, open either most_recent.ipynb or old_tftest3classes.ipynb. Then simply run this code to create the tflite model. 

Run main.py with the tflite model on the openMV camera.


With any questions, email me @ enla2020@mymail.pomona.edu







Thanks to Suren Jayasuriya, Odrika Iqbal, Seth Thorn, Byron Lahey as a part of the Visual Media REU at ASU
Special thanks to @CzJLee for help cleaning up code
