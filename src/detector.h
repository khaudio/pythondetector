#ifndef DETECTOR_H
#define DETECTOR_H

#include <array>
#include <memory>
#include <stdexcept>
#include <string>
#include <stdlib.h>
#include <vector>

class Detector
{
    public:
        static bool check(const char*, const char*);
        static std::string execute(const char*);
        static std::vector<std::string> split(std::string, const char);
        static std::array<int, 3> convertVersion(std::string);
        static bool minimumVersionInstalled(
                std::array<int, 3>, std::array<int, 3>
            );
};

#endif