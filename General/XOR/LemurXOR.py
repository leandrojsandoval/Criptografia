from PIL import Image
import numpy as np

# Cargar las imágenes
image_lemur = Image.open("lemur.png");
image_flag = Image.open("flag.png");

# Convertir las imágenes a matrices numpy (RGB)
lemur_data = np.array(image_lemur);
flag_data = np.array(image_flag);

# Verificar que las dimensiones de las imágenes sean iguales
if lemur_data.shape != flag_data.shape:
    raise ValueError("Las dimensiones de las imágenes no coinciden.");

# Crear una matriz para la imagen resultante
result_data = np.zeros_like(lemur_data);

# Aplicar XOR píxel a píxel
for i in range(lemur_data.shape[0]):
    for j in range(lemur_data.shape[1]):
        for k in range(lemur_data.shape[2]):
            result_data[i, j, k] = lemur_data[i, j, k] ^ flag_data[i, j, k];

# Crear una imagen PIL a partir de los datos resultantes
result_image = Image.fromarray(result_data.astype('uint8'));

# Guardar y mostrar la imagen resultante
result_image.save("result_xor.png");
result_image.show();
