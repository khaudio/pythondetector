#include "detector.h"
#include <iostream>

std::string Detector::execute(const char* command)
{
    std::array<char, 64> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(
            popen(command, "r"), pclose
        );
    if (!pipe)
    {
        throw std::runtime_error("Could not open");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr)
    {
        result += buffer.data();
    }
    return result;
}

std::vector<std::string> Detector::split(
        std::string incoming, const char delimiter
    )
{
    std::vector<std::string> words;
    std::string buffer;
    const char* chars = incoming.c_str();
    int last = incoming.size() - 1;
    for (int i = 0; i < incoming.size(); i++)
    {
        if (i == last)
        {
            buffer += chars[i];
            words.push_back(buffer);
            break;
        }
        else if (chars[i] == delimiter)
        {
            words.push_back(buffer);
            buffer.clear();
        }
        else
        {
            buffer += chars[i];
        }
    }
    return words;
}

std::array<int, 3> Detector::convertVersion(std::string delimited)
{
    std::vector<std::string> versionStr = split(delimited, '.');
    std::array<int, 3> version;
    if (versionStr.size() < 3)
    {
        throw std::runtime_error("Not enough version information");
    }
    for (int i = 0; i < 3; i++)
    {
        version[i] = atoi(versionStr[i].c_str());
    }
    return version;
}

bool Detector::minimumVersionInstalled(
        std::array<int, 3> current, std::array<int, 3> required
    )
{
    bool skip = false;
    for (int i = 0; i < 3; i++)
    {
        if (current[i] > required[i])
        {
            skip = true;
        }
        else if (!skip && (required[i] > current[i]))
        {
            return false;
        }
    }
    return true;
}

bool Detector::check(const char* versionString, const char* installed)
{
    std::vector<std::string> words = Detector::split(
            Detector::execute(versionString), ' '
        );
    std::array<int, 3> current = Detector::convertVersion(words[1]);
    std::array<int, 3> required = Detector::convertVersion(
            std::string(installed)
        );
    return Detector::minimumVersionInstalled(current, required);
}
