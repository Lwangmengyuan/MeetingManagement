--common: 公共类
       --base_page.py: 公共page页类，所有的pages都可以继承该类，使用它的方法
       --setting.py: 配置文件类，所有的配置信息都写在该类中
       --deal_excel.py：Excel操作类，Excel读写操作都写在该类中
       --random_data.py：根据时间按一定规则生成用户信息用于注册和新增
       --log.py: 日志记录方法
--testcases: 测试用例集
       --test_login.py: 登录测试用例
       --test_register.py: 注册测试用例
       --test_.......py: 其他测试用例
--data: 测试用例存放位置
       --case.xlsx: 测试用例(待补充测试数据)
--log: 日志存放位置，包含.log文件和截图文件
--pages: 页面操作封装类
       --login_page.py: 登录界面的操作类
       --register_page.py: 注册用户界面的操作类
       --.............py: 其他界面的操作类
--conftest.py: 测试夹具，前置后置方法
--run.py: 运行类