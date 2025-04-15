file = open('image.txt', 'r')

# [x, y, ASCII]

image_list = []
image_box = []
for i in range(0,100):
    image_box.append([' ']*100)
    
    
lines = file.readlines()
for line in lines:
    list_ascii = line.replace('[', '').replace(']', '').split(",")
    for i in range(len(list_ascii)):
        list_ascii[i] = int(list_ascii[i])
        
    x = list_ascii[0]
    y = list_ascii[1]
    code = list_ascii[2]
    image_box[y][x] = chr(code)

                
for i in image_box:
    print(''.join(i))