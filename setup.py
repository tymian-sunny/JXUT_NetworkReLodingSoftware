from cx_Freeze import setup, Executable

build_options = {
    "packages": [],
    "excludes": [],
    "include_files": [("config.json")],  # 将 data.json 包含到输出目录
    "build_exe": "dist"
}

# 这里指定脚本的名称和要生成的可执行文件的名称
setup(
    name="NetworkReLoding",
    version="1.0",
    description="description",
options={"build_exe": build_options},
    executables=[Executable("NetworkReLoding.py")]
)
