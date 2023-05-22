#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# In[12]:


grid = np.zeros((4, 3))
policy = np.zeros_like(grid, dtype=str)
print(grid)
print(policy)


# In[13]:


grid[:] = -0.04
grid[0,1]=1     # THE REWARD STATE
grid[0,2]=-1;   #THE RED STATE
grid[2,1]=np.nan
policy[2,1]="NA"
grid


# In[14]:


reward_Step=-0.04
reward_red=-1
reward_goal=1
p_indirec_action=0.7
p_perp=0.15


# In[15]:


gamma=0.95 #discount factor 

threshold=0.0001 #this is the convergenve threshold


# In[16]:


# Define a function to get the next state based on the current state and action
def get_next_state(row, col, action):
    if action == "up":
        next_row = max(row - 1, 0)
        next_col = col
    elif action == "down":
        next_row = min(row + 1, grid.shape[0] - 1)
        next_col = col
    elif action == "left":
        next_row = row
        next_col = max(col - 1, 0)
    elif action == "right":
        next_row = row
        next_col = min(col + 1, grid.shape[1] - 1)
    
    if(np.isnan(grid[next_row,next_col])):
        return row,col
    return next_row, next_col


# In[19]:


# Perform Value Iteration
V = np.zeros_like(grid)
V[0,1]=1
V[0,2]=-1
print(V)


# In[20]:


def get_utility(grid,V,row,col):
    expected_utility = [] #this will take max of multiply with gamma and add it to the reward
    perp_actions = {"up": ["left", "right"], "down": ["left", "right"], "left": ["up", "down"], "right": ["up", "down"]}
    for action in perp_actions.keys():
        next_row, next_col = get_next_state(row, col, action)
        perp_row_col = [(get_next_state(row, col, perp_action)) for perp_action in perp_actions[action]]
        expected_utility.append(p_indirec_action*V[next_row, next_col] + p_perp*(V[perp_row_col[0][0], perp_row_col[0][1]] + V[perp_row_col[1][0], perp_row_col[1][1]]))
        
#     print(expected_utility)
    policy[row, col] = max(perp_actions.keys(), key=lambda x: expected_utility[list(perp_actions.keys()).index(x)])
    if grid[row,col] == 1:
        return reward_goal
    elif grid[row,col] == -1:
        return reward_red 
    else:
        return reward_Step + gamma*max(expected_utility)

           


# In[21]:


iterations=0
while True:
    delta = 0
    iterations=iterations+1
    V_temp = np.zeros_like(V)
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            V_temp[row][col]=V[row][col]
            
    for row in range(grid.shape[0]-1, -1, -1):
        for col in range(grid.shape[1]):
            if np.isnan(grid[row, col]):
                V[row,col]=0
                continue    
            V[row, col] = get_utility(grid, V_temp, row, col)
            delta = max(delta, np.abs(V_temp[row][col] - V[row, col]))

    if delta < threshold:
        break
    print("Utility values:")
    print(V)

        


# In[22]:


print(V)
print(policy)
print(iterations)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




