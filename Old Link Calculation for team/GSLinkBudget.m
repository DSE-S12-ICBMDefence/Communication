% six.m
close all
clearvars
clc
B = 10e6
angles = linspace(5, 90, 100);      % elevation angle in degrees
altitude = 600;                     % circular orbit altitude in km
t = 15;                             % air temperature in degC
p = 1023;                           % air temperature in hPa
ro = 7.5;                           % water vapor content in g/m^3
f = 34;                             % frequency in GHz
lambda = 0.3 ./ f;                  % wavelength in meters
rxAntennaGain = 15;                 % gain in dB
txAntennaGain = 0;                  % gain in dB
polarizationLoss = 0;               % losses in dB
transmitterLosses = 1.2;            % losses in dB
outputPower = 0 %0.01; % power in dBW
Ta = 790
T0 = 290
L = 10
F = 2
SystemNoiseTemp = Ta + T0*((1-L)/L) + T0*(10^(F/10)-1)
GoverT = rxAntennaGain-(10*log10(SystemNoiseTemp))


                     % ground station G/T in dB
bitrate = 20e3; % bit rate in bits/s
codeGain = 0;
EbN0threshold = 10.5-codeGain;                % Eb/N0 threshold for concatenated code + BPSK with BER = 10^-6
implementationLoss = 1;             % value in dB
receiverLosses = 2;                 % losses in dB
linkMargin = 3;                     % link margin in dB

% Boltzmann constant
kb = 1.3807e-23;                    % in J / K

% distance satellite - ground station as a function of elevation in meters
distance = 0.5 * (-2 * 6371000 * sin(angles * pi / 180) + sqrt(4 * (6371000^2) * ...
    (sin(angles * pi / 180).^2) - 4 * (6371000^2 - (6371000 + (altitude * 1000)).^2)));

linestyles = cellstr(char('-b','-.r','--k',':g'));

% attenuation in dB
freeSpace = 20*log10(4 * pi * distance / lambda);
atmosphericAttenuation = (attenuationWetAir(f, t, p, ro) + attenuationDryAir(f, t, p, ro)) ./ sin(angles / 180 * pi);
% attenuation + atmospheric losses
attenuation = freeSpace + atmosphericAttenuation;
% signal transmitted by the antenna
txSignal = outputPower - transmitterLosses + txAntennaGain;
% signal received by the antenna
rxSignal = txSignal - attenuation - polarizationLoss - receiverLosses;
% signal received at the antenna port
rxSignalAntenna = rxSignal + rxAntennaGain;

% signal to noise ratio
snr = rxSignal + GoverT - 10 * log10(kb) ;

% Eb/N0 calculated at the receiver
EbN0 = snr -  10 * log10(bitrate) + 10*log10(B) ;

% full link budget: take link margin into account
margin = EbN0 - EbN0threshold  - implementationLoss - linkMargin;

figure
plot(angles, margin, '-b', 'LineWidth', 2)
title(sprintf('Link margin over elevation for a %d km orbit', altitude))
xlabel('Elevation - deg')
ylabel('Margin - dB')
grid on
print('six', '-dpng')
