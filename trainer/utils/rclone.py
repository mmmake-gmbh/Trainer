import os
import subprocess

def update_local_data(repo_name:str, branch_name:str, target_folder:str, upload: bool = False):
    #TODO do not sync, only copy metadata.csv and wavs folder from lakefs to local
    if upload:
        command = ["rclone", "sync", target_folder,
                   f"lakefs:{repo_name}/{branch_name}"]
    else:
        command = ["rclone", "sync",
                   f"lakefs:{repo_name}/{branch_name}", target_folder]
    print(command)
    result = subprocess.run(command, capture_output=True)
    print(result.stderr)
    print(os.listdir(target_folder))
    assert result.returncode == 0