import os
import hashlib
import requests
import subprocess

update_json_url = "http://techapp.techsize.com.br"  # Link update

def calculate_file_hash(file_path):
    hash_object = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def download_file(url, local_path):
    response = requests.get(url)
    with open(local_path, "wb") as f:
        f.write(response.content)

def update_files(update_data, base_folder=""):
    for item, data in update_data.items():
        current_folder = os.path.join(base_folder, item)
        if isinstance(data, dict):  # If it's a folder, create the directory and update its contents
            if not os.path.exists(current_folder):
                os.makedirs(current_folder)
            update_files(data, current_folder)
        elif isinstance(data, str):  # If it's a file, download it
            remote_url = update_json_url + "/files/" + os.path.join(base_folder, item).replace("\\", "/")
            local_path = os.path.join(base_folder, item)

            print(f"Checking {item} from {remote_url} ...")

            if os.path.isfile(local_path):
                local_hash = calculate_file_hash(local_path)
                if local_hash != data:
                    print(f"{item} needs to be updated. Downloading...")
                    download_file(remote_url, local_path)
                    print(f"Downloaded updated file: {item}")
                else:
                    print(f"{item} is up to date.")
            else:
                print(f"{item} does not exist locally. Downloading...")
                download_file(remote_url, local_path)
                print(f"Downloaded new file: {item}")
        else:
            print(f"Unsupported data type for item: {item}")

if __name__ == "__main__":
    try:
        # Download update.json
        print(f"Fetching {update_json_url} ...")
        response = requests.get(update_json_url)

        # Check for HTTP errors
        response.raise_for_status()

        # Get response content
        response_text = response.text

        # Check if the content is not empty
        if response_text:
            print("Decoding update.json ...")
            try:
                update_data = response.json()
                # Update files based on the data from update.json
                if 'file_hashes' in update_data:
                    print("Updating files ...")
                    update_files(update_data['file_hashes'])
                else:
                    print("'file_hashes' not found in update.json")
            except ValueError as e:
                print(f"Error decoding update.json: {e}")
                print("Response content:")
                print(response_text)
        else:
            print("update.json is empty")
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching update.json: {e}")
    try:
        subprocess.run("GLPI.exe -updated", shell=True)
    except subprocess.CalledProcessError:
        print("Erro ao executar o arquivo .exe")        
