import os
from extractLocationFromText import ExtractLocationFormText
from getIdentifer import getWikiRecord


if __name__ == '__main__':

    testDataPath = "test_data/"
    parser = ExtractLocationFormText()
    englishTestData = os.path.join(testDataPath, "en_magellan_voyage.txt")
    englishText = open(englishTestData, "r").read()
    foundLocations = parser.getLocationsEnglish(englishText)
    for loc in foundLocations:
        loc.wikiID, loc.geonameID, loc.longitude, loc.lattitude = getWikiRecord(loc.text, loc.language)
        print(loc.__dict__)