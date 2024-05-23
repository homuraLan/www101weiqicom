#ifndef STRING_WSTRING_H
#define STRING_WSTRING_H

#include <Windows.h>
#include <tchar.h>
#include <vector>
#include <string>
#include <cstdio>
#include <cwchar>
#include <locale>
#include <codecvt>

#pragma warning(disable:4996)

std::string WStringToString(const std::wstring& ws);
std::wstring StringToWString(const std::string& str);
std::vector<std::string> SpiteStringCharacter(std::string context);
bool IsChineseChar(std::wstring value);
int GetStringChineseCharCount(std::string context);
FILE* OpenFile(const std::wstring& filePath, const char* mode);

#endif // STRING_HELPER_H
