% Set the range of N values
N_values = 1:100;

% Initialize the vector to store the probabilities
prob = zeros(size(N_values));

% Loop over the N values and calculate the probabilities
for i = 1:length(N_values)
    % Initialize the number of successful trials to zero
    num_success = 0;
    
    % Run a large number of trials to estimate the probability
    num_trials = 10000;
    for j = 1:num_trials
        % Set the initial position to zero
        pos = -1;
        
        % Simulate the random walk for N steps
        for k = 1:N_values(i)
            % Generate a random step (-1 or 1)
            step = 2*randi([0, 1], 1) - 1;
            
            % Update the position
            pos = pos + step;
        end
        
        % Check if the final position is zero
        if pos == 0
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