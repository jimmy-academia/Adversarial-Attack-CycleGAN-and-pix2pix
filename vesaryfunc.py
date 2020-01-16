import torch

import math
from tqdm import tqdm

def perturb(data, models, Dloss, suffix=None, eps=0.2, alpha=0.005, verbose=1, modeltype='cyc', add_random=True):

    xstr = lambda s: ''.join(str(s).split('.'))

    Gs = []
    for model in models:
        if type(model) == list:
            G1 = getattr(model[0], 'netG')
            G2 = getattr(model[1], 'netG')
            G = lambda x: G2(G1(x))
        else:
            G = getattr(model, 'netG')
        Gs.append(G)

    pdata = {}
    for char in 'AB':
        pdata[char] = PGD(data[char], Gs, Dloss, eps, alpha, modeltype, verbose, add_random)
        suf = suffix if suffix else modeltype+'e'+xstr(eps)+'a'+xstr(alpha)
        pdata[char+'_paths'] = [data[char+'_paths'][0].split('.jpg')[0]+'%s.jpg'%suf]

    return pdata

def PGD(images, Gs, Dloss, eps, alpha, modeltype, verbose, add_random):
    X_orig = images.clone()
    X_var = images.clone()
    X_orig, X_var = X_orig.cuda(), X_var.cuda()
    if type(Dloss) != str:
        Dloss.cuda()

    if Dloss == 'Distorting':
        first_imgs = [G(X_orig).detach() for G in Gs]

    if add_random:
        random = torch.rand_like(X_var).uniform_(-eps, eps)
        X_var += random

    pbar = tqdm(range(iter_), ncols=70, desc='PGD') if verb == 1 else range(iter_)
    for __ in pbar:
        for i, G in enumerate(Gs):
            X = X_var.clone()
            X.requires_grad = True
            output = G(X)
            if type(Dloss) == str:
                if Dloss == 'Nullifying':
                    loss = -1 * ((output - X_orig)**2).sum()  
                elif Dloss == 'Distorting':
                    loss = ((output - first_imgs[i])**2).sum()
            else:
                if modeltype=='pix':
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
