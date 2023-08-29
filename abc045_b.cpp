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

int main() {
    
    string a, b, c;
    
    int a_count = 0, b_count = 0, c_count = 0;
    int turn = 0;
    
    cin >> a >> b >> c;
    
    while (true) {
        if (turn == 0) {
            if (a[a_count] == 'a') {
                turn = 0;
            } else if (a[a_count] == 'b') {
                turn = 1;
            } else if (a[a_count] == 'c') {
                turn = 2;
            }
            a_count = a_count + 1;
            
            if (a_count > a.size()) {
                cout << "A \n";
                break;
            }
            
        } else if (turn == 1) {
            if (b[b_count] == 'a') {
                turn = 0;
            } else if (b[b_count] == 'b') {
                turn = 1;
            } else if (b[b_count] == 'c') {
                turn = 2;
            }
            b_count = b_count + 1;
            
            if (b_count > b.size()) {
                cout << "B \n";
                break;
            }
        } else if (turn == 2) {
            if (c[c_count] == 'a') {
                turn = 0;
            } else if (c[c_count] == 'b') {
                turn = 1;
            } else if (c[c_count] == 'c') {
                turn = 2;
            }
            c_count = c_count + 1;
            
            if (c_count > c.size()) {
                cout << "C \n";
                break;
            }
            
        }
    }

}
