# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2023/07/21 10:03:53
@Author  :   Evan
@Version :   1.0
@Desc    :   None
"""

import boto3
from botocore.client import Config
import random

access_key = 'c60b18f3f3aa4bafb522495e82083e9e'
secret_key = '45a3b3032f0fb4a14847985f68581170'
endpoint = 'https://s3.api.upyun.com'


import boto3
from botocore.client import Config


class UpyunS3Client:
    def __init__(self, access_key, secret_key):
        self.ak = access_key
        self.sk = secret_key
        self.endpoint = 'https://s3.api.upyun.com'
        self.s3 = boto3.client(
            's3',
            endpoint_url=self.endpoint,
            aws_access_key_id=self.ak,
            aws_secret_access_key=self.sk,
            config=Config(signature_version='s3v4'),
        )

    def list_buckets(self):
        # 列出所有的bucket：
        buckets = []
        response = self.s3.list_buckets()
        for bucket in response['Buckets']:
            buckets.append(bucket["Name"])
        return buckets

    def list_folders(self, bucket):
        # 列出指定bucket下的所有文件夹：
        folders = []
        response = self.s3.list_objects_v2(Bucket=bucket, Delimiter='/')
        for prefix in response.get('CommonPrefixes', []):
            folders.append(prefix.get('Prefix'))

        return folders

    def list_files(self, bucket, folder):
        # 列出指定bucket下的指定文件夹下的所有文件：
        files = []
        response = self.s3.list_objects_v2(Bucket=bucket, Prefix=folder)
        for obj in response.get('Contents', []):
            files.append(obj.get('Key'))
        return files[1:]

    def delete_file(self, bucket, file):
        # 删除指定bucket下的指定文件：
        response = self.s3.delete_object(Bucket=bucket, Key=file)
        return response

    def delete_folder(self, bucket, folder):
        # 删除指定bucket下的指定文件夹：
        response = self.s3.delete_object(Bucket=bucket, Key=folder)
        return response

    def delete_folder(self, bucket, folder):
        # 删除指定bucket下的指定文件夹以及其下文件
        objects_to_delete = []
        response = self.s3.list_objects_v2(Bucket=bucket, Prefix=folder)

        for obj in response.get('Contents', []):
            objects_to_delete.append({'Key': obj['Key']})

        if objects_to_delete:
            self.s3.delete_objects(
                Bucket=bucket, Delete={'Objects': objects_to_delete}
            )

    def create_folder(self, bucket, folder_name):
        # 创建文件夹
        try:
            self.s3.put_object(Bucket=bucket, Key=folder_name + '/')
            print(f"Folder {folder_name} has been created in {bucket}.")
        except Exception as e:
            print(f"Something went wrong: {e}")

    def upload_file(self, bucket, file, key):
        # 上传文件
        response = self.s3.upload_file(file, bucket, key)
        return response

    def upload_file(self, bucket, file_path, object_name=None):
        # 上传文件
        if object_name is None:
            object_name = file_path

        try:
            self.s3.upload_file(file_path, bucket, object_name)
            print(
                f"File {file_path} has been uploaded to {bucket}/{object_name}."
            )
        except Exception as e:
            print(f"Something went wrong: {e}")

    def upload_binary_file(self, bucket, file_path, object_name=None):
        # 上传二进制文件
        if object_name is None:
            object_name = file_path

        try:
            with open(file_path, 'rb') as data:
                self.s3.put_object(Bucket=bucket, Key=object_name, Body=data)
            print(
                f"Binary file {file_path} has been uploaded to {bucket}/{object_name}."
            )
        except Exception as e:
            print(f"Something went wrong: {e}")

    def get_file_info(self, bucket, object_name):
        # 获取文件信息
        try:
            response = self.s3.head_object(Bucket=bucket, Key=object_name)
            return response
        except Exception as e:
            print(f"Something went wrong: {e}")
            return None

    def get_random_file(self, bucket, folder):
        # 获取随机文件
        files = self.list_files(bucket, folder)
        file = random.choice(files)
        return file

    def download_file(self, bucket, object_name, file_path):
        # 下载文件
        try:
            self.s3.download_file(bucket, object_name, file_path)
            print(f"File {object_name} has been downloaded to {file_path}.")
        except Exception as e:
            print(f"Something went wrong: {e}")


if __name__ == '__main__':
    client = UpyunS3Client(access_key, secret_key, endpoint)
    # resp = client.download_file(
    #     'image-upyun-reido',
    #     'ImageApi/desktop/Indigo bunting.jpg',
    #     './Indigo bunting.jpg',
    # )
    # print(resp)
    print(client.__dir__())
