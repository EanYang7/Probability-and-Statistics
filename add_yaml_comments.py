# 批量给md文件顶部添加font matter的yaml语句
import os


def add_yaml_comments(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    # # 从无到有添加yaml语句
                    # if not content.startswith("---"):
                    #     with open(filepath, "w", encoding="utf-8") as f:
                    #         f.write("---\ncomments: true\n---\n" + content)
                    # 在已有yaml语句的情况下添加其他属性
                    if content.startswith("---"):
                        # 查找现有的YAML语句位置
                        yaml_end = content.find("\n---\n", 4)
                        if yaml_end != -1:
                            # 添加新的属性
                            new_content = (
                                content[:yaml_end]
                                + "\ncomments: true\n"
                                + content[yaml_end:]
                            )
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(new_content)


# 用法示例
add_yaml_comments(".")  # 在当前文件夹及其子文件夹中查找并修改所有md文件
