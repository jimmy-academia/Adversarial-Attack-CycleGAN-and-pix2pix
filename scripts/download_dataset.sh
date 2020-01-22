#!/bin/bash
### celeba HQ mask google drive


wget --load-cookies /tmp/cookies.txt\
     "https://docs.google.com/uc?export=download&confirm=$(wget\
       --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate\
          'https://docs.google.com/uc?export=download&id=1badu11NqxGf6qM3PTTooQDJvQbejgbTv' -O- |\
              sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1badu11NqxGf6qM3PTTooQDJvQbejgbTv"\
               -O CelebAMask-HQ.zip && rm -rf /tmp/cookies.txt

unzip CelebAMask-HQ.zip
rm CelebAMask-HQ.zip

mkdir celebafiles
mv CelebAMask-HQ/CelebA-HQ-img celebafiles/hqimages
mkdir celebafiles/hairmasks
mv CelebAMask-HQ/CelebAMask-HQ-mask-anno/*/*hair.png celebafiles/hairmasks/

mkdir celebafiles/othermasks
mv CelebAMask-HQ/CelebAMask-HQ-mask-anno/* celebafiles/othermasks
mkdir celebafiles/attr
mv CelebAMask-HQ/CelebA-HQ-to-CelebA-mapping.txt celebafiles/attr/indexmap.txt
mv CelebAMask-HQ/CelebAMask-HQ-attribute-anno.txt celebafiles/attr/anno.txt
mv CelebAMask-HQ/CelebAMask-HQ-pose-anno.txt celebafiles/attr/pose.txt
mv CelebAMask-HQ/README.txt celebafiles/attr/orig_README.md

rm -r CelebAMask-HQ







## alternative backup files, Celeba-HQ and CelebA-HQ-img2 contains the images, while ...mask-anno contains masks.
## may require multiple tries to randomly arive at faster download speed from github

# wget https://github.com/jimmy-academia/downloadable/releases/download/dset.celeba/CelebA-HQ.zip
# wget https://github.com/jimmy-academia/downloadable/releases/download/dset.celeba/CelebA-HQ-img2.zip
# wget https://github.com/jimmy-academia/downloadable/releases/download/dset.celeba/CelebAMask-HQ-mask-anno.zip

# unzip CelebA-HQ.zip
# unzip CelebA-HQ-img2.zip
# unzip CelebAMask-HQ-mask-anno.zip