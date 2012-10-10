* If you touch the sides of the screen, you die.
* The screen scrolls faster as the game continues.
* Obstacles appear randomly -- the level is generated dynamically.
* More obstacles as the game continues.
* Score (duration survived) displayed in upper right

1. Set up the screen, graphics, score counters etc.

* player
* level
* obstacles
* start time
* current time
* score (duration survived)
* scroll speed
* speed of obstacle generation

2. Start loop to finish when player quits/dies.

End when:
* player touches edges of the screen
* player quits

3. Draw graphic objects on screen.

* draw / scroll level
* draw / scroll / create obstacles
* draw / move player

4. Get input from user (eg keyboard or mouse).

* slide
* jump

5. Check game logic (eg player hit enemy?)

* collision detection:
  * if player collides with an obstacle, its horizontal speed becomes the obstacle's horizontal speed

6. Update graphic objects accordingly.
7. Go back to 3.

