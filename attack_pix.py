'''
script for adversarial attacking pix2pix model
use this in a "pytorch-CycleGAN-and-pix2pix" repository 
(https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

example usage: 
    python attack_pix.py --dataroot datasets/single_dset
'''

import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
from util.visualizer import save_images
from util import html
from adversaryfunc import perturb

if __name__ == '__main__':
    opt = TestOptions().parse()  
    opt.num_threads = 0   
    opt.batch_size = 1    
    opt.serial_batches = True  # disable data shuffling
    opt.no_flip = True    
    opt.display_id = -1   
    dataset = create_dataset(opt)  

    opt.model = 'pix2pix'
    opt.name = 'pix_black_masked'
    opt.norm = 'batch'
    opt.netG = 'unet_256'

    modela = create_model(opt)
    modela.setup(opt)

    opt.name = 'pix_masked_blond'
    modelb = create_model(opt)
    modelb.setup(opt)

    model = [modela, modelb]

    # The directory for saving results
    web_dir = os.path.join(opt.results_dir, 'attack_pix')   ## results/attack_pix
    print('saving in directory', web_dir)
    
    webpage = html.HTML(web_dir, 'Experiment = %s, Phase = %s, Epoch = %s' % (opt.name, opt.phase, opt.epoch))

    for i, data in enumerate(dataset):
        if i >= opt.num_test:
            break
        model.set_input(data)  
        model.test()           
        visuals = model.get_current_visuals()  
        img_path = model.get_image_paths()     
        save_images(webpage, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize)


        pdata = perturb(data, model, 'Nullifying', suffix='pgd_null_attack', modeltype='pix')
        modela.set_input(pdata)
        modela.test()
        visuals = modela.get_current_visuals()  
        visuals.pop('real_B')
        img_path = modela.get_image_paths()     
        save_images(webpage, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize)

        middata = {
            'A': visuals['fake_B'],
            'B': visuals['fake_B'],
            'A_paths':[visuals['A_paths'][0].split('.jpg')[0]+'_mid.jpg'],
            'B_paths':['none'],
        }

        modelb.set_input(middata)
        modelb.test()
        visuals = modelb.get_current_visuals()  
        visuals.pop('real_B')
        img_path = modelb.get_image_paths()     
        save_images(webpage, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize)


        pdata = perturb(data, model, 'Distorting', suffix='pgd_dist_attack', modeltype='pix')
        modela.set_input(pdata)
        modela.test()
        visuals = modela.get_current_visuals()  
        visuals.pop('real_B')
        img_path = modela.get_image_paths()     
        save_images(webpage, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize)

        middata = {
            'A': visuals['fake_B'],
            'B': visuals['fake_B'],
            'A_paths':[visuals['A_paths'][0].split('.jpg')[0]+'_mid.jpg'],
            'B_paths':['none'],
        }

        modelb.set_input(middata)
        modelb.test()
        visuals = modelb.get_current_visuals()  
        visuals.pop('real_B')
        img_path = modelb.get_image_paths()     
        save_images(webpage, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize)

    webpage.save()  # save the HTML
