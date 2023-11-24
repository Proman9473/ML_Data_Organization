% Define the main directory
mainDir = 'C:\Users\MahdiKhalili\Desktop\Pit_13 - Copy\pit_1';

% Create the destination directories D1 to D5
for i = 1:5
    mkdir(fullfile(mainDir, ['D' num2str(i)]));
end

% Initialize a global counter for file names
fileCounter = 0;

% Get a list of all subdirectories in the main directory
subDirs = dir(fullfile(mainDir, 'surf*'));
subDirs = subDirs([subDirs.isdir]);  % Filter out non-directories

% Iterate over each subdirectory
for k = 1:length(subDirs)
    subDirPath = fullfile(mainDir, subDirs(k).name);
    
    % Extract diameter value from the directory name
    diaValue = regexp(subDirs(k).name, 'dia(\d+)', 'tokens');
    if isempty(diaValue)
        continue;  % Skip if no diameter value is found
    end
    diaValue = str2double(diaValue{1}{1});

    % Check if the diameter value is between 1 and 5
    if diaValue >= 1 && diaValue <= 5
        destDir = fullfile(mainDir, ['D' num2str(diaValue)]);
        
        % List all files in the subdirectory
        files = dir(subDirPath);
        
        % Iterate over each file
        for f = 1:length(files)
            [~, name, ext] = fileparts(files(f).name);
            
            % Check for .jpg and .xml pair
            if strcmp(ext, '.jpg')
                xmlFile = fullfile(subDirPath, [name '.xml']);
                jpgFile = fullfile(subDirPath, files(f).name);
                
                if exist(xmlFile, 'file')
                    % Increment the fileCounter and use it for naming
                    fileCounter = fileCounter + 1;
                    newBaseName = sprintf('%d', fileCounter);
                    copyfile(jpgFile, fullfile(destDir, [newBaseName '.jpg']));
                    copyfile(xmlFile, fullfile(destDir, [newBaseName '.xml']));
                end
            end
        end
    end
end
