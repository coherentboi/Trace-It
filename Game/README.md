# Trace It!

Trace it is a game where you are given an image and you have to replicate it as best as possible. The game will then rate your drawing based on how close it is.

## Dependencies

### Python 3.9

To check python version, run:

On Mac:
```bash
python3 --version
```
On Windows:
```bash
python --version
```
### Pygame 1.9.6

To download pygame, run:

On Mac:
```bash
pip3 install pygame
```

On Windows:
```bash
pip install pygame
```

## Run

To run, run main.py.

On Mac:
```bash
python3 main.py
```

On Windows:
```bash
python main.py
```

## Add Drawings

If you want to add your own drawings to copy to the game, upload them into the `images` folder. Make sure that it has a different name from the existing images and also that it is exactly `750px` x `500px`. 

## Important Notes

### Do Not Modify File Structure

Under no circumstances should you have to modify ```drawings.json``` or the ```previous``` or ```grading``` folders. Modification of these folders may lead to the program malfunctioning. All changes can be  made through the game GUI.

### Unfinished Parts

Some parts were omitted from the final project. Most notably, there are no settings, mainly because of a lack of things to include within the settings. Most "extra" features in the plan were omitted because I wanted to focus on a simple but very robust, pretty and functional game.

### Inaccurate API

When one plays this game more, they may realize that the grading is sometimes inaccurate. What may seem close to us may not reflect in the grading. The reason for this is because of the AI that I chose. It is an image recognition AI and is meant to assess the "distance" between two images. Note that we don't really know what "distance" means, so in order to grade, I had to use a control by comparing the drawn image to a white screen. There are no better free AIs on the internet, and I don't think that coding one myself would have yielded better results, while it would also have made the project singificantly harder due to having to learn from scratch and train the AI. 

### Free Tokens Expired

Because I am using an online API, there may be times where the grading malfuncitons because of: "ran out of free tokens". The reason for this is that the AI usually charges money for its service. When using the AI at first, it allows a certain amount of uses before it has to be paid for. If you do run into the situation in which this is the case, it is likely that this message will show up in the console. Go to the website `https://deepai.org/machine-learning-model/image-similarity`, create a new account, and copy the API Key. Then go to variables and paste the API key into the APIKEY variable. 

### Negative Percentage

Sometimes, a negative percentage will show up for grading. This basically means that you would have been closer to the image should you have drawn nothing than what you drew :).