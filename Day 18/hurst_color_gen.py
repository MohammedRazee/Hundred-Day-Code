import colorgram
colors = colorgram.extract('./Day 18/image.jpg', 30)


def gen_colors():
    rgb_colors = []

    for color in colors:
        r = color.rgb
        red = r.r
        green = r.g
        blue = r.b
        if red < 210 and green < 210 and blue < 210:
            rgb_colors.append((r.r, r.g, r.b))

    return rgb_colors

# print(gen_colors())
