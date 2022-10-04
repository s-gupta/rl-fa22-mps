import torch
def dagger_trainer(env,learner,query_expert,device):
    # get image observations
    obs = env.reset()
    # transform to pytorch tensor
    obs = torch.from_numpy(obs).permute(2,0,1).to(device)
    # get state from environment
    state = torch.tensor(env.state).float().to(device)
    # query expert for action
    action = query_expert(state)
    print('expert action: ', action)
    # take step with expert action
    obs,reward,done,info = env.step(action)
    print('next state: ', env.state)
    print('image shape: ', obs.shape)

    # TODO: Implement dagger here
