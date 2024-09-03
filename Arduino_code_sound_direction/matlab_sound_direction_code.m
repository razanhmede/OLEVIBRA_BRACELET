% Initialize serial port communication
s = serial('COM5', 'BaudRate', 9600); % Adjust COM port as necessary
fopen(s);

% Parameters
numMicrophones = 6;
samplingRate = 1000; % Adjust according to Arduino code delay
frameSize = 6; % Number of samples to read per frame

while true
    % Read data from Arduino
    data = fscanf(s, '%s', [numMicrophones, frameSize]);
    
    beamformedSignal = sum(data, 1);
    
    [maxValue, maxIndex] = max(beamformedSignal);
    estimatedDirection = (maxIndex - 1) * (360 / frameSize); % Convert index to degrees
    
    % Display estimated direction
    fprintf('Estimated direction of sound source: %.2f degrees\n', estimatedDirection);
end

% Clean up
fclose(s);
delete(s);
clear s;