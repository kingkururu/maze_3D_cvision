#include "vision.hpp"

void VisionSystem::initializeVisionSystem() {
    visionPipe = popen("./.venv/bin/python ./vision.py", "r");
    if (visionPipe) {
        // Get the file descriptor for the pipe
        int fd = fileno(visionPipe);
        // Set it to non-blocking mode
        int flags = fcntl(fd, F_GETFL, 0);
        fcntl(fd, F_SETFL, flags | O_NONBLOCK);
    }
}

void VisionSystem::getVisionInput() {
    char buffer[128];

    if (fgets(buffer, sizeof(buffer), visionPipe) != NULL) {
        try {
            std::string str(buffer);
            // Quick cleanup of whitespace/newlines
            str.erase(std::remove_if(str.begin(), str.end(), ::isspace), str.end());

            if (str.empty()) return;

            int gesture = std::stoi(str);

            // Update your Game State here instead of just printing
            switch(gesture) {
                case 1: std::cout << "C++ Received: FORWARD" << std::endl; break;
                case 2: std::cout << "C++ Received: BACKWARD" << std::endl; break;
                case 3: std::cout << "C++ Received: LEFT" << std::endl; break;
                case 4: std::cout << "C++ Received: RIGHT" << std::endl; break;
                case 5: std::cout << "C++ Received: NONE" << std::endl; break;
                default: std::cout << "C++ Received: UNKNOWN" << std::endl; break;
            }
        } catch (const std::exception& e) {
            log_error("Error parsing vision input: " + std::string(e.what()));
        }
    }
}

void VisionSystem::cleanupVisionSystem() {
    if (visionPipe) {
        pclose(visionPipe);
        visionPipe = nullptr;
    }
}