import os
import subprocess

def get_data_from_lakefs(repo_name:str, branch_name:str, target_folder:str):
    command = ["rclone", "sync",
                   f"lakefs:{repo_name}/{branch_name}", target_folder]
    result = subprocess.run(command, capture_output=True)
    print("Rclone stderr:", result.stderr)
    assert result.returncode == 0
    
def sync_data2s3bucket(bucket_name:str, source_folder:str):
    command = ["rclone", "sync", source_folder, f"s3:{bucket_name}"]
    result = subprocess.run(command, capture_output=True)
    print("Rclone stderr:", result.stderr)
    assert result.returncode == 0