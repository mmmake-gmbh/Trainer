import os
import subprocess

def get_data_from_lakefs(repo_name:str, branch_name:str, target_folder:str):
    command = ["rclone", "sync",
                   f"lakefs:{repo_name}/{branch_name}", target_folder]
    result = subprocess.run(command, capture_output=True)
    print("Rclone stderr:", result.stderr)
    assert result.returncode == 0
    
def sync_data2s3bucket(bucket_name:str, source_folder:str, name_from_config:str="lakefs"):
    command = ["rclone", "sync", source_folder, f"{name_from_config}:{bucket_name}"]
    result = subprocess.run(command, capture_output=True)
    print("Rclone stderr:", result.stderr)
    assert result.returncode == 0
    
def copy_data_from_s3bucket(bucket_uri:str, target_folder:str):
    splitted_bucket_uri = [s for s in bucket_uri.split("/") if s != ""]
    if len(splitted_bucket_uri) > 1:
        #assumption: only one folder is specified in the bucket_uri
        target_folder = os.path.join(target_folder,splitted_bucket_uri[-1])
    command = ["rclone", "copy", bucket_uri, target_folder]
    result = subprocess.run(command, capture_output=True)
    print("Rclone stderr:", result.stderr)
    assert result.returncode == 0
    return target_folder