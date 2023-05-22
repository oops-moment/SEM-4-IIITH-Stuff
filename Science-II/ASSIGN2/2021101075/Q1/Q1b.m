% first we will declare all the constant required for the formula.
A=106;
C=1283;
M=6075;
I=1;


% now we can store ith random variable in array[i]
array=zeros(1,1000);
array(1)=I;

% loop for all random variable

for i = 2: 1000
    I=mod(A*I+C,M);
    array(i)=I;
end



% plot random variable Ij+1 vs Ij.

scatter(array(1:end-1), array(2:end),".");
xlabel('Ij');
ylabel('Ij+1');
title('Plot of Linear Congruential method of Ij, Ij+1');







