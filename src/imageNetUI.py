from CombineExtraction import XmlExtraction
from ImageExtraction import ImgExtraction


class ImageNetUI:
    
#|-----------------------------------------------------------------------------|
# imagenetObjectDetection
#|-----------------------------------------------------------------------------|
    def imagenetObjectDetection(self, filePath):
        """
        1. for all files, find xml details and make its dict
        2. based on these xml, detect objects
        3. train data
        
        """
        xmlExtraction=XmlExtraction()
        xmlFilePath="../xmlData/lady.xml"
        elementDict = xmlExtraction.extractXMLData(xmlFilePath = xmlFilePath)
        
        imgpath="../img/lady.jpeg"
        imgExtraction=ImgExtraction()
        flag=imgExtraction.extractImgData(imgpath,elementDict)
#|------------------------imagenetObjectDetection -ends------------------------|    















if __name__ == '__main__':
    filePath = ""
    imageNetUI = ImageNetUI()
    imageNetUI.imagenetObjectDetection(filePath)
    