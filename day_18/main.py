
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb[1]
    b = color.rgb[2]
    add = (r, g, b)
    rgb_colors.append(add)

print(rgb_colors)
