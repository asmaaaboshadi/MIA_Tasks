% Parameters
t = 0:0.01:2; % Time vector
analog_signal = 1.4 * sin(pi * t); % Analog signal (sine wave with amplitude 1.4)

% Sampling times
sampling_times = [0.25, 0.5, 1];

% Bit depths and corresponding levels
bit_depths = [3, 2];
level_dict = containers.Map({3, 2}, {8, 4});

figure;

for i = 1:length(sampling_times)
    sampling_time = sampling_times(i);
    for j = 1:length(bit_depths)
        bit_depth = bit_depths(j);
        levels = level_dict(bit_depth);

        % Sampling
        sampling_points = 0:sampling_time:2;
        sampled_signal = interp1(t, analog_signal, sampling_points);

        % Quantization
        max_val = max(sampled_signal);
        min_val = min(sampled_signal);
        quantized_signal = round((sampled_signal - min_val) / (max_val - min_val) * (levels - 1));

        % Discrete-time signal
        discrete_signal = quantized_signal * (1.4 / (levels - 1));

        % Plotting
        subplot(4, 2, (i-1)*2 + j);
        plot(t, analog_signal, 'b-', 'DisplayName', 'Analog Signal'); hold on;
        stem(sampling_points, sampled_signal, 'r', 'DisplayName', 'Sampled Points');
        stairs(sampling_points, discrete_signal, 'g', 'DisplayName', 'Discrete Signal');
        
        title([num2str(bit_depth), '-bit Encoder with Sampling Time = ', num2str(sampling_time), ' sec']);
        xlabel('Time (sec)');
        ylabel('Voltage (V)');
        legend;
        hold off;
    end
end
