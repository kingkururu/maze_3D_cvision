# 3D Maze Game (Updated with Computer Vision)

A 3D maze game built with C++ and SFML, featuring Computer Vision gesture-based input, A* pathfinding, and a custom raycasting engine. This project extends traditional keyboard-based navigation by using real-time hand tracking to control movement and orientation.

New: Computer Vision Integration
This version integrates a vision processing layer to allow touchless control:

OpenCV: Handles the camera feed, image processing, and frame buffering.

MediaPipe: Provides the machine learning backend for high-fidelity hand landmark detection.

<img width="641" alt="Image" src="https://github.com/user-attachments/assets/681bd3e9-5e92-47ae-bc73-865dbb595454" />
<img width="884" alt="Image" src="https://github.com/user-attachments/assets/4856a85c-618c-4cc3-9e42-bb8f56957bd5" />
<img width="950" alt="Image" src="https://github.com/user-attachments/assets/ae51ba5a-fd90-45b8-8330-e17a46d82088" />

## Features

- **Procedural Maze Generation**: Random maze creation using Depth-First Search and Prim's algorithms
- **3D Raycasting Rendering**: Immersive 3D perspective from 2D maze data
- **Auto-Navigation**: Computer-guided movement with "Navigate Maze" functionality via A* algorithm
- **Real-time Path Visualization**: Visual representation of calculated paths
- **Performance Optimized**: Efficient maze generation and pathfinding algorithms
- **File I/O Integration**: Save and load maze configurations
  
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

2. **Build the Project**:
   ```bash
   make
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
- **OpenCV**: For camera capture and image processing.
- **MediaPipe**: For hand tracking and landmark recognition.
