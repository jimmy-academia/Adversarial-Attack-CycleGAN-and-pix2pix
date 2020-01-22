'''
prepare datasets for predefined models + custom cyclegan types
'''


import os
import argparse
import random
import sys
from shutil import copyfile, copy
from tqdm import tqdm

def create_dirs(rootdirs):
    dir_list = ['trainA', 'trainB', 'testA', 'testB']
    for rootdir in rootdirs:
        for dir_ in dir_list:
            subdir = os.path.join(rootdir, dir_)
            if not os.path.exists(subdir):
                os.makedirs(subdir)

def create_train_test_split(opt):
    if not os.path.exists(os.path.join(opt.splitdir, 'trainlist.txt')):
        with open('celebafiles/attr/anno.txt', 'r') as f:
            length = int(f.readline())
            attrs = f.readline()
            trainlist = [attrs]
            testlist = [attrs]
            for line in f:
                r = random.random()
            if r < 0.9:
                trainlist.append(line)
            else:
                testlist.append(line)

    with open('../data/att/train_att.txt', 'w') as f:
        f.write(str(len(trainlist))+'\n')
        for line in trainlist:
            f.write(line)

    with open('../data/att/test_att.txt', 'w') as f:
        f.write(str(len(testlist))+'\n')
        for line in testlist:
            f.write(line)        


def copyfile(rootdirs, class_names):
    image_dir = 'celebafiles/hqimages'
    if len(rootdirs) == 1:
        rootdirs = rootdirs*2

    for group_type in ['train', 'test']:
        group_list = os.path.join(opt.splitdir, '%s_list.txt'%group_type)
        dst_dir = group_type

        with open(group_list, 'r') as f:
            length = int(f.readline())
            attrs = f.readline().split()

            index1 = attrs.index(class_names[0]) + 1 if class_names[0] else None
            index2 = attrs.index(class_names[1]) + 1 if class_names[1] else None

            if index1 and index2
                indexs = [index1, index2]
                attrs = ['1', '1']
            elif index1:
                indexs = [index1, index1]
                attrs = ['1', '-1']
            else:
                indexs = [index2, index2]
                attrs = ['-1', '1']


            index = attrs.index(class_name) + 1
            for line in tqdm(f):
                line = line.split()
                path = line[0]
                if line[indexs[0]] == attrs[0]:
                    copy(os.path.join(image_dir, path), os.path.join(rootdirs[0], dst_dir+'A'))
                elif line[indexs[1]] == attrs[1]:
                    copy(os.path.join(image_dir, path), os.path.join(rootdirs[1], dst_dir+'B'))

def make_masked()

def combine_for_pix()


def main:
    parser = argparse.ArgumentParser()
    parser.add_argument('--imagesize', type=int, default=256, help='image size')
    parser.add_argument('--splitdir', type=str, default='scripts', help='directory for trainlist.txt and testlist.txt')
    parser.add_argument('--model', type=str, default='Smile', help='prepare dataset for predefined modeltypes or Customize with \'Custom\' option [ Smile | Blond | Bald | Glass | Blond-pix | Blond-HD | Custom ]')
    parser.add_argument('--attr1', type=str, default=None, help='attribute 1 for custom dataset')
    parser.add_argument('--attr2', type=str, default=None, help='attribute 2 for custom dataset')

    opt = parser.parse_args()

    if opt.model not in ["Smile", "Blond", "Bald", "Glass", "Blond-pix", "Blond-HD", "Custom"]:
        print('this script is for default settings, rewrite script for other considerations!!')
        sys.exit(0)

    rootdirs = [opt.model] if '-' not in opt.model else ['black_masked', 'masked_blond']
    create_dirs(rootdirs)
    create_train_test_split(opt)
    class_dict = {
        'Smile': ['Smiling', None]
        'Blond': ['Black_Hair', 'Blond_Hair'],
        'Blond-pix': ['Black_Hair', 'Blond_Hair'],
        'Blond-HD': ['Black_Hair', 'Blond_Hair'],
        'Bald': [None, 'Bald'],
        'Glass': [None, 'Eyeglasses'],
        'Custom': [opt.attr1, opt.attr2]
    }
    copyfiles(rootdirs, class_dict[opt.model])
    if '-' in opt.model:
        make_masked(opt)
    if 'pix' in opt.model:
        combine_for_pix(opt)

if __name__ == '__main__':
    main()



'''
 5_o_Clock_Shadow Arched_Eyebrows Attractive Bags_Under_Eyes Bald Bangs Big_Lips 
Big_Nose Black_Hair Blond_Hair Blurry Brown_Hair Bushy_Eyebrows Chubby Double_Chin 
Eyeglasses Goatee Gray_Hair Heavy_Makeup High_Cheekbones Male Mouth_Slightly_Open 
Mustache Narrow_Eyes No_Beard Oval_Face Pale_Skin Pointy_Nose Receding_Hairline 
Rosy_Cheeks Sideburns Smiling Straight_Hair Wavy_Hair Wearing_Earrings Wearing_Hat 
Wearing_Lipstick Wearing_Necklace Wearing_Necktie Young 
'''
