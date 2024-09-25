# 9. LIST, STRING. A simple code that could help you match your tie, your shirt and your jacket. 
# Of course it does it  randomly)
import random
shirts = ["red", "yellow", "blue", 
              "navy", "orange", "green", 
              "violet", "scarlet", "charcoal grey", 
              "white", "black", "gold", "silver"]
ties = ["red", "yellow", "blue", 
              "navy", "orange", "green", 
              "violet", "scarlet", "charcoal grey", 
              "white", "black", "gold", "silver"]
jackets = ["red", "yellow", "blue", 
              "navy", "orange", "green", 
              "violet", "scarlet", "charcoal grey", 
              "white", "black", "gold", "silver"]
print ("You should match your", random.choice(jackets), "jacket with your", 
       random.choice(shirts), "shirt and with your", random.choice(ties), "tie.", "Looking spiffy!")