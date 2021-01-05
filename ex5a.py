name = "Moses U. Ufomba"
age = 25 #not a lie
height = 74 #inches
weight = 120 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#This is a converter for inches and pounds to centimeters and Kilos
inches = 2.54
pounds = 0.454

print "Let's talk about %s." % name
print "He's %d inches tall." % height
#this converts his height from inches to centimeters
print "What is his height if expresed in centimeters? %s" %(height * inches)
print "He's %d pounds heavy" % weight
#this converts his weight from pounds to kilos
print "His weight can also be expressed in Kilos as %s" %(weight * pounds)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, height, age + height + weight)