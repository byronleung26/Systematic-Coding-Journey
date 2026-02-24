# 项目概述
1. 项目名称  
   校园信息管理系统（campus-information-management-system）。
2. 开发环境
 - 操作系统：WSL（Ubuntu）
 - 开发工具：VS Code
 - 语言版本：Python 3.13.12
 - 版本控制：Git

# v1.0版本设计
1. 核心目标：实现基本的注册、登录和信息管理功能
2. 主要功能：
- [ ] 管理员账号生成（用户名查重、密码长度检查）
- [ ] 创建教师/学生账号
- [ ] 用户登录（三次机会）
- [ ] 课程管理（待开发）
- [ ] 成绩管理（待开发）
3. 技术实现
 - 文件存储、函数模块化

# 业务流程图
## 主业务流程
```mermaid
graph LR

Start(开始) -->|已注册| L{登录}
Start(开始) -->|未注册| R((注册)) --> L

L -->|成功| C{身份识别}

C -->|管理员| 管理员菜单 --> M[管理员功能]
C -->|教师| 教师菜单 --> T[教师功能]
C -->|学生| 学生菜单 --> S[学生功能]
```
## 管理员注册流程
```mermaid
graph LR

Start([进入注册]) --> 追加打开文件 --> InputUser[输入用户名] --> Checkuser{合规检查}

Checkuser -->|已存在| Error1[提示：用户名被占用] --> InputUser
Checkuser -->|不合规| Error2[提示：用户名不合规] --> InputUser

Checkuser -->|合规| InputPwd[输入密码] --> CheckPw{长度≥6?}

CheckPw -->|否| Error3[提示：密码至少6位] --> InputPwd
CheckPw -->|是| SaveToFile[保存用户名和密码到user.txt] --> Success([注册成功])

```
## 登录流程
```mermaid
graph LR

Start(进入登录) --> User[输入用户名] --> PW[输入密码]--> 读文件 --> Check{检查}

Check -->|失败| Count[次数+1]
Count -->|次数<3| User
Count -->|次数=3| Lock[锁定退出]

Check -->|成功| Role{判断身份}

Role -->|管理员| Admin[管理员菜单]
Role -->|教师| Teacher[教师菜单]
Role -->|学生| Student[学生菜单]
```
## 管理员功能
- 创建教师/学生账号
- 删除/修改教师/学生账号信息
- 查看所有账号
- 重置密码
## 教师功能
- 增加课程
- 录入成绩
- 修改密码
## 学生功能
- 查看成绩、排名、绩点
- 修改密码
## 内置功能
- 成绩排序
- 绩点计算
