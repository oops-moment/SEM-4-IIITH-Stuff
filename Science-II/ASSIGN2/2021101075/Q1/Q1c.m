% first we will declare all the constant required for the formula.
A=106;
C=1283;
M=6075;
I=1;


% create an array of N values
N = [1, 10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000];

% initialize an array to store the expectation values
E = zeros(size(N));

% loop over all values of N
for i = 1:length(N)
    % generate N random numbers
    array = zeros(1, N(i));
    array(1) = I;
    for j = 2:N(i)
        I = mod(A * I + C, M);
        array(j) = I;
    end
% calculate the expectation value of the random numbers
    E(i) = mean(array);
end

% plot the expectation values as a function of N
plot(N, E);
xlabel('N');
ylabel('Expectation value E(Ij)');






