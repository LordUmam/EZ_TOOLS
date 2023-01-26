from rembg import remove
import easygui
from PIL import Image
import PIL
from tkinter.filedialog import *

print(''' 
Pilih tools yang ingin digunakan :
1. Background remover
2. Image Converter ''')
print()

pilihan = int(input('Tools yang dipilih: '))
print()

for i in range(pilihan):
    
    if pilihan == 1:
        

        inputPath = easygui.fileopenbox(title='Select image file')
        outputPath = easygui.filesavebox(title='Save file to..')

        input = Image.open(inputPath)
        output = remove(input)
        output.save(outputPath+".png")
        print('selesai')
        break

    if pilihan == 2:
        

        file_path = askopenfilename()
        img = PIL.Image.open(file_path)
        myHeight, myWidth = img.size

        img = img.resize((myHeight, myWidth) , PIL.Image.Resampling.LANCZOS)
        save_path = asksaveasfilename()

        img.save(save_path + "_compressed.jpg")
        print('foto telah tercompres')
        break
        
    else:
        print('Tools yang dipilih salah')
        break

