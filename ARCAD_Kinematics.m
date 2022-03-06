syms x y z Rx Ry Rz theta result rx ry rz

Rx(x) = [1 0 0;...
         0 cos(x) -sin(x);...
         0 sin(x) cos(x)];

Ry(y) = [cos(y) 0 sin(y);...
         0 1 0;...
         -sin(y) 0 cos(y)];

Rz(z) = [cos(z) -sin(z) 0;...
         sin(z) cos(z) 0;...
         0 0 1];


%Axis and Angle Representation 
%Direct Problem
theta = 0.7*3.14

rx = -0.53;
ry = 0.74;
rz = 0.42;

z=atan2(ry,rx);
y=atan2((rx^2 + ry^2)^0.5,rz);

result = double(Rz(z)*Ry(y)*Rz(theta)*Ry(-y)*Rz(-z));

%DH Parameter
syms l lambda d delta trans_mat q1

trans_mat(l,lambda, d, delta) = [cos(delta) -sin(delta)*cos(lambda) sin(delta)*cos(lambda) l*cos(delta);...
    sin(delta) cos(delta)*cos(lambda) -cos(delta)*sin(lambda) l*sin(delta);...
    0 sin(lambda) cos(lambda) d;...
    0 0 0 1];

trans_mat(0,3.14/2,0.089,q1)*trans_mat(0,3.14/2,0.089,q1)




