# gjzWeb
甘井子的网站

前端和后端我全放一起管理了
前端是Nuxt3
后端是Django

当然，以下是结合 `Makefile` 的更新后的 `README.md` 示例：

```markdown
# 项目名称

## 项目简介

这是一个结合 Nuxt3 前端和 Django 后端的项目。

## 安装步骤

1. **安装后端依赖**：
   在项目根目录下运行：
   ```bash
   make install-backend
   ```

2. **安装前端依赖**：
   在项目根目录下运行：
   ```bash
   make install-frontend
   ```

## 启动项目

### 使用 Makefile 启动

在项目根目录下运行以下命令启动后端服务器：

```bash
make backend
```

启动前端开发服务器：

```bash
make frontend
```

### 手动启动后端

如果 `make` 命令无法正常工作，可以手动启动：

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

## 访问项目

打开浏览器，访问 [http://localhost:8000](http://localhost:8000) 查看项目。

```



