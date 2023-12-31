# 又拍云存储-s3 支持

## 接口说明

### 获取服务列表

list_buckets

参数
| 参数 | 必选 | 类型 | 说明 |
| ---- | ---- | ---- | ---- |
| None | None | None | None |

### 获取目录列表

list_folders

参数
| 参数 | 必选 | 类型 | 说明 |
| ------ | ---- | ---- | -------------- |
| bucket | 是 | str | 又拍云服务名称 |

### 获取目录文件列表

list_files

参数
| 参数 | 必选 | 类型 | 说明 |
| ------ | ---- | ---- | -------------- |
| bucket | 是 | str | 又拍云服务名称 |
| folder | 是 | str | 又拍云服务目录 |

### 删除文件

delete_file

参数
| 参数 | 必选 | 类型 | 说明 |
| ------ | ---- | ---- | -------------- |
| bucket | 是 | str | 又拍云服务名称 |
| file | 是 | str | 又拍云文件名称 |

### 删除目录

delete_folder

参数
| 参数 | 必选 | 类型 | 说明 |
| ------ | ---- | ---- | -------------- |
| bucket | 是 | str | 又拍云服务名称 |
| folder | 是 | str | 又拍云服务目录 |

### 创建目录

create_folder

参数
| 参数 | 必选 | 类型 | 说明 |
| ------ | ---- | ---- | -------------- |
| bucket | 是 | str | 又拍云服务名称 |
| folder | 是 | str | 又拍云服务目录 |

### 上传文件

upload_file

参数
| 参数 | 必选 | 类型 | 说明 |
| ----------- | ---- | ---- | ------------------------------------------------------------ |
| bucket | 是 | str | 又拍云服务名称 |
| file_path | 是 | str | 本地文件路径 |
| object_name | 否 | str | 如果 object 为 None，则又拍云的存储文件名称为 file_path 文件名，并且存放位置是根目录 |

### 获取文件信息

get_file_info

参数
| 参数 | 必选 | 类型 | 说明 |
| ----------- | ---- | ---- | ------------------ |
| bucket | 是 | str | 又拍云服务名称 |
| object_name | 是 | str | 又拍云存储文件名称 |

### 获取随机文件

get_random_file

参数
| 参数 | 必选 | 类型 | 说明 |
| ------ | ---- | ---- | -------------- |
| bucket | 是 | str | 又拍云服务名称 |
| folder | 是 | str | 又拍云服务目录 |

### 下载文件

download_file

参数
| 参数 | 必选 | 类型 | 说明 |
| ----------- | ---- | ---- | ------------------------ |
| bucket | 是 | str | 又拍云服务名称 |
| object_name | 是 | str | 又拍云存储文件名称 |
| file_path | 否 | str | 本地存储的文件路径及名称 |

### 生成预签名 URL

generate_presigned_url

| 参数        | 必选 | 类型 | 说明                                                    |
| ----------- | ---- | ---- | ------------------------------------------------------- |
| bucket      | 是   | str  | 又拍云服务名称                                          |
| object_name | 是   | str  | 又拍云存储文件名称                                      |
| expiration  | 否   | int  | 过期时间，单位秒，最大不能超过 604800，默认不填 3600 秒 |

## 代码示例

```python
from upyuns3client import UpYunS3Client
ak = "xxxxx"
sk = "xxxxx"
client = UpYunS3Client(ak, sk)
client.generate_presigned_url(
    bucket="test-bucket", object_name="test.png", expiration=3600
)
```
