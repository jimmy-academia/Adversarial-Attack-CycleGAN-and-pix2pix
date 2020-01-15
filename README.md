# Adversarial-Attack-CycleGAN-and-pix2pix
Generating Adversarial Images for Image-to-Image models in Pytorch

We provide PyTorch implementations for adversarially attacking CycleGAN, pix2pix and pix2pixHD models.

The code was written by [Chin-Yuan Yeh](https://github.com/jimmy-academia).

This PyTorch implementation is to be used alongside the [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) repository or the [pix2pixHD](https://github.com/NVIDIA/pix2pixHD) repository.

## Getting Started

### dataset specifics
This work uses CelebA-HQ and CelebAMask-HQ. The datasets can be found in this [google drive link](https://drive.google.com/file/d/1badu11NqxGf6qM3PTTooQDJvQbejgbTv/view) provided by this repository [CelebAMask-HQ](https://github.com/switchablenorms/CelebAMask-HQ). (In case google drive link fails, backup version can also be found in [downlable repository](https://github.com/jimmy-academia/downloadable/releases/tag/dset.celeba)

### Installation

* clone this repo
```
git clone https://github.com/jimmy-academia/Adversarial-Attack-CycleGAN-and-pix2pix.git
```
* clone the CycleGAN-pix2pix or pix2pixHD repo and move the corresponding files to the correct place.

for CycleGAN:
```
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
cd Adversarial-Attack-CycleGAN-and-pix2pix
mv attack_cyc.py ../pytorch-CycleGAN-and-pix2pix
mv vesaryfunc_cyc.py ../pytorch-CycleGAN-and-pix2pix
```
or for pix2pix
```
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
cd Adversarial-Attack-CycleGAN-and-pix2pix
mv attack_pix.py ../pytorch-CycleGAN-and-pix2pix
mv vesaryfunc_pix.py ../pytorch-CycleGAN-and-pix2pix
```
or for pix2pixHD
```
git clone https://github.com/NVIDIA/pix2pixHD.git
cd Adversarial-Attack-CycleGAN-and-pix2pix
mv attack_pphd.py ../pix2pixHD
mv vesaryfunc_pphd.py ../pix2pixHD
```
* prepare the CelebaHQ and mask datasets
download the datasets.
```
bash download.sh
```
Run one of the following to produce datasets for each models. 
```
python prepare_cyclegan_dataset.py
python prepare_pix2pix_dataset.py
python prepare_pix2pixhd_dataset.py
```
