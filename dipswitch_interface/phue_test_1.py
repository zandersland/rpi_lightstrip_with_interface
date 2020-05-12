from phue import Bridge

b = Bridge('192.168.2.74')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
# b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
# print(b.get_api())




# Prints if light 1 is on or not
print(b.get_light('Duck1', 'on'))

# # Set brightness of lamp 1 to max
# b.set_light(1, 'bri', 254)

# # Set brightness of lamp 2 to 50%
# b.set_light(2, 'bri', 127)

# # Turn lamp 2 on
# b.set_light(2,'on', True)

# # You can also control multiple lamps by sending a list as lamp_id
# b.set_light( [1,2], 'on', True)

# Get the name of a lamp
print(b.get_light(13, 'name'))

# # You can also use light names instead of the id
# b.get_light('Kitchen')
# b.set_light('Kitchen', 'bri', 254)

# # Also works with lists
# b.set_light(['Bathroom', 'Garage'], 'on', False)

# # The set_light method can also take a dictionary as the second argument to do more fancy stuff
# # This will turn light 1 on with a transition time of 30 seconds
# command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
# b.set_light(1, command)
b.set_light('Duck1', {'transitiontime': 1, 'on': True, 'bri': 254})
