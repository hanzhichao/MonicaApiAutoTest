# Monica接口自动化测试项目
分层接口测试框架，基于Requests + Pytest + Allure。
> [Monica接口文档参考](https://www.monicahq.com/api)

## 特性
- 支持切换测试环境
- 支持数据库断言
- 支持并发测试

## 框架结构


## 使用方法
1. 部署Monica（测试环境）
基于Docker的安装方式如下，其他安装安装方式参考：
https://github.com/monicahq/monica/blob/main/docs/installation/readme.md
（1）安装并启动Docker；
（2）在命令行运行以下命令；
```bash
$ mysqlCid="$(docker run -d \
 -e MYSQL_RANDOM_ROOT_PASSWORD=true \
 -e MYSQL_DATABASE=monica \
 -e MYSQL_USER=homestead \
 -e MYSQL_PASSWORD=secret \
 -p 3306:3306 mysql:5.7)"
docker run -d --link "$mysqlCid":mysql -e DB_HOST=mysql -p 8080:80 monica
```
注意：需要当前主机8080或3306端口已被占用，可以修改上面命令中映射的端口号。
（3）等待1-3分钟后，打开浏览器访问http://localhost:8080，如图8.3所示：

2. 配置当前环境base_url、token、及数据库信息
3. 编写接口测试用例

## 运行方法


## 目录说明
