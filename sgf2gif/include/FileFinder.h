#ifndef FILEFINDER_H  
#define FILEFINDER_H  
  
#include <vector>  
#include <string>  
#include <experimental/filesystem>  
#include <iostream>



#include <Windows.h>
#include <tchar.h>
#include <vector>
#include <string>
#include <iostream> 
#include "StringWString.h"

#pragma warning(disable:4996)

namespace fs = std::experimental::filesystem;

namespace sgf_finder {  
  
    // 检查路径是否为SGF文件  
    bool is_sgf_file(const fs::path& path, const std::string& extension);  
  
    // 在文件夹中递归查找SGF文件  
    std::vector<fs::path> find_sgf_files_in_directory(const fs::path& directory, const std::string& extension);  
  
    // 处理外部输入的参数，可能是文件或文件夹  
    std::vector<fs::path> process_input_arguments(const std::vector<std::string>& arguments, const std::string& extension);  
  
} // namespace sgf_finder  
  
#endif // SGF_FINDER_MODULE_H