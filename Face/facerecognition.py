import face_recognition
from PIL import Image, ImageDraw

prat_image = face_recognition.load_image_file("prat.jpg")
prat_face_encoding = face_recognition.face_encodings(prat_image)[0]

prasad_image = face_recognition.load_image_file("prasad.jpeg")
prasad_face_encoding = face_recognition.face_encodings(prasad_image)[0]

obama_image = face_recognition.load_image_file("bhavesh.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

baiden_image = face_recognition.load_image_file("bhavik.jpg")
baiden_face_encoding = face_recognition.face_encodings(baiden_image)[0]


known_face_encodings = [
   
    prat_face_encoding,
    prasad_face_encoding,
    baiden_face_encoding,
    obama_face_encoding
    
]
known_face_names = [
    "Prat",
    "Prasad",
    "Bhavik Patalia",
    
    "Bhavesh"
]

unknown_image = face_recognition.load_image_file("1.jpg")

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)

draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")
