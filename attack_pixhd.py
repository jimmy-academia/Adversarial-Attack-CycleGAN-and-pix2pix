import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
from util.visualizer import save_images
from util import html

print('testrunn attack!')
from adversaryfunc import perturb

if __name__ == '__main__':
    opt = TestOptions().parse()  
    opt.num_threads = 0   
    opt.batch_size = 1    
    opt.serial_batches = True  # disable data shuffling
    opt.no_flip = True    
    opt.display_id = -1   
    dataset = create_dataset(opt)  
    model = create_model(opt)     
    model.setup(opt)               
    model.eval()

    # The directory for saving results
    web_dir = os.path.join(opt.results_dir, 'attack_cyc')  
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


        pdata = perturb(data, model, 'Nullifying', suffix='pgd_null_attack')
        model.set_input(pdata)
        model.test()
        visuals = model.get_current_visuals()  
        img_path = model.get_image_paths()     
        save_images(webpage, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize)


        pdata = perturb(data, model, 'Distorting', suffix='pgd_dist_attack')
        model.set_input(pdata)
        model.test()
        visuals = model.get_current_visuals()  
        img_path = model.get_image_paths()     
        save_images(webpage, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize)

    webpage.save()  # save the HTML
