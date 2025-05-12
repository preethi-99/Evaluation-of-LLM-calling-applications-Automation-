# Experiment Results

## 📊 Call Setup Time Results

| Application       | Min (ms) | Mean (ms) | Std Dev (ms)  |
|-------------------|----------|-----------|---------------|
| Gemini            | 530      | 655       | 111.13        |
| ChatGPT           | 980      | 990       | 7.9           |
| Instagram         | 1600     | 1675      | 59.16         |
| Messenger         | 1460     | 1475      | 12.9          |
| Copilot           | 1950     | 2164      | 282.36        |
| ChatGPT Pro       | 870      |  930      | 47.43         |
| Gemini Advanced   |          |           |               |


## TTS Performance

| Phase   | Idle CPU | Active CPU | App CPU | system_server CPU | audioserver CPU   | Used RAM | Free RAM |
|---------|----------|------------|---------|--------------------|------------------|----------|----------|
| Before  | 873%     | 27%        | -       | 6.6%               | -                | ~94%     | 405MB    |
| During  | 707%     | 193%       | 20.6%   | 72.4%              | 10.3%            | ~95%     | 340MB    |
| After   | 863%     | 37%        | -       | 6.6%               | -                | ~95.6%   | 340MB    |

## ASR Performance

| Phase   | Idle CPU | Active CPU | App CPU | ASR Service CPU | system_server CPU | audioserver CPU | Used RAM    | Free RAM |
|---------|----------|------------|---------|------------------|--------------------|------------------|----------|----------|
| Before  | 845%     | 55%        | -       | -                | 6.8%               | -                | ~95%     | 450MB    |
| During  | 689%     | 211%       | 21.4%   | 57.1%            | 3.3%               | 10.7%            | ~94%     | 451MB    |
| After   | 877%     | 23%        | -       | -                | 3.3%               | -                | ~94%     | 451MB    |
