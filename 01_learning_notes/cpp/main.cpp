#include <iostream>
using namespace std;

// 传值：复制一份进去
void 传值(int x) {
    x = 999;  // 改的是副本
    cout << "函数内部 传值: " << x << endl;
}

// 传引用：直接改原物
void 传引用(int &x) {  // 注意这个 &
    x = 999;  // 改的是原物
    cout << "函数内部 传引用: " << x << endl;
}

int main() {
    int a = 10;
    int b = 10;
    
    cout << "调用前 a = " << a << endl;
    传值(a);
    cout << "调用后 a = " << a << " ← 没变！" << endl << endl;
    
    cout << "调用前 b = " << b << endl;
    传引用(b);
    cout << "调用后 b = " << b << " ← 变了！" << endl;
    
    return 0;
}