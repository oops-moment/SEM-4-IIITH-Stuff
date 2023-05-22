a=[1 -1.0 1.0;1 -0.5 0.25;1 0.0 0.0;1 0.5 0.25;1 1.0 1.0]; % A matrix formed by 1 t t^2
b=[1.0;0.5;0.0;0.5;2.0];                 % values of y corresponding to t
Atranspose = a.';           % calculating A transpose
A_dash = Atranspose * a; % calculating Atranspose*A
B_dash=Atranspose * b; % calculating Atranspose *B
x=mldivide(A_dash,B_dash);  % solves for AX=B
t = -100:1:100; % set of data points to plot
y = x(1,1) + x(2,1)*t + x(3,1)*t.^2; 
plot(t,y) % plot the graph
xlabel('t');   % take t on x-axis
ylabel('y') ;  % take y on y-axis