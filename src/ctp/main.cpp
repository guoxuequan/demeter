#include "include/ThostFtdcMdApi.h"
//#include "MdSpi.h"
#include <iostream>

// UserApi对象
CThostFtdcMdApi* pUserApi;

// 配置参数
char FRONT_ADDR[] = "tcp://180.168.146.187:10111";		// 前置地址
TThostFtdcBrokerIDType	BROKER_ID = "9999";				// 经纪公司代码
TThostFtdcInvestorIDType INVESTOR_ID = "143407";			// 投资者代码
TThostFtdcPasswordType  PASSWORD = "19870621";			// 用户密码
const char *ppInstrumentID[] = {"rb1910"};			// 行情订阅列表
int iInstrumentID = 2;									// 行情订阅数量

// 请求编号
int iRequestID = 0;

int main(void)
{
	// 初始化UserApi
	pUserApi = CThostFtdcMdApi::CreateFtdcMdApi();
	//CThostFtdcMdSpi* pUserSpi = new CMdSpi();
        /*
	pUserApi->RegisterSpi(pUserSpi);						// 注册事件类
	pUserApi->RegisterFront(FRONT_ADDR);					// connect
	pUserApi->Init();

	pUserApi->Join();
//	pUserApi->Release();
        */
    std::cout<<"hello quant!"<<std::endl;
    return 0;
}
