from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register a cursive font (update the path to where your .ttf file is)
pdfmetrics.registerFont(TTFont('DancingScript', 'DancingScript-Regular.ttf'))

# PDF setup
c = canvas.Canvas("cursive_alphabet.pdf", pagesize=letter)
width, height = letter

# Font settings
font_name = 'DancingScript'
font_size = 30
line_height = 40
margin = 72

# Draw Uppercase
c.setFont(font_name, font_size)
c.drawString(margin, height - margin, "Uppercase Cursive Alphabet:")
c.drawString(margin, height - margin - line_height, "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")

# Draw Lowercase
c.drawString(margin, height - margin - 3*line_height, "Lowercase Cursive Alphabet:")
c.drawString(margin, height - margin - 4*line_height, "a b c d e f g h i j k l m n o p q r s t u v w x y z")

# Pangram
c.drawString(margin, height - margin - 6*line_height, "Pangram (26 letters):")
c.drawString(margin, height - margin - 7*line_height, "Mr Jock, TV quiz PhD, bags few lynx.")

c.save()
