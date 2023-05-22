% Define the function f(x) = x*sin(x).
% Generate a large number of random points within the range [-π,π].
% Evaluate the function f(x) at each of these points.
% Calculate the average of these function values.
% Multiply the average by the range of integration (π - (-π) = 2π) to obtain the approximate value of the integral.



f = @(x) x.*sin(x); %define the function we need to integrate.

N = 100000;  % Set the number of random points to generate, more the points more the accuracy

% rand(N,1) will generate number between 0-1 hence finally 0-2pi - pie will
% give between in -pie to pie.

x = 2*pi*rand(N, 1) - pi;

% Evaluate the function at each point
y = f(x);

% now we need to calculate the average of y values
avg_y = mean(y);

% Multiply the average by the range of integration to obtain the approximate integral value
integral_value = avg_y * 2*pi;

% Display the result
disp(['Approximate integral value: ', num2str(integral_value)]);
