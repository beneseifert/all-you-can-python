from PIL import Image

pfad = "./bilder/"
bild_name = "python.jpg"
bild = Image.open(pfad + bild_name)

pfad_generierte_bilder = pfad + "output/"
bild.thumbnail((120, 120))
bild.save(pfad_generierte_bilder + "thumbnail_" + bild_name)

bild.convert("L").save(pfad_generierte_bilder + "gray_" + bild_name)
