from PIL import Image

images_path_list = []

while True:
    try:
        photo_Count = int(input("Kaç fotoğrafınız var: "))
        break
    except ValueError:
        print("Lütfen sayıyı düzgünce giriniz!!")

for x in range(photo_Count):
    images_path_list.append(input("Fotoğrafın adını giriniz: "))


def create_gif(images_path_list):
    image_list = [Image.open(file) for file in images_path_list]
    image_list[0].save('animation.gif', save_all=True, append_images=image_list[1:], duration=1000, loop=0)


create_gif(images_path_list)
