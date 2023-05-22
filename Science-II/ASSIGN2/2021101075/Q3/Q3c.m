% Set the range of N values
N_values = 1:1:100;

% Initialize the vector to store the mean displacements
mean_displacements = zeros(size(N_values));

% Set the initial position to the origin
initial_position = 0;

% Loop over the N values and calculate the mean displacements
for i = 1:length(N_values)
    % Initialize the vector to store the final positions
    final_positions = zeros(1, 10000);
    
    % Simulate a large number of trials to estimate the mean displacement
    num_trials = 10000;
    for j = 1:num_trials
        % Set the initial position
        position = initial_position;
        
        % Simulate the random walk for N steps
        for k = 1:N_values(i)
            % Generate a random step (-1 or 1)
            step = 2*randi([0, 1], 1) - 1;
            
            % Update the position
            position = position + step;
        end
        
        % Store the final position
        final_positions(j) = position;
    end
    
    % Calculate the mean displacement as the average final position
    mean_displacements(i) = mean(final_positions);
end

% Plot the mean displacements as a function of N
plot(N_values, mean_displacements);
xlabel('N');
ylabel('Mean displacement');
title('Mean Displacement after N Steps');
