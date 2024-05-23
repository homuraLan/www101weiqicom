#include <Windows.h>
#include <tchar.h>
#include <vector>
#include <string>
#include <iostream> 
#include <tchar.h>
#include "StringWString.h"

#pragma warning(disable:4996)
using namespace std;
 
std::string WStringToString(const std::wstring& ws)
{
    std::string strLocale = setlocale(LC_ALL, "");
    const wchar_t* wchSrc = ws.c_str();
    size_t nDestSize = wcstombs(NULL, wchSrc, 0) + 1;
    char *chDest = new char[nDestSize];
    memset(chDest, 0, nDestSize);
    wcstombs(chDest, wchSrc, nDestSize);
    std::string strResult = chDest;
    delete[]chDest;
    setlocale(LC_ALL, strLocale.c_str());
    return strResult;
}
 
std::wstring StringToWString(const std::string &str)
{
    std::wstring wContext = L"";
    int len = MultiByteToWideChar(CP_ACP, 0, str.c_str(), str.size(), NULL, 0);
    WCHAR* buffer = new WCHAR[len + 1];
    MultiByteToWideChar(CP_ACP, 0, str.c_str(), str.size(), buffer, len);
    buffer[len] = '\0';
    wContext.append(buffer);
    delete[] buffer;
 
    return wContext;
}



FILE* OpenFile(const std::wstring& filePath, const char* mode) {
    // 将宽字符路径转换为多字节字符路径
    std::wstring_convert<std::codecvt_utf8<wchar_t>, wchar_t> converter;
    std::string narrowPath = converter.to_bytes(filePath);

    // 使用多字节字符路径打开文件
    FILE* file = std::fopen(narrowPath.c_str(), mode);
    if (!file) {
        std::cerr << "Failed to open file!" << std::endl;
    }
    return file;
}

std::vector<std::string> SpiteStringCharacter(std::string context)
{
    std::vector<std::string> res;
 
    std::wstring wContext = StringToWString(context);
    for (int i = 0; i < wContext.length(); ++i)
    {
        std::wstring tmp = wContext.substr(i, 1);
        res.push_back(WStringToString(tmp));
    }
 
    return res;
}
 
bool IsChineseChar(std::wstring value)
{
    if (value.size() == 1)
    {
        unsigned char* pCh = (unsigned char*)&value[0];
        if (((*pCh >= 0) && (*pCh <= 0xff)) && (*(pCh + 1) >= 0x4e && *(pCh + 1) <= 0x9f))
        {
            return true;
        }
    }
 
    return false;
}
 
int GetStringChineseCharCount(std::string context)
{
    std::wstring wContext = StringToWString(context);
 
    int chineseCharCount = 0;
    for (int i = 0; i < wContext.length(); ++i)
    {
        if (IsChineseChar(wContext.substr(i, 1)))
        {
            ++chineseCharCount;
        }
    }
 
    return chineseCharCount;
}
 
// int main()
// {
//     std::string value = "你好";
//     std::wstring Wvalue = StringToWString(value);
//     //int count = GetStringChineseCharCount(value);
//     std::wcout << Wvalue;
 
//     return 0;
// }