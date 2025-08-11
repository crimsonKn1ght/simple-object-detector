import torch


model_path = "./game_weights.pt"
conf_thres = 0.5
imgsz = 640
device = 0 if torch.cuda.is_available() else "cpu"