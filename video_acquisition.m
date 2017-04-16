% This program will only work if you have properly installed the drivers for your
% USB AV adapter.

% Code taken from https://www.mathworks.com/help/imaq/videoinput.html

adaptorname = 'winvideo';

obj = videoinput(adaptorname, 1, 'I420_640x480');
preview(obj);
%frame = getsnapshot(obj);
%image(frame);