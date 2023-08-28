f = open("cTemplate.cpp", "w")

f.write("#ifndef _GLIBCXX_NO_ASSERT\n \
#include <cassert>\n \
#endif\n \
#include <cctype>\n \
#include <cerrno>\n \
#include <cfloat>\n \
#include <ciso646>\n \
#include <climits>\n \
#include <clocale>\n \
#include <cmath>\n \
#include <csetjmp>\n \
#include <csignal>\n \
#include <cstdarg>\n \
#include <cstddef>\n \
#include <cstdio>\n \
#include <cstdlib>\n \
#include <cstring>\n \
#include <ctime>\n \
\n \
#if __cplusplus >= 201103L\n \
#include <ccomplex>\n \
#include <cfenv>\n \
#include <cinttypes>\n \
#include <cstdbool>\n \
#include <cstdint>\n \
#include <ctgmath>\n \
#include <cwchar>\n \
#include <cwctype>\n \
#endif\n \
\n \
// C++\n \
#include <algorithm>\n \
#include <bitset>\n \
#include <complex>\n \
#include <deque>\n \
#include <exception>\n \
#include <fstream>\n \
#include <functional>\n \
#include <iomanip>\n \
#include <ios>\n \
#include <iosfwd>\n \
#include <iostream>\n \
#include <istream>\n \
#include <iterator>\n \
#include <limits>\n \
#include <list>\n \
#include <locale>\n \
#include <map>\n \
#include <memory>\n \
#include <new>\n \
#include <numeric>\n \
#include <ostream>\n \
#include <queue>\n \
#include <set>\n \
#include <sstream>\n \
#include <stack>\n \
#include <stdexcept>\n \
#include <streambuf>\n \
#include <string>\n \
#include <typeinfo>\n \
#include <utility>\n \
#include <valarray>\n \
#include <vector>\n \
\n \
#if __cplusplus >= 201103L\n \
#include <array>\n \
#include <atomic>\n \
#include <chrono>\n \
#include <condition_variable>\n \
#include <forward_list>\n \
#include <future>\n \
#include <initializer_list>\n \
#include <mutex>\n \
#include <random>\n \
#include <ratio>\n \
#include <regex>\n \
#include <scoped_allocator>\n \
#include <system_error>\n \
#include <thread>\n \
#include <tuple>\n \
#include <typeindex>\n \
#include <type_traits>\n \
#include <unordered_map>\n \
#include <unordered_set>\n \
#endif\n\n")

f.write("using namespace std;\n\n")

f.write("int main() {\n\n")

f.write("}")

f.close()

