# 注意

> 为什么在static目录下新建了`polls`再新建`style.css`，而不是直接把`style.css`放在`polls/`下

Django 只会使用第一个找到的静态文件。如果你在 其它 应用中有一个相同名字的静态文件，Django 将无法区分它们。我们需要指引 Django 选择正确的静态文件，而最好的方式就是把它们放入各自的 命名空间 。也就是把这些静态文件放入 另一个 与应用名相同的目录中。