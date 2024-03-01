# DNSPOD_Domain_Log

HTTP请求方式：

POST
请求参数：
参数名	是否必须	参数描述
公共参数	是	详见：公共参数
domain_id 或 domain	是	分别对应域名ID和域名, 提交其中一个即可
offset	否	记录开始的偏移，第一条记录为 0，依次类推，默认为0
length	否	共要获取的日志条数，比如获取20条，则为20，默认为500条，单次最多获取500条
![image](https://github.com/hanyan007/DNSPOD_Domain_Log/assets/14324188/2b70a3c6-5e70-4fb6-866e-e7620d308199)


响应代码：
共通返回
-15 域名已被封禁
6 域名ID错误
7 非域名所有者
8 域名无效

![image](https://github.com/hanyan007/DNSPOD_Domain_Log/assets/14324188/78da8984-26f5-4699-bfff-25efdb5e002e)


![images](https://github.com/hanyan007/DNSPOD_Domain_Log/blob/master/dns.png)

参考：https://docs.dnspod.cn/api/domain-log/
