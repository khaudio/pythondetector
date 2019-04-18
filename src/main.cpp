#include "detector.h"
#include <iostream>

int main(int argc, const char** argv)
{
    bool isCurrent = Detector::check("python -V", argv[1]);
    std::cout << (isCurrent ? "minimum version installed" : "minimum version not installed") << std::endl;
    return !isCurrent;
}
