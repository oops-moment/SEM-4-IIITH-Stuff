A=[1 0 0 0 ; 0 1 0 0 ; 0 0 1 0; 0 0 0 1; 1 -1 0 0 ; 1 0 -1 0; 1 0 0 -1; 0 1 -1 0 ; 0 1 0 -1 ; 0 0 1 -1]; % A matrix formed by 1 t t^2
B=[2.95;1.74;-1.45;1.32;1.23;4.45;1.61;3.21;0.45;-2.75];

Atranspose = A.'; % calculating transpose of A
B_dash=Atranspose * B; % calculating Atranspose *B
A_dash = Atranspose * A; % calculating Atranspose*A
xu=mldivide(A_dash,B_dash);  % solves for AX=B
x = [B(1,1),xu(1,1); B(2,1),xu(2,1); B(3,1),xu(3,1) ;B(4,1), xu(4,1)];

bar(x)
title('Comparison of values')
xlabel('x-values')
ylabel('Value')
