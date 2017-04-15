s=serial('COM6','BaudRate',115200);
fopen(s);
writedata=uint16(500); %0x01F4
for i=1:10000
   fwrite(s,writedata,'uint16') %write datac
end
 fclose(s);
 delete(s);