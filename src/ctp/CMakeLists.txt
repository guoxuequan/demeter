#cmake最低版本需求，不加入此行会受到警告信息
CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(md) #项目名称
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/include)
#把当前目录(.)下所有源代码文件和头文件加入变量SRC_LIST
AUX_SOURCE_DIRECTORY(. SRC_LIST)
#set extern libraries  
SET(LIBRARIES ${PROJECT_SOURCE_DIR}/lib/libthostmduserapi.so) 
#生成应用程序 hello (在windows下会自动生成hello.exe)
ADD_EXECUTABLE(md ${SRC_LIST})
TARGET_LINK_LIBRARIES(md ${LIBRARIES}) #添加libmxnet.so
