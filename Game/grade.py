import requests
import os

from variables import APIKEY

def gradeApi(chosenImage):
    """
    Args:
        str: chosenImage

    Returns:
        float

    Uses API to grade drawing
    """
    #Find Distance Between Original And Copy
    grade = requests.post(
        "https://api.deepai.org/api/image-similarity",
        files={
            'image1': open(os.path.join("images", chosenImage), 'rb'),
            'image2': open(os.path.join("grading", "drawing.jpg"), 'rb'),
        },
        headers={'api-key': APIKEY}
    )

    #Find Distance Between Original and Whitescreen
    control = requests.post(
        "https://api.deepai.org/api/image-similarity",
        files={
            'image1': open(os.path.join("images", chosenImage), 'rb'),
            'image2': open(os.path.join("whiteScreen.png"), 'rb'),
        },
        headers={'api-key': APIKEY}
    )
    
    #Set Both As Variables
    numGrade = grade.json()["output"]["distance"]
    numControl = control.json()["output"]["distance"]

    #Calculate Overall Score In Decimals
    overall = round(1-(numGrade**3/numControl**3), 2)

    #Return Score
    return round(overall*100)
