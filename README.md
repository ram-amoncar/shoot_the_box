
# 📦 Shoot The Box 🔫

A simple 2D shooting game developed as a Mini-Project for the 'Python Programming' subject in Graduation year.

## Gameplay

- 1 Player game with PvE mechanics.
- Player uses the mouse as a gun in the game.
- The objective is to shoot multiple moving box targets that appear on the screen.
- The game tracks hits and accuracy, displayed in the top left corner (e.g., "Hits: 0 Accuracy: 100%").
- The player controls a gun at the left of the screen, within a green circular area.
- Mouse motion controls the gun's movement, and any mouse button or space bar can be used to shoot.
- Boxes move continuously, bounce off screen edges, and periodically change direction randomly.

## Controls

- **Mouse Motion**: Move the gun within the green circular area.
- **Any Mouse Button or Space bar**: Shoot at the box targets.

## Features

- **Hit Counter**: Tracks the number of successful hits on the boxes.
- **Accuracy Percentage**: Displays the player's shooting accuracy in real-time.
- **Multiple Moving Targets**: Boxes move across the screen, bouncing off edges and changing direction.
- **Simple Graphics**: Minimalistic 2D design with a green player area, a gun, and multiple box targets.

## Development

- **Libraries**:  
    - `pygame` for graphics and event handling.
    - `asyncio` for asynchronous game loop management.
- **Purpose**: Created as a learning project to demonstrate basic game development concepts like event handling, collision detection, sprite management, and user interface updates.

## How to Play

1. Launch the game.
2. Use your mouse to move the gun within the green circular area.
3. Click any mouse button or press the spacebar to shoot at the moving box targets.
4. Aim to hit the boxes as many times as possible to increase your score.
5. Monitor your hits and accuracy in the top left corner.

## Future Improvements

- Code optimization (Scoring, Refactoring & CleanUp) ✅
- Introduce moving targets or multiple boxes for increased difficulty. ✅
- Implement a scoring system with bonuses for consecutive hits.

## Installation

1. Ensure Python is installed on your system.
2. Clone the repository.
3. Create a virtual environment & install `pygame`.
4. Run the main script (e.g., `python main.py`).