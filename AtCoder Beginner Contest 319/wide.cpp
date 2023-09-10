#ifndef _GLIBCXX_NO_ASSERT
 #include <cassert>
 #endif
 #include <cctype>
 #include <cerrno>
 #include <cfloat>
 #include <ciso646>
 #include <climits>
 #include <clocale>
 #include <cmath>
 #include <csetjmp>
 #include <csignal>
 #include <cstdarg>
 #include <cstddef>
 #include <cstdio>
 #include <cstdlib>
 #include <cstring>
 #include <ctime>
 
 #if __cplusplus >= 201103L
 #include <ccomplex>
 #include <cfenv>
 #include <cinttypes>
 #include <cstdbool>
 #include <cstdint>
 #include <ctgmath>
 #include <cwchar>
 #include <cwctype>
 #endif
 
 // C++
 #include <algorithm>
 #include <bitset>
 #include <complex>
 #include <deque>
 #include <exception>
 #include <fstream>
 #include <functional>
 #include <iomanip>
 #include <ios>
 #include <iosfwd>
 #include <iostream>
 #include <istream>
 #include <iterator>
 #include <limits>
 #include <list>
 #include <locale>
 #include <map>
 #include <memory>
 #include <new>
 #include <numeric>
 #include <ostream>
 #include <queue>
 #include <set>
 #include <sstream>
 #include <stack>
 #include <stdexcept>
 #include <streambuf>
 #include <string>
 #include <typeinfo>
 #include <utility>
 #include <valarray>
 #include <vector>
 
 #if __cplusplus >= 201103L
 #include <array>
 #include <atomic>
 #include <chrono>
 #include <condition_variable>
 #include <forward_list>
 #include <future>
 #include <initializer_list>
 #include <mutex>
 #include <random>
 #include <ratio>
 #include <regex>
 #include <scoped_allocator>
 #include <system_error>
 #include <thread>
 #include <tuple>
 #include <typeindex>
 #include <type_traits>
 #include <unordered_map>
 #include <unordered_set>
 #endif

using namespace std;

// there's something wrong with this, I'll fix it later

int main() {
    long long int n, m;
    cin >> n >> m;
    long long int l[n];
    long long int tot = 0;
    
    for (int i = 0; i < n; i++) {
        cin >> l[i];
        tot = l[i] + tot + 1;
    }
    
    long long int baseVal = (tot - tot % m)/m;
    
    long long int maxWidth = 0;
    
    for (int i = 0; i < m; i++) {
        long long int lineSum = 0;
        long long iter = 0;
        while (lineSum < baseVal) {
            lineSum = lineSum + l[iter] + 1;
            iter++;
        }
        if (lineSum > maxWidth)  {
            maxWidth = lineSum;
        }
    }
    
    cout << maxWidth - 1 << "\n";
    
    
    
}
