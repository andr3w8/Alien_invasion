# 12-1. Blue Sky: Make a Pygame window with a blue background.
# 12-2. Game Character: Find a bitmap image of a game character you like or
# convert an image to a bitmap. Make a class that draws the character at the
# center of the screen and match the background color of the image to the background color of the screen, or vice versa.
# 12-3. Pygame Documentation: We’re far enough into the game now that you
# might want to look at some of the Pygame documentation. The Pygame home
# page is at https://www.pygame.org/, and the home page for the documentation
# is at https://www.pygame.org/docs/. Just skim the documentation for now.
# You won’t need it to complete this project, but it will help if you want to modify
# Alien Invasion or make your own game afterward.
# 12-4. Rocket: Make a game that begins with a rocket in the center of the
# screen. Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of the screen.
# 12-5. Keys: Make a Pygame file that creates an empty screen. In the event
# loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected.
# Run the program and press various keys to see how Pygame responds.
##########12-6. Sideways Shooter: Write a game that places a ship on the left side of the
# screen and allows the player to move the ship up and down. Make the ship fire
# a bullet that travels right across the screen when the player presses the spacebar.
# Make sure bullets are deleted once they disappear off the screen.

#Pana aici, 529 linii de cod , fara exercitiile de mai jos :*

#From here we need to make exercise.


# 13-1. Stars: Find an image of a star. Make a grid of stars appear on the screen.
# 13-2. Better Stars: You can make a more realistic star pattern by introducing
# randomness when you place each star. Recall that you can get a random number like this:
# from random import randint
# random_number = randint(-10, 10)
# This code returns a random integer between −10 and 10. Using your code
# in Exercise 13-1, adjust each star’s position by a random amount.
# 13-3. Raindrops: Find an image of a raindrop and create a grid of raindrops.
# Make the raindrops fall toward the bottom of the screen until they disappear.
# 13-4. Steady Rain: Modify your code in Exercise 13-3 so when a row of raindrops
# disappears off the bottom of the screen, a new row appears at the top of
# the screen and begins to fall.
# 13-5. Sideways Shooter Part 2: We’ve come a long way since Exercise 12-6,
# Sideways Shooter. For this exercise, try to develop Sideways Shooter to the
# same point we’ve brought Alien Invasion to. Add a fleet of aliens, and make
# them move sideways toward the ship. Or, write code that places aliens at random
# positions along the right side of the screen and then sends them toward
# the ship. Also, write code that makes the aliens disappear when they’re hit.
#13-6. Game Over: In Sideways Shooter, keep track of the number of times the
# ship is hit and the number of times an alien is hit by the ship. Decide on an
# appropriate condition for ending the game, and stop the game when this situation occurs.
# 14-1. Press P to Play: Because Alien Invasion uses keyboard input to control
# the ship, it would be useful to start the game with a keypress. Add code that
# lets the player press P to start. It might help to move some code from _check
# _play_button() to a _start_game() method that can be called from _check_play
# _button() and _check_keydown_events().
# 14-2. Target Practice: Create a rectangle at the right edge of the screen that
# moves up and down at a steady rate. Then have a ship appear on the left side
# of the screen that the player can move up and down while firing bullets at the
# moving, rectangular target. Add a Play button that starts the game, and when
# the player misses the target three times, end the game and make the Play button reappear.
# Let the player restart the game with this Play button.
# 14-3. Challenging Target Practice: Start with your work from Exercise 14-2
# (page 285). Make the target move faster as the game progresses, and restart
# the target at the original speed when the player clicks Play.
# 14-4. Difficulty Levels: Make a set of buttons for Alien Invasion that allows the
# player to select an appropriate starting difficulty level for the game. Each button
# should assign the appropriate values for the attributes in Settings needed
# to create different difficulty levels.
# 14-5. All-Time High Score: The high score is reset every time a player closes
# and restarts Alien Invasion. Fix this by writing the high score to a file before
# calling sys.exit() and reading in the high score when initializing its value in
# GameStats.
# 14-6. Refactoring: Look for methods that are doing more than one task, and
# refactor them to organize your code and make it efficient. For example, move
# some of the code in _check_bullet_alien_collisions(), which starts a new level
# when the fleet of aliens has been destroyed, to a function called start_new
# _level(). Also, move the four separate method calls in the __init__() method
# in Scoreboard to a method called prep_images() to shorten __init__(). The
# prep_images() method could also help simplify _check_play_button() or start
# _game() if you’ve already refactored _check_play_button().
# 14-7. Expanding the Game: Think of a way to expand Alien Invasion. For
# example, you could program the aliens to shoot bullets down at the ship or
# add shields for your ship to hide behind, which can be destroyed by bullets
# from either side. Or use something like the pygame.mixer module to add sound
# effects, such as explosions and shooting sounds.
# 14-8. Sideways Shooter, Final Version: Continue developing Sideways Shooter,
# using everything we’ve done in this project. Add a Play button, make the game
# speed up at appropriate points, and develop a scoring system. Be sure to
# refactor your code as you work, and look for opportunities to customize the
# game beyond what was shown in this chapter.

