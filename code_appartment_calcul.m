clear all;close all;
%% Param�tres
F4=90; %m�pour un F4
F3=72; %m� pour un F3
G=17; %m�pour un garage � verifier
C=7; %m� pour une cave
Ptot=252000; %prix total de l'achat connu

%% Calcul des coefficients
%X a �t� obtenu par substitution de x dans z et de x dans w selon les hypoth�ses faites
%x,y,z,w sont les coefficient � mutliplier en fonction lieu pour avoir un
%prix.
%Deux hypoth�se sont faites:
%-le prix du m� du F4 et eguale au prix du m� du F3
%-le prix du m� du garage coute 1/4 du m� du f4 et donc F3

%formule: Ptot=2*F4*x+F3*y+12*G*z+3*C*w

x=831.68; %calculer par substitution
y=x;
hyp=1/4; %hypoth�se de valeur pour le garrage 1/4 du m� d'un F4
z=hyp*x;%coefficient garage
%% calcul du coefficient w
Xsum=2*F4+F3+12*G*hyp;
w=Ptot/(3*C)-(Xsum/(3*C))*x; %calcul du coefficient pour la cave
a=2*F4*x+F3*y+12*G*z+3*C*w; %Prix total d'achat

%% Prix � l'unit�
prixF4=(a-(F3*y+12*G*z+3*C*w))/2; %prix � l'unit� pour un F4
prixF3=a-(2*F4*x+12*G*z+3*C*w);%prix � l'unit� pour un F3
prixG=(a-(2*F4*x+F3*y+3*C*w))/12;%prix � l'unit� pour
prixC=(a-(2*F4*x+F3*y+12*G*z))/3;%prix � l'unit�
verificationptot=2*prixF4+prixF3+12*prixG+3*prixC;

%% Prix au m�tre carr�

mcarreF4=prixF4/F4;
mcarreF3=prixF3/F3;
mcarreG=prixG/G;
mcarreC=prixC/C;
