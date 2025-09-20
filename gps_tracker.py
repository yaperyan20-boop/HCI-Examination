def move_player():
    x, y = 0, 0  # Starting position at (0, 0)

    while True:
        # Get the user's input direction
        direction = input("Enter direction (N/S/E/W or STOP to end): ").strip().lower()

        # Handle 'STOP' to end the session
        if direction == 'stop':
            break

        # Handle invalid inputs
        if direction not in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']:
            print("Invalid input! Please enter N, S, E, W or STOP.")
            continue

        # Update position based on direction
        if direction in ['n', 'north']:
            y += 1
        elif direction in ['s', 'south']:
            y -= 1
        elif direction in ['e', 'east']:
            x += 1
        elif direction in ['w', 'west']:
            x -= 1

        # Show the current position
        print(f"Current position: ({x}, {y})")

    # After session ends, check if returned to origin
    print(f"Final position: ({x}, {y})")
    if x == 0 and y == 0:
        print("You returned to the origin (0, 0).")
    else:
        print("You did not return to the origin.")

# Call the function to start the tracker
move_player()
