'''
Dictionary Comprehension
========================

dict comprehension are often used to transform an existing dict, either
modifying entries or filtering unwanted entries (or both).  
'''

def rgb(v):
    # return a rgb tuple
    return (v>>16) &0xFF, (v>>8) &0xFF, v&0xFF


colors = {
	'maroon':			0x800000,
	'dark red':			0x8B0000,
	'brown':			0xA52A2A,
	'firebrick':		0xB22222,
	'crimson':			0xDC143C,
	'red':				0xFF0000,
	'tomato':			0xFF6347,
	'coral':			0xFF7F50,
	'indian red':		0xCD5C5C,
	'light coral':		0xF08080,
	'dark salmon':		0xE9967A,
	'salmon':			0xFA8072,
	'light salmon':		0xFFA07A,
	'orange red':		0xFF4500,
	'dark orange':		0xFF8C00,
	'orange':			0xFFA500,
	'gold':				0xFFD700,
	'dark golden rod':	0xB8860B,
	'golden rod':		0xDAA520,
	'pale golden rod':	0xEEE8AA,
	'dark khaki':		0xBDB76B,
	'khaki':			0xF0E68C,
	'olive':			0x808000,
	'yellow':			0xFFFF00,
	'yellow green':		0x9ACD32,
	'dark olive green':	0x556B2F,
	'olive drab':		0x6B8E23,
	'lawn green':		0x7CFC00,
	'chartreuse':		0x7FFF00,
	'green yellow':		0xADFF2F,
	'dark green':		0x006400,
	'green':			0x008000,
	'forest green':		0x228B22,
	'lime':				0x00FF00,
	'lime green':		0x32CD32,
	'light green':		0x90EE90,
	'pale green':		0x98FB98,
	'dark sea green':	0x8FBC8F,
	'medium spring green':0x00FA9A,
	'spring green':		0x00FF7F,
	'sea green':		0x2E8B57,
	'medium aqua marine':0x66CDAA,
	'medium sea green':	0x3CB371,
	'light sea green':	0x20B2AA,
	'dark slate gray':	0x2F4F4F,
	'teal':				0x008080,
	'dark cyan':		0x008B8B,
	'aqua':				0x00FFFF,
	'cyan':				0x00FFFF,
	'light cyan':		0xE0FFFF,
	'dark turquoise':	0x00CED1,
	'turquoise':		0x40E0D0,
	'medium turquoise':	0x48D1CC,
	'pale turquoise':	0xAFEEEE,
	'aqua marine':		0x7FFFD4,
	'powder blue':		0xB0E0E6,
	'cadet blue':		0x5F9EA0,
	'steel blue':		0x4682B4,
	'corn flower blue':	0x6495ED,
	'deep sky blue':	0x00BFFF,
	'dodger blue':		0x1E90FF,
	'light blue':		0xADD8E6,
	'sky blue':			0x87CEEB,
	'light sky blue':	0x87CEFA,
	'midnight blue':	0x191970,
	'navy':				0x000080,
	'dark blue':		0x00008B,
	'medium blue':		0x0000CD,
	'blue':				0x0000FF,
	'royal blue':		0x4169E1,
	'blue violet':		0x8A2BE2,
	'indigo':			0x4B0082,
	'dark slate blue':	0x483D8B,
	'slate blue':		0x6A5ACD,
	'medium slate blue':0x7B68EE,
	'medium purple':	0x9370DB,
	'dark magenta':		0x8B008B,
	'dark violet':		0x9400D3,
	'dark orchid':		0x9932CC,
	'medium orchid':	0xBA55D3,
	'purple':			0x800080,
	'thistle':			0xD8BFD8,
	'plum':				0xDDA0DD,
	'violet':			0xEE82EE,
	'magenta / fuchsia':0xFF00FF,
	'orchid':			0xDA70D6,
	'medium violet red':0xC71585,
	'pale violet red':	0xDB7093,
	'deep pink':		0xFF1493,
	'hot pink':			0xFF69B4,
	'light pink':		0xFFB6C1,
	'pink':				0xFFC0CB,
	'antique white':	0xFAEBD7,
	'beige':			0xF5F5DC,
	'bisque':			0xFFE4C4,
	'blanched almond':	0xFFEBCD,
	'wheat':			0xF5DEB3,
	'corn silk':		0xFFF8DC,
	'lemon chiffon':	0xFFFACD,
	'light golden rod yellow':0xFAFAD2,
	'light yellow':		0xFFFFE0,
	'saddle brown':		0x8B4513,
	'sienna':			0xA0522D,
	'chocolate':		0xD2691E,
	'peru':				0xCD853F,
	'sandy brown':		0xF4A460,
	'burly wood':		0xDEB887,
	'tan':				0xD2B48C,
	'rosy brown':		0xBC8F8F,
	'moccasin':			0xFFE4B5,
	'navajo white':		0xFFDEAD,
	'peach puff':		0xFFDAB9,
	'misty rose':		0xFFE4E1,
	'lavender blush':	0xFFF0F5,
	'linen':			0xFAF0E6,
	'old lace':			0xFDF5E6,
	'papaya whip':		0xFFEFD5,
	'sea shell':		0xFFF5EE,
	'mint cream':		0xF5FFFA,
	'slate gray':		0x708090,
	'light slate gray':	0x778899,
	'light steel blue':	0xB0C4DE,
	'lavender':			0xE6E6FA,
	'floral white':		0xFFFAF0,
	'alice blue':		0xF0F8FF,
	'ghost white':		0xF8F8FF,
	'honeydew':			0xF0FFF0,
	'ivory':			0xFFFFF0,
	'azure':			0xF0FFFF,
	'snow':				0xFFFAFA,
	'black':			0x000000,
	'dim gray / dim grey':0x696969,
	'gray / grey':		0x808080,
	'dark gray / dark grey':0xA9A9A9,
	'silver':			0xC0C0C0,
	'light gray / light grey':0xD3D3D3,
	'gainsboro':		0xDCDCDC,
	'white smoke':		0xF5F5F5,
	'white':			0xFFFFFF,
}

rgb_colors = {k:rgb(v) for k,v in colors.items()}

for k, v in rgb_colors.items():
    print(f"{k:32}: {v}")


