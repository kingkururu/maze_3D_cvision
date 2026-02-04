# 3D Maze Game (Updated with Computer Vision)

A 3D maze game built with C++ and SFML, featuring Computer Vision gesture-based input, A* pathfinding, and a custom raycasting engine. This project extends traditional keyboard-based navigation by using real-time hand tracking to control movement and orientation.

<img width="997" height="488" alt="Image" src="https://github.com/user-attachments/assets/407ee617-9dd3-4170-aa46-f8f1a3ce445a" />

<img width="997" height="484" alt="Image" src="https://github.com/user-attachments/assets/e9b9fa7d-2057-4456-8da9-91252695fad2" />

<img width="1002" height="488" alt="Image" src="https://github.com/user-attachments/assets/e69997c4-8f57-47b1-a953-25d62ae7ff8d" />

<img width="998" height="485" alt="Image" src="https://github.com/user-attachments/assets/874a40d3-eeb9-4ece-87b1-ca39363684fa" />

<img width="997" height="487" alt="Image" src="https://github.com/user-attachments/assets/fbf6b104-7f38-4c6b-b6e6-e8335b2f7ccf" />

## Features

- **Procedural Maze Generation**: Random maze creation using Depth-First Search and Prim's algorithms
- **3D Raycasting Rendering**: Immersive 3D perspective from 2D maze data
- **Auto-Navigation**: Computer-guided movement with "Navigate Maze" functionality via A* algorithm
- **Real-time Path Visualization**: Visual representation of calculated paths
- **Performance Optimized**: Efficient maze generation and pathfinding algorithms
- **File I/O Integration**: Save and load maze configurations
- **Gesture Control System**: Use your hands to navigate the maze via OpenCV and MediaPipe.
  
## Controls

- **W/thumbs up**: Move forward
- **S/thumbs down**: Move backward  
- **A/thumbs up left**: Rotate camera left / turn player left
- **D/thumbs up right**: Rotate camera right / turn player right
  
## Project Structure

```
/maze_3D
│
├── src/                      # Source files
│   ├── main.cpp              # Main entry point of the game
│   └── game/                 # Core engine functionalities
│       ├── globals/          # Constants and flags
│       ├── core/             # Game loop and state management
│       ├── physics/          # Physics and collision detection
│       ├── camera/           # Window and view management
│       ├── utils/            # Utility functions
│       ├── vision/           # hand gesture recognition 
│       └── scenes/           # Scene management
│
├── assets/                   # Game assets
│   ├── fonts/                # Text files and sources
│   ├── sound/                # Sound effects
│   ├── tiles/                # Tiles and tilemaps
│   └── sprites/              # Sprite images
│
├── libs/                      # External libraries
│   └── logging/               # Logging system
│
├── Makefile                   # Build instructions
└── README.md                  # Project documentation
```
### Prerequisites
- **Compiler**: Requires clang++ (or g++) with C++17 support
- **SFML**: Simple and Fast Multimedia Library for graphics
- **Custom Game Framework**: Built on top of the SFML Game Framework

## Building & Running

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kingkururu/maze_3D_cvision
   cd maze_3D_cvision (location will be different)
   ```

2. **Build and run the Project**:
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install mediapipe==0.10.15
   mkdir build 
   cmake .
   make
   ./run
   ```

3. **How to Clean the Build**:
   ```bash
   make clean
   ```

## Assets Credits

- **Music**: [Game Background](https://pixabay.com/music/video-games-game-background-1-321720/) from Pixabay
- **Pixel font**: [LLPixel Font](https://www.dafont.com/llpixel.font)
- **Graphics**: Custom artwork created using Canva and Canva AI
- **Framework**: Built using the Custom SFML Game Framework https://github.com/kingkururu/sfml_game_template/edit/main/README.md

## Tools Used
- **SFML**: https://github.com/SFML/SFML 
- **Yaml-cpp**: https://github.com/jbeder/yaml-cpp
- **Spdlog**: https://github.com/gabime/spdlog 
- **FMT**: https://github.com/fmtlib/fmt
- **OpenCV**: https://github.com/opencv/opencv 
- **MediaPipe**: https://github.com/topics/mediapipe 
