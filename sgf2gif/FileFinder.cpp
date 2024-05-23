#include "FileFinder.h"

namespace sgf_finder {


    bool is_sgf_file(const fs::path& path, const std::string& extension) {
        return path.extension() == extension;
    }

    std::vector<fs::path> find_sgf_files_in_directory(const fs::path& directory, const std::string& extension) {
        std::vector<fs::path> sgf_files;
        for (const auto& entry : fs::recursive_directory_iterator(directory)) {
            if (is_sgf_file(entry.path(), extension)) {
                sgf_files.push_back(entry.path());
            }
        }
        return sgf_files;
    }

    std::vector<fs::path> process_input_arguments(const std::vector<std::string>& arguments, const std::string& extension) {
        std::vector<fs::path> sgf_files;
        for (const auto& arg : arguments) {
            fs::path path_to_check(arg);
            if (fs::is_regular_file(path_to_check)) {
                if (is_sgf_file(path_to_check, extension)) {
                    sgf_files.push_back(path_to_check);
                }
            } else if (fs::is_directory(path_to_check)) {
                auto dir_files = find_sgf_files_in_directory(path_to_check, extension);
                sgf_files.insert(sgf_files.end(), dir_files.begin(), dir_files.end());
            } else {
                std::cerr << "Warning: " << path_to_check << " is not a file or directory. Skipping." << std::endl;
            }
        }
        return sgf_files;
    }

} // namespace sgf_finder
