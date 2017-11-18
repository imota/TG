s=serial('COM6','BaudRate',9600);
fopen(s);
writedata=uint16(8);
for i=2:19
    fwrite(s,i,'int8');
end
 fclose(s);
 delete(s);