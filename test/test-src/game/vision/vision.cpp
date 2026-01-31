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
                case 1: 
                    FlagSystem::flagEvents.cv_wPressed = true; 
                    break;
                case 2: 
                    FlagSystem::flagEvents.cv_sPressed = true; 
                    break;
                case 3:
                    FlagSystem::flagEvents.cv_aPressed = true; 
                    break;
                case 4: 
                    FlagSystem::flagEvents.cv_dPressed = true; 
                    break;
                case 5:                   
                    FlagSystem::flagEvents.cv_allDirectionKeyReleased();
                    break;
                default: 
                    FlagSystem::flagEvents.cv_allDirectionKeyReleased();
                    break;
            }

            //  std::cout << "Current CV Flags - W: " << FlagSystem::flagEvents.cv_wPressed
            //               << ", A: " << FlagSystem::flagEvents.cv_aPressed
            //               << ", S: " << FlagSystem::flagEvents.cv_sPressed
            //               << ", D: " << FlagSystem::flagEvents.cv_dPressed << std::endl;

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