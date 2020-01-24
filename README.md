# Adversarial-Attack-CycleGAN-and-pix2pix
Generating Adversarial Images for Image-to-Image models in Pytorch

We provide PyTorch implementations for adversarially attacking CycleGAN, pix2pix and pix2pixHD models.

The code was written by [Chin-Yuan Yeh](https://github.com/jimmy-academia).

This PyTorch implementation is to be used alongside the [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) repository or the [pix2pixHD](https://github.com/NVIDIA/pix2pixHD) repository.

### dataset specifics
This work uses CelebA-HQ and CelebAMask-HQ. The datasets can be found in this [google drive link](https://drive.google.com/file/d/1badu11NqxGf6qM3PTTooQDJvQbejgbTv/view) provided by this repository [CelebAMask-HQ](https://github.com/switchablenorms/CelebAMask-HQ). (In case google drive link fails, backup version can also be found [here](https://github.com/jimmy-academia/downloadable/releases/tag/dset.celeba))

## Getting Started

### Installation

* clone this repo
```
git clone https://github.com/jimmy-academia/Adversarial-Attack-CycleGAN-and-pix2pix.git
```
* clone the CycleGAN-pix2pix or pix2pixHD repo and copy the corresponding files to the correct place.

for CycleGAN or pix2pix:
```
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
cd Adversarial-Attack-CycleGAN-and-pix2pix
cp -v attack_cyc_pix.py adversaryfunc.py ../pytorch-CycleGAN-and-pix2pix
```
or for pix2pixHD
```
git clone https://github.com/NVIDIA/pix2pixHD.git
cd Adversarial-Attack-CycleGAN-and-pix2pix
cp -v attack_pixhd.py adversaryfunc.py ../pix2pixHD
```

### Model Setup -- Prepare Your Own Model:

* download and prepare the CelebaHQ and mask datasets
```
bash scripts/download_dataset.sh
python scripts/prepare_dataset.py --imagesize [default: 256] --datatype [default: Smile | Blond | Bald | Glass | Blond-pix | Blond-HD | Custom ]
```
* than move resulting new directory to the correct location, ex:
```
mv smilehq ../pytorch-CycleGAN-and-pix2pix/datasets
```
> refer to [customizations](docs/customize.md) for dataset preparation details.

* train the model with original CycleGAN-pix2pix or pix2pixHD repository:
```
cd ../pytorch-CycleGAN-and-pix2pix
python train.py --dataroot  datasets/smilehq --name smile --model cycle_gan
```
```
python train.py --dataroot  datasets/black_masked --name black_masked --model pix2pix
python train.py --dataroot  datasets/masked_blond --name masked_blond --model pix2pix
```
(pix2pixHD)
```
python train.py --dataroot datasets/black_masked --name black_masked --resize_or_crop scale_width_and_crop --loadSize 572 --fineSize 512 --label_nc 0 --no_instance 

python train.py --dataroot datasets/masked_blond --name masked_blond --resize_or_crop scale_width_and_crop --loadSize 572 --fineSize 512 --label_nc 0 --no_instance 
```

### Model Setup -- Use Pretrained Weights

* Alternatively, you can use pretrained weights by:
```
bash script/download_weights.sh
```
* then move the corresponding folders to the correct location, ex:
```
mkdir -p ../pytorch-CycleGAN-and-pix2pix/checkpoints/
mv weights/smile ../pytorch-CycleGAN-and-pix2pix/checkpoints/
```
* also copy the dataset directory for single running example if you didn't download the celebahq dataset, ex:
```
cp -vr single_dset ../pytorch-CycleGAN-and-pix2pix/datasets
```

### Attack:

* basic attack -- CycleGAN or pix2pix
```
python <attack_cyc.py|attack_pix.py> --dataroot datasets/<single_dset|smilehq|...> --name smile --model <cycle_gan|pix2pix>
```
* basic attack -- pix2pixHD
```
python attack_pixhd.py
```

* more attack templates:
in `template` directory
```
a for ...
```


