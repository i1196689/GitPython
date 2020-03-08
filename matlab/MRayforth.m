function F=MRayforth(L)
[m,~]=size(L);
M=[L(:,1)];
aver=sum(M)/m;
sita=[];
for i=1:m
    mm=i*2*pi/m;
    sita=[sita,mm];
end
for i=1:m
    G=plot([0,(M(i)+(M(i)-aver)*aver/8000)*cos(sita(i))],[0,(M(i)+(M(i)-aver)*aver/8000)*sin(sita(i))],'g','linewidth',2);
    hold on
end
F=G;
end