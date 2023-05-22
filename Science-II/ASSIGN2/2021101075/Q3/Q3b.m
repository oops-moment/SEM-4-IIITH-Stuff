% Set the range of N values
N_values = 1:1:100;

% Initialize the vector to store the probabilities
prob = zeros(size(N_values));

% Set the initial positions
a = -1;
b = 1;

% Loop over the N values and calculate the probabilities
for i = 1:length(N_values)
    % Initialize the number of successful trials to zero
    num_success = 0;
    
    % Run a large number of trials to estimate the probability
    num_trials = 10000;
    for j = 1:num_trials
        % Set the initial positions
        pos_a = a;
        pos_b = b;
        
        % Simulate the random walks for N steps
        for k = 1:N_values(i)
            % Generate random steps (-1 or 1) for both people
            step_a = 2*randi([0, 1], 1) - 1;
            step_b = 2*randi([0, 1], 1) - 1;
            
            % Update the positions
            pos_a = pos_a + step_a;
            pos_b = pos_b + step_b;
        end
        
        % Check if the two people meet at the same position
        if pos_a == pos_b
            num_success = num_success + 1;
        end
    end
    
    % Estimate the probability as the fraction of successful trials
    prob(i) = num_success / num_trials;
end

% Plot the probabilities as a function of N
plot(N_values, prob);
xlabel('N');
ylabel('Probability');
