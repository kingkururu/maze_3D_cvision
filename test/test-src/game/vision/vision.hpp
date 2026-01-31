#include <iostream>
#include <cstdio>
#include <memory>
#include <stdexcept>
#include <string>
#include <fcntl.h>
#include <unistd.h>

#include "../globals/globals.hpp"

namespace VisionSystem {
    inline FILE* visionPipe = nullptr;

    void initializeVisionSystem();
    void getVisionInput();
    void cleanupVisionSystem();
}