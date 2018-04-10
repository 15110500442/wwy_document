#``Django后端开发前奏：``
#配置python虚拟环境
（豆瓣源https://pypi.douban.com/simple/ ）
#步骤1：pip安装virtualenv和virtualenvwrapper:
```python
1.pip3 install virtualenv   
2.pip3 install virtualenvwrapper
```
##virtualenv的优点：
###1、使不同应用开发环境独立
###2、环境升级不影响其他应用，也不会影响全局的python环境
###3、它可以防止系统中出现包管理混乱和版本的冲突
##virtualenvwrapper：
###理解为管理virtualenv的配套工具
##步骤2：把virtualenv和virtualenvwrapper配置到我们终端shell配置文件里面
```bash
export WORKON_HOME=/home/bc/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh 
```  
##步骤3：使我们的配置生效 source .zshrc   (或者 source .bashrc)
#``Django开发进行时：``
#步骤1：创建虚拟机环境 mkvirtualenv + 虚拟环境的名字
#步骤2：配置django开发环境：
```python
1、pip install django==1.8.2
2、pip install pymysql
```
#步骤3：创建项目 
```python
django-admin startproject + 项目名称
```
#步骤4：创建应用 
```python
python manage.py startapp +应用名称
```
#步骤5：打开项目 两种方案：
##1、命令行 charm+项目名称
##2、IDE 里面的open选项
#步骤6：在项目的setting设置里面有一个INSTALLED_APPS把我们的应用添加进去
#步骤7：配置数据库（MySQL）
```python
import pymysql
pymysql.install_as_MySQLdb()
```
#步骤8：设置模型之后我们需要有两个步骤：
##1、生成迁移文件 python manage.py makemigrations
##2、执行迁移（迁移生成表）python manage.py migrate
``注意``：
>pymysql 是Python2Python3通用
>mysqldb Python3是不能够用
>mysqlclient
>https://www.cnblogs.com/roystime/p/6920489.html

