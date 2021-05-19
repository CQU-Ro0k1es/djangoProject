# 1. 基础必要操作

## 1.1 创建项目

第一次使用 Django 的话，你需要一些初始化设置。也就是说，你需要用一些自动生成的代码配置一个 Django project —— 即一个 Django 项目实例需要的设置项集合，包括数据库配置、Django 配置和应用程序配置。

```shell
django-admin startproject mysite
```

如果使用Pycharm的话，会自动帮你创建，无需手动创建

---

## 1.2 创建应用

```shell
py manage.py startapp 应用名
```

>项目和应用有什么区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者小型的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

--

## 1.3 数据库配置

```shell
py manage.py migrate
```

## 1.4 模型迁移

迁移是非常强大的功能，它能让你在开发过程中持续的改变数据库结构而不需要重新删除和创建表 - 它专注于使数据库平滑升级而不会丢失数据。

```shell
 py manage.py makemigrations polls
```

```shell
py manage.py migrate
```

---

## 1.5 创建超级账户

```shell
 py manage.py createsuperuser
```

键入你想要使用的用户名 -> 输入想要使用的邮件地址 -> 输入密码


---

