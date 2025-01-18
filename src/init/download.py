from huggingface_hub import snapshot_download

def download_hf_model(model_name, save_path):
    snapshot_download(model_name, local_dir=save_path)
