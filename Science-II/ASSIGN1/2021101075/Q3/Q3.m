N = 500;
Ds = [0, 1, 5, 10]; % four sets of values for D

for i = 1:length(Ds)
    D = Ds(i);
    M = randn(N, N); % generate a matrix with random elements from N(0,1)
    M = M - diag(diag(M)) + diag(-D * ones(N, 1)); % make the diagonal elements equal to -D
    
    [V, lambda] = eig(M); % compute the eigenvalues of the matrix
    lambda = diag(lambda); % extract the diagonal of the eigenvalue matrix
    
    figure;
    scatter(real(lambda), imag(lambda), '.'); % plot the eigenvalues in the complex plane
    xlabel('Real(\lambda)');
    ylabel('Imag(\lambda)');
    title(sprintf('D = %d', D));
end
