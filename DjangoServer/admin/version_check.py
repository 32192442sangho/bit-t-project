import numpy as np
import tensorflow as tf
import torch
import sklearn
from tensorflow.python.client import device_lib
import riotwatcher
import matplotlib.pyplot as plt
if __name__ == '__main__':
    print(f'numpy version : {np.__version__}')
    print(f'tensorflow version : {tf.__version__}')
    print(f'torch version : {torch.__version__}')
    print(f'sklearn version : {sklearn.__version__}')
    print(f'이 PC에 설치된 디바이스 상세보기 : {device_lib.list_local_devices()}')
    print(f'CUDA 프로그래밍 가능여부 :  {torch.cuda.is_available()}')
    print(f'CUDA 프로그래밍 가능여부 : {torch.cuda.get_device_name()}')
    print(f'사용 가능 GPU 갯수 :  {torch.cuda.device_count()}')
    print(riotwatcher.__version__)
    plt.plot([1,2,3,4])
    plt.show()