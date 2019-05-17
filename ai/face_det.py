from PIL import Image
import face_recognition
import numpy as np
import sys
sys.path.append('./align')
from align.detector import detect_faces
from align.visualization_utils import show_results

class Face:
    """All tools related to face is wrapped in this class.

    This class used MTCNN for detection and landmark localization.
    Due to the uncertainty of database implementation, one database
    interface is left to anyone in need.

    """
    def __init__(self, candidate_list={}):
        """Initializer

        # Arguments
            candidate_list: a dict, contains the `names` and `absolute paths`
            of people, e.g. {'Zhichao Duan':'/home/matthew/pic.jpg',}
        """
        self.candidate_list = candidate_list

    @classmethod
    def is_the_same_person(cls, img1, img2):
        """Class method used to justify if the two given images are
        from the same person

        # Arguments
            img1: str, absolute path of one image
            img2: str, absolute path of the other

        # Returns
            result: bool, the result.
        """

        pic1 = face_recognition.load_image_file(img1)
        pic2 = face_recognition.load_image_file(img2)
        encoding1 = face_recognition.face_encodings(pic1)[0]
        encoding2 = face_recognition.face_encodings(pic2)[0]
        result = face_recognition.compare_faces([encoding1], encoding2)[0]
        return result

    def load(self):
        known_face_encodings = []
        know_face_names = []
        for k, v in self.candidate_list.items():
            img = face_recognition.load_image_file(v)
            encoding = face_recognition.face_encodings(img)[0]
            know_face_names.append(k)
            known_face_encodings.append(encoding)
        return (know_face_names, known_face_encodings)

    def get_all_matched_faces(self, img):
        """This method can identify all persons in the given picture.

        # Arguments
            img: str, path of one single image.

        # Returns
            face_names: list, all identifies persons.
        """
        know_face_names, known_face_encodings = self.load()
        img = face_recognition.load_image_file(img)
        face_locations = face_recognition.face_locations(img)
        face_encodings = face_recognition.face_encodings(img, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = 'unknown'
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = know_face_names[best_match_index]
            face_names.append(name)
        return face_names

    @classmethod
    def get_box_and_lm(cls, img, content='path'):
        assert content in ('path', 'PILImage')
        if content == 'path':
            img = Image.open(img)
            bounding_boxes, landmarks = detect_faces(img)
        return (bounding_boxes, landmarks)
