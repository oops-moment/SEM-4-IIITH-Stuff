% Define the function f(x) = x*sin(x).
% Generate a large number of random points within the range [-π,π].
% Evaluate the function f(x) at each of these points.
% Calculate the average of these function values.
% Multiply the average by the range of integration (π - (-π) = 2π) to obtain the approximate value of the integral.



f = @(x) x.*sin(x); %define the function we need to integrate.

% Set the range of N values
N_vals = 1:1000:100000;


% Initialize a vector to store the integration values
integral_values = zeros(size(N_vals));

% Loop over the N values and compute the integration for each value
for i = 1:length(N_vals)
    % Generate random points within the range [-π,π]
    x = 2*pi*rand(N_vals(i), 1) - pi;
    
    % Evaluate the function at each point
    y = f(x);
    
    % Calculate the average of the function values
    avg_y = mean(y);
    
    % Multiply the average by the range of integration to obtain the approximate integral value
    integral_values(i) = avg_y * 2*pi;
end

% Plot the integration values as a function of N
plot(N_vals, integral_values);
xlabel('N');
ylabel('Integration value');
title('Monte Carlo Integration of x*sin(x) in [-π,π]');