import torch
import math
from tqdm import tqdm

def perturb(data, model, Dloss, suffix=None, eps=0.2, alpha=0.005, verbose=1, modeltype='cyc', init_noise=True):

    pdata = {}

    if not (Dloss == 'Nullifying' and not init_noise):
        init_noise = eps    

    if modeltype == 'cyc':

        for char in 'AB':
            G = getattr(model, 'netG_%s'%char)
            pdata[char] = PGD(data[char], G, Dloss, eps, alpha, verbose, init_noise)
            suf = suffix if suffix else modeltype+'_e'+xstr(eps)+'_a'+xstr(alpha)
            pdata[char+'_paths'] = [data[char+'_paths'][0].split('.jpg')[0]+'%s.jpg'%suf]

    else:
        xstr = lambda s: ''.join(str(s).split('.'))

        G1 = getattr(model[0], 'netG')
        G2 = getattr(model[1], 'netG')
        G = lambda x: G2(G1(x))
        pdata['A'] = PGD(data['A'], G, Dloss, eps, alpha, verbose, init_noise)
        pdata['B'] = torch.zeros_like(pada['A'])
        suf = suffix if suffix else modeltype+'_e'+xstr(eps)+'_a'+xstr(alpha)
        pdata['A_paths'] = [data[char+'_paths'][0].split('.jpg')[0]+'%s.jpg'%suf]        
        pdata['B_paths'] = 'not_used'

    return pdata

def PGD(images, G, Dloss, eps, alpha, verbose, init_noise, concat=False):
    X_orig = images.clone()
    X_var = images.clone()
    X_orig, X_var = X_orig.cuda(), X_var.cuda()
    if type(Dloss) != str:
        Dloss.cuda()

    if Dloss == 'Distorting':
        first_imgs = [G(X_orig).detach()]

    if init_noise:
        random = torch.rand_like(X_var).uniform_(-init_noise, init_noise)
        X_var += random

    pbar = tqdm(range(iter_), ncols=70, desc='PGD') if verb == 1 else range(iter_)
    for __ in pbar:
        X = X_var.clone()
        X.requires_grad = True
        output = G(X)
        if type(Dloss) == str:
            if Dloss == 'Nullifying':
                loss = -1 * ((output - X_orig)**2).sum()  
            elif Dloss == 'Distorting':
                loss = ((output - first_imgs[i])**2).sum()
        else:
            if concat:
                output = torch.cat([output, X], 1)
            loss = Dloss(output)

        loss = loss.mean()
        loss.backward()
        grad_value = X.grad.data

        X_var = X_var + alpha*grad_value
        X_var = torch.where(X_var < X_orig-eps, X_orig-eps, X_var)
        X_var = torch.where(X_var > X_orig+eps, X_orig+eps, X_var)
        X_var = X_var.clamp(-1, 1)

    return X_var
