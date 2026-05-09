# 1 C语言概述
## 1.1 C语言的历史
1. 起源  
- 贝尔实验室的Dennis Ritchie，用于编写Unix操作系统  
- B语言——>NB——>C语言  
2. 标准化  
- K & R  
- C89或C90  
- C99  
- C11  
- C18  
3. 基于C的语言  
- C++：包括了所有C特性，但增加了类和其他特性以支持面向对象编程  
- Java：基于C++，因此也继承了C的许多特性  
- C#：由C++和Java发展起来的一种较新的语言  
- Perl：最初是一种非常简单的脚本语言，在发展过程中采用了C的许多特性  
## 1.2 C语言的优缺点
1. C语言是一种底层语言，C语言是一种小型语言，C语言是一种包容性语言  
2. 优点  
- 高效  
- 可移植  
- 功能强大  
- 灵活  
- 标准库  
- 与UNIX的集成  
3. 缺点  
- C程序更容易隐藏错误  
- C程序可能会难以理解  
- C程序可能会难以修改  
4. 高效的使用C语言
- Andrew Koenig的《C陷阱与缺陷》  
- 使用软件工具使程序更加可靠，lint/调试工具  
- 利用现有的代码库  
- 编码规范  
- 避免“投机取巧“和过度复杂的代码  
- 紧贴标准  

# 2 C语言基本概念
## 2.1 一个简单的C程序
1. 显示双关语  
    ``` c
    #include <stdio.h>  //  C语言标准输入/输出库的相关信息，必不可少
    int main(void)  //  程序的可执行代码都在main主函数中
    {
    printf("To C, or not to C: that is the question.\n");  //  用来显示期望信息的。printf函数来自标准输入/输出库，可以产生完美的格式化输出。代码\n告诉printf函数执行完消息显示后要进行换行操作
    return 0;  //  表明程序终止时会向操作系统返回值 0
    } 
    ```  
2. 编译和链接    
- 预处理，预处理器（preprocessor），执行以#开头的命令，纯文本替换，输出：.i文件  
- 编译，编译器（compiler），输出：.s 汇编代码文件  
- 汇编，汇编器，把汇编指令翻译成机器码（CPU真正能执行的0和1），输出：.o 目标文件  
- 链接，链接器（linker），符号解析、重定位、合并段，输出：可执行文件  
- `% gcc pun.c`  
3. 集成开发环境  
集成开发环境（integrated development environment, IDE）  
## 2.2 预处理指令（Preprocessor Directive）
## 2.3 函数
1. 程序员编写的函数
2. 库函数（library function）
3. 所有程序都有且只有一个 main 函数
- int，整数
- void，没有参数
- return，函数终止，指定返回值
4. 函数调用（function call）
## 2.4 语句
1. 每条语句以;结尾
2. 字面串（string literal）
3. 换行符\n
## 2.5 注释（comment）
1. `/* This is a comment */` 
2. //，C99，行末自动终止
## 2.6 变量（variable）
1. 类型（type）
2. 声明
- `类型 变量名`
- 每一条完整的声明都要以分号结尾
- 把声明放置在语句之前
- 建议在声明和语句之间留出一个空行
3. 赋值（assignment）
- 常量（constant）
- 把一个包含小数点的常量赋值给 float 型变量时，最好在该常量后面加一个字母 f，`profit = 2.54f`
- `printf("Height: %d\n", height);`，`printf("Profit: $%.2f\n", profit);`，`printf("Height: %d Length: %d\n", height, length);`
4. 初始化
- 未初始化的（uninitialized）
- `int height = 8;`
- 初始化器（initializer）




