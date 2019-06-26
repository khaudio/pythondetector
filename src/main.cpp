#include "detector.h"
#include <iostream>

int main(int argc, const char** argv)
{
    bool isCurrent;
    std::array<const char*, 2> versions = {"python -V", "python3 -V"};
    for (auto& version: versions)
    {
        bool isCurrent = Detector::check(version, argv[1]);
        std::cout << (
                isCurrent ? "minimum version installed"
                : "minimum version not installed"
            ) << std::endl;
        if (isCurrent)
        {
            return !isCurrent;
        }
    }
    return !isCurrent;
}
